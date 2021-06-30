from django import forms
# __________________________________________________________________________
choise_one_answer = ((1, 'x'), (2,'y'))
choise_two_answer = ((1, 'x'), (2, 'y'), (3, 'z'))
chois_three_answer = ((1, 'x'), (2, 'y'), (3, 'z'), (4, 'd'))
chois_fore_answer = ((1, 'x'), (2, 'y'), (3, 'z'), (4, 'd'), (5, 'e'))

# ___________________________________________________________________________
class formInput(forms.Form):
    text_pols = forms.CharField(max_length=200, label='', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

# ______________________________________________________________________
class MyForm(forms.Form):
    check = forms.MultipleChoiceField(choices=choise_one_answer,required=True,widget=forms.CheckboxSelectMultiple,)
    check_1 = forms.MultipleChoiceField(choices=choise_one_answer,required=True,widget=forms.CheckboxSelectMultiple, )
    RadiobuttonClick_1 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}),choices=chois_three_answer)

    RadiobuttonClick_2 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}), choices=choise_two_answer,)
    RadiobuttonClick_3 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}), choices=choise_two_answer,)
    RadiobuttonClick_4 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}),choices=chois_fore_answer,)
    RadiobuttonClick_5 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}), choices=chois_three_answer,)
    RadiobuttonClick_6 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}), choices=chois_three_answer,)
    RadiobuttonClick_7 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}), choices=choise_two_answer,)
    RadiobuttonClick_8 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}),choices=chois_three_answer,)
    RadiobuttonClick_9 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'star'}), choices=choise_two_answer)
