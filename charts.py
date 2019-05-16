# -*- coding: utf-8 -*-
from example.commons import Faker

from pyecharts.charts import Bar, Gauge
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, ThemeType


def pass_rate_bar(date, data, title):
    c = (
        Bar()
            .add_xaxis(list(data.index))
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
            title_opts=opts.TitleOpts(title=title)
        ).add_yaxis(date, list(data.values))
    )

    return c




def geo_effectscatter(data, title) -> Geo:
    c = (
        Geo()
            .add_schema(maptype="china", is_roam=False)
            .add(
            "各省通过率",
            [list(z) for z in zip(data.index, data.values)],
            type_=ChartType.EFFECT_SCATTER,
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title=title))
    )
    return c


def gaugegauge_base_color(data, title) -> Gauge:
    c = (
        Gauge()
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
            title_opts=opts.TitleOpts(title=title),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c
