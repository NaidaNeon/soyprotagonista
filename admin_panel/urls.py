from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='home'), #http://127.0.0.1:8000/
    path('chats/', chats, name='chats'), #http://127.0.0.1:8000/chats/
    path('statistics/', statistics, name='statistics'),  #http://127.0.0.1:8000/statistics/
    path('studies/', study, name='studies'), #http://127.0.0.1:8000/studies/
    path('sets/', sets, name='sets'), #http://127.0.0.1:8000/sets/


    # path('studies/<int:study_id>/', study), #http://127.0.0.1:8000/studies/1 (2, 3)
    # path('chat/<slug:chat_type>/', chat), #http://127.0.0.1:8000/chat/main_HR || http://127.0.0.1:8000/chat/accountant  
    # path('sets/<path:set_type>/', sets), #http://127.0.0.1:8000/sets/account || http://127.0.0.1:8000/sets/notifications
]
