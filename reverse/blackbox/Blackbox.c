#include <stdio.h>
#include <stdlib.h>

int Usage();
int main (int argc, char *argv[])
{
    int num,cnt,result;
    
    if (argc != 5){
        Usage();
    }
    
    for (cnt=1,num=0;cnt<5;cnt++){
        if (*argv[cnt] !='0' && *argv[cnt] != '1'){
            Usage();
            exit(1);
        }
        else if(*argv[cnt]=='1'){
            num++; //check if there is 1
        }
    }
    printf("------------------------------------\n");
    for (cnt=1;cnt<5;cnt++){
        if(atoi(argv[cnt]) == 0 || atoi(argv[cnt]) ==1){
            printf("[*] Position %d = %d\n", cnt,atoi(argv[cnt]));
        }
    }

    if (num > 0) result = 1;
    else result = 0;
    
    printf("------------------------------------\n");
    printf("[*] Final Output : %d\n", result);

    return 0;
}

int Usage(){
    printf("\nUsage: ./Blackbox 0|1 0|1 0|1 0|1\n\n");
    printf("Please run program with 4 binary(1 or 1) inputs\n\n");
    return -1;
}
