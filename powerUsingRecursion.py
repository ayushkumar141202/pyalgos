N=int(input("Enter the number"))
P=int(input("Enter the power"))
if P == 0:
    print(N*P(N, P-1))
