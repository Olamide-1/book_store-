from rest_framework import serializers
from .models import Book, PurchasedBooks


class BookSerialier(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ["book"]

    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)
        self.fields["book_id"].read_only = True

    def update(self, instance, validated_data):
        if "title" in validated_data:
            title = validated_data["title"].lower().replace(" ", "-")
            validated_data["book_id"] = f'{title}-{instance.id}'

        return super().update(instance, validated_data)


class MyBooksSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    book = serializers.StringRelatedField()

    class Meta:
        model = PurchasedBooks
        fields = "__all__"
