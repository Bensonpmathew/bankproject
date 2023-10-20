from django import forms

class regform1(forms.Form):
    fname=forms.CharField(max_length=30)
    lname = forms.CharField(max_length=30)
    uname = forms.CharField(max_length=30)
    num=forms.IntegerField()
    em=forms.EmailField()
    im=forms.FileField()
    pin=forms.CharField(max_length=30)
    cpin = forms.CharField(max_length=30)
    # ac_num=forms.IntegerField()


class logform1(forms.Form):
    uname=forms.CharField(max_length=30)
    pswd=forms.CharField(max_length=30)

class newsform(forms.Form):
    topic=forms.CharField(max_length=300)
    content = forms.CharField(max_length=3000)
    # date=forms.DateField(auto_now_add=True)


class adminform(forms.Form):
    username=forms.CharField(max_length=30)
    # email=forms.EmailField()
    password=forms.CharField(max_length=30)



class tablesform(forms.Form):

    name=forms.CharField(max_length=30)
    age = forms.CharField(max_length=30)
    number = forms.CharField(max_length=30)