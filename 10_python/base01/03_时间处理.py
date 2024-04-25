#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/12 23:46
# @Author     : fany
# @Project    : PyCharm
# @File       : 03_时间处理.py
# @description:
# time更偏重于时间类型的相互转化
# datetime更偏重于时间的计算

# import time
#
# # 当前时间-时间戳
# timestamp = time.time()
# print(timestamp)     # 1659772005.7518127
#
#
# # localtime()：将【时间戳】转化为【结构时间】，返回值类型为【time.struct_time】。若缺省参数，则将当前时间转化为结构时间
# p_tuple = time.localtime(timestamp)
# print(p_tuple)       # time.struct_time(tm_year=2022, tm_mon=8, tm_mday=6, tm_hour=15, tm_min=31, tm_sec=50, tm_wday=5, tm_yday=218, tm_isdst=0)
# p_tuple = time.localtime()
# print(p_tuple)    # time.struct_time(tm_year=2022, tm_mon=8, tm_mday=6, tm_hour=15, tm_min=31, tm_sec=50, tm_wday=5, tm_yday=218, tm_isdst=0)
#
#
# # mktime()：将【结构时间】转化为【时间戳】，返回值类型为【float】
# f_time = time.mktime(p_tuple)
# print(f_time)
#
#
# # strftime()：将【结构时间】转化为【字符串时间】，返回值类型为【str】。格式由参数 format 决定。若缺省p_tuple参数，则默认转化当前时间
# now_date = time.strftime("%Y-%m-%d", p_tuple)
# print(now_date)     # 日期格式：2022-08-06
# now_time = time.strftime("%Y-%m-%d %H:%M:%S")
# print(now_time)     # 时间格式：2022-08-06 15:27:51
# gmt_time = time.strftime("%a %b %d %Y %H:%M:%S GMT+0800")
# print(gmt_time)     # GMT时间格式：Sat Aug 06 2022 16:01:37 GMT+0800
#
#
# # strptime()：将【字符串时间】转化为【结构时间】，返回值类型为【time.struct_time】。format的格式必须与时间字符串对应
# p_tuple = time.strptime(gmt_time, "%a %b %d %Y %H:%M:%S GMT+0800")
# print(p_tuple)      # time.struct_time(tm_year=2022, tm_mon=8, tm_mday=6, tm_hour=16, tm_min=8, tm_sec=25, tm_wday=5, tm_yday=218, tm_isdst=-1)
# p_tuple = time.strptime(now_time, "%Y-%m-%d %H:%M:%S")
# print(p_tuple)      # time.struct_time(tm_year=2022, tm_mon=8, tm_mday=6, tm_hour=16, tm_min=8, tm_sec=25, tm_wday=5, tm_yday=218, tm_isdst=-1)

import datetime


# 当前时间。返回值类型为 datetime.datetime
now_time = datetime.datetime.now()
print(now_time)    # 2022-08-06 16:16:16.292192

# 当前日期。返回值类型为 datetime.date
now_date = datetime.date.today()
print(now_date)     # 2022-08-06

# 时间（datetime.datetime）可以转化为时间戳，日期不行。返回值类型为 float
timestamp_time = now_time.timestamp()
print(timestamp_time)   # 1659774174.285991

# 两种类型均可转化为【结构时间】。返回值类型为 time.struct_time
print(now_time.timetuple())     # time.struct_time(tm_year=2022, tm_mon=8, tm_mday=6, tm_hour=16, tm_min=26, tm_sec=9, tm_wday=5, tm_yday=218, tm_isdst=-1)
print(now_date.timetuple())     # time.struct_time(tm_year=2022, tm_mon=8, tm_mday=6, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=218, tm_isdst=-1)

# 两种类型均可转化为【字符串时间】
print(now_time.strftime("%Y-%m-%d %H:%M:%S"))       # 2022-08-06 16:29:43
print(now_time.strftime("%a %b %d %Y %H:%M:%S GMT+0800"))   # Sat Aug 06 2022 16:29:43 GMT+0800
print(now_date.strftime("%Y-%m-%d %H:%M:%S"))       # 2022-08-06 00:00:00


# 两种类型均可进行日期计算。计算后的类型与计算前相同
# 当前时间减1小时。timedelta参数可为（days、seconds、microseconds、milliseconds、minutes、hours、weeks）
print(now_time - datetime.timedelta(hours=1))      # 2022-08-06 15:38:25.974166
# 当前时间加1天
print(now_time + datetime.timedelta(days=1))        # 2022-08-07 16:38:25.974166
# 当前日期减1天
print(now_date - datetime.timedelta(days=1))        # 2022-08-05