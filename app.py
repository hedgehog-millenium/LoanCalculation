from flask import Flask, render_template, jsonify
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
    return render_template('Index.html')

if __name__ == '__main__':
    app.run(debug=True)