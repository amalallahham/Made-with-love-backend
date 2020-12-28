from django.urls import path
from django.urls import include, re_path
from .views import getCategoryStore
from .views import addItem
from .views import SnippetDetailSeller
from .views import getItems
from .views import getItemsVisit
from .views import sellerVisit
from .views import getListOrder
from .views import editItem

urlpatterns = [
 path('<slug:cat>', getCategoryStore.as_view(), ),  
 path('addItem', addItem.as_view(),),
 path('delete/<int:pk>/', SnippetDetailSeller.as_view()),
 path('editProfile', SnippetDetailSeller.as_view()),
 path('profile/<int:pk>', SnippetDetailSeller.as_view()),
 path('profile/items/<int:pk>', getItems.as_view()),
 path('visit/items/<int:pk>', getItemsVisit.as_view()),
 path('visit/<int:pk>', sellerVisit.as_view()),
 path('addItem', addItem .as_view(), ),
 path('editProfile/<int:pk>', editItem.as_view(), ),

 path('order/list/<int:pk>', getListOrder.as_view(), )

 ]
