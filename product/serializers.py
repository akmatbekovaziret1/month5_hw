from rest_framework import serializers
from .models import Category, Product, Review

# Category
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Product
class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only = True)
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'category']

class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer(read_only = True)
    
    class Meta:
        model = Product
        fields = '__all__'

# Review
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars']
        
class ReviewDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only = True)
    
    class Meta:
        model = Review
        fields = '__all__'
    
#hw2        
class ProductReviewListSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(
        source = 'review_set',
        many = True,
        read_only = True
    )
    
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'reviews',
            'average_rating'
        ]
    
    def get_average_rating(self, product):
        reviews = product.review_set.all()
        
        if reviews:
            total = sum(review.stars for review in reviews)
            return total/ len(reviews)

        return 0