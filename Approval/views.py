# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView
# from rest_framework.pagination import PageNumberPagination
# from rest_framework import generics, status, filters

# from . import models as approval_models
# from . import serializers as approval_serializer
# from Shop import models as shop_models


# class AcceptRejectGroceryApproval(generics.DestroyAPIView):
#     renderer_classes = [JSONRenderer]

#     def get_queryset(self):
#         approval = approval_models.GroceryApproval.objects.filter(pk=self.kwargs['pk']).first()
#         grocery = shop_models.Grocery.objects.filter(pk=approval.grocery.pk).first()
#         if self.kwargs['action'] == 'Accept':
#             grocery.is_approved = True
#             grocery.save()
#         else:
#             grocery.is_approved = False
#             grocery.delete()
#         return approval_models.GroceryApproval.objects.all()


# class AcceptRejectFruitApproval(generics.DestroyAPIView):
#     renderer_classes = [JSONRenderer]

#     def get_queryset(self):
#         approval = approval_models.FruitApproval.objects.filter(pk=self.kwargs['pk']).first()
#         fruit = shop_models.Fruit.objects.filter(pk=approval.fruit.pk).first()
#         if self.kwargs['action'] == 'Accept':
#             fruit.is_approved = True
#             fruit.save()
#         else:
#             fruit.is_approved = False
#             fruit.delete()
#         return approval_models.FruitApproval.objects.all()


# class AcceptRejectVegetableApproval(generics.DestroyAPIView):
#     renderer_classes = [JSONRenderer]

#     def get_queryset(self):
#         import pdb;pdb.set_trace()
#         approval = approval_models.VegetableApproval.objects.filter(pk=self.kwargs['pk']).first()
#         vegetable = shop_models.Vegetable.objects.filter(pk=approval.vegetable.pk).first()
#         if self.kwargs['action'] == 'Accept':
#             vegetable.is_approved = True
#             vegetable.save()
#         else:
#             vegetable.is_approved = False
#             vegetable.delete()
#         return approval_models.VegetableApproval.objects.all()


# class LisApprovals(APIView):
#     renderer_classes = [JSONRenderer]
#     def get(self, request):
#         data = {
#             'grocery': [],
#             'fruit': [],
#             'vegetable': []
#         }
#         groceries = approval_models.GroceryApproval.objects.all()
#         fruites = approval_models.FruitApproval.objects.all()
#         vegetables = approval_models.VegetableApproval.objects.all()
#         for grocery in groceries:
#             data['grocery'].append(approval_serializer.GetGroceryApprovalSerializer(grocery).data)
#         for fruit in fruites:
#             data['fruit'].append(approval_serializer.GetFruitApprovalSerializer(fruit).data)
#         for vegetable in vegetables:
#             data['vegetable'].append(approval_serializer.GetGVegetableApprovalSerializer(vegetable).data)
#         return Response(data, status=status.HTTP_200_OK)