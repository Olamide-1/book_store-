from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.AddBookView.as_view(), name="add"),
    path("<str:id>/", views.RetrieveBookView.as_view(), name="retrieve"),
    path("manage/<str:id>/", views.EditBookDetailView.as_view(), name="manage"),
    path("mybooks/", views.FetchByBooksView.as_view(), name="my-books"),
    path("", views.ListBooksView.as_view(), name="list"),
]
