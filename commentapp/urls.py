from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteview

app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteview.as_view(), name='delete'),
]