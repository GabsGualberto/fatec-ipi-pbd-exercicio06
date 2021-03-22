import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset = pd.read_csv('HeightVsWeight.csv')
ind = dataset.iloc[:, -2].values
dep = dataset.iloc[:,-1].values


dep = dep.reshape(len(dep), 1)
ind = ind.reshape(len(ind), 1)

linearRegression = LinearRegression()
linearRegression.fit(ind, dep)
 
poly_features = PolynomialFeatures(degree= 2)
ind_poly = poly_features.fit_transform(ind)
polyLinearRegression = LinearRegression()
polyLinearRegression.fit(ind_poly, dep)


#modelo linear simples
plt.scatter(ind, dep, color='red')
plt.plot(ind, linearRegression.predict(ind), color="blue")
plt.title("Regressão Linear Simples")
plt.xlabel("Idade")
plt.ylabel("Altura")
plt.show()
#modelo polinomial
plt.scatter(ind, dep, color="red")
plt.plot(ind, polyLinearRegression.predict(ind_poly),
color="blue")
plt.title("Regressão Linear Polinomial com grau 2")
plt.xlabel("Nível")
plt.ylabel("Salário")
plt.show()


poly_features = PolynomialFeatures(degree= 4)
ind_poly = poly_features.fit_transform(ind)
polyLinearRegression = LinearRegression()
polyLinearRegression.fit(ind_poly, dep)
plt.scatter(ind, dep, color="red")

plt.plot(ind, polyLinearRegression.predict(ind_poly),
color="blue")
plt.title("Regressão Linear Polinomial com grau 4")
plt.xlabel("Nível")
plt.ylabel("Salário")
plt.show()