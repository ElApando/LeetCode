def climbStairs( n: int) -> int:

    Guarda = [0] * (n + 1); Guarda[0] = 1; Guarda[1] = 1

    for i in range(1, n + 1,1):
        Guarda[i] = Guarda[i-1] + Guarda[i-2]
        print(Guarda,Guarda[i-1],Guarda[i-2],i)
    
    return Guarda[-1]

a = [2,3]

for i in range(0,len(a),1):
    Activo = climbStairs(a[i])
    print(Activo)