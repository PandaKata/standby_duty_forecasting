import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('/Users/kata/Desktop/GitHub/standby_duty_forecasting/sickness_table.csv', index_col=0)
df.head()

def calc_mse(column1, column2):
    '''column1 is the default drivers
    column2 the needed ones'''
    mse_total = [] 
    for row in column1:
        mse = (column1 - column2)**2
    mse_total.append(mse)
    return sum(mse_total)

(calc_mse(df.n_sby, df.sby_need)).sum()

model = LinearRegression()


X = df.index.values.reshape(-1,1)
y = df.sby_need
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size = .8)

model.fit(X, y)

pred = model.predict(X)

df['y_predicted'] = pred

df.head()


print("Coefficients:")
print("Slope: " + str(model.coef_))
print("y-intercept: " + str(model.intercept_))
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(df['sby_need'], df['y_predicted']))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(df['sby_need'], df['y_predicted']))



plt.figure(figsize=(14, 8))
ax = plt.axes()
ax.scatter(df.date, y)
ax.plot(df.date, pred, color='red', linewidth=3)

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.axis('tight')


plt.show()