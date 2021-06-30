
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from psycopg2 import IntegrityError
from rest_framework import generics
import re
from .models import *
from .serializers import *
from .forms import formInput,MyForm
from  rest_framework.views import APIView
from  rest_framework.response import Response
from datetime import datetime, date, time

# __________________________________________________Получаем необходимы модели
form = formInput()
my_form = MyForm()
text_sitepolls = sitepolls.objects.all()
text = Interview.objects.all()
questions_class = questions.objects.all()
answer_class = answer.objects.all()
radio_button = category_button.objects.all()
button_checkbox = checkbox_button.objects.all()
themFor_ID = ThemeForall_ObjectId.objects.all()


# ___________________________________________________Состовляем сортированные списки в ходе программы
len_questions = []
len_list = []
result_radbutton_answer = []
result_chekbutton_answer = []
radioquestionAll = []
checkboxanswerAll = []
number_userId = 0

# _____________________________________________Класс серелизатор:получение ID всех пользователей которые прошли опрос
class SerializerId_forDataTime(APIView):
    # serializer_class = sId_forDataTime
    def get(self,request):
        all_object = Id_forDataTime.objects.all()
        serializers = sId_forDataTime(all_object,many=True)
        return Response(serializers.data)

# _________________________________Класс серелизатор: получение вопросов от ответов пользователей типа выборки Checkbox
class SerializerUser_IdforQuestionsCheckbox_Button(APIView):
    def get(self,request):
        all_object = User_Id_forQuestionsCheckbox_Button.objects.all()
        serializers2 = sUser_Id_forQuestionsCheckbox_Button(all_object,many=object)
        return Response(serializers2.data)

# ___________________________Класс серелизатор:получение получение вопросов от ответов пользователей типа выборки Radio
class SerializerUser_Id_forQuestionsRadio_Button(APIView):
    def get(self,request):
        all_object = User_Id_forQuestionsRadio_Button.objects.all()
        serializers =  sUser_Id_forQuestionsRadio_Button(all_object,many=True)
        return Response(serializers.data)

# ______________________________________________Класс серелизатор:получение ответов пользователей типа выборки Checkbox
class SerializeruserId_Checkboxbutton(APIView):
    def get(self,request):
        all_object = userIdForCheckboxbutton.objects.all()
        serializers =  suserIdForCheckboxbutton(all_object,many=True)
        return Response(serializers.data)

# __________________________________Класс серелизатор:получение ответов пользователей типа выборки Radio
class SerializeruseridForRadiobutton(APIView):
    def get(self,request):
        all_object = user_idForRadiobutton.objects.all()
        serializers =  suser_idForRadiobutton(all_object,many=True)
        return Response(serializers.data)

# _____________________________________Класс серелизатор:получение начало даты и времени прохождения опроса
class SerializerDatatime(APIView):
    def get(self,request):
        all_object = Datatime.objects.all()
        serializers =  sDatatime(all_object,many=True)
        return Response(serializers.data)

# _____________________________________________________Класс серелизатор:окончание даты и времени прохождения опроса
class SerializerDataEnd(APIView):
    def get(self,request):
        all_object = DataEnd.objects.all()
        serializers =  sDataEnd(all_object,many=True)
        return Response(serializers.data)

# ________________________________________________Класс серелизатор:получение всех вопрос-ответ опроса
class Serializerquestions(APIView):
    def get(self,request):
        all_object = questions.objects.all()
        serializers =  squestions(all_object,many=True)
        return Response(serializers.data)

# ___________________________________________Класс серелизатор:получение категории опроса к которым относяться вопросы
class SerializerTheme_all_ObjectPolls(APIView):
    def get(self,request):
        all_object = Theme_all_ObjectPolls.objects.all()
        serializers =  sTheme_all_ObjectPolls(all_object,many=True)
        return Response(serializers.data)

# ____________________________________________Класс серелизатор:получение категории опроса к которым относяться ответы
class SerializerThemeForall_ObjectAnswer(APIView):
    def get(self,request):
        all_object = ThemeForall_ObjectAnswer.objects.all()
        serializers =  sThemeForall_ObjectAnswer(all_object,many=True)
        return Response(serializers.data)

# ___________________________________________Класс серелизатор:получение категории опроса к которым относяться ответы
class SerializersTheme_name_ForId(APIView):
    def get(self,request):
        all_object = Theme_name_ForId.objects.all()
        serializers = sTheme_name_ForId(all_object,many=True)
        return Response(serializers.data)


# _______________________________Состовляем словарь id-название опроса
def functionForId_user(model):
    id_Dict = {}
    for model in model:
        id = id_Dict[model.textnameAll_themeForId] = []
        for rel_id in model.nameTheme_questions_relId.values_list():
            id.append(rel_id[1])
    return id_Dict


# _________________________В этом болке из поле ввода внутреннего API  получаем сылку котор содержит так же число ID
"Если id cуществует в словаре составленый из базы данных то не пускаем пользователя ,иначе пускаем пользователя для" \
"прохождение опроса"
def index(request):
    global id_number
    result_box = []
    if request.method == 'POST':
        f = formInput(request.POST)
        if f.is_valid():
            valid = f.cleaned_data['text_pols']
            result_box.append(valid)
            result = re.findall(r'home/api/v6/[\d+]+', valid)
            try:
                if str(result[0]) == str(result_box[0]):
                    find_num = re.findall(r'[\d*]*', result[0])
                    num_for_id = [*filter(None, find_num)]
                    try:
                        result_ThemeId = functionForId_user(themFor_ID)
                        for key, value in result_ThemeId.items():
                            if int(num_for_id[1]) not in value:
                                num = int(num_for_id[1])
                                global number_userId
                                number_userId = num
                                user_id.objects.create(text_number=int(num_for_id[1]))
                                return redirect('ques')
                    except:
                        return render(request, 'interview_api/polls.html',
                                      {'text': text, 'form': form,
                                       'tracback': 'Введёный Id занята другим ползователем'})


            except IndexError:
                return render(request, 'interview_api/polls.html',
                              {'text': text, 'form': form, 'tracback': 'Введите API правильно'})

    return render(request, 'interview_api/polls.html', {'text': text, 'form': form})



# ___________________________________В этом болке получаем из базы даных список всех вопро-ответов из текущего опроса
def func_vel():
    result = {}
    for w in questions.objects.all():
        result[w.text_questions] = []
        len_questions.append(w.text_questions)
        len_list.append(w.text_questions)
        for i in w.name_category_questions.values():
            result[w.text_questions].append(i['text_answer'])
    return result


# ________________________________________________В этом блоке получаем типы ответов относящийся к Radio,Checkbutton
def func_answer_for_radiobutton(name_category_button):
    if name_category_button is category_button:
        for w in name_category_button.objects.all():
            for i in w.name_category_button_radio.values_list():
                result_radbutton_answer.append(i[1])
    if name_category_button is checkbox_button:
        for w in name_category_button.objects.all():
            for i in w.name_category_button_checkbox.values_list():
                result_chekbutton_answer.append(i[1])

func_answer_for_radiobutton(category_button)
func_answer_for_radiobutton(checkbox_button)


# ______В этом блоке получаем типы ответов-вопросов относящийся к Radio,Checkbutton с могут повторятся по несколько раз
# далее сортируем их в другом блоке
result_releted = func_vel()
def func_generate_answer_objects_button(list, elem):
    for k in result_releted.keys():
        for v_answer_for_button in list:
            if v_answer_for_button in result_releted[k]:
                elem.append(k)
                continue
            continue
func_generate_answer_objects_button(result_radbutton_answer, radioquestionAll)
func_generate_answer_objects_button(result_chekbutton_answer, checkboxanswerAll)

radioquestionAll = sorted([*set(radioquestionAll)])  #Сортируем повторящиеся элементы
checkboxanswerAll = sorted([*set(checkboxanswerAll)])


# _____________________________В этом блоке получаем нужные нам для вывода в приложения вопросы и ответы
# относящийся к Radio,Checkbutton
resultEnd_radio = dict()
resultEnd_checkbox = dict()
def functions_result(list):
    for question_radiobutton in list:
        for all_elementquestions, all_elementanswer in result_releted.items():
            if question_radiobutton == all_elementquestions:
                if list == radioquestionAll:
                    resultEnd_radio[all_elementquestions] = all_elementanswer
                else:
                    resultEnd_checkbox[all_elementquestions] = all_elementanswer
functions_result(radioquestionAll)
functions_result(checkboxanswerAll)



# _________________________________В этом блоке с настоящим API переходим в страницу опроса и проходим опрос
def number_pk(request, pk):
    global number_userId
    if request.method == 'POST':
        pass
    for n in user_id.objects.all():
        try:
            result_ThemeId = functionForId_user(themFor_ID)
            for key, value in result_ThemeId.items():
                print(value)
                if pk not in value:
                    number_userId = pk
                    print(number_userId)
                    user_id.objects.create(text_number=pk)
                    return  redirect('ques')
        except:
            return render(request, 'interview_api/polls.html',
                              {'text': text, 'tracback': 'Введёный Id занята другим ползователем'})

# _________________________________В этом блоке получаем и оправляем данные в Базу данных
# так же рендерим шаблон страницы Опроса
def Questions(request):
    print(number_userId)
    global data_now
    data_now = str(datetime.now())
    global checkboxAnswer, get_rel
    if request.method == 'POST':
        forms = MyForm(request.POST)
        if forms.is_valid():
            try:
                def save():
                    resultclean = forms.cleaned_data
                    result_cleanedDate = [data for data in resultclean.values()]
                    print(result_cleanedDate)
                    checkbox_number = [cleanData for cleanData in result_cleanedDate if type(cleanData) is list]
                    checkbox_number_Answer = [int(answer) for check in checkbox_number for answer in check]
                    radiobutton_number_Answer = [int(cleanData) for cleanData in result_cleanedDate if type(cleanData) is not list]
                    chekbox_value = [v for k, v in resultEnd_checkbox.items()]
                    radio_value = [v for k, v in resultEnd_radio.items()]
                    # try:_____________________________В этом блоке получаем и сохроняем вопро-ответ нужного типа после
                    # прохождения пользователем опроса ,в нужный нам в базе данных таблицу
                    try:
                        resultclean = forms.cleaned_data
                        result_cleanedDate = [data for data in resultclean.values()]
                        print(result_cleanedDate)
                        checkbox_number = [cleanData for cleanData in result_cleanedDate if type(cleanData) is list]
                        checkbox_number_Answer = [int(answer) for check in checkbox_number for answer in check]
                        radiobutton_number_Answer = [int(cleanData) for cleanData in result_cleanedDate if type(cleanData) is not list]
                        chekbox_value = [v for k, v in resultEnd_checkbox.items()]
                        radio_value = [v for k, v in resultEnd_radio.items()]
                        id = userIdForCheckboxbutton.objects.create(text_numberCheckbox=number_userId)
                        id_Radiobutton = user_idForRadiobutton.objects.create(text_numberRadio=number_userId)
                    except:
                        id = userIdForCheckboxbutton.objects.get(text_numberCheckbox=number_userId)
                        id_Radiobutton = user_idForRadiobutton.objects.get(text_numberRadio=number_userId)
                    i = 0
                    for answer in checkbox_number:
                        for num in answer:
                            try:
                                checkboxAnswer = user_answerCheckboxButton.objects.create(
                                    textAnswer_userCheckbutton=chekbox_value[i][int(num) - 1])
                                id.numberAnswer_relForCheckBut.add(checkboxAnswer)
                            except:
                                get_rel = user_answerCheckboxButton.objects.get(
                                    textAnswer_userCheckbutton=chekbox_value[i][int(num) - 1])
                                id.numberAnswer_relForCheckBut.add(get_rel)
                            continue
                        i += 1
                        j = 0
                        for numberRadio in radiobutton_number_Answer:
                            try:
                                radioAnswer = user_answer.objects.create(
                                    text_answer_user=radio_value[j][numberRadio - 1])
                                id_Radiobutton.numberAnswer_relForRadioBut.add(radioAnswer)
                                j += 1
                            except:
                                get_radio = user_answer.objects.get(text_answer_user=radio_value[j][numberRadio - 1])
                                id_Radiobutton.numberAnswer_relForRadioBut.add(get_radio)
                                j += 1
                            continue

                    # ____________________В этом блоке получаем и сохраняем данные вопросы относящиеся к типам выборки
                    # Radio
                    try:
                        id_QuestionsRadio = User_Id_forQuestionsRadio_Button.objects.create(
                            text_QuestionsRadio=number_userId)
                    except:
                        id_QuestionsRadio = User_Id_forQuestionsRadio_Button.objects.get(
                            text_QuestionsRadio=number_userId)
                    for questions in resultEnd_radio.keys():
                        try:
                            textQuestionsRadio_Button = User_forQuestionsRadio_Button.objects.create(
                                radio_question=questions)
                            id_QuestionsRadio.relet_radio.add(textQuestionsRadio_Button)
                        except:
                            textQuestionsRadio_Button = User_forQuestionsRadio_Button.objects.get(
                                radio_question=questions)
                            id_QuestionsRadio.relet_radio.add(textQuestionsRadio_Button)

                    # _____________________В этом блоке получаем и сохраняем данные вопросы относящиеся к типам выборки
                    # Checkbox
                    try:
                        id_QuestionsCheckbox = User_Id_forQuestionsCheckbox_Button.objects.create(
                            text_QuestionsCheckbox=number_userId)
                    except:
                        id_QuestionsCheckbox = User_Id_forQuestionsCheckbox_Button.objects.get(
                            text_QuestionsCheckbox=number_userId)
                    for questions in resultEnd_checkbox.keys():
                        try:
                            textQuestionsCheckbox_Button = User_forQuestionsCheckbox_Button.objects.create(
                                checkbox_question=questions)
                            id_QuestionsCheckbox.relet_checkbox.add(textQuestionsCheckbox_Button)
                        except:
                            textQuestionsCheckbox_Button = User_forQuestionsCheckbox_Button.objects.get(
                                checkbox_question=questions)
                            id_QuestionsCheckbox.relet_checkbox.add(textQuestionsCheckbox_Button)

                    # _____________________В этом блоке получаем и сохраняем Id пользователя относящийся к теме опроса
                    try:
                        id_user = user_id.objects.create(text_number=number_userId)
                    except:
                        id_user = user_id.objects.get(text_number=number_userId)
                    for namePolls in sitepolls.objects.all():
                        try:
                            name_pols = ThemeForall_ObjectId.objects.get(textnameAll_themeForId=namePolls.text_polls)
                            name_pols.nameTheme_questions_relId.add(id_user)
                        except:
                            name_pols = ThemeForall_ObjectId.objects.create(textnameAll_themeForId=namePolls.text_polls)
                            name_pols.nameTheme_questions_relId.add(id_user)

                    # ____________________В этом блоке получаем и сохраняем дату и время начало опроса
                    try:
                        UserFOR_id = Id_forDataTime.objects.create(TimeNow_Id=number_userId)
                    except:
                        UserFOR_id = Id_forDataTime.objects.get(TimeNow_Id=number_userId)
                    try:
                        timE_now = Datatime.objects.create(TimeNow=data_now)
                    except:
                        timE_now = Datatime.objects.get(TimeNow=data_now)
                        timE_now.TimeNow_rel(UserFOR_id)


                return redirect('next')

            except:
                return redirect('snd')
        else:
           return redirect('ques')


    return render(request, 'interview_api/questions.html',
                  {'questions': text_sitepolls, 'send': MyForm(), 'radiobuttonObj': resultEnd_radio,
                   'checkbuttonObj': resultEnd_checkbox})


# _______________________________В этом блоке рендерим шаблон страницы потверждения
def Next(request):
    if request.method == 'POST':
         pass
    return render(request, 'interview_api/confirmation.html')


# _____________________________В этом блоке получаем дату и время окончания прохождение опроса
def function_end_data():
    data_end = datetime.now()
    try:
        UserFOR_id = Id_forDataTime.objects.create(TimeNow_Id=number_userId)
    except:
        UserFOR_id = Id_forDataTime.objects.get(TimeNow_Id=number_userId)
    try:
        timE_End = DataEnd.objects.create(TimeEnd=data_end)
    except:
        timE_End = DataEnd.objects.get(TimeEnd=data_end)
        timE_End.TimeEnd_rel(UserFOR_id)


# _____________________________В этом блоке рендерим окончания опроса
def Send(request):
    function_end_data()
    global data_after
    data_after = datetime.now()
    conversion = True
    if request.method == 'POST':
        pass

    return render(request, 'interview_api/send.html')



# _________________________________В этом блоке рендерим шаблон документации
def functionDocumentations(request):
    if request.method == 'POST':
        pass
    return render(request,'interview_api/Documentation.html')




