# -*- coding: utf-8 -*-
import os
import random

from flask import Flask, url_for
from flask_cors import CORS

from flask import jsonify, make_response

from .charts import charts

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    num_charts = len(charts)
    response_object = {
        'status': 'success',
        'message': 'Deu certo, você conseguiu entrar',
        'random_chart': url_for('chart'),
        'charts': [{
            'id': i,
            'type': charts[i]['chartType'], 
            'url': url_for('chart', id=i)} for i in range(num_charts)],
        'num_charts': num_charts
    }
    return make_response(jsonify(response_object)), 200

@app.route('/chart')
@app.route('/chart/<int:id>')
def chart(id=None):
    if isinstance(id, int):
        if id < len(charts):
            chart = charts[id]
        else:
            response_object = {
                'status': 'fail',
                'message': 'This chart does not exists.',
                'chart_index': id
            }
            return make_response(jsonify(response_object)), 404
    else:
        chart = random.choice(charts)
    return make_response(jsonify(chart)), 200