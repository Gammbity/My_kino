from datetime import datetime
from rest_framework import serializers
from .models import CommentModel, FilmModel, User, AktyorModel

class AddActorSerializer(serializers.Serializer):
    actor = serializers.IntegerField()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        fields = '__all__'
    
    def validate_name(sender, value):
        if value.isalpha():
            if value[0].isupper():
                return value
            e = 'Kiritilgan qiymatning birinchi harifi katta harifda bo\'lishi kerak'
            raise serializers.ValidationError({'name': e})
        e = 'Kiritilgan qiymatning birinchi belgisi harif qiymat bo\'lishi kerak'
        raise serializers.ValidationError({'name': e})
        

    def validate_created_at(sender, value):
        value_str = value.strftime('%Y-%m-%d')
        if value_str < '2024-01-01':
            return value_str
        e = f"Kinoning ishlab chiqarilgan yili 2024-01-01 dan kichik bo\'lishi kerak"
        raise serializers.ValidationError({'created_at': e})

    
        
class AktyorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AktyorModel
        fields = '__all__'

    def validate_age(sender, value):
        value_str = value.strftime('%Y-%m-%d')
        if value_str < '2000-01-01':
            return value
        e = 'Aktyorning tug\'ilgan yili 2000-01-01 dan kichik bo\'lishi kerak'
        raise serializers.ValidationError({'age': e}) 

    def validate_name(sender, value):
        if value[0].isupper:
            return value
        e = 'Kiritilgan qiymatning birinchi harifi katta harifda bo\'lishi kerak'
        raise serializers.ValidationError({'name': e})
    