# ** _0 _1 _2 **    **    ** 12 13 14 **
#    _5 _4 _3    _6 _7 _8    17 16 15
#       **    ** 11 10 _9 **    **
#
#             ** 18 19 20 **
#                23 22 21
#                   **
class Pyraminx:
    def __init__(s):
        s.X = [0]*6+[1]*6+[2]*6+[3]*6

    def to_tuple(s):
        return tuple(s.X)

    def from_tuple(s, X):
        s.X = list(X)

    def move(s, m):
        if m=="L":
            s.X[ 4], s.X[11], s.X[18] = s.X[18], s.X[ 4], s.X[11]
            s.X[ 3], s.X[10], s.X[23] = s.X[23], s.X[ 3], s.X[10]
            s.X[ 5], s.X[ 6], s.X[19] = s.X[19], s.X[ 5], s.X[ 6]
        elif m=="L'":
            s.X[ 4], s.X[11], s.X[18] = s.X[11], s.X[18], s.X[ 4]
            s.X[ 3], s.X[10], s.X[23] = s.X[10], s.X[23], s.X[ 3]
            s.X[ 5], s.X[ 6], s.X[19] = s.X[ 6], s.X[19], s.X[ 5]
        elif m=="R":
            s.X[ 9], s.X[16], s.X[20] = s.X[20], s.X[ 9], s.X[16]
            s.X[ 8], s.X[15], s.X[19] = s.X[19], s.X[ 8], s.X[15]
            s.X[10], s.X[17], s.X[21] = s.X[21], s.X[10], s.X[17]
        elif m=="R'":
            s.X[ 9], s.X[16], s.X[20] = s.X[16], s.X[20], s.X[ 9]
            s.X[ 8], s.X[15], s.X[19] = s.X[15], s.X[19], s.X[ 8]
            s.X[10], s.X[17], s.X[21] = s.X[17], s.X[21], s.X[10]
        elif m=="U":
            s.X[ 2], s.X[12], s.X[ 7] = s.X[ 7], s.X[ 2], s.X[12]
            s.X[ 1], s.X[17], s.X[ 6] = s.X[ 6], s.X[ 1], s.X[17]
            s.X[ 3], s.X[13], s.X[ 8] = s.X[ 8], s.X[ 3], s.X[13]
        elif m=="U'":
            s.X[ 2], s.X[12], s.X[ 7] = s.X[12], s.X[ 7], s.X[ 2]
            s.X[ 1], s.X[17], s.X[ 6] = s.X[17], s.X[ 6], s.X[ 1]
            s.X[ 3], s.X[13], s.X[ 8] = s.X[13], s.X[ 8], s.X[ 3]
        elif m=="B":
            s.X[ 0], s.X[22], s.X[14] = s.X[14], s.X[ 0], s.X[22]
            s.X[ 1], s.X[23], s.X[15] = s.X[15], s.X[ 1], s.X[23]
            s.X[ 5], s.X[21], s.X[13] = s.X[13], s.X[ 5], s.X[21]
        elif m=="B'":
            s.X[ 0], s.X[22], s.X[14] = s.X[22], s.X[14], s.X[ 0]
            s.X[ 1], s.X[23], s.X[15] = s.X[23], s.X[15], s.X[ 1]
            s.X[ 5], s.X[21], s.X[13] = s.X[21], s.X[13], s.X[ 5]
        else:
            raise Exception("error")

    def str(s):
        T = [
            "\x1b[41mL\x1b[0m",
            "\x1b[42mF\x1b[0m",
            "\x1b[44mR\x1b[0m",
            "\x1b[43mD\x1b[0m",
        ]
        return (
            T[s.X[ 0]]+T[s.X[ 0]]+T[s.X[ 1]]+T[s.X[ 2]]+T[s.X[ 2]]+" "+T[s.X[ 7]]+" "+T[s.X[12]]+T[s.X[12]]+T[s.X[13]]+T[s.X[14]]+T[s.X[14]]+"\n"+
            " "       +T[s.X[ 5]]+T[s.X[ 4]]+T[s.X[ 3]]+" "+T[s.X[ 6]]+T[s.X[ 7]]+T[s.X[ 8]]+" "+T[s.X[17]]+T[s.X[16]]+T[s.X[15]]+"\n"+
            " "       +" "       +T[s.X[ 4]]+" "+T[s.X[11]]+T[s.X[11]]+T[s.X[10]]+T[s.X[ 9]]+T[s.X[ 9]]+" "+T[s.X[16]]+"\n"+
            "\n"+
            " "       +" "       +" "       +" "+T[s.X[18]]+T[s.X[18]]+T[s.X[19]]+T[s.X[20]]+T[s.X[20]]+"\n"+
            " "       +" "       +" "       +" "       +" "+T[s.X[23]]+T[s.X[22]]+T[s.X[21]]+"\n"+
            " "       +" "       +" "       +" "       +" "       +" "+T[s.X[22]]+"\n")

    def pair(s):
        return (
            s.X[ 0]==s.X[ 5] and s.X[22]==s.X[23] or
            s.X[ 0]==s.X[ 1] and s.X[14]==s.X[13] or
            s.X[ 2]==s.X[ 1] and s.X[12]==s.X[13] or
            s.X[ 2]==s.X[ 3] and s.X[ 7]==s.X[ 6] or
            s.X[ 4]==s.X[ 3] and s.X[11]==s.X[ 6] or
            s.X[ 4]==s.X[ 5] and s.X[18]==s.X[23] or

            s.X[ 7]==s.X[ 8] and s.X[12]==s.X[17] or
            s.X[ 9]==s.X[ 8] and s.X[16]==s.X[17] or
            s.X[ 9]==s.X[10] and s.X[20]==s.X[19] or
            s.X[11]==s.X[10] and s.X[18]==s.X[19] or

            s.X[14]==s.X[15] and s.X[22]==s.X[21] or
            s.X[16]==s.X[15] and s.X[20]==s.X[21]
        )

    def block(s):
        return (
            s.X[ 0]==s.X[ 5] and s.X[22]==s.X[23] and s.X[ 0]==s.X[ 1] and s.X[14]==s.X[13] or
            s.X[ 2]==s.X[ 1] and s.X[12]==s.X[13] and s.X[ 2]==s.X[ 3] and s.X[ 7]==s.X[ 6] or
            s.X[ 4]==s.X[ 3] and s.X[11]==s.X[ 6] and s.X[ 4]==s.X[ 5] and s.X[18]==s.X[23] or

            s.X[ 2]==s.X[ 3] and s.X[ 7]==s.X[ 6] and s.X[ 7]==s.X[ 8] and s.X[12]==s.X[17] or
            s.X[ 9]==s.X[ 8] and s.X[16]==s.X[17] and s.X[ 9]==s.X[10] and s.X[20]==s.X[19] or
            s.X[11]==s.X[10] and s.X[18]==s.X[19] and s.X[ 4]==s.X[ 3] and s.X[11]==s.X[ 6] or

            s.X[ 7]==s.X[ 8] and s.X[12]==s.X[17] and s.X[ 2]==s.X[ 1] and s.X[12]==s.X[13] or
            s.X[ 0]==s.X[ 1] and s.X[14]==s.X[13] and s.X[14]==s.X[15] and s.X[22]==s.X[21] or
            s.X[16]==s.X[15] and s.X[20]==s.X[21] and s.X[ 9]==s.X[ 8] and s.X[16]==s.X[17] or

            s.X[ 4]==s.X[ 5] and s.X[18]==s.X[23] and s.X[11]==s.X[10] and s.X[18]==s.X[19] or
            s.X[ 9]==s.X[10] and s.X[20]==s.X[19] and s.X[16]==s.X[15] and s.X[20]==s.X[21] or
            s.X[14]==s.X[15] and s.X[22]==s.X[21] and s.X[ 0]==s.X[ 5] and s.X[22]==s.X[23]
        )

    def v(s):
        #return s.X[ 0]==s.X[ 2]==s.X[ 4]==0 and int(s.X[ 1]==0 and s.X[13]==2)+int(s.X[ 3]==0 and s.X[ 6]==1)>=2
        return (
            s.X[ 0]==s.X[ 2]==s.X[ 4]==0 and int(s.X[ 1]==0 and s.X[13]==2)+int(s.X[ 3]==0 and s.X[ 6]==1)+int(s.X[ 5]==0 and s.X[23]==3)>=2 or
            s.X[ 7]==s.X[ 9]==s.X[11]==1 and int(s.X[ 6]==1 and s.X[ 3]==0)+int(s.X[ 8]==1 and s.X[17]==2)+int(s.X[10]==1 and s.X[19]==3)>=2 or
            s.X[12]==s.X[14]==s.X[16]==2 and int(s.X[13]==2 and s.X[ 1]==0)+int(s.X[15]==2 and s.X[21]==3)+int(s.X[17]==2 and s.X[ 8]==1)>=2 or
            s.X[18]==s.X[20]==s.X[22]==3 and int(s.X[19]==3 and s.X[10]==1)+int(s.X[21]==3 and s.X[15]==2)+int(s.X[23]==3 and s.X[ 5]==0)>=2
        )

    def oneface(s):
        return (
            s.X[ 0]==s.X[ 2]==s.X[ 4]==0 and int(s.X[ 1]==0 and s.X[13]==2)+int(s.X[ 3]==0 and s.X[ 6]==1)+int(s.X[ 5]==0 and s.X[23]==3)==3 or
            s.X[ 7]==s.X[ 9]==s.X[11]==1 and int(s.X[ 6]==1 and s.X[ 3]==0)+int(s.X[ 8]==1 and s.X[17]==2)+int(s.X[10]==1 and s.X[19]==3)==3 or
            s.X[12]==s.X[14]==s.X[16]==2 and int(s.X[13]==2 and s.X[ 1]==0)+int(s.X[15]==2 and s.X[21]==3)+int(s.X[17]==2 and s.X[ 8]==1)==3 or
            s.X[18]==s.X[20]==s.X[22]==3 and int(s.X[19]==3 and s.X[10]==1)+int(s.X[21]==3 and s.X[15]==2)+int(s.X[23]==3 and s.X[ 5]==0)==3
        )

M = ["L", "L'", "R", "R'", "U", "U'", "B", "B'"]
pyra = Pyraminx()

P = [set() for _ in range(12)]
P[0].add(pyra.to_tuple())
for d in range(12):
    print(d, len(P[d]))
    for p in P[d]:
        for m in M:
            pyra.from_tuple(p)
            pyra.move(m)
            p2 = pyra.to_tuple()
            f = True
            for d2 in range(d+1):
                if p2 in P[d2]:
                    f = False
                    break
            if f:
                P[d+1].add(p2)

def solve(p):
    ans = []
    pyra = Pyraminx()
    pyra.from_tuple(p)
    for d in range(12):
        if p in P[d]:
            break
    while d>0:
        for m in range(len(M)):
            pyra.move(M[m])
            if pyra.to_tuple() in P[d-1]:
                ans += [M[m]]
                d -= 1
                break
            pyra.move(M[m^1])
    return ans

for p in P[11]:
    pyra.from_tuple(p)
    print(*(M[M.index(a)^1] for a in solve(p)[::-1]))
    print(pyra.str())

total = [0]*12
no = [0]*12
pair = [0]*12
block = [0]*12
v = [0]*12
oneface = [0]*12

for d in range(12):
    for p in P[d]:
        pyra.from_tuple(p)
        total[d] += 1
        if pyra.oneface():
            oneface[d] += 1
        if pyra.v():
            v[d] += 1
        elif pyra.block():
            block[d] += 1
        elif pyra.pair():
            pair[d] += 1
        else:
            no[d] += 1
    print(d, total[d], no[d], pair[d], block[d], v[d], oneface[d])

T = [0]*5
T[0] = 1
for _ in range(4):
    for j in range(4)[::-1]:
        T[j+1] += T[j]*2
print(T)

total2 = [0]*16
no2 = [0]*16
pair2 = [0]*16
block2 = [0]*16
v2 = [0]*16
oneface2 = [0]*16

for d in range(12):
    for i in range(5):
        total2[d+i] += total[d]*T[i]
        no2[d+i] += no[d]*T[i]
        pair2[d+i] += pair[d]*T[i]
        block2[d+i] += block[d]*T[i]
        v2[d+i] += v[d]*T[i]
        oneface2[d+i] += oneface[d]*T[i]

for d in range(16):
    print(d, total2[d], no2[d], pair2[d], block2[d], v2[d], oneface2[d])

PV = [set() for _ in range(12)]
for d in range(12):
    for p in P[d]:
        pyra.from_tuple(p)
        if pyra.v():
            PV[0].add(p)

for d in range(12):
    for p in PV[d]:
        for m in M:
            pyra.from_tuple(p)
            pyra.move(m)
            p2 = pyra.to_tuple()
            f = True
            for d2 in range(d+1):
                if p2 in PV[d2]:
                    f = False
                    break
            if f:
                PV[d+1].add(p2)
    print(d, len(PV[d]))

def solve_v(p):
    ans = []
    pyra = Pyraminx()
    pyra.from_tuple(p)
    for d in range(12):
        if p in PV[d]:
            break
    while d>0:
        for m in range(len(M)):
            pyra.move(M[m])
            if pyra.to_tuple() in PV[d-1]:
                ans += [M[m]]
                d -= 1
                break
            pyra.move(M[m^1])
    return ans

for p in PV[7]:
    pyra.from_tuple(p)
    print(*(M[M.index(a)^1] for a in solve(p)[::-1]))
    print(*solve_v(p))
    print(pyra.str())

PV2 = [0]*12
for d in range(12):
    for p in PV[d]:
        for d2 in range(12):
            if p in P[d2]:
                s = d2
        for t in range(5):
            if s+t>=6:
                PV2[d] += T[t]
for d in range(12):
    print(d, PV2[d])
