# -*- coding: utf-8 -*-
from pyecharts.charts import Bar
from pyecharts import options as opts


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
