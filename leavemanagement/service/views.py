from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Leave, LeaveType, User

# Create your views here.

class LeaveAPI(APIView):
	def post(self, request,format=None):
		data = self.request.data
		type_id=data.get("type")
		leavetype_inst = LeaveType.objects.get(id=type_id)
		user_id=data.get("user")
		user_instance=User.objects.get(id=user_id)
		leave_instace=Leave(desc=data.get("desc"),
			type=leavetype_inst,
			leavedate=data.get("leavedate"),
			user=user_instance)
		leave_instace.save()
		return Response("Leave created successfully")
	def put(self, request, pk,format=None):
		leave_instance=Leave.objects.get(id=pk)
		data = self.request.data 
		if "desc" in data:
			leave_instance.desc=data.get("desc")
		if "type" in data:
			type_id=data.get("type")
			leavetype_inst = LeaveType.objects.get(id=type_id)
			leave_instance.type=leavetype_inst
		if "user" in data:
			user_id=data.get("user")
			user_instance=User.objects.get(id=user_id)
			leave_instance.user=user_instance
		if "leavedate" in data:
			leave_instance.leavedate=data.get("leavedate")
		leave_instance.save()
		return Response("leave updated successfully!!")


		
	def get(self, request,pk=None, format=None):
		#return Response("hello world")
		if not pk:
			leaves=Leave.objects.all()
			
		if pk:
			leaves=Leave.objects.filter(id=pk)
		data = [{"id":obj.id,"description":obj.desc,"leavetype":obj.type.name,
		"leavedate":obj.leavedate,"applied":obj.user.username} for obj in leaves]
		return Response(data)
	def delete(self,request, pk,format=None):
		leave_instance=Leave.objects.get(id=pk)
		leave_instance.delete()
		return Response("leave deleted successfully")