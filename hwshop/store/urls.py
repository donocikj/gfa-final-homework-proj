'''
this contains routes pertaining to items listed (or soon to be listed)
at the store.
/store/items/{id}/
/store/items/
'''
from django.urls import path
from store.views import list_view, item_detail_view

urlpatterns = [
    path('items/<int:id/', item_detail_view, name="item-detail-view"),
    path('items/', list_view, name="items_view")
]
