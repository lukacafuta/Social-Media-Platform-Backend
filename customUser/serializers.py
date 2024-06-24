from rest_framework import serializers
from .models import CustomUser  # import the model here

class CustomUserSerializerPrivate(serializers.ModelSerializer):
    class Meta:
        # look at the Item model and give me all the fields
        model = CustomUser
        #fields = '__all__'
        exclude = ['password']



# for public -> exclude many info
class CustomUserSerializerPublic(serializers.ModelSerializer):

    class Meta:
        # look at the Item model and give me all the fields
        model = CustomUser
        #fields = '__all__'
        # flexible
        exclude = ['password', 'last_login', 'is_superuser',
                   'is_staff', 'is_active', 'date_joined', 'email',
                   'groups', 'user_permissions'
                   ]
