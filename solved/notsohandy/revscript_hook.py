#! /usr/bin/python3
import angr
import claripy

def FakeStrlen(state):
    print("FakeStrlen called!!")
    print("index ", state.mem[state.regs.rbp-0x1c].int)
    index = state.mem[state.regs.rbp-0x1c].int
    realvalue = 0x31 - index.concrete
    print("realvalue: ", realvalue)
    state.regs.rax = claripy.BVV(realvalue, 64)

def FakeStrlenFixed(state):
    print("FakeStrlen called!!")
    state.regs.rax = claripy.BVV(0x31,64)
BASE = 0X400000
TARGET = 0x01422
#
chars = [claripy.BVS("c_"+str(i), size=8) for i in range(0x31)]
flag = claripy.Concat(*chars)
project = angr.Project("./notsohandy", auto_load_libs=False)
# project.hook_symbol('strlen', FakeStrlen(), replace=True)
# project.hook_symbol("strlen", angr.SIM_PROCEDURES['libc']['strlen']())
project.hook(BASE+0x00012cc, FakeStrlenFixed, length=5)
project.hook(BASE+0x0001400, FakeStrlenFixed, length=5)
project.hook(BASE+0x00012f8, FakeStrlen, length=5)
project.hook(BASE+0x0001319, FakeStrlen, length=5)
project.hook(BASE+0x0001362, FakeStrlen, length=5)
project.hook(BASE+0x0001383, FakeStrlen, length=5)
initial_state = project.factory.entry_state(args=["./notsohandy", flag], replace=True)
initial_state.options.add(angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS)
initial_state.options.add(angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY)
initial_state.options.add(angr.options.LAZY_SOLVES)

for i in chars:
    initial_state.solver.add(i >= 0x20)
    initial_state.solver.add(i <= 0x7f)

simul = project.factory.simulation_manager(initial_state)
while len(simul.active) > 0:
    #print(flag)
    print(simul, simul.active)
#    for i in simul.active:
#        print(i, "rax: ", i.regs.rax)
#        print(i, "rbx: ", i.regs.rbx)
#        print(i, "rcx: ", i.regs.rcx)
#        print(i, "rdx: ", i.regs.rdx)
#        print(i, "rdi: ", i.regs.rdi)
#        print(i, "rsi: ", i.regs.rsi)
#        print(i, "rsp: ", i.regs.rsp)
#        print(i, "rbp: ", i.regs.rbp)
#        print(i.dbg_print_stack(15))
#        print(i.mem[i.regs.rbp-0x1c].int)
    simul.explore(find=TARGET+BASE, n=1, num_find=1)
    if len(simul.found) > 0:
        print("FOUND")
        print(simul.found[0].solver.eval(flag).to_bytes(49,byteorder="big", signed=True))
        break
