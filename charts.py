# -*- coding: utf-8 -*-
from pyecharts.charts import Bar, Gauge, Pie
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, ThemeType


def pass_rate_bar(date=None, data=None, title=None, width=None, height=None, reverse=False):
    c = (
        Bar(init_opts=opts.InitOpts(
            width="{}px".format(width), height="{}px".format(height),
        ))
            .add_xaxis(list(data.index))
            .add_yaxis(date, list(data.values), color="#7dd0f3")
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30, color="#ffffff"),
                                                      axisline_opts=opts.AxisLineOpts(
                                                          linestyle_opts=opts.LineStyleOpts(color="#fff"))),
                             yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color="#ffffff"),
                                                      axisline_opts=opts.AxisLineOpts(
                                                          linestyle_opts=opts.LineStyleOpts(color="#ffffff"))))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(legend_opts=opts.LegendOpts(is_show=False))
    )

    if reverse:
        c.reversal_axis()

    return c


def geo_effectscatter(data, title, width, height) -> Geo:
    c = (
        Geo(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height)))
            .add_schema(maptype="china", is_roam=False)
            .add(
            "各省通过率",
            [list(z) for z in zip(data.index, data.values)],
            type_=ChartType.EFFECT_SCATTER,
            effect_opts=opts.EffectOpts(scale=1000)
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c


def gaugegauge_base_color(data, title, width, height) -> Gauge:
    c = (
        Gauge(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height)), )
            .add(
            "整体通过率",
            [("通过率", data)],
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#fd666d"), (0.7, "#37a2da"), (1, "#67e0e3")], width=30
                )
            ),
        )
            .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                             )
    )
    return c


def pie_rich_label(data, title, width, height) -> Pie:
    c = (
        Pie(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height)))
            .add(
            "",
            [list(z) for z in zip(data.index, [int(a) for a in data.values])],
            radius=["40%", "60%"],

        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .set_global_opts(legend_opts=opts.LegendOpts(is_show=False))

    )
    return c
