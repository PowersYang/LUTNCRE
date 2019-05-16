# -*- coding: utf-8 -*-
from pyecharts.charts import Bar, Gauge, Pie
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, ThemeType


def pass_rate_bar(date, data, title, width, height):
    c = (
        Bar(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height),
                                    theme=ThemeType.MACARONS))
            .add_xaxis(list(data.index))
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-90)),
            # title_opts=opts.TitleOpts(title=title)
        ).add_yaxis(date, list(data.values))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    )

    return c


def geo_effectscatter(data, title, width, height) -> Geo:
    c = (
        Geo(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height)))
            .add_schema(maptype="china", is_roam=False)
            .add(
            "各省通过率",
            [list(z) for z in zip(data.index, data.values)],
            type_=ChartType.EFFECT_SCATTER,
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # .set_global_opts(title_opts=opts.TitleOpts(title=title))
    )
    return c


def gaugegauge_base_color(data, title, width, height) -> Gauge:
    c = (
        Gauge(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height)))
            .add(
            "整体通过率",
            [("通过率", data)],
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#fd666d"), (0.7, "#37a2da"), (1, "#67e0e3")], width=30
                )
            ),
        )
            .set_global_opts(
            # title_opts=opts.TitleOpts(title=title),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c


def pie_rich_label(data, title, width, height) -> Pie:
    c = (
        Pie(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height)))
            .add(
            "",
            [list(z) for z in zip(data.index, [int(a) for a in data.values])],
            radius=["40%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter=" {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
            # .set_global_opts(title_opts=opts.TitleOpts(title=title))
    )
    return c
