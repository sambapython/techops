from django.shortcuts import render
from django.http import HttpResponse
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class CustomerAPIView(APIView):
	def get(self,format=None):
		return Response(["user1","user2","user3"])
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
