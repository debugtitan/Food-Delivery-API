from .models import DeliveryFeedback
from rest_framework.serializers import ModelSerializer,ValidationError

class DeliveryFeedbackSerializer(ModelSerializer):
    class Meta:
        model  = DeliveryFeedback
        fields = "__all__"
        
        
    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['customer'] = user
            return super().create(validated_data)
        else:
            raise ValidationError("Only authenticated users can give feedback.")