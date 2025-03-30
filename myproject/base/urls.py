from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete_/<int:pk>',views.delete_,name='delete_'),
    path('history',views.history,name='history'),
    path('restore/<int:pk>/',views.restore,name='restore'),
    path('del_his/<int:pk>/',views.del_his,name='delete from history'),
]