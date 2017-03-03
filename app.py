from flask import Flask, send_from_directory, jsonify
import loan as ln
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/annuity_calc')
def annuity():
    PV, DURATION, RATE, ADD_PAY = 30000, 20, 8, 100
    graph = ln.loan.calc_annuity_graph(PV, DURATION, RATE, ADD_PAY)
    df = pd.DataFrame(np.around(graph, decimals=2))
    return df.to_json()

@app.route('/')
def index():
    return send_from_directory('vizual_part\\Loan Calc','Index.html')

if __name__ == '__main__':
    app.run(debug=True)