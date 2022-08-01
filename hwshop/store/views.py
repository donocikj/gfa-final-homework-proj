from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def list_view(request):
    '''
    view for handling of the item list
    GET - retrieve list of all items available for sale
    POST - create an item to be listed for sale
    '''

@api_view(['GET', 'POST'])
def item_detail_view(request, id):
    '''
    view for handling individual items.
    GET - retrieve detailed information on item
    POST - purchase an item
    '''
