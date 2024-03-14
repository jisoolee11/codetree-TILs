from collections import deque

def move_atoms():
    global atoms
    
    for _ in range(len(atoms)):
        x, y, m, s, d = atoms.popleft() 
        nx = (x + (dx[d]*s)) % N
        ny = (y + (dy[d]*s)) % N
        atoms.append((nx, ny, m, s, d))

    atoms = deque(sorted(list(atoms), key = lambda x: (x[0], x[1])))


def atom_synthesis():
    ax, ay = -1, -1
    all_synthesis = []
    synthesis = []
    for _ in range(len(atoms)):
        x, y, m, s, d = atoms.popleft()
        if ax == x and ay == y:
            synthesis.append((x, y, m, s, d))
        else:
            if synthesis:
                all_synthesis.append(synthesis)
            synthesis = [(x, y, m, s, d)]
        ax, ay = x, y
    
    for asyn in all_synthesis:
        x, y, a_m, a_s, a_do, a_de = -1, -1, 0, 0, False, False
        if len(asyn) > 1:
            for a in asyn:
                x, y = a[0], a[1]
                a_m += a[2]
                a_s += a[3]
                if a[4] % 2 == 0:
                    a_de = True
                else:
                    a_do = True
            if a_do == True and a_de == True and int(a_m/5) > 0:
                for i in range(1, 8, 2):
                    atoms.append((x, y, int(a_m/5), int(a_s/len(asyn)), i))
            else:
                for i in range(0, 8, 2):
                    atoms.append((x, y, int(a_m/5), int(a_s/len(asyn)), i))
        

N, M, K = map(int, input().split())
atoms = deque()
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    atoms.append((x, y, m, s, d))
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    move_atoms()
    atom_synthesis()

total = 0
for a in atoms:
    total += a[2]

print(total)