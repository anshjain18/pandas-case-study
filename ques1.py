import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data=pd.read_csv("startup_funding.csv",skipinitialspace=True,)
#print(data.CityLocation)
data["CityLocation"].fillna("Dummy",inplace=True)
data["AmountInUSD"].fillna("0",inplace=True)
ext_city=[]
def seperateCity(city):
    if len(city.split("/")) ==2:
        ext_city.append(city.split('/')[1].strip())
    return city.split('/')[0].strip()



data["CityLocation"]=data["CityLocation"].apply(seperateCity)
data["CityLocation"].replace("Delhi","New Delhi",inplace=True)
data["CityLocation"].replace("bangalore","Bangalore",inplace=True)
for i in data.CityLocation:
    ext_city.append(i)
data2=data.CityLocation.value_counts()
# print(type(data.CityLocation))
ext_city=np.array(ext_city)
labels=[]
sizes=[]

array,counts=np.unique(ext_city,return_counts=True)
# print(len(array),len(counts))
for i in range(len(array)):
    if array[i]=="Bangalore" or array[i]=="New Delhi" or array[i]=="Noida" or array[i]=="Gurgaon" or array[i]=="Mumbai":
        labels.append(array[i])
        sizes.append(counts[i])
print(sizes)

plt.bar(labels,sizes,width=0.5)
plt.xlabel("CityLOcation")
plt.ylabel("Number_Of_Times_Funding_Received")
plt.show()
# print(ext_city)
# print(data2)

