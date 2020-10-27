from django import forms
from curdapp.models import Student
class StudentForm(forms.ModelForm):
	"""form validation"""
	def clean_student_phone_no(self):
		phone_no=self.cleaned_data['student_phone_no']
		if phone_no<10:
			raise forms.ValidationError('The minimum digits should be 10')
		return phone_no
	class Meta:
		model = Student
		fields = '__all__'
