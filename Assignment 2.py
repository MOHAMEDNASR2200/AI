import pandas as pd
A=pd.read_csv(r"C:\Users\Sara\Downloads\Telegram Desktop\insurance-data.csv")
#print(A.shape)
#print(A.info())
#print(A.describe())
#print(A["smoker"].nunique())
#print(A["region"].nunique())
#print(A.columns)
#Question:1
Q_1=A.loc[(A["smoker"]=="yes")&(A["sex"]=="female")]
Q_1_1=A.loc[A["smoker"]=="yes"]
print((len(Q_1)/len(Q_1_1))*100)
#Question:2
Q_2=max(A["charges"])
Q_2_2=A["region"][A["charges"]==Q_2]
print(Q_2_2)
#Question:3
Q_3=A["sex"][A["charges"]==Q_2]
print(Q_3)
#Question:4
Q_4=Q_1["age"].unique()
lis=[]
for i in Q_4:
    B=len(Q_1.loc[Q_1["age"]==i])/len(A.loc[(A["age"]==i)&(A["sex"]=="female")])*100
    lis.append(B)
Q_4_4=sum(lis)/len(Q_1)
print(Q_4_4)
#Question:5
Q_5=len(A.loc[(A["children"]>0)&(A["sex"]=="male")])
Q_5_5=len(A.loc[A["sex"]=="male"])
print((Q_5/Q_5_5)*100)
#Question:6
Q_6=len(A.loc[(A["children"]>0)&(A["sex"]=="female")])
Q_6_6=len(A.loc[A["sex"]=="female"])
print((Q_6/Q_6_6)*100)
#Question:7
Q_7=max(A.loc[A["sex"]=="male"]["children"])
print(Q_7)
#Question:8
Q_8=max(A.loc[A["sex"]=="female"]["children"])
print(Q_8)
#Question:9
Q_9=A["region"].unique()
lis1=[]
for j in Q_9:
    s=sum(A.loc[(A["region"]==j)&(A["sex"]=="female")]["charges"])
    lis1.append(s)
print(Q_9[lis1.index(max(lis1))])
