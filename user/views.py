from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        userName = request.POST.get('userName',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (userName and password and re_password):
            res_data['error'] = '모든 항목을 입력해야 합니다.'
        elif password != re_password:
            # return HttpResponse('비밀번호가 다릅니다')
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            user = User(
                userName = userName,
                password = make_password(password)
            )
            res_data['success'] = '회원가입을 축하합니다'

            user.save()

        return render(request, 'register.html', res_data)
