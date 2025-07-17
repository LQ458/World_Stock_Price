import pandas as pd
f=open("World-Stock-Prices-Dataset.csv","r")
df=pd.read_csv(f)
#1
a=df.sort_values(by="High",ascending=False)
print(a.head(1))
#2
d={}
d2={}
for x,y in df.iterrows():
    # print(y[6])
    if y[6] in d:
        d[y[6]][0]+=y[5]
        d[y[6]][1]+=1
    else:
        d[y[6]]=[y[5],1]
for x in d.keys():
    d2[x]=(d[x][0]/d[x][1])
print(d2)
#3
d3={}
for x,y in df.iterrows():
    if y[9] in d3:
        d3[y[9]]+=1
    else:
        d3[y[9]]=1
print(d3)
#question 7
d4={}
print(df["Brand_Name"].unique())
for x in df["Brand_Name"].unique():
    d4[x]=["","",0]
# print(df["Brand_Name"].unique()[0])
mx=0
for i in df["Brand_Name"].unique():
    l=[]
    for x,y in df.iterrows():
        # print(i,y[6])
        if y[6]!=i:
            continue
        l.append([y[0],y[4]])
    # print(sorted(l,key=lambda x: x[1],reverse=True))
    # break
    for x in range(len(l)-5):
        a=l[x][0]
        b=l[x+5][0]
        cnt=0
        for y in range(5):
            cnt+=l[x+y][1]
        # print(d4[i][2])
        mx=max(mx,cnt)
        if d4[i][2]<=cnt:
            d4[i][2]=cnt
            d4[i][0]=a
            d4[i][1]=b
    # print(mx)
    # break
print(d4)