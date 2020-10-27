from django.shortcuts import render
from django.views.generic import View
from curdapp.models import Student
from curdapp.forms import StudentForm
from curdapp.utils import is_data_json
from django.http import HttpResponse
from curdapp.mixins import MixinHttpResponse,SerializeMixin
from django.core.serializers import serialize
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentDetailsCbv(MixinHttpResponse,SerializeMixin,View):
	def get_object_data_by_id(self,id):
		try:
			student=Student.objects.get(id=id)
		except Student.DoesNotExist:
			student=None
		return student

	#GET Method
	def get(self,request,*args,**kwargs):
		data=request.body

		#checking whether json data or not
		valid_json_data=is_data_json(data)
		#If not valid json data then dispaly Error message

		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_http_response(json_data,status=400)
		#coverting json data into python dictionary format
		entered_data=json.loads(data)

		id=entered_data.get('id',None)
		#if id is None
		if id is not None:
			student=self.get_object_data_by_id(id=id)
		#if student is None
			if student is None:
				json_data=json.dumps({'msg':'The requested data is not available'})
				return self.render_http_response(json_data,status=400)
			#if student is not none
			json_data=self.serialize([student,])
			return self.render_http_response(json_data)
		#if id is not None 
		query_string=Student.objects.all()
		json_data=self.serialize(query_string)
		return self.render_http_response(json_data)

		#POST Method

	def post(self,request,*args,**kwargs):
		data=request.body

		#checking whether json data or not
		valid_json_data=is_data_json(data)
		#If not valid json data then dispaly Error message

		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_http_response(json_data,status=400)
		#coverting json data into python dictionary format
		student_data=json.loads(data)
		form=StudentForm(student_data)
		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg':'Data created successfully'})
			return self.render_http_response(json_data)

		

			#update operation
	def put(self,request,*args,**kwargs):
		data=request.body
		valid_json_data=is_data_json(data)
		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		"""This  data is from  Python application inorder to update"""
		entered_data = json.loads(data)

		id=entered_data.get('id',None)

		if id is None:
			json_data=json.dumps({'msg':'Id is mandatory to perform update operation'})
			return self.render_to_http_response(json_data,status=400)

		student=self.get_object_data_by_id(id)

		if student is None:
			json_data = json.dumps({'msg':'The required data is not available'})
			return self.render_http_response(json_data,status=404)

		
		original_data = {'student_name':student.student_name,'student_phone_no':student.student_phone_no,'student_mail_id':student.student_mail_id,'student_address':student.student_address}
		
		print('Data before Updation')
		print(original_data)
		
		print('Data After updation')
		#Performing updation on the existing original data
		original_data.update(entered_data)
		print(original_data)

		form = StudentForm(original_data,instance=student)
		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg':'Data Updated successfully'})
			return self.render_http_response(json_data)


		#delete operation
		
	def delete(self,request,*args,**kwargs):
			data=request.body
			valid_json_data=is_data_json(data)
			if not valid_json_data:
				json_data=json.dumps({'msg':'Please send the valid json data'})
				return self.render_http_response(json_data,status=400)

			"""This  data is from  Python application inorder to update"""
			entered_data = json.loads(data)

			id=entered_data.get('id',None)

			if id is not None:
				student = self.get_object_data_by_id(id)
				if student is None:
					json_data = json.dumps({'msg':'deletion is not possible'})
					return self.render_http_response(json_data,status=404)
				(status,deleted_item)=student.delete()
				if status==1:
					json_data=json.dumps({'msg':'Resource deleted successfully'})
					return self.render_http_response(json_data)
				json_data=json.dumps({'msg':'data is not deleted '})
				return self.render_http_response(json_data)

			json_data=json.dumps({'msg':'To perform deletion id is compulsory'})
			return self.render_http_response(json_data,status=400)

			form = StudentForm(original_data,instance=student)
			if form.is_valid():
				form.save(commit=True)
				json_data = json.dumps({'msg':'Data deleted successfully'})
				return self.render_http_response(json_data)

			
