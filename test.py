# -*- coding: utf-8 -*-
# 2017/6/24 14:42
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 

code is far away from bugs with the god Animal protecting
               ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
                  
-------------------------------------------------------------------------------
"""

# import datetime
# old_time='2016-01-01'
# imp_time=datetime.datetime.strptime(old_time,'%Y-%m-%d')
# z = datetime.datetime.now()
# print(z)
# print(imp_time)
# if z>imp_time:
#     print('sss')



# from pylab import *
#
# # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# figure(figsize=(8,6), dpi=80)
#
# # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
# subplot(1,1,1)
#
# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)
#
# # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
# plot(X, C, color="blue", linewidth=1.0, linestyle="-")
#
# # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
# plot(X, S, color="green", linewidth=1.0, linestyle="-")
#
# # 设置横轴的上下限
# xlim(-4.0,4.0)
#
# # 设置横轴记号
# xticks(np.linspace(-4,4,9,endpoint=True))
#
# # 设置纵轴的上下限
# ylim(-1.0,1.0)
#
# # 设置纵轴记号
# yticks(np.linspace(-1,1,5,endpoint=True))
#
# # 以分辨率 72 来保存图片
# # savefig("exercice_2.png",dpi=72)
#
# # 在屏幕上显示
# show()
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.figure(1)  # 创建图表1
# plt.figure(2)  # 创建图表2
# ax1 = plt.subplot(211)  # 在图表2中创建子图1
# ax2 = plt.subplot(212)  # 在图表2中创建子图2
#
# x = np.linspace(0, 3, 100)
# for i in range(5):
#     plt.figure(1)  # ❶ # 选择图表1
#     plt.plot(x, np.exp(i * x / 3))
#     plt.sca(ax1)  # ❷ # 选择图表2的子图1
#     plt.plot(x, np.sin(i * x))
#     plt.sca(ax2)  # 选择图表2的子图2
#     plt.plot(x, np.cos(i * x))
#
# plt.show()

# import jieba
# # jieba.suggest_freq('会从', True)
# jieba.set_dictionary("foobar.txt")
# seg_list = jieba.cut("【首届中国青年APP大赛报名】各位大大好，由共青团江西省委举办的首届中国青年APP大赛江西分赛报名开始（相关文件见群共享），报名及初赛时间为3-4月，如有意愿参赛的同学，请各班级汇总报名信息（可先不提交作品），并于3月24日晚20:00前将报名汇总表反馈至294259899@qq.com。")
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式

import pymysql
db = pymysql.connect(host='localhost',
                            port=3308,
                             user='sly',
                             password='070801382',
                             db='work',charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor )


cursor = db.cursor()

sql='select DISTINCT 批号 from 电池片汇总2'
# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql)
bottole = []
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
for i  in data:
    plus_sql='select * from 电池片汇总2 where 批号='+'"'+i['批号']+'"'
    # print(plus_sql)
    cursor.execute(plus_sql)
    new_data=cursor.fetchall()
    count=0

    if len(new_data)>1:
        # print(i)
        for j in new_data[1:]:
            if new_data[0]['效率']!=j["效率"] or new_data[0]['颜色']!=j["颜色"] or new_data[0]['细等级']!=j["细等级"]:
                if i not in bottole:
                    bottole.append(i)
                    # print(bottole)
print(bottole)
        # # print(new_data)
        # for j in new_data[1:]:
        #     count+=1
        #     new_batch=str(i["批号"])+'-S'+str(count)
        #     print(j)
        #     update_sql='update 电池片汇总 set 批号 ='+'"'+ new_batch+'"'+'where 导入序号='+str(j["导入序号"])
        #     print(update_sql)
        #     cursor.execute(update_sql)

# print ("Database version : %s " % data)
# db.commit()
# 关闭数据库连接

db.close()