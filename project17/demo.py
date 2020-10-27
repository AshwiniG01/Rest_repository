import requests
import json

BASE_URL='http://127.0.0.1:8000/'
END_POINT='crudapi/'

#get operation
def get_data(id=None):

	data = {}
	if id is not None:
		data  = {'id':id}

	response=requests.get(BASE_URL+END_POINT,data = json.dumps(data))
	print(response.status_code)
	print(response.json())

#get_data()

#post operation
def post_data():
	student_name=input("Enter Student Name: ")
	student_phone_no=int(input("Enter Phone Number of the Student: "))
	student_mail_id=input("Enter Student Mail Id: ")
	student_address=input("Enter Student Address: ")
	student_data={'student_name':student_name,'student_phone_no':student_phone_no,'student_mail_id':student_mail_id,'student_address':student_address}
	response = requests.post(BASE_URL+END_POINT,data=json.dumps(student_data))
	print(response.status_code)
	print(response.json())
#create_data()


#update operation
def update_data(id):
	student_name=input("Enter Student Name: ")
	student_phone_no=int(input("Enter Phone Number of the Student: "))
	student_mail_id=input("Enter Student Mail Id: ")
	student_address=input("Enter Student Address: ")
	student_data={'id':id,'student_name':student_name,'student_phone_no':student_phone_no,'student_mail_id':student_mail_id,'student_address':student_address}
	
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(student_data))
	print(response.json())
	print(response.status_code)


#delete operation
def delete_data(id):
	data={'id':id}
	response = requests.delete(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)




if __name__ == '__main__':
	print('Select your options to perform mentioned activities:\n 1 : (Get complete Data)\n 2 : (Post Complete data)\n 3 : (Update data based upon id)\n 4 : (Delete data based upon id)\n')

	choice=input('enter your choice to perform any of the mentioned activities: ')
	if choice=='1':
		get_data()
	elif choice=='2':
		post_data()
	elif choice=='3':
		id=int(input("Enter id: "))
		update_data(id)
	elif choice=='4':
		id=int(input("Enter id: "))
		delete_data(id)






