from django.shortcuts import render


# Create your views here.

# class CreateShopPromocode(generics.CreateAPIView):
#     renderer_classes = [JSONRenderer]
#     serializer_class = shop_serializer.CreateShopPromocodeSerializer


# class ListShopPromocode(generics.ListAPIView):
#     renderer_classes = [JSONRenderer]
#     serializer_class = shop_serializer.ListShopPromocodeSerializer

#     def get_queryset(self):
#         shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
#         return shop_models.ShopPromocode.objects.filter(shop=shop)


# class UpdateDeleteShopPromocode(generics.RetrieveUpdateDestroyAPIView):
#     renderer_classes = [JSONRenderer]
#     serializer_class = shop_serializer.ListShopPromocodeSerializer
#     queryset = shop_models.ShopPromocode.objects.all()