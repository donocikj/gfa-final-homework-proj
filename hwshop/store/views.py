'''
implementation of views pertaining to store logic
'''

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def list_view(request):
    '''
    view for handling of the item list
    GET - retrieve list of all items available for sale
    POST - create an item to be listed for sale
    '''
    if request.method == 'POST':
        return Response(data={"message":"new item listing attempt"}, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        return Response(data={"message":"listed items list retrieval attempt"}, status=status.HTTP_200_OK)
    else:
        return Response(data={"message":"no such method allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST'])
def item_detail_view(request, id):
    '''
    view for handling individual items.
    GET - retrieve detailed information on item
    POST - purchase an item
    '''
    if request.method == 'POST':
        return Response(data={"message":"new item listing attempt"}, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        return Response(data={"message":"listed items list retrieval attempt"}, status=status.HTTP_200_OK)
    else:
        return Response(data={"message":"no such method allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
