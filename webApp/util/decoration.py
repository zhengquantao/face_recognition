"""
验证登录
"""

from django.shortcuts import redirect
from functools import wraps


def login(func):
    @wraps(func)
    def login_func(request, *args, **kwargs):
        if request.session.get('user'):
            return func(request, *args, **kwargs)
        else:
            red = redirect('/login/')
            return red
    return login_func