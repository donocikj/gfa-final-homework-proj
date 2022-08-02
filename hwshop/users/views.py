'''
implementation of views pertaining to the user and their authentication via jwt
'''
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def registration_view(request):
    '''
    endpoint to handle registration request for a new user
    '''
    return Response(data={"message":"registration attempt"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def login_view(request):
    '''
    endpoint to handle user login - set up authentication cookie (with jwt)
    '''
    return Response(data={"message":"login attempt"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def auth_view(request):
    '''
    endpoint to retrieve authentication information when given cookie 
    (to set up client state after refresh)
    '''

    return Response(data={"message":"auth recovery attempt?"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout_view(request):
    '''
    endpoint to handle logout - revoke the cookie upon client's request
    '''
    return Response(data={"message":"logout attempt"}, status=status.HTTP_200_OK)