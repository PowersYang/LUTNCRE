# -*- coding:utf-8 -*-

from flask import Flask, render_template

from analysis import Analysis
from charts import pass_rate_bar

app = Flask(__name__)

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/charts/<date>')
def render_charts(date):
    analysis = Analysis(date)
    c1 = pass_rate_bar(date, analysis.pass_rate('college'), '各学院通过率')
    c2 = pass_rate_bar(date, analysis.pass_rate('major'), '各专业通过率')

    return render_template('pyecharts.html', c1=c1.render_embed(), c2=c2.render_embed())


if __name__ == '__main__':
    app.run(debug=True)
