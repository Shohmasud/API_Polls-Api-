from rest_framework import serializers
from .models import Id_forDataTime,User_Id_forQuestionsCheckbox_Button,User_Id_forQuestionsRadio_Button,userIdForCheckboxbutton,user_idForRadiobutton,\
    Datatime,DataEnd,questions,Theme_all_ObjectPolls,ThemeForall_ObjectAnswer,Theme_name_ForId



class sId_forDataTime(serializers.ModelSerializer):
    class Meta:
        model = Id_forDataTime
        fields = '__all__'


# ________________________________________________
class sUser_Id_forQuestionsCheckbox_Button(serializers.ModelSerializer):
    relet_checkbox = serializers.SlugRelatedField(slug_field='checkbox_question',read_only=True,many=True)
    class Meta:
        model = User_Id_forQuestionsCheckbox_Button
        fields = '__all__'


# _____________________________________________
class sUser_Id_forQuestionsRadio_Button(serializers.ModelSerializer):
    relet_radio = serializers.SlugRelatedField(slug_field='radio_question',read_only=True,many=True)
    class Meta:
        model = User_Id_forQuestionsRadio_Button
        fields = '__all__'


# ____________________________________________
class suserIdForCheckboxbutton(serializers.ModelSerializer):
    numberAnswer_relForCheckBut = serializers.SlugRelatedField(slug_field='textAnswer_userCheckbutton',read_only=True,many=True)
    class Meta:
        model = userIdForCheckboxbutton
        fields = '__all__'


# ___________________________________________
class suser_idForRadiobutton(serializers.ModelSerializer):
    numberAnswer_relForRadioBut = serializers.SlugRelatedField(slug_field='text_answer_user',read_only=True,many=True)
    class Meta:
        model = user_idForRadiobutton
        fields = '__all__'


# ___________________________________________
class sDatatime(serializers.ModelSerializer):
    TimeNow_rel = serializers.SlugRelatedField(slug_field='TimeNow_Id',read_only=True,many=True)
    class Meta:
        model = Datatime
        fields = '__all__'


# ___________________________________________
class sDataEnd(serializers.ModelSerializer):
    TimeEnd_rel = serializers.SlugRelatedField(slug_field='TimeNow_Id',read_only=True,many=True)
    class Meta:
        model = DataEnd
        fields = '__all__'


# ____________________________________________
class squestions(serializers.ModelSerializer):
    name_category_questions = serializers.SlugRelatedField(slug_field='text_answer',read_only=True,many=True)
    class Meta:
        model = questions
        fields = '__all__'


# ___________________________________________________
class sTheme_all_ObjectPolls(serializers.ModelSerializer):
    nameTheme_questions = serializers.SlugRelatedField(slug_field='text_questions',read_only=True,many=True)
    class Meta:
        model = Theme_all_ObjectPolls
        fields = '__all__'


# _____________________________________________________
class sThemeForall_ObjectAnswer(serializers.ModelSerializer):
    nameTheme_questions_relAnwers = serializers.SlugRelatedField(slug_field='text_answer',read_only=True,many=True)
    class Meta:
        model = ThemeForall_ObjectAnswer
        fields = '__all__'


# ___________________________________________________
class sTheme_name_ForId(serializers.ModelSerializer):
    nameTheme_id = serializers.SlugRelatedField(slug_field='text_number',read_only=True,many=True)
    class Meta:
        model = Theme_name_ForId
        fields = '__all__'