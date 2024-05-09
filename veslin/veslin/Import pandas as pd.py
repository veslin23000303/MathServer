Import pandas as pd
frd sklearn import linear_model
data-pd.read_csv('car.csv')
x=data[['Weight', 'Volume']]
y=data['CO2']
regression-linear_model.LinearRegression()
regression.fit(x,y)
print("Coefficient:", regression.coef_)
print("Intercept:,regression.intercept_)
predictC02-regression.predict([[3300,1300]])
print("CO2 required is", predict(02)