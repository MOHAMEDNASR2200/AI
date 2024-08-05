def cal_det(lis):
    value=0
    switch=-1
    sign=2
    for i in range(len(lis[0])):
        lis1=[]
        for j in range(1,len(lis[0])):
            lis2=[]
            for s in range(len(lis[0])):
                if s!=i:
                    lis2.append(lis[j][s])
            lis1.append(lis2)
        p=(lis1[0][0]*lis1[1][1])-(lis1[0][1]*lis1[1][0])
        value=value+((lis[0][i]*(switch**(sign+i)))*p)
    return value
def transpose(l):
    Tran=[]
    for i in range(len(l)):
        item=[]
        for j in range(len(l)):
            item.append(l[j][i])
        Tran.append(item)
    return Tran
def inverse(A,D):
    B=[]
    switch=-1
    sign=2
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            lis1=[]
            for z in range(len(A)):
                lis2=[]
                if z!=i:
                    for y in range(len(A[0])):
                        if y!=j:
                            lis2.append(A[z][y])
                    lis1.append(lis2)
            value=((lis1[0][0]*(lis1[1][1]))-(lis1[1][0]*lis1[0][1]))*(switch**sign)*(1/D)
            sign=sign+1
            row.append(value)
        B.append(row)
    return B
def Multiplication(lis,lis1):
    result=[]
    for i in range(len(lis)):#row index
        row=[]
        for s in range(len(lis1[0])):#column index
            res=0
            for j in range(len(lis[0])):#operation 
                res=res+(lis[i][j]*lis1[j][s])
            row.append(res)
        result.append(row)
    return result
Matrix=[[1,2,3],[0,1,4],[5,6,0]]
det=cal_det(Matrix)
tran=transpose(Matrix)
Inverse=inverse(tran,det)
F_result=Multiplication(Matrix,Inverse)
print(F_result)