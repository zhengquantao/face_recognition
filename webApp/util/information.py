success = {"status": 1000, "msg": "登录成功", "path": "/list/"}
error = {"status": 1001, "msg": "登录失败,用户名或者密码错误"}
timeout = {"status": 1002, "msg": "网络超时"}
unsave = {"status": 1003, "msg": "无法通过安全验证"}
load = {"status": 1004, "msg": "正在加载..."}
play_success = {"status": 1005, "msg": "签到成功"}
play_error = {"status": 1006, "msg": "签到失败"}
play_exits = {"status": 1010, "msg": "你已签到过"}
play_back = {"status": 1010, "msg": "签退成功"}
play_other_error = {"status": 1011, "msg": "光线不够无法识别, 请确保光线充足, 重新刷新试试"}
record_success = {"status": 1007, "msg": "记录成功"}
record_erorr = {"status": 1008, "msg": "记录失败, 请刷新页面后重试"}
is_image = {"status": 2001, "msg": "你已经录过人脸, 请勿重复操作"}
add_success = {"status": 2002, "msg": "增加用户成功"}
add_error = {"status": 2003, "msg": "增加失败, 请稍后再试"}
delete = {"status": 3001, "msg": "操作成功"}
error_path = "/error/"

morning = [8, 12]
after = [14, 18]