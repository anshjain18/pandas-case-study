import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data=pd.read_csv("startup_funding.csv",skipinitialspace=True,)


data["CityLocation"].fillna("Dummy",inplace=True)
data["AmountInUSD"].fillna("0",inplace=True)
data["InvestorsName"].fillna("Dummy",inplace=True)
data["InvestorsName"].replace(" ","Dummy",inplace=True)
ext_inv=[]

for i in data.InvestorsName:
    for j in i.split(","):
        if "undisclosed" not in j and "Undisclosed" not in j:
            ext_inv.append(j.strip())

ext_inv=np.array(ext_inv)


ext_inv=pd.Index(ext_inv)

labels=ext_inv.value_counts().index[0:5]
sizes=ext_inv.value_counts().values[0:5]
print("Investors_Name","\t\t\t","Number_Of_Times_They_Invested")
for i in range(5):
    print('{:30}'.format(labels[i]),sizes[i])


