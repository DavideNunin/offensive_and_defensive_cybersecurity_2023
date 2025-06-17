#include<stdio.h>

int main(){
    char xor[]={0x1b,0x51,0x17,0x2a,0x1e,0x4e,0x3d,0x10,0x17,0x46,0x49,0x14,0x3d};
    char firsthalf[14];
    char magic[]={0xeb,0x51,0xb0,0x13,0x85,0xb9,0x1c,0x87,0xb8,0x26,0x8d,0x07};
    char current=(-69);
    char secondhalf[12];
    for(int i=0;i<13;i++){
            firsthalf[i]=xor[i] ^ "babuzz"[i % 6];
    }
    firsthalf[14]=0;
    for(int i=0;i<12;i++){
        secondhalf[i]=magic[i]-current;
        current=magic[i];
    }
    secondhalf[13]=0;




    printf("%s%s",firsthalf,secondhalf);

    return 0;
}




