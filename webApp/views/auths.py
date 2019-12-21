from django.utils.deprecation import MiddlewareMixin


class CORSMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        # 允许你的域名来访问
        # response['Access-Control-Allow-Origin'] = "*"
        # 允许你携带 Content-Type 请求头 不能写*
        # response['Access-Control-Allow-Headers'] = 'Content-Type'
        # 允许你发送 DELETE PUT请求
        # response['Access-Control-Allow-Methods'] = 'DELETE,PUT'
        # host = request.get_host()
        response['Access-Control-Allow-Origin'] = "*"
        if request.method == "OPTIONS":
            response['Access-Control-Allow-Headers'] = 'Content-Type'  # 可以在'Content-Type，x'添加请求头
            response['Access-Control-Allow-Methods'] = 'GET,POST'  # 允许发的请求方式

        return response

