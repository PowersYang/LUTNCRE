# -*- coding: utf-8 -*-

import pandas as pd


# # 加载数据 并将所有columns变为小写
# df_201803 = pd.read_excel('data/201803.xlsx')
# df_201803.columns = [col.lower() for col in df_201803]
#
# df_201803_xq = pd.read_excel('data/201803xq.xlsx')
# df_201803_xq.columns = [col.lower() for col in df_201803_xq]
#
# df_201809 = pd.read_excel('data/201809.xlsx')
# df_201809.columns = [col.lower() for col in df_201809]
#
# df_201809_xq = pd.read_excel('data/201809xq.xlsx')
# df_201809_xq.columns = [col.lower() for col in df_201809_xq]


# # 所有学院
# colleges = set(students_lib['FY'])
#
# # 所有专业
# majors = set(students_lib['专业名称'])

# 整合两个校区的数据
# df_201803 = df_201803.append(df_201803_xq)
# df_201809 = df_201809.append(df_201809_xq)


# def rate(flag='college'):
#     data_201803 = pd.merge(students_lib, df_201803, left_on='SFZH', right_on='zjh')
#     data_201809 = pd.merge(students_lib, df_201809, left_on='SFZH', right_on='zjh')
#
#     group_key = ''
#     if flag == 'college':
#         group_key = 'FY'
#     elif flag == 'major':
#         group_key = '专业名称'
#     else:
#         pass
#
#     rate_college_201803 = data_201803[data_201803['cj'] >= 60].groupby(group_key).count()['cj'] / \
#                           data_201803.groupby(group_key).count()['cj']
#
#     rate_college_201809 = data_201809[data_201809['cj'] >= 60].groupby(group_key).count()['cj'] / \
#                           data_201809.groupby(group_key).count()['cj']
#     res = pd.DataFrame(list(zip(rate_college_201803, rate_college_201809)), columns=['201803', '201809'],
#                        index=rate_college_201803.index).round(2)
#     res.fillna(0)
#     return res


class Analysis():
    def __init__(self, date):
        self.date = date
        self.df = pd.read_excel('data/{}.xlsx'.format(self.date))
        self.df.columns = [col.lower() for col in self.df]

        self.df_xq = pd.read_excel('data/{}xq.xlsx'.format(self.date))
        self.df_xq.columns = [col.lower() for col in self.df_xq]
        self.df = self.df.append(self.df_xq)

        self.students_lib = pd.read_excel('data/兰州理工大学在籍学籍库.xlsx')
        self.students_list = pd.read_excel('data/在籍在校学生名单.xls')

        self.df = pd.merge(self.students_lib, self.df, left_on='SFZH', right_on='zjh')

    def pass_rate(self, compute_by):

        if compute_by == 'college':
            res = self.df[self.df['cj'] >= 60].groupby('FY').count()['cj'] / \
                   self.df.groupby('FY').count()['cj']
            return res.round(3)
        elif compute_by == 'major':
            res = self.df[self.df['cj'] >= 60].groupby('专业名称').count()['cj'] / \
                   self.df.groupby('专业名称').count()['cj']
            return res.round(3)
        elif compute_by == 'subject':
            pass
        else:
            raise Exception('参数不合法')
