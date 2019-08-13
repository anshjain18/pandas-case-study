import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("startup_funding.csv",skipinitialspace=True,)
data["CityLocation"].fillna("Dummy",inplace=True)
data["AmountInUSD"].fillna("0",inplace=True)
data["InvestorsName"].fillna("Dummy",inplace=True)
data["InvestorsName"].replace("","Dummy",inplace=True)
data["InvestorsName"].replace(np.nan,"Dummy",inplace=True)

data['InvestmentType']= data['InvestmentType'].str.replace("SeedFunding", "Seed Funding")
data['InvestmentType']= data['InvestmentType'].str.replace("Crowd funding", "Crowd Funding")
data['InvestmentType']= data['InvestmentType'].str.replace("PrivateEquity", "Private Equity")
ext_inv=[]
data2=data[(data["InvestmentType"]== "Seed Funding") | (data["InvestmentType"]=="Crowd Funding")]
for i in data2.InvestorsName:
    for j in i.split(","):
        if "undisclosed" not in j and "Undisclosed" not in j:
            ext_inv.append(j.strip())

ext_inv=np.array(ext_inv)
ext_inv=pd.Index(ext_inv)
labels=ext_inv.value_counts().index
sizes=ext_inv.value_counts().values
data3 = data2["StartupName"].value_counts()
data4 = data3[data3.values >0]
# for i in data4.index:
#     print(i)
u = []
# for i in data[data["StartupName"] == "Ola"].InvestorsName:
#     v = i.split(",")
#     for j in v:
#         u.append(j.strip())
# for i in u:
#     print(i)
for i in data4.index:
    dict={}
    for j in data2[data2["StartupName"]==i].InvestorsName:
        v=j.split(",")
        for z in v:
          dict[z]=dict.get(z,0)+1
    for vk in dict:
        for kl in range(len(labels)):
            if labels[kl] == vk:
                sizes[kl] -= dict[vk]-1

c=0
i=0
sizes1=[]
labels1=[]
while c<5:
    if labels[i]!="":
        labels1.append(labels[i])
        sizes1.append(sizes[i])
        print('{:30}'.format(labels[i]) , sizes[i])
        c += 1
    i += 1
plt.bar(labels1,sizes1)

plt.show()
