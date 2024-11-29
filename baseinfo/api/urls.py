from django.urls import path
from baseinfo.api.views import BaseInfoview

urlpatterns = [
    path('base-info/', BaseInfoview.as_view(), name='base-info'),
]