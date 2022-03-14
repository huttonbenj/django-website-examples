from django.db import models
from django.core import validators

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=70,
        verbose_name='Reservation Type',
        null=True,
        blank=False
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=[
            validators.MinValueValidator(25),
            validators.MaxValueValidator(100000)
        ],
        null=True,
        blank=False
    )

    # You can change as a Foreign Key to the user model
    customer_email = models.EmailField(
        verbose_name='Customer Email',
        null=True,
        blank=False
    )

    customer_name = models.CharField(
        verbose_name='Customer Name',
        max_length=255,
        null=True,
        blank=False
    )

    amount = models.IntegerField(
        verbose_name='Number of Days',
        null=True,
        blank=False
    )

    stripe_payment_intent = models.CharField(
        max_length=200,
        null=True,
        blank=False
    )

    total_cost = models.IntegerField(
        null=True,
        blank=False
    )

    amount_paid = models.IntegerField(
        null=True,
        blank=False
    )

    amount_owed = models.IntegerField(
        null=True,
        blank=False
    )

    # This field can be changed as status
    has_paid = models.BooleanField(
        default=False,
        verbose_name='Payment Status',
    )

    paid_in_full = models.BooleanField(
        default=False, verbose_name='Has Paid In Full'
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=False
    )

    updated_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=False
    )

    session_key = models.CharField(
        max_length=255,
        null=True,
        blank=False
    )
    # def __str__(self):
    #     return self.customer_email
        
    class Meta:
        verbose_name='Payment History'
        verbose_name_plural='Payment History'