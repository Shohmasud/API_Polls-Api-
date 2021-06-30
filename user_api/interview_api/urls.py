from  .views import  SerializerId_forDataTime,SerializerUser_IdforQuestionsCheckbox_Button,SerializerUser_Id_forQuestionsRadio_Button,\
SerializeruserId_Checkboxbutton,SerializeruseridForRadiobutton,SerializerDatatime,SerializerDataEnd,Serializerquestions,\
SerializerTheme_all_ObjectPolls,SerializerThemeForall_ObjectAnswer,SerializersTheme_name_ForId
from django.urls import path

urlpatterns = [
    path('api/v6/id/',  SerializerId_forDataTime.as_view()),
    path('api/v6/id/questions/checkbox/', SerializerUser_IdforQuestionsCheckbox_Button.as_view()),
    path('api/v6/id/questions/radio/', SerializerUser_Id_forQuestionsRadio_Button.as_view()),
    path('api/v6/id/answer/answer/checkbox/', SerializeruserId_Checkboxbutton.as_view()),
    path('api/v6/id/answer/answer/radio/', SerializeruseridForRadiobutton.as_view()),
    path('api/v6/id/answer/data/first/', SerializerDatatime.as_view()),
    path('api/v6/id/answer/data/end/', SerializerDataEnd.as_view()),
    path('api/v6/id/answer/questions/', Serializerquestions.as_view()),
    path('api/v6/id/theme/questions/', SerializerTheme_all_ObjectPolls.as_view()),
    path('api/v6/id/theme/answer/', SerializerThemeForall_ObjectAnswer.as_view()),
    path('api/v6/id/theme/id/', SerializersTheme_name_ForId.as_view()),
]