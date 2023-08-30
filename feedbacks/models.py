from django.db import models
from users.models import User

class DeliveryFeedback(models.Model):
    SATISFACTION_CHOICES = [
        (1, 'Not Satisfied'),
        (2, 'Somewhat Satisfied'),
        (3, 'Neutral'),
        (4, 'Satisfied'),
        (5, 'Very Satisfied')
    ]

    RECOMMEND_CHOICES = [
        (1, 'Not Likely'),
        (2, 'Somewhat Likely'),
        (3, 'Neutral'),
        (4, 'Likely'),
        (5, 'Very Likely')
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    satisfaction_rating = models.PositiveIntegerField(choices=SATISFACTION_CHOICES)
    product_quality_comment = models.TextField(blank=True)
    delivery_experience_comment = models.TextField(blank=True)
    customer_service_comment = models.TextField(blank=True)
    ease_of_ordering_comment = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)
    recommend_rating = models.PositiveIntegerField(choices=RECOMMEND_CHOICES)
    additional_comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.customer.username}"
