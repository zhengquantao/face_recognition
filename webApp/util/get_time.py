import datetime
# 获取前1天或N天的日期，beforeOfDay=1：前1天；beforeOfDay=N：前N天


def getdate(beforeOfDay):
    today = datetime.datetime.now()
    # 计算偏移量
    offset = datetime.timedelta(days=-beforeOfDay)
    # 获取想要的日期的时间
    re_date = (today + offset).strftime('%Y-%m-%d')
    return re_date

