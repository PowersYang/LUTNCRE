import random

from flask import Flask, render_template
from example.commons import Faker
from pyecharts import options as opts

from pyecharts.charts import Bar, Pie, Page, Bar3D

app = Flask(__name__)

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/2018')
def hello():
    bar1 = pie_base()
    bar2 = bar3d_base()

    return render_template('pyecharts.html', bar1=bar1.render_embed(), bar2=bar2.render_embed())


@app.route('/2019')
def hello2():
    return '2019'


def pie_base() -> Pie:
    c = (
        Pie()
            .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


def bar3d_base() -> Bar3D:
    data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()
            .add(
            "",
            [[d[1], d[0], d[2]] for d in data],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=20),
            title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
        )
    )
    return c


if __name__ == '__main__':
    app.run()
