#! /usr/bin/python3
import angr
import claripy


TARGET = 0x004033c2

chars = [claripy.BVS(f"c_{i}", size = 8 ) for i in range(0x17)]
flag = claripy.Concat(*chars)
project = angr.Project("./cracksymb")
initial_state = project.factory.entry_state(stdin=flag)
initial_state.options.add(angr.options.LAZY_SOLVES)

for i in chars:
    initial_state.solver.add( i>= 0x20 )
    initial_state.solver.add( i<= 0x7e )

simul = project.factory.simulation_manager(initial_state)
to_avoid = [0x00403369,0x0040317c,0x00402f79,0x00402d77,0x00402b7c,0x0040297c,0x00402781,0x00402576,0x00402379,0x00401f7d,0x00401d7a,0x00401b6d,0x00401978,0x0040177f,0x00401592,0x0040139d,0x004011af,0x00400fac,0x00400da6,0x00400bad,0x004009ac,0x00400797]
while len(simul.active) > 0:
    print(simul, simul.active)
    simul.explore(find=TARGET, n=1, num_find=1, avoid=to_avoid)

    if simul.found:
        print("FOUND")
        print(simul.found[0].posix.dumps(0))

        break
