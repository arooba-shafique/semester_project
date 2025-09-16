from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import date
import datetime

class User(AbstractUser):
    
    passkey_enabled = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='shopify_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='shopify_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Trial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"Trial for {self.user}"

    def save(self, *args, **kwargs):
        # Set status based on 'is_active'
        self.status = 'Active' if self.is_active else 'Expired'
        super().save(*args, **kwargs)

class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    features = models.TextField()
    duration_days = models.IntegerField()
    def __str__(self):
        return f"{self.name} - ${self.price} - {self.duration_days} days"



class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(default=datetime.date.today)

    is_active = models.BooleanField(default=True)

    def check_active(self):
        today = date.today()
        active = today <= self.end_date
        if self.is_active != active:
            self.is_active = active
            self.save(update_fields=['is_active'])
        return active

    def save(self, *args, **kwargs):
        self.is_active = date.today() <= self.end_date
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Subscription: {self.user} to {self.plan.name} ({self.start_date} - {self.end_date})"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100)


class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    domain = models.CharField(max_length=100)

    def __str__(self):
        return self.name


from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=50)
    file = models.ImageField(upload_to='themes/')  # Use this for the image of the theme

    def __str__(self):
        return self.name


class StoreTheme(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    is_published = models.BooleanField(default=True)

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    restock_date = models.DateField(null=True, blank=True)


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(null=True, blank=True)

class ShippingMethod(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    estimated_days = models.IntegerField()

class ShippingDetail(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    method = models.ForeignKey(ShippingMethod, on_delete=models.SET_NULL, null=True)
    tracking_number = models.CharField(max_length=100, null=True)

class Customer(models.Model):
    customer_name= models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

class EmailCampaign(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    sent_at = models.DateTimeField(null=True)


class StoreAnalytics(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_visitors = models.IntegerField()


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Promotion(models.Model):
    code = models.CharField(max_length=20)
    discount_percentage = models.PositiveIntegerField()
    valid_from = models.DateField()
    valid_to = models.DateField()

class GiftCard(models.Model):
    code = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    issued_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    redeemed = models.BooleanField(default=False)
    expiration_date = models.DateField()


class TermsAgreement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted_at = models.DateTimeField(auto_now_add=True)
    version = models.CharField(max_length=10)

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class RefundPolicy(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    policy_text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

class HelpArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=100)

class LegalDocument(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=100)
    content = models.TextField()
    version = models.CharField(max_length=10)
    file = models.FileField(upload_to='legal_docs/', null=True, blank=True)
    effective_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

class TaxRule(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)

    
class TaxTransaction(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rule_applied = models.ForeignKey(TaxRule, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

