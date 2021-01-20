def metode_caesar():

    S = input()
    lst = input().split()
    n = lst[0]
    T = lst[1]

    N = int(n)
    res1 = list(S)
    

    for i in range (len(S)):
        res1[i] = chr(ord(S[i])-N-10)

    S = "".join(res1)

    p = len(T)

    hasil = list(S)

    for i in range (len(res1)):
        hasil[i] = chr(ord(res1[i])^ord(T[i%p]))

    S = "".join(hasil)
    print(S)

metode_caesar()
