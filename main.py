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

@app.route('/pred_result', methods=['POST', 'GET'])
def pred_result():

    if request.method == 'POST':
    ## Untuk Predict
        input = request.form
        
        hotel_type = ''
        if input['hotel_type'] == 'resort_hotel':
            hotel_type = 1
        else:
            hotel_type = 0

        lead_time = input['lead_time']
        special_request = input['special_request']
        arv_date_year = input['arv_date_year']
        arv_date_month = input['arv_date_month']
        arv_date_week_number = input['arv_date_week_number']
        arv_date_day = input['arv_date_day']
        stay_in_weekend_night = input['stay_in_weekend_night']
        stays_in_week_nights = input['stays_in_week_nights']
        adults = input['adults']
        children = input['children']
        babies = input['babies']

        BB_meal, FB_Meal, HB_Meal, SC_Meal  = 0, 0, 0, 0

        if input['meal'] == 'FB_Meal':
            FB_Meal = 1
        elif input['meal'] == 'HB_Meal':
            HB_Meal = 1
        elif input['meal'] == 'BB_meal':
            BB_meal = 1
        else:
            SC_Meal = 1

        country__BEL, country__BRA, country__DEU, country__ESP, country__FRA, country__GBR, country__IRL, country__ITA, country__Other, country__PRT = 0,0,0,0,0,0,0,0,0,0

        if input['country'] == 'country__BEL':
            country__BEL = 1
        elif input['country'] == 'country__BRA':         
            country__BRA = 1
        elif input['country'] == 'country__DEU':         
            country__DEU = 1
        elif input['country'] == 'country__ESP':         
            country__ESP = 1
        elif input['country'] == 'country__FRA':         
            country__FRA = 1
        elif input['country'] == 'country__GBR':         
            country__GBR = 1
        elif input['country'] == 'country__IRL':         
            country__IRL = 1
        elif input['country'] == 'country__ITA':         
            country__ITA = 1
        elif input['country'] == 'country__PRT':         
            country__PRT = 1
        else:
            country__Other = 0
        
        ms_Aviation, ms_Complementary, ms_Corporate, ms_Direct, ms_Groups, ms_Offline_TA_TO, ms_Online_TA = 0,0,0,0,0,0,0
        

        if input['market_segment'] == 'ms_Aviation':
            ms_Aviation = 1
        elif input['market_segment'] == 'ms_Complementary':         
            ms_Complementary = 1
        elif input['market_segment'] == 'ms_Corporate':         
            ms_Corporate = 1
        elif input['market_segment'] == 'ms_Direct':         
            ms_Direct = 1
        elif input['market_segment'] == 'ms_Groups':         
            ms_Groups = 1
        elif input['market_segment'] == 'ms_Offline_TA_TO':         
            ms_Offline_TA_TO = 1
        else:
            ms_Online_TA = 1


        dc_Corporate, dc_Direct, dc_GDS, dc_TA_TO = 0,0,0,0

        if input['distribution_channel'] == 'dc_Direct':
            dc_Direct = 1
        elif input['distribution_channel'] == 'dc_Corporate': dc_Corporate = 1
        elif input['distribution_channel'] == 'dc_TA_TO': dc_TA_TO = 1
        else:
           dc_GDS = 1

        is_repeated = ''
        if input['is_repeated'] == 'yes':
            is_repeated = 1
        else:
            is_repeated = 0

        pre_cancellations = input['pre_cancellations']
        pre_not_cancel = input['pre_not_cancel']

        reserved_room_type__A, reserved_room_type__B, reserved_room_type__C, reserved_room_type__D, reserved_room_type__E, reserved_room_type__F, reserved_room_type__G, reserved_room_type__H, reserved_room_type__L, = 0,0,0,0,0,0,0,0,0


        if input['reserved_room_type'] == 'A':
            reserved_room_type__A = 1
        elif input['reserved_room_type'] == 'B':         
            reserved_room_type__B = 1
        elif input['reserved_room_type'] == 'C':         
            reserved_room_type__C = 1
        elif input['reserved_room_type'] == 'D':         
            reserved_room_type__D = 1
        elif input['reserved_room_type'] == 'E':         
            reserved_room_type__E = 1
        elif input['reserved_room_type'] == 'F':         
            reserved_room_type__F = 1
        elif input['reserved_room_type'] == 'G':         
            reserved_room_type__G = 1
        elif input['reserved_room_type'] == 'H':         
            reserved_room_type__H = 1
        else:         
            reserved_room_type__L = 1

        assigned_room_type__A, assigned_room_type__B, assigned_room_type__C, assigned_room_type__D, assigned_room_type__E, assigned_room_type__F, assigned_room_type__G, assigned_room_type__H, assigned_room_type__I, assigned_room_type__K, assigned_room_type__L = 0,0,0,0,0,0,0,0,0,0,0


        if input['assigned_room_type'] == 'A':
            assigned_room_type__A = 1
        elif input['assigned_room_type'] == 'B':         
            assigned_room_type__B = 1
        elif input['assigned_room_type'] == 'C':         
            assigned_room_type__C = 1
        elif input['assigned_room_type'] == 'D':         
            assigned_room_type__D = 1
        elif input['assigned_room_type'] == 'E':         
            assigned_room_type__E = 1
        elif input['assigned_room_type'] == 'F':         
            assigned_room_type__F = 1
        elif input['assigned_room_type'] == 'G':         
            assigned_room_type__G = 1
        elif input['assigned_room_type'] == 'H':         
            assigned_room_type__H = 1
        elif input['assigned_room_type'] == 'I':         
            assigned_room_type__I = 1
        elif input['assigned_room_type'] == 'K':         
            assigned_room_type__K = 1
        else:
            assigned_room_type__L = 1

        booking_change = input['booking_change']

        deposit_type__No_Deposit, deposit_type__Non_Refund, deposit_type__Refundable = 0,0,0


        if input['deposit_type'] == 'No_Deposit':
            deposit_type__No_Deposit = 1
        elif input['deposit_type'] == 'Refundable': 
            deposit_type__Refundable = 1
        else: 
            deposit_type__Non_Refund  = 1

        agent = input['agent']
        company = input['company']
        waiting_list = input['waiting_list']

        customer_type__Contract, customer_type__Group, customer_type__Transient, customer_type__Transient_Party = 0,0,0,0

        if input['customer_type'] == 'Transient':
            customer_type__Transient = 1
        elif input['customer_type'] == 'Contract':
            customer_type__Contract = 1
        elif input['customer_type'] == 'Transient-Party':
            customer_type__Transient_Party = 1
        else:
            customer_type__Group = 1

        adr = input['adr']

        car_parking = input['car_parking']

        pred = model.predict([[hotel_type, lead_time,arv_date_year, arv_date_month, arv_date_week_number, arv_date_day, stay_in_weekend_night, stays_in_week_nights, adults, children, babies, is_repeated, pre_cancellations, pre_not_cancel, booking_change, agent, waiting_list, adr, car_parking, special_request, BB_meal, FB_Meal, HB_Meal, SC_Meal, country__BEL, country__BRA, country__DEU, country__ESP, country__FRA, country__GBR, country__IRL, country__ITA, country__Other, country__PRT, ms_Aviation, ms_Complementary, ms_Corporate, ms_Direct, ms_Groups, ms_Offline_TA_TO, ms_Online_TA, dc_Corporate,dc_Direct, dc_GDS, dc_TA_TO, deposit_type__No_Deposit, deposit_type__Non_Refund, deposit_type__Refundable, customer_type__Contract, customer_type__Group, customer_type__Transient, customer_type__Transient_Party, reserved_room_type__A, reserved_room_type__B, reserved_room_type__C, reserved_room_type__D, reserved_room_type__E, reserved_room_type__F, reserved_room_type__G, reserved_room_type__H, reserved_room_type__L, assigned_room_type__A, assigned_room_type__B, assigned_room_type__C, assigned_room_type__D, assigned_room_type__E, assigned_room_type__F, assigned_room_type__G, assigned_room_type__H, assigned_room_type__I, assigned_room_type__K, assigned_room_type__L]])[0]


        result_pred = ''
        if pred == 1:
            result_pred = 'Canceled'
        else:
            result_pred = 'Not Cancel'

        return render_template('sucess_predict.html',
            data = input,
            booking_pred = pred,
            result_str = result_pred
        )

if __name__ == '__main__':
        
    # sqlengine = create_engine('mysql://root:1234@localhost/hotel_pwdk', pool_recycle=3306)
    # dbConnection = sqlengine.connect()
    # engine = sqlengine.raw_connection()
    # cursor = engine.cursor()

    # tips = pd.read_sql("select * from tips", dbConnection)
    # tips = pd.read_csv('./static/tips.csv')
    ## Load Model
    model = joblib.load('Booking_hotel_classification')
    app.run(debug=True)