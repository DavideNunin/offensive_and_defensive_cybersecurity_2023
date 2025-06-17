import z3
res = []
precomputed_table = []
def add_constr(flag,solver):
    for i in range(len(flag)):
        length = len(flag)-i
        if len(flag)-4 <= i:
            break
        if length < 5:
            length = len(flag)-i
            cycles = length & 0xffffffff
        else:
            cycles = 4
        check = xhashe

solver = z3.Solver()
flag = [z3.BitVec("char_{i}", 8) for i in range(0x2e)]

add_constr(flag,solver)
print(solver.assertions())
check = solver.check()
m = solver.model()
print(m)
