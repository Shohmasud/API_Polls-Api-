from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Interview, sitepolls, questions, answer, category_button, checkbox_button, user_answer, user_id, \
Theme_all_ObjectPolls,user_answerCheckboxButton,ThemeForall_ObjectAnswer,user_idForRadiobutton,userIdForCheckboxbutton,\
ThemeForall_ObjectId,User_forQuestionsRadio_Button,User_Id_forQuestionsRadio_Button,\
User_forQuestionsCheckbox_Button,User_Id_forQuestionsCheckbox_Button,Theme_name_ForId,Datatime,Id_forDataTime,DataEnd
LogEntry.objects.all().delete()


# Register your models here.
# ________________________________________
class Admin_interview(admin.ModelAdmin):
    list_display = ('id', 'text_pols', 'text_entry', 'text_example_id', 'text_id', 'text_button')
    search_fields = ['id', 'text_pols', 'text_entry', 'text_example_id', 'text_id', 'text_button']
admin.site.register(Interview, Admin_interview)


# ____________________________________________
class Id(admin.ModelAdmin):
    list_display = (['id', 'text_number'])
admin.site.register(user_id, Id)


# ______________________________________________-
class Admin_site_polls(admin.ModelAdmin):
    list_display = ('id', 'text_polls', 'text_head_handling', 'text_handling', 'text_for_whom')
    search_fields = ['id', 'text_pols', 'text_entry', 'text_example_id', 'text_id', 'text_button']
admin.site.register(sitepolls, Admin_site_polls)


# ______________________________________________
class my_questions(admin.ModelAdmin):
    list_display = (['id', 'text_questions'])
    search_fields = (['id', 'text_questions'])
admin.site.register(questions, my_questions)


# _______________________________________________
class my_answer(admin.ModelAdmin):
    list_display = (['id', 'text_answer'])
    search_fields = (['id', 'text_answer'])
admin.site.register(answer, my_answer)


# _________________________________________________
class Button_category(admin.ModelAdmin):
    list_display = (['id', 'radio_button'])
    search_fields = (['id', 'radio_button'])
admin.site.register(category_button, Button_category)


# ____________________________________________________
class Button_category_checkbox(admin.ModelAdmin):
    list_display = (['id', 'checkbox_button'])
    search_fields = (['id', 'checkbox_button'])
admin.site.register(checkbox_button, Button_category_checkbox)


# ______________________________________________________
class User_answer(admin.ModelAdmin):
    list_display = (['id', 'text_answer_user'])
    search_fields = (['id', 'text_answer_user'])
admin.site.register(user_answer, User_answer)


# ________________________________________________________
class UserAnswerCheckboxButton(admin.ModelAdmin):
    list_display = (['id', 'textAnswer_userCheckbutton'])
    search_fields = (['id', 'textAnswer_userCheckbutton'])
admin.site.register(user_answerCheckboxButton, UserAnswerCheckboxButton)


# _________________________________________________________
class theme_all_objectPolls(admin.ModelAdmin):
    list_display = (['id', 'text_nameAll_theme'])
    search_fields = (['id', 'text_nameAll_theme'])
admin.site.register(Theme_all_ObjectPolls, theme_all_objectPolls)


# __________________________________________________________
class ThemeFor_Answer(admin.ModelAdmin):
    list_display = (['id', 'ThemeForAnswers'])
    search_fields = (['id', 'ThemeForAnswers'])
admin.site.register(ThemeForall_ObjectAnswer, ThemeFor_Answer)


# ________________________________________________________
class User_id_Radiobutton(admin.ModelAdmin):
    list_display = (['id', 'text_numberRadio'])
    search_fields = (['id', 'text_numberRadio'])
admin.site.register(user_idForRadiobutton,User_id_Radiobutton)


# ________________________________________________
class UserId_forCheckboxbutton(admin.ModelAdmin):
    list_display = (['id', 'text_numberCheckbox'])
    search_fields = (['id', 'text_numberCheckbox'])
admin.site.register(userIdForCheckboxbutton,UserId_forCheckboxbutton)


# _________________________________________________
class theme_forAll_ObjectId(admin.ModelAdmin):
    list_display = (['id', 'textnameAll_themeForId'])
    search_fields = (['id', 'textnameAll_themeForId'])
admin.site.register(ThemeForall_ObjectId,theme_forAll_ObjectId)


# ____________________________________________________
class userForQuestionsRadio_button(admin.ModelAdmin):
    list_display = (['id', 'radio_question'])
    search_fields = (['id', 'radio_question'])
admin.site.register(User_forQuestionsRadio_Button,userForQuestionsRadio_button)


# _____________________________________________________
class UserIdForQuestionsRadio_Button(admin.ModelAdmin):
    list_display = (['id', 'text_QuestionsRadio'])
    search_fields = (['id', 'text_QuestionsRadio'])
admin.site.register(User_Id_forQuestionsRadio_Button,UserIdForQuestionsRadio_Button)


# _______________________________________________________
class userForQuestionsCheckbox_Button(admin.ModelAdmin):
    list_display = (['id', 'checkbox_question'])
    search_fields= (['id', 'checkbox_question'])
admin.site.register(User_forQuestionsCheckbox_Button,userForQuestionsCheckbox_Button)


# __________________________________________________________
class userIdForQuestionsCheckbox_Button(admin.ModelAdmin):
    list_display = (['id', 'text_QuestionsCheckbox'])
    search_fields = (['id', 'text_QuestionsCheckbox'])
admin.site.register(User_Id_forQuestionsCheckbox_Button,userIdForQuestionsCheckbox_Button)


# ______________________________________________________
class theme_nameForId(admin.ModelAdmin):
    list_display = (['id', 'text_nameATheme'])
    search_fields = (['id', 'text_nameATheme'])
admin.site.register(Theme_name_ForId,theme_nameForId)

# _______________________________________________________
class DataTimeUser(admin.ModelAdmin):
    list_display = (['id', 'TimeNow'])
    search_fields = (['id', 'TimeNow'])
admin.site.register(Datatime,DataTimeUser)

# __________________________________________________________
class IdForDataTime(admin.ModelAdmin):
    list_display = (['id', 'TimeNow_Id'])
    search_fields = (['id', 'TimeNow_Id'])
admin.site.register(Id_forDataTime,IdForDataTime)

# __________________________________________________________
class dataFOR_END(admin.ModelAdmin):
    list_display = (['id', 'TimeEnd'])
    search_fields = (['id', 'TimeEnd'])
admin.site.register(DataEnd,dataFOR_END)