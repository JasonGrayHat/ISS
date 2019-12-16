#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <endian.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>

#define HT16K33_BLINK_CMD       0x80
#define HT16K33_BLINK_DISPLAYON 0x01
#define HT16K33_BLINK_OFF       0
#define HT16K33_BLINK_2HZ       1
#define HT16K33_BLINK_1HZ       2
#define HT16K33_BLINK_HALFHZ    3

#define HT16K33_CMD_SETUP       0x21
#define HT16K33_CMD_BRIGHTNESS  0x0E
#define HT16K33_ADDR            0x70

#define BUFFER_SIZE             8

unsigned short displaybuffer[ BUFFER_SIZE ];
int handle  = 0;
int i2c_bus = 2;

const unsigned char numbertable[] =
{
    0x3F, /* 0 */
    0x06, /* 1 */
    0x5B, /* 2 */
    0x4F, /* 3 */
    0x66, /* 4 */
    0x6D, /* 5 */
    0x7D, /* 6 */
    0x07, /* 7 */
    0x7F, /* 8 */
    0x6F, /* 9 */
    0x77, /* a */
    0x7C, /* b */
    0x39, /* C */
    0x5E, /* d */
    0x79, /* E */
    0x71, /* F */
};

int i2c_write( void *buf, int len )
{
    int rc = -1;
    
    if ( write( handle, buf, len ) != len )
    {
        printf( "I2C write failed: %s\n", strerror( errno ) );
    }
    else
    {
        rc = 0;
    }
    
    return rc;
}

void buffer_clear( void )
{
    int i;
    
    for ( i = 0; i < BUFFER_SIZE; i++ )
    {
        displaybuffer[ i ] = 0;
    }
}

void buffer_write_digit( int digit, int number )
{
    if ( ( digit > 4 ) || ( number > 0xF ) )
        return;

    displaybuffer[ digit ] = numbertable[ number ];
}

int ht16k33_update( void )
{
    unsigned short buf[ BUFFER_SIZE ];
    int i;
    
    for( i = 0; i < BUFFER_SIZE; i++ )
    {
        buf[ i ] = htobe16( displaybuffer[ i ] );
    }

    return i2c_write( buf, sizeof( displaybuffer ) );
}

int ht16k33_brightness( unsigned char brightness )
{
    unsigned char buf[ 2 ];

    if ( brightness > 15 )
        brightness = 15;
        
    buf[ 0 ] = ( HT16K33_CMD_BRIGHTNESS | brightness );
    
    return i2c_write( buf, 1 );
}

int ht16k33_blink_rate( unsigned char rate )
{
    unsigned char buf[ 2 ];

    if ( rate > 3 )
        rate = 0; // turn off if not sure
        
    buf[ 0 ] = ( HT16K33_BLINK_CMD | HT16K33_BLINK_DISPLAYON | ( rate << 1 ) );
    
    return i2c_write( buf, 1 );
}

int ht16k33_init( void )
{
    unsigned char buf[ 2 ];
    int rc = 0;
        
    buf[ 0 ] = HT16K33_CMD_SETUP;
    if ( i2c_write( buf, 1 ) == 0 )
    {    
        ht16k33_blink_rate( HT16K33_BLINK_OFF );
        ht16k33_brightness( 7 );
        ht16k33_update();
    }
    else
    {
        rc = 1;
    }
    
    return rc;
}

int main( int argc, char *argv[] )
{
    char filename[ 20 ];

    snprintf( filename, 19, "/dev/i2c-%d", i2c_bus );
    handle = open( filename, O_RDWR );
    if ( handle < 0 )
    {
        fprintf( stderr, "Error opening device: %s\n", strerror( errno ) );
        exit( 1 );
    }

    if ( ioctl( handle, I2C_SLAVE, HT16K33_ADDR ) < 0 )
    {
        fprintf( stderr, "IOCTL Error: %s\n", strerror( errno ) );
        exit( 1 );
    }

    /* Usage */
    if ( ht16k33_init() == 0 )
    {
        if ( argc > 1 )
        {
            int n = ( int )strtoul( argv[ 1 ], NULL, 0 );
            
            if ( n < 8 )
            {
                buffer_write_digit( 0, n );
                displaybuffer[ 2 ] = ( 1 << n );
                displaybuffer[ 4 ] = ( 1 << n );
                ht16k33_update();                
            }
        }
        else
        {
            int i;
            
            for ( i = 9; i >= 0; i-- )
            {
                buffer_write_digit( 4, i );
                ht16k33_update();                
                sleep( 1 );
            }
        }
    }

    close( handle );
    return 0;
}


