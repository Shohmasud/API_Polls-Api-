from django.db import models
# Create your models here.
# _________________________________________________________
class Interview(models.Model):
    text_pols = models.CharField(verbose_name='Заголовок опроса', db_index=True, unique=True, max_length=400)
    text_entry = models.CharField(verbose_name='Описание входа', db_index=True, unique=True, max_length=400)
    text_example_id = models.CharField(verbose_name='Описание id', db_index=True, unique=True,max_length=400)
    text_id = models.CharField(verbose_name='Пример состовление Api ', db_index=True, unique=True, max_length=400)
    text_button = models.CharField(verbose_name='Кнопка входа', db_index=True, unique=True, max_length=400)

    class Meta:
        verbose_name = '[Динамические временные данные,заполняет админ]-описание входа в приложение через внутренний api(1 страница приложения)'
        ordering = ['id']


# ____________________________________________________________
class sitepolls(models.Model):
        text_polls = models.CharField(verbose_name='Тема опроса', db_index=True, unique=True, max_length=1000)
        text_head_handling = models.CharField(verbose_name='Заголовок обращения', db_index=True, unique=True, max_length=1000)
        text_handling = models.CharField(verbose_name='Обращения', db_index=True, unique=True,max_length=1000)
        text_for_whom = models.CharField(verbose_name='Для кого', db_index=True, unique=True, max_length=1000)

        class Meta:
           verbose_name = '[Динамические временные данные,заполняет админ]-описание заголовок и названия приложения (1 страница приложения)'
           ordering = ['id']


# ________________________________________________________________
class answer(models.Model):
    text_answer = models.CharField(verbose_name='Ответы',max_length=100,db_index=True, unique=True)

    class Meta:
        verbose_name = '[Статичные данные,заполняет админ]-Ответы'
        ordering = ['id']
    def __str__(self):
        return self.text_answer


# ____________________________________________________________________
class questions(models.Model):
        text_questions = models.CharField(verbose_name='Вопросы', max_length=400, db_index=True, unique=True)
        name_category_questions = models.ManyToManyField(answer)

        class Meta:
            verbose_name = '[Статичные данные данные,заполняет админ]-Вопросы'
            ordering = ['id']
        def __str__(self):
            return self.text_questions


# _________________________________________________________________________
class Theme_all_ObjectPolls(models.Model):
    text_nameAll_theme = models.CharField(verbose_name='Название опроса относящийся к определенным вопросы', db_index=True, unique=True, max_length=400)
    nameTheme_questions = models.ManyToManyField(questions)
    class Meta:
        verbose_name = '[Статичные данные,заполняет админ]-список всех вопросов относящиеся к теме опроса'
        ordering = ['id']


# _____________________________________________________________________________
class ThemeForall_ObjectAnswer(models.Model):
    ThemeForAnswers = models.CharField(verbose_name='Название опроса для всех ответов ', db_index=True, unique=True, max_length=400)
    nameTheme_questions_relAnwers = models.ManyToManyField(answer)

    class Meta:
        verbose_name = '[Статичные данные,заполняет админ]-список всех ответов относящиеся к теме опроса'
        ordering = ['id']


# ________________________________________________________________________________
class category_button(models.Model):
    radio_button = models.CharField(verbose_name='Радио кнопка', max_length=400, db_index=True, unique=True)
    name_category_button_radio = models.ManyToManyField(answer)
    class Meta:
        verbose_name = '[Динамические временные данные,заполняет админ]-выборка ответов типа Radio отображающиеся в приложении, вопрос сгенерируется автоматичеки'
        ordering = ['id']

    def __str__(self):
       return  self.radio_button


# ______________________________________________________________________________________
class checkbox_button(models.Model):
    checkbox_button = models.CharField(verbose_name='Чекбокс кнопка', max_length=400, db_index=True, unique=True)
    name_category_button_checkbox = models.ManyToManyField(answer)
    class Meta:
        verbose_name = '[Динамические временные данные,заполняет админ]-выборка ответов типа CheckboxButton отображающиеся в приложении, вопрос сгенерируется автоматичеки'
        ordering = ['id']
    def __str__(self):
        return self.checkbox_button


# ____________________________________________________________________________________________
class user_id(models.Model):
    text_number = models.BigIntegerField(verbose_name='Хранения числогвого ID пользователя', unique=True)
    class Meta:
        verbose_name = '[Автозаполнение]-Id пользователя'
        ordering = ['id']

    def __int__(self):
        return self.text_number


# _________________________________________________________________________________
class user_answer(models.Model):
    text_answer_user = models.CharField(verbose_name='Ответы типа радио кнопка', max_length=400, db_index=True, unique=True)
    class Meta:
        verbose_name = '[Автозаполнение]-Ответы пользователя относящиеся к вопросу типа выборки Radiobutton'
        ordering = ['id']
    def __str__(self):
        return self.text_answer_user


# ______________________________________________________________________________________
class user_answerCheckboxButton(models.Model):
    textAnswer_userCheckbutton = models.CharField(verbose_name='Ответы  типа чекбокс кнопки', max_length=400, db_index=True, unique=True)
    class Meta:
        verbose_name = '[Автозаполнение]-Ответы пользователя относящиеся к типу выборки CheckboxButton'
        ordering = ['id']
    def __str__(self):
        return self.textAnswer_userCheckbutton


# __________________________________________________________________________________________
class user_idForRadiobutton(models.Model):
    text_numberRadio = models.BigIntegerField(verbose_name='Хранения числогвого ID для радио кнопки', unique=True)
    numberAnswer_relForRadioBut = models.ManyToManyField(user_answer)
    class Meta:
        verbose_name = '[Автозаполнение]-ID пользователя относящиеся к типу выборки Radiobutton'
        ordering = ['id']


# _____________________________________________________________________________________________
class userIdForCheckboxbutton(models.Model):
    text_numberCheckbox = models.BigIntegerField(verbose_name='Хранения числогвого ID для Чекбокс кнопки', unique=True)
    numberAnswer_relForCheckBut = models.ManyToManyField(user_answerCheckboxButton)
    class Meta:
        verbose_name = '[Автозаполнение]-ID пользователя относящиеся к типу выборки Checkboxbutton'
        ordering = ['id']


# ____________________________________________________________________________________________________
class ThemeForall_ObjectId(models.Model):
    textnameAll_themeForId = models.CharField(verbose_name='Название опроса для Id ползователя', db_index=True, unique=True, max_length=400)
    nameTheme_questions_relId = models.ManyToManyField(user_id)
    class Meta:
        verbose_name = '[Динамические временные данные,заполняет админ]-динамическое название опроса для Id ползователя,для логики работы приложения'
        ordering = ['id']


# _______________________________________________________________________________________
class User_forQuestionsRadio_Button(models.Model):
    radio_question = models.CharField(verbose_name='Вопросы относящиеся к ответам кнопки Радио от пользователя',db_index=True,unique=True, max_length=400)
    class Meta:
        verbose_name = '[Автозаполнение]-Вопросы ответов пользователя относящиеся к типу выборки Radio_Button'
        ordering = ['id']

    def __str__(self):
        return self.radio_question


# _______________________________________________________________________________________
class User_Id_forQuestionsRadio_Button(models.Model):
    text_QuestionsRadio = models.BigIntegerField(
        verbose_name='Хранения числогвого ID для вопросов от ответов Радио кнопки', unique=True)
    relet_radio = models.ManyToManyField(User_forQuestionsRadio_Button)

    class Meta:
        verbose_name = '[Автозаполнение]-ID пользователя относящиеся к типу выборки Radiobutton'
        ordering = ['id']


# ____________________________________________________________________________________________
class User_forQuestionsCheckbox_Button(models.Model):
    checkbox_question = models.CharField(verbose_name='Вопросы относящиеся к ответам кнопки Чекбокс от пользователя',
                                      db_index=True,
                                      unique=True, max_length=400)
    class Meta:
        verbose_name = '[Автозаполнение]-Вопросы ответов пользователя относящиеся к типу выборки Checkboxbutton '
        ordering = ['id']
    def __str__(self):
        return self.checkbox_question


# ________________________________________________________________________________________________
class User_Id_forQuestionsCheckbox_Button(models.Model):
    text_QuestionsCheckbox = models.BigIntegerField(
        verbose_name='Хранения числогвого ID для вопросов от ответов Чекбокс кнопки', unique=True)
    relet_checkbox = models.ManyToManyField(User_forQuestionsCheckbox_Button)
    class Meta:
        verbose_name = '[Автозаполнение]-ID пользователя относящиеся к вопросу типа выборки Checkboxbutton '
        ordering = ['id']


# __________________________________________________________________________________________________
class Theme_name_ForId(models.Model):
    text_nameATheme = models.CharField(verbose_name='Название опроса относящийся к ID-пользователя', db_index=True, unique=True, max_length=400)
    nameTheme_id = models.ManyToManyField(user_id)
    class Meta:
        verbose_name = '[Статичные данные,заполняет админ]-список названии тем опроса относящиеся к ID пользователя'
        ordering = ['id']


# ____________________________________________________________________________________________________
class Id_forDataTime(models.Model):
    TimeNow_Id = models.BigIntegerField(verbose_name='ID пользователя для начало даты и времени опроса', unique=True)
    class Meta:
        verbose_name = '[Автозаполнение]-ID пользователя для даты и времени опроса пользователя'
        ordering = ['id']
    def __int__(self):
        return self.TimeNow_Id


 
class DataEnd(models.Model):
    TimeEnd = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True)
    TimeEnd_rel = models.ManyToManyField(Id_forDataTime)
    class Meta:
        verbose_name = '[Автозаполнение]-Дата окочание опроса пользователя(Id)'
        ordering = ['id']   
    
    
# _______________________________________________________________________________________
class Datatime(models.Model):
    TimeNow = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    TimeNow_rel = models.ManyToManyField(Id_forDataTime)
    class Meta:
        verbose_name = '[Автозаполнение]-Дата и время старта опроса пользователя(Id)'
        ordering = ['id']

