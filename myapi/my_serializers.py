from myapp.models import Place
from rest_framework import serializers
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
    
    def validate_name(self, value):
        try:
            Place.objects.get(name=value)
            raise serializers.ValidationError(f"{value} đã tồn tại. Vui lòng chọn name khác")
        except Place.DoesNotExist: # Là `Place` không có tồn tại
            return value