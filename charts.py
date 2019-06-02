# -*- coding: utf-8 -*-
from pyecharts.charts import Bar, Gauge, Pie
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, ThemeType


def pass_rate_bar(date=None, data=None, width=None, height=None, reverse=False, xrotate=None, yrorate=None,
                  datazoom=False):
    c = (
        Bar(init_opts=opts.InitOpts(
            width="{}px".format(width), height="{}px".format(height),
        ))
            .add_xaxis(list(data.index))
            .add_yaxis(date, list(data.values), color="#7dd0f3")
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=xrotate, color="#ffffff"),
                                                      axisline_opts=opts.AxisLineOpts(
                                                          linestyle_opts=opts.LineStyleOpts(color="#ffffff"))),
                             yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=yrorate, color="#ffffff"),
                                                      axisline_opts=opts.AxisLineOpts(
                                                          linestyle_opts=opts.LineStyleOpts(color="#ffffff"))),
                             legend_opts=opts.LegendOpts(is_show=False),
                             toolbox_opts=opts.ToolboxOpts(pos_left='right'))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )

    if reverse:
        c.reversal_axis().set_global_opts(toolbox_opts=opts.ToolboxOpts(orient='vertical', pos_left='right'),
                                          legend_opts=opts.LegendOpts(is_show=False),
                                          yaxis_opts=opts.AxisOpts(
                                              axislabel_opts=opts.LabelOpts(font_size=6, rotate=yrorate,
                                                                            color="#ffffff"),
                                              axisline_opts=opts.AxisLineOpts(
                                                  linestyle_opts=opts.LineStyleOpts(color="#ffffff"))))

    if datazoom:
        c.set_global_opts(datazoom_opts=[opts.DataZoomOpts(type_='inside'), opts.DataZoomOpts()],
                          legend_opts=opts.LegendOpts(is_show=False), toolbox_opts=opts.ToolboxOpts(pos_left='right'))

    return c


def geo_effectscatter(data, width, height) -> Geo:
    data = [list(z) for z in zip(data.index, data.values)]

    c = (
        Geo(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height)))
            .add_schema(maptype="china", is_roam=False,
                        itemstyle_opts=opts.ItemStyleOpts(color='#0f1c2f', border_color="#ace3f0", border_color0='red'))
            .add("各省通过率",
                 data,
                 type_=ChartType.EFFECT_SCATTER,
                 effect_opts=opts.EffectOpts(scale=1000), color="#d0f551")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(legend_opts=opts.LegendOpts(is_show=False), toolbox_opts=opts.ToolboxOpts(pos_left='70%'))
    )
    return c


def gaugegauge_base_color(data, width, height) -> Gauge:
    c = (
        Gauge(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height)), )
            .add(
            "整体通过率",
            [("", data)],
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#fd666d"), (0.7, "#37a2da"), (1, "#67e0e3")], width=30
                )
            ),
        )
            .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                             toolbox_opts=opts.ToolboxOpts(orient='vertical', pos_left='right'))
    )
    return c


def pie_rich_label(data, width, height) -> Pie:
    c = (
        Pie(init_opts=opts.InitOpts(width="{}px".format(width), height="{}px".format(height)))
            .add(
            "",
            [list(z) for z in zip(data.index, [int(a) for a in data.values])],
            radius=["40%", "60%"],

        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                             toolbox_opts=opts.ToolboxOpts(orient='vertical', pos_left='right'))

    )
    return c
