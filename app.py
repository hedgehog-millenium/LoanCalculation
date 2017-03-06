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
    duration= json_req.get('duration', 20000)
    rate = json_req.get('rate', 20000)
    add_pay = json_req.get('addpay', 0)
    return (pv, duration, rate, add_pay)

def add_month_to_currdate(months_to_add):
    return now + relativedelta(months=months_to_add)

app = Flask(__name__)


@app.route('/annuity_calc', methods=['POST'])
def annuity():
    #PV, DURATION, RATE, ADD_PAY = 30000, 20, 8, 100
    PV, DURATION, RATE, ADD_PAY = get_loan_data_from_req(req=request)
    graph = ln.loan.calc_annuity_graph(PV, DURATION, RATE, ADD_PAY)
    df = pd.DataFrame(np.around(graph, decimals=2), columns=['PMT', 'Interest', 'Principal', 'Add_Pay', 'Principal_Left'])

    df['date'] = list(map(add_month_to_currdate, df.index))
    # df.set_index('date', inplace=True)
    # df.index = pd.to_datetime(df.index)
    # DFyr1 = df.resample('12M').sum()

    s = (df.index.to_series() / 12).astype(int)
    DFn = df.groupby(s).sum()

    print(df)
    print(df.to_json(orient='records'))
    print(DFn)
    return DFn.to_json(orient='records')


@app.route('/')
def index():
    return render_template('Index.html')


if __name__ == '__main__':
    app.run(debug=True)

