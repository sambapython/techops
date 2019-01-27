from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Customer
# Create your views here.
def index_view(request):
	return render(request,"app1/index.html")
def customers_view(request):
	data =Customer.objects.all()
	return render(request, "app1/customers.html",{"data":data})
def cust_delte_view(request,cust_id):
	customer=Customer.objects.get(id=cust_id)
	message=""
	if request.method=="POST":
		customer.delete()
		message="customer deleted successfuly"
		return redirect("/web_customers/")
	return render(request,"app1/cust_delete_form.html",
		{"name":customer.name,"email":customer.email,"msg":message})
def cust_update_view(request, cust_id):
	customer=Customer.objects.get(id=cust_id)
	message=""
	if request.method=="POST":
		new_data=request.POST 
		customer.name=new_data.get('cust_name')
		customer.email=new_data.get('cust_email')
		customer.save()
		message="customer updated successfuly"
		return redirect("/web_customers/")
	return render(request,"app1/cust_update_form.html",
		{"name":customer.name,"email":customer.email,"msg":message})
'''
def cust_create_view(request):
	resp="""
		<html>
			<body>
				<h1>HELLO</h1>
			</body>
		</html>
	"""
	return HttpResponse(resp)
'''
def cust_create_view(request):
	# render will read the data from template and it will create HTtpResponse object with 
	#the data it is read and send it to the server. 
	message=""
	if request.method=="POST":
		data = request.POST
		obj = Customer(name=data.get("cust_name"),email=data.get("cust_email"))
		obj.save()
		message="customer created successfully!!"
		return redirect("/web_customers/")
	return render(request, "app1/cust_create_form.html",
		{"msg":message})
class CustomerAPIView(APIView):
	def get(self,format=None):
		customers = Customer.objects.all()
		data=[]
		for customer in customers:
			data.append({"name":customer.name,"email":customer.email})
		return Response(data)
	def post(self,format=None):
		pass
	def put(self,format=None):
		pass
	def delete(self,format=None):
		pass
def fun(request):
	# connect to database
	# filter the users
	#resp = requests.get("url",auth=(username, password))
	return HttpResponse(["user1","user2"])
