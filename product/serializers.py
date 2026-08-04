from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError
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
    
    average_rating = serializers.FloatField(read_only = True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'reviews',
            'average_rating'
        ]


#hw4

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 250)
    
class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 250)
    description = serializers.CharField(required=False)
    price = serializers.FloatField()
    category_id = serializers.IntegerField()
    
    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id = category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')
        return category_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required = False)
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField(min_value = 1, max_value = 5)
    
    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exist')
        return product_id