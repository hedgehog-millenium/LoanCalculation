from flask import Flask, render_template, request, jsonify
import loan as ln
import pandas as pd
import numpy as np
import datetime as date
from dateutil.relativedelta import relativedelta

now = date.datetime.today().date()

def get_loan_data_from_req(req):
    json_req = req.json
    pv = json_req.get('amount', 20000)
    duration= json_req.get('duration', 120)
    rate = json_req.get('rate', 10)
    add_pay = json_req.get('addpay', 0)
    add_pay_frequency = json_req.get('add_pay_frequency', 1)
    print(add_pay_frequency)
    return (pv, duration, rate, add_pay,add_pay_frequency)

def add_month_to_currdate(months_to_add):
    return now + relativedelta(months=months_to_add)

app = Flask(__name__)


@app.route('/annuity_calc/<int:series>', methods=['POST'])
def annuity(series=12):
    #PV, DURATION, RATE, ADD_PAY = 30000, 20, 8, 100
    PV, DURATION, RATE, ADD_PAY ,ADD_PAY_FREQ = get_loan_data_from_req(req=request)
    graph = ln.loan.calc_annuity_graph(PV, DURATION, RATE, ADD_PAY, ADD_PAY_FREQ)
    df = pd.DataFrame(np.around(graph, decimals=2), columns=['PMT', 'Interest', 'Principal', 'Add_Pay', 'Principal_Left'])

    #df['date'] = list(map(add_month_to_currdate, df.index))

    s = (df.index.to_series() / series).astype(int)
    DFn = df.groupby(s).sum()
    print(DFn)
    return DFn.to_json(orient='records')

@app.route('/')
def index():
    return render_template('Index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # PV, DURATION, RATE, ADD_PAY ,PAY_FREQUENCY= 30000, 15, 12, 100 ,1
    # graph = ln.loan.calc_annuity_graph(PV, DURATION, RATE, ADD_PAY,PAY_FREQUENCY)
    # df = pd.DataFrame(np.around(graph, decimals=2), columns=['PMT', 'Interest', 'Principal', 'Add_Pay', 'Principal_Left'])
    # print(df.head())

