from django.forms import ModelForm
from .models import *


class statmentForm(ModelForm):
	class Meta:
		model = category
		fields = ['gym']
