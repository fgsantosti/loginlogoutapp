from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def page_login(request):
	return render(request, 'blog/login.html',{})


def login(request):
	user = authenticate(username=request.POST['user'], password=request.POST['password'])
	if user is not None:
		return render(request, 'blog/authenticated_perfil.html',{'user':user})
	    #return render(request, 'blog/perfil.html',{'user':user})
	else:
		return render(request, 'blog/authenticated_perfil.html',{'user':user})
	    #return render(request, 'blog/login.html',{})

'''
def login(request):
	user = authenticate(username=request.POST['user'], password=request.POST['password'])
	return render(request, 'blog/authenticated_perfil.html',{'user':user})

'''
def logout_view(request):
	logout(request)
	return render(request, 'blog/login.html',{})
