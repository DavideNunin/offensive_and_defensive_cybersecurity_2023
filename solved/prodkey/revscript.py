#! /usr/bin/python3
import angr
import claripy
import pwn

TARGET = 0X400DEB

chars = [claripy.BVS(f"c_{i}", size = 8) for i in range(32)]
flag = claripy.Concat(*chars)
project = angr.Project("./prodkey")
initial_state = project.factory.entry_state()


for char in chars:
    initial_state.solver.add( char >= 0x20 )
    initial_state.solver.add( char <= 0x7e )

simgr = project.factory.simulation_manager(initial_state)
while len(simgr.active) > 0:
    print(simgr, simgr.active)
    simgr.explore(find=TARGET, n=1, num_find=1)

    if simgr.found:
        print("Found")
        for i in initial_state.solver.constraints:
            print(i)
        r = pwn.remote("bin.training.offdef.it", 2021)
        r.send(simgr.found[0].posix.dumps(0))
        r.interactive()

        print(simgr.found[0].posix.dumps(0).hex())
        break
