from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
data= pd.read_csv("consommation.csv")
data["mois_num"]= range(1,13)
X=data[["mois_num"]]
Y=data["consommation_kwh"]
model=LinearRegression()
model.fit(X,Y)
prediction=model.predict([[13]])
print("prédiction pour le mois 13:",prediction[0])
print(list(range(1,13)))
print(data)
print("moyenne:",data["consommation_kwh"].mean())
moyenne=data["consommation_kwh"].mean()
data[data["consommation_kwh"]> moyenne]
mois_sup=data[data["consommation_kwh"]> moyenne]
print("\nmois avec une consommation supérieure à la moyenne:")
print(mois_sup)
print("consommation maximale:",data["consommation_kwh"].max())
print("consommation minimale:",data["consommation_kwh"].min())
print("somme total:",data["consommation_kwh"].sum())

import matplotlib.pyplot as plt
moyenne=data["consommation_kwh"].mean()
couleurs=[]
for i in data["consommation_kwh"]:
    if i>moyenne:
        couleurs.append("red")
    else:
        couleurs.append("blue")
ligne_prediction=model.predict(X)
plt.bar(data["mois"],data["consommation_kwh"],color=couleurs)
plt.xlabel("mois")
plt.ylabel("consommation (kwh)")
plt.title("consommation électrique annuelle")
plt.xticks(rotation=45)
plt.axhline(y=moyenne,color="black",linestyle="--",label="moyenne")
plt.plot(data["mois"],ligne_prediction,color="yellow",linestyle="--")
plt.legend()
plt.show()

