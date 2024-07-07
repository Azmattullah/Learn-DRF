from rest_framework import serializers
from ..models import Carlist, Showroomlist



class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroomlist
        fields = "__all__"


def alphanumberic(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("only alphanumeric character are allowed")

class CarSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Carlist
        # fields = ['id', 'name', 'description'] #for Sepecific fields
        fields = '__all__' #For all field
        # exclude = ['price'] # Exclude fields

    def get_discounted_price(self,object):
        if object.price is None:
            return None
        discountprice = object.price - 5000
        return discountprice
    
    
        
    def validate_price(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.00")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description must be different")
        return data
    
    