#! /usr/bin/python3
import pwn
import sys

pwn.context.terminal = ['tmux', 'split-window', '-h']
args = sys.argv
if "remote" not in args:
    r = pwn.process("./dynamism")
    pwn.context.log_level = "DEBUG"
    pwn.context.arch = "amd64"
    if "gdb" in args:
        print("debug")
        gdb = pwn.gdb.attach(r, '''
            b main
        ''')
r.sendline('ciaone')
r.interactive()
