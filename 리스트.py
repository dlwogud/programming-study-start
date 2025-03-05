N=int(input("정수 N값을 입력하세요.(N=2~10000):\n"))


Num_M=0
for i in range(2,N+1):
    M=2**i-1
    if M>N:
        break
    else: 
        Check=1
        for i in range(2,N):
            if N%i==0:
                Check=0
        if Check==1:
            for i in range(2,M):
                if M%i==0:
                    Check=0

        if Check==1:
            Num_M+=1
            print("메르센 소수%d:%d"%(Num_M,M))









    







    