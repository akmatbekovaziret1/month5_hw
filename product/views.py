from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .serializers import *
from .models import Category, Product, Review
from django.db.models import Avg

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView



class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'

# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail_update_api_view(request, id):
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response(
#             data = {'error': 'category not found!'},
#             status = status.HTTP_404_NOT_FOUND
#         )
#     if request.method == "GET":
#         data = CategoryDetailSerializer(category, many=False).data
#         return Response(data = data)
#     elif request.method == "DELETE":
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "PUT":
#         serializer = CategoryValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        
#         category.name = request.data.get('name')
#         category.save()
#         return Response(
#             status=status.HTTP_201_CREATED,
#             data = CategoryDetailSerializer(category).data
#         )

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    
    

# @api_view(['GET','POST'])
# def category_list_create_api_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         list_ = CategoryListSerializer(categories, many = True).data
        
#         return Response(
#             data = list_,
#             status = status.HTTP_200_OK
#         )
        
#     elif request.method == 'POST':
#         serializer = CategoryValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        
#         name = request.data.get('name')
#         category = Category.objects.create(
#             name = name
#         )
        
#         return Response(
#             status = status.HTTP_201_CREATED,
#             data = CategoryDetailSerializer(category).data
#         )

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'


# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail_update_api_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(
#             data = {'error': 'product not found!'},
#             status = status.HTTP_404_NOT_FOUND
#         )     
#     if request.method == 'GET':
#         data = ProductDetailSerializer(product, many=False).data
#         return Response(data = data)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = ProductValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
#         product.title = request.data.get("title")
#         product.description = request.data.get('description')
#         product.price = request.data.get('price')
#         product.category_id = request.data.get('category_id')
#         product.save()
#         return Response(
#             status=status.HTTP_201_CREATED,
#             data = ProductDetailSerializer(product).data
#         )

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

# @api_view(['GET', "POST"])
# def product_list_create_api_view(request):
    
#     products = Product.objects.all()
    
#     # list_ = ProductListSerializer(products, many = True).data
    
#     # return Response(
#     #     data = list_,
#     #     status = status.HTTP_200_OK
#     # )
    
#     #HW2
#     if request.method == "GET":
#         serializer = ProductListSerializer(products, many = True)
        
#         return Response({
#             'products_count': products.count(),
#             'products': serializer.data
#         })
#     elif request.method == 'POST':
#         # title = models.CharField(max_length=250)
#         # description = models.TextField(null=True, blank=True)
#         # price = models.FloatField()
#         # category = models.ForeignKey(Category, on_delete=models.CASCADE)
        
#         serializer = ProductValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        
#         title = request.data.get('title')
#         description = request.data.get('description')
#         price = request.data.get('price')
#         category_id = request.data.get('category_id')
        
#         product = Product.objects.create(
#             title = title,
#             description = description,
#             price = price,
#             category_id = category_id
#         )
        
#         return Response(
#             status=status.HTTP_201_CREATED,
#             data = ProductDetailSerializer(product).data
#         )

class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    lookup_field = 'id'
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_update_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(
#             data = {'error': 'product not found!'},
#             status = status.HTTP_404_NOT_FOUND
#         )     
#     if request.method == "GET":
#         data = ReviewDetailSerializer(review, many=False).data
#         return Response(data = data)
#     elif request.method == "DELETE":
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "PUT":
#         serializer = ReviewValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        
#         review.text = request.data.get('text')
#         review.product_id = request.data.get('product_id')
#         review.stars = request.data.get('stars')
#         review.save()
#         return Response(
#             status = status.HTTP_201_CREATED,
#             data = ReviewDetailSerializer(review).data
#         )

class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    

# @api_view(['GET', 'POST'])
# def review_list_create_api_view(request):
    
#     reviews = Review.objects.all()
#     list_ = ReviewListSerializer(reviews, many = True).data
#     if request.method == 'GET':
#         return Response(
#             data = list_,
#             status = status.HTTP_200_OK
#         )
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
#         text = request.data.get('text')
#         product_id = request.data.get('product_id')
#         stars = request.data.get('stars')
        
#         reviews = Review.objects.create(
#             text = text,
#             product_id = product_id,
#             stars = stars 
#         )
#         return Response(
#             status = status.HTTP_201_CREATED,
#             data = ReviewDetailSerializer(reviews).data
#         )

class ProductReviewListAPIView(ListAPIView):
    serializer_class = ProductReviewListSerializer
    
    def get_queryset(self):
        return Product.objects.annotate(
            average_rating = Avg('review__stars')
        ).prefetch_related('review_set')
    
# @api_view(['GET'])
# def product_review_list_api_view(request):
#     products = Product.objects.annotate(
#         average_rating = Avg('review__stars')
#     ).prefetch_related('review_set')
    
#     serializer = ProductReviewListSerializer(products, many = True)
    
#     return Response(serializer.data)
    