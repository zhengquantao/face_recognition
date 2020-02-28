from django.shortcuts import render, redirect, HttpResponse
from webApp.util import information, decoration, get_time
from webApp.models import UserInfo, DateAndWeek, UserAndTitle
import datetime
import xlwt
from django.db.models import Count
from io import BytesIO


@decoration.login
def show(request):
    job = request.session.get('user')
    if not job:
        return redirect(information.error_path)
    is_user = UserAndTitle.objects.filter(username__job=job, title__profession="管理员")
    year = datetime.datetime.now().year
    attendance = list()
    if is_user:
        time_list = DateAndWeek.objects.filter(starttime__year=year).values("user__job", "user__username", "status", "starttime", "endtime")
        for i in range(7):
            time = get_time.getdate(i)
            attendance_count = DateAndWeek.objects.filter(starttime__contains=time).count()
            all_person = UserInfo.objects.count()
            attendance.append(int(attendance_count/all_person*100))
    else:
        time_list = DateAndWeek.objects.filter(user__job=job, starttime__year=year).values("user__job", "user__username", "status", "starttime", "endtime")
        for i in range(7):
            time = get_time.getdate(i)
            attendance_count = DateAndWeek.objects.filter(user__job=job, starttime__contains=time).count()
            attendance.append(attendance_count*100)
    item = {}
    try:
        for item_obj in time_list:
            # datetime转化时间成字符串
            if item_obj['starttime']:
                starttime = datetime.datetime.strftime(item_obj['starttime'], '%Y-%m-%d %H:%M:%S')
            else:
                starttime = ""
            if item_obj['endtime']:
                endtime = datetime.datetime.strftime(item_obj['endtime'], '%Y-%m-%d %H:%M:%S')
            else:
                endtime = ""
            if item_obj['user__job'] in item.keys():
                item[item_obj['user__job']].append(
                    [starttime, endtime, item_obj['status'], item_obj['user__username']])
            else:
                item[item_obj['user__job']] = [
                    [starttime, endtime, item_obj['status'], item_obj['user__username']]]
    except:
        pass
    return render(request, "show.html", {"item": item, "attendance": attendance})


@decoration.login
def export(request):
    """
    导出xlsx文件
    """
    start = request.POST.get("start")
    end = request.POST.get("end")
    job = request.session.get('user')
    if not job:
        return redirect("/error/")
    profession = UserAndTitle.objects.filter(username__job=job).values("title__profession")
    if profession[0]['title__profession'] == "管理员":
        excel_list = DateAndWeek.objects.filter(starttime__range=(start, end)).values("user__username", "user__job", "starttime", "endtime", "status").annotate(users=Count("user__job"))
    else:
        excel_list = DateAndWeek.objects.filter(user__job=job, starttime__range=(start, end)).values("user__username", "user__job", "starttime", "endtime", "status")

    # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=content.xls'
    # 创建一个文件对象
    wb = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet对象
    sheet = wb.add_sheet('order-sheet')

    # 设置文件头的样式,这个不是必须的可以根据自己的需求进行更改
    style_heading = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index white,
                    bold on,
                    height 0xA0;
                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour 0x19;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """)

    # 写入文件标题
    sheet.write(0, 0, '用户名', style_heading)
    sheet.write(0, 1, '工号', style_heading)
    sheet.write(0, 2, '签到时间', style_heading)
    sheet.write(0, 3, '签退时间', style_heading)
    sheet.write(0, 4, '状态', style_heading)

    # 写入数据
    data_row = 1
    # 这个是查询条件,可以根据自己的实际需求做调整.

    for i in excel_list:
        if i['starttime']:
            start_time = i['starttime'].strftime('%Y-%m-%d %H:%M:%S')
        else:
            start_time = None
        if i['endtime']:
            end_time = i['endtime'].strftime('%Y-%m-%d %H:%M:%S')
        else:
            end_time = None
        sheet.write(data_row, 0, i['user__username'])
        sheet.write(data_row, 1, i['user__job'])
        sheet.write(data_row, 2, start_time)
        sheet.write(data_row, 3, end_time)
        sheet.write(data_row, 4, i['status'])

        data_row = data_row + 1

    # 写出到IO
    output = BytesIO()
    wb.save(output)
    # 重新定位到开始
    output.seek(0)
    response.write(output.getvalue())
    return response
