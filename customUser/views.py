from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView, \
    GenericAPIView
from rest_framework.response import Response

from .models import CustomUser

from .serializers import CustomUserSerializerPrivate, CustomUserSerializerPublic

from django.db.models import Q

# Create your views here.


# class me

#################### TODO: how to handle PATCH and get ?????
class ListCreateMeView(RetrieveUpdateAPIView):
    # define that the filter must be only the ones for the logged in user
    lookup_field = 'username'
    def get_queryset(self):
        # select the ones from CustomUsers
        # get the username
        username_here = self.kwargs['username']
        pass
        if username_here == 'me':
            return CustomUser.objects.filter(username=self.request.user)
        else:  # TODO
            return CustomUser.objects.filter(username=self.request.user)

    # define serializer for special cases
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomUserSerializerPrivate  # private info
        return CustomUserSerializerPublic  # PATCH -> only public patch according to the specifics

    # overwrite the serializers for the internal method of the CRUD operations
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



"""
# I need to retrieve only 1 instance, but I use the ListCreateAPIView bc I do not know the id in advance
# Problem: this does not have patch -> test RetrieveUpdateAPIView
class ListCreateMeView(ListCreateAPIView):

    # define that the filter must be only the ones for the logged in user
    def get_queryset(self):
        # select the ones from CustomUsers
        return CustomUser.objects.filter(username=self.request.user)

    # define serializer for special cases
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomUserSerializerPrivate  # private info
        return CustomUserSerializerPublic  # PATCH -> only public patch according to the specifics

    # overwrite the serializers for the internal method of the CRUD operations
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

"""

# .... above = me how to handle???

# .....................................
# List all users
class ListAllUserView(ListAPIView):

    pass

    # define that the filter must take all userss
    def get_queryset(self):
        # select the ones from CustomUsers
        return CustomUser.objects.all()


    # which serializer to use
    def get_serializer_class(self):
        return CustomUserSerializerPublic  # return only public info

    # # overwrite the serializers for the internal method of the CRUD operations
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# .....................................
# List user by Id
# class ListUserByIdView(RetrieveAPIView):  # I do not understand RetrieveAPIView
# -> use GenericAPIView
class ListUserByIdView(GenericAPIView):
    """
        Search the user by user_id
    """

    # which serializer to use
    serializer_class = CustomUserSerializerPublic

    # define that the filter must be only the ones for the logged in user
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        print ('user_id = ', user_id)
        # select the ones from CustomUsers
        return CustomUser.objects.filter(id=user_id)  # this was the problem

    # define explicitly in GenericAPIView
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # # overwrite the serializers for the internal method of the CRUD operations
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



# .....................................
# List user by Id
class ListUserByQueryView(ListAPIView):
    """
    Search the pattern in the queryset in username, email, first_name, last_name
    """

    ## search=<str:search_string>/

    # which serializer to use
    serializer_class = CustomUserSerializerPublic

    def get_queryset(self):  # , *args, **kwargs):
        queryset = CustomUser.objects.all()
        search = self.kwargs.get('search_string') # test
        #search = self.request.query_params.get('search_string', None)

        if search is not None:
            # like pattern with OR
            queryset = queryset.filter(
                #username=search
                Q(username__contains=search)
                | Q(email__contains=search)
                | Q(first_name__contains=search)
                | Q(last_name__contains=search)
                )
            # a single pipe is OR

        return queryset



