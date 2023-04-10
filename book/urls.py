from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListBooksView.as_view(), name="list"),
    path("add/", views.AddBookView.as_view(), name="add"),
    path("my-books/", views.FetchMyBooksView.as_view(), name="fetchmybooks"),
    path("manage/<str:id>/", views.EditBookDetailView.as_view(), name="manage"),
    path("<str:id>/", views.RetrieveBookView.as_view(), name="retrieve"),
]
