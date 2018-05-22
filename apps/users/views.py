from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def landing(request):
	return redirect('/users')

def userslist(request):
	context={
		"users": User.objects.all()
	}
	return render(request, 'users/index.html', context)

def user(request, id):
	context={
		"user": User.objects.get(id = id)
	}

	return render(request, 'users/userInfo.html', context)

def userEdit(request, id):
	context={
		"user": User.objects.get(id = id)
	}
	request.session['user_id'] = id
	return render(request, 'users/edit.html', context)

def userDelete(request, id):
	print("deleting user --->", id)
	user = User.objects.get(id = id)
	user.delete()
	return redirect('/')

def userNew(request):
	return render(request, 'users/login.html')

def userCreate(request):
	canCreate = False
	if request.method == "POST":
		request.session['first_name'] = request.POST['first_name']
		request.session['last_name'] = request.POST['last_name']
		request.session['email'] = request.POST['email']
		newUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
		newUser.save()
		print("in here")
		response = [request.session['first_name'],request.session['last_name'],request.session['email']]
		return redirect("/users")
	elif canCreate == True:
		response = "create one"
	else:
		response = "didnt work"
	return HttpResponse(response)

def userUpdate(request):
	if request.method == "POST":
		updatedUser = User.objects.get(id = request.session['user_id'])
		updatedUser.first_name = request.POST['first_name']
		updatedUser.last_name = request.POST['last_name']
		updatedUser.email = request.POST['email']
		updatedUser.save()
	return redirect('/')



