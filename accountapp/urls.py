from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"
# 127.0.0.1:8000/account/hello_world 경로 대신 app_name:hello_world로 쉽게 주소 사용가능

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), # 함수형
    path('create/', AccountCreateView.as_view(), name='create'), # class형
]
