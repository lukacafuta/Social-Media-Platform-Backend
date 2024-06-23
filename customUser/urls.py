from django.urls import path, re_path

from .views import ListCreateMeView, ListAllUserView, ListUserByIdView, ListUserByQueryView

urlpatterns = [
    # path('<str:username>/', ListCreateMeView.as_view()),  # does not work for me
    path('', ListAllUserView.as_view()),
    path('<int:user_id>/', ListUserByIdView.as_view()),
    #path('?search=<str:search_string>', ListUserByQueryView.as_view()),
    path('search=<str:search_string>', ListUserByQueryView.as_view()), # senza ? funziona
    #path('search/', ListUserByQueryView.as_view(), name="search_string"),
    #path('search/?search=<str:search_string>', ListUserByQueryView.as_view()),
]

