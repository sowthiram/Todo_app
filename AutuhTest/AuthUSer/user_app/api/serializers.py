from rest_framework import serializers
from user_app.models import MyUser
from bson import ObjectId

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()  # Define SerializerMethodField for id
    password = serializers.CharField(write_only=True)
    
    def get_id(self, obj):
        # Check if the id field is an ObjectId, then convert it to a string
        if hasattr(obj, 'id') and isinstance(obj.id, ObjectId):
            return str(obj.id)
        return obj.id  # Return the id as it is if it's not an ObjectId
    
    def save(self, validated_data):
        # Override create method to handle user creation with hashed password
        user = MyUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'password') 