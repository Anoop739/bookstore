from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from api.serializers import BookSerializer,UserSerializer
from api.models import Books
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import  Response
from rest_framework.decorators import  action
from rest_framework import  authentication,permissions

class BooksView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=BookSerializer
    model=Books
    queryset=Books.objects.all()
    


   # localhost:8000/api/v1/books/gerne/
    @action(methods=["GET"],detail=False)
    def gerne(self,request,*args,**kwargs):
        qs=Books.objects.all().values_list("gerne", flat=True).distinct()

        return Response(data=qs)

#localhost:8000/api/v1/books?gerne=comedy/
#localhost:8000/api/v1/books?price_gt=400

    def list(self,request,*args,**kwargs):
        qs=Books.objects.all()
    
        if "gerne" in self.request.query_params:
            cat=self.request.query_params.get("gerne")

            qs=qs.filter(gerne=cat)

        if "price_gt" in self.request.query_params:
            pri=self.request.query_params.get("price_gt")
            qs=qs.filter(price__gt=pri)

        Serializer=BookSerializer(qs,many=True)
        return Response(data=Serializer.data)


# def get_queryset(self):
#         qs=Books.objects.all()
    
#         if "gerne" in self.request.query_params:
#             cat=self.request.query_params.get("gerne")
#             qs=qs.filter(gerne=cat)

#         if "price_gt" in self.request.query_params:
#             pri=self.request.query_params.get("price_gt")
#             print(pri)
#             qs=qs.filter(price_gt=pri)
            
#         return qs

# #localhost:8000/api/v1/books?price_gt=400


class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

    # def create(self, request, *args, **kwargs):
    #     Serializer=UserSerializer(data=request.data)
    #     if Serializer.is_valid():
    #         usr=User.objects.create_user(**Serializer.validated_data)
    #         Serializer=UserSerializer(usr,many=False)
    #         return Response(data=Serializer.data)
    #     else:
    #         return Response(data=Serializer.errors)