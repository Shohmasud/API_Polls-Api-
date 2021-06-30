
from django.contrib import admin
from django.urls import path,include
from  interview_api.views import index,Questions,number_pk,Send,Next,functionDocumentations
#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    # path('api/v6/interview_api', include(urls)),
    path('api/v6/', index, name='index'),
    path('questions/', Questions, name='ques'),
    path('connect/api/v6/<int:pk>', number_pk, name='num'),
    path('confirmation/', Next, name='next'),
    path('send_data/', Send, name='snd'),
    path('documentations/', functionDocumentations, name='documentations'),
    path('', include('interview_api.urls')),
    path('form/',Questions)
]
