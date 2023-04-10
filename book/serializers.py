from rest_framework import serializers
from .models import Book


class BookSerialier(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ["id"]

    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)
        self.fields["book_id"].read_only = True

    def update(self, instance, validated_data):
        if "title" in validated_data:
            title = validated_data["title"].lower().replace(" ", "-")
            validated_data["book_id"] = f'{title}-{instance.id}'

        return super().update(instance, validated_data)


class ListBookSerializer(BookSerialier):

    class Meta:
        model = Book
        fields = '__all__'
