# -*- coding:utf-8 -*-

from flask import Flask, render_template

from analysis import Analysis
from charts import pass_rate_bar, geo_effectscatter, gaugegauge_base_color, pie_rich_label

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/charts/<date>')
def render_charts(date):
    analysis = Analysis(date)

    c1 = pass_rate_bar(date, analysis.pass_rate('college'), 680, 380, False, -20, 0)
    c2 = pass_rate_bar(date, analysis.pass_rate('major'), 650, 380, False, -20, 0, True)
    c3 = pass_rate_bar(date, analysis.pass_rate('subject'), 300, 610, True, 0, -20)
    c4 = pie_rich_label(analysis.pass_rate_fd(), 300, 300)
    c5 = gaugegauge_base_color(analysis.pass_rate(), 330, 330)
    c6 = geo_effectscatter(analysis.pass_rate('jg'), 700, 700)

    return render_template('pyecharts.html', c1=c1.render_embed(), c2=c2.render_embed(),
                           c3=c3.render_embed(), c4=c4.render_embed(),
                           c5=c5.render_embed(), c6=c6.render_embed())


if __name__ == '__main__':
    app.run(debug=True)
