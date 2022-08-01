from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def registration_view(request):
    '''
    endpoint to handle registration request for a new user
    '''

@api_view(['POST'])
def login_view(request):
    '''
    endpoint to handle user login - set up authentication cookie (with jwt)
    '''

@api_view(['POST'])
def auth_view(request):
    '''
    endpoint to retrieve authentication information when given cookie 
    (to set up client state after refresh)
    '''

@api_view(['POST'])
def logout_view(request):
    '''
    endpoint to handle logout - revoke the cookie upon client's request
    '''