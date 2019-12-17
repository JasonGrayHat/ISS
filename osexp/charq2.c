#include <linux/init.h>   
#include <linux/module.h> 
#include <linux/kernel.h>
#include <linux/device.h>
#include <linux/fs.h>    
#include <linux/uaccess.h>

#define  DEVICE_NAME "JaesungLee-char" 
#define  CLASS_NAME  "ebb"  

// Prototypes
static int     dev_open(struct inode *inode, struct file *f);
static int     dev_release(struct inode *inode, struct file *f);
static ssize_t dev_read(struct file *f, char *buf, size_t len, loff_t *off);
static ssize_t dev_write(struct file *f, const char __user *buf, size_t len, loff_t *off);

// Module info
MODULE_LICENSE("GPL"); 
MODULE_AUTHOR("Jaesung Lee");
MODULE_DESCRIPTION("Lab2 Quiz"); 
MODULE_VERSION("N/A"); 

static int            majorNumber;
static char           message[256]={0};
static short          size_of_message;
static int            numberOpens=0; 
static struct class*  ebbcharClass  = NULL;
static struct device* ebbcharDevice = NULL;

static struct file_operations fops =
{
  .open = dev_open,
  .read = dev_read,
  .write = dev_write,
  .release= dev_release,
};

static int __init ebbchar_init(void){
      printk(KERN_INFO "Initializing EBBChar LKM\n");
  // Create char device
  if ((majorNumber = register_chrdev(0, DEVICE_NAME, &fops)) < 0)
    {
      printk(KERN_ALERT "EBBChar failed to register a major number\n");
      return majorNumber;
    }
   printk(KERN_INFO "EBBChar: major number %d\n", majorNumber);

// Register the device class
   ebbcharClass = class_create(THIS_MODULE, CLASS_NAME);
   if (IS_ERR(ebbcharClass))
     {
       unregister_chrdev(majorNumber, DEVICE_NAME);
       printk(KERN_ALERT "Failed to register device class\n");
       return PTR_ERR(ebbcharClass); 
   }

   printk(KERN_INFO "device class registered correctly\n");

// Register the device driver
   ebbcharDevice = device_create(ebbcharClass, NULL, MKDEV(majorNumber, 0), NULL, DEVICE_NAME);
   if (IS_ERR(ebbcharDevice))
     {
       class_destroy(ebbcharClass);
       unregister_chrdev(majorNumber, DEVICE_NAME);
       printk(KERN_ALERT "Failed to create the device\n");
       return PTR_ERR(ebbcharDevice);
     }
     printk(KERN_ALERT "EBBchar to create the device driver\n");
     return 0;
 }

static void __exit ebbchar_exit(void) 
{
  // Destroy the device
  device_destroy(ebbcharClass, MKDEV(majorNumber, 0));
  class_unregister(ebbcharClass);
  class_destroy(ebbcharClass);
  unregister_chrdev(majorNumber, DEVICE_NAME);     
  printk(KERN_INFO "Bye LKM\n");
}

static int dev_open(struct inode *inode, struct file *f)
{
    numberOpens++;
    printk(KERN_INFO " Device was open \n");
    return 0;
}

static ssize_t dev_read(struct file *f, char *buf, size_t len, loff_t *off)
{
   int error_count = 0;
   // copy_to_user has the format ( * to, *from, size) and returns 0 on success
   error_count = copy_to_user(buf, message, size_of_message);
 
   if (error_count==0){            // if true then have success
      printk(KERN_INFO "EBBChar: Sent %d characters to the user\n", size_of_message);
      return (size_of_message=0);  // clear the position to the start and return 0
   }
   else {
      printk(KERN_INFO "EBBChar: Failed to send %d characters to the user\n", error_count);
      return -EFAULT;              // Failed -- return a bad address message (i.e. -14)
   }

}

static ssize_t dev_write(struct file *f, const char *buf, size_t len, loff_t *off)
{ 
   sprintf(message,"%s(%zu letters)", buf, len);
   size_of_message=strlen(message);
   printk(KERN_INFO "EBBChar recieved characters\n");
   return len;
}

static int dev_release(struct inode *inode, struct file *f)
{
  printk(KERN_INFO "Device closed");
  return 0;
}

module_init(ebbchar_init);
module_exit(ebbchar_exit);

