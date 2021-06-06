# Flask : library utama untuk membuat API
# render_template : agar dapat memberikan respon file html
# request : untuk membaca data yang diterima saat request datang
from flask import Flask, render_template, request
# plotly dan plotly.graph_objs : membuat plot
import plotly
import plotly.graph_objs as go
# pandas : untuk membaca csv dan men-generate dataframe
import pandas as pd
import json
from sqlalchemy import create_engine

## Joblib untuk Load Model
import joblib

# untuk membuat route
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    ## Me-Load data dari Database
    sqlengine = create_engine('mysql://root:1234@localhost/hotel_pwdk', pool_recycle=3306)
    dbConnection = sqlengine.connect()
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    # tips = pd.read_sql("select * from tips", dbConnection)
    # tips = pd.read_csv('./static/tips.csv')
    ## Load Model
    model = joblib.load('Booking_hotel_classification')
    app.run(debug=True)