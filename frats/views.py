# Create your views here.
from django.shortcuts import *
from unis.models import *
from models import *
from users.models import *

def detail(request, university_name, frat_name):
	return render_to_response('frats/index.html', {'frats':frats})

def index(request, university_name):
	uni = University.objects.get(name = university_name)
	frats = Frat.objects.filter(university = uni)
	return render_to_response('frats/index.html', {'frats':frats})
	
def profile(request, university_name, frat_name, user_name):
	return render_to_response('users/profile.html', {'frats':frats})