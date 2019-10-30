from flask import Flask, redirect, url_for, request,render_template

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/test')
def chartTest(data):
    lnprice=data
    plt.plot(lnprice)
    plt.savefig('images/new_plot')
    return render_template('show_image.html', name = 'new_plot', url ='/images/')

@app.route('/')
def index():
   dataset=pd.read_csv('Salary_Data.csv')
   X=dataset.iloc[:,:-1].values
   y=dataset.iloc[:,1].values
   X=X.reshape(-1,1)
   y=y.reshape(-1,1)
   from sklearn.model_selection import train_test_split
   X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)

   from sklearn.linear_model import LinearRegression
   reg=LinearRegression()
   reg.fit(X_train,y_train)

   price=reg.predict(X_test)
   return redirect(url_for('chartTest',data=price))


if __name__ == '__main__':
   price=[]
   app.run(debug = True)
