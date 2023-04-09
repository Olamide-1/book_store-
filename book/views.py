from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerialier, ListBookSerializer
from .models import Book


class AddBookView(generics.CreateAPIView):

    serializer_class = BookSerialier
    permission_classes = [IsAdminUser]


class EditBookDetailView(generics.UpdateAPIView):

    serializer_class = BookSerialier
    permission_classes = [IsAdminUser]

    def get_object(self):
        try:
            id = int(self.kwargs["id"].split("-")[-1])
        except:
            raise Http404("Path Does Not Exist")

        obj = get_object_or_404(Book, id=id)
        self.check_object_permissions(request=self.request, obj=obj)

        return obj

    def delete(self):

        obj = self.get_object()
        obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class RetrieveBookView(generics.RetrieveAPIView):

    serializer_class = BookSerialier

    def get_object(self):

        id = self.kwargs["id"]
        obj = get_object_or_404(Book, book_id=id)
        self.check_object_permissions(request=self.request, obj=obj)

        return obj


class ListBooksView(generics.ListAPIView):

    serializer_class = ListBookSerializer

    def get_queryset(self):
        return Book.objects.all()
