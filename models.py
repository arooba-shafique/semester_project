# Updated models file - testing git push

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Login / Signup
class User(AbstractUser):
 login_method = models.CharField(
 max_length=20,
 choices=[
 ('email', 'Email'),
 ('facebook', 'Facebook'),
 ('google', 'Google'),
 ('apple', 'Apple')
 ]
 )
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
# Free Trial
class Trial(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 start_date = models.DateField(auto_now_add=True)
 end_date = models.DateField()
 is_active = models.BooleanField(default=True)


# Choose a Plan
class Plan(models.Model):
 name = models.CharField(max_length=50)
 price = models.DecimalField(max_digits=8, decimal_places=2)
 features = models.TextField()
 duration_days = models.IntegerField()
def __str__(self):
        return self.name

class Subscription(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
 start_date = models.DateField(auto_now_add=True)
 is_active = models.BooleanField(default=True)

def __str__(self):
        return self.name

# Payment Gateway
class Payment(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 amount = models.DecimalField(max_digits=10, decimal_places=2)
 method = models.CharField(max_length=20)
 status = models.CharField(max_length=20)
 transaction_id = models.CharField(max_length=100)

 
# Store Setup
# Store Setup
class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    domain = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Customization
class Theme(models.Model):
 name = models.CharField(max_length=50)
 file = models.FileField(upload_to='themes/')
def __str__(self):
        return self.name

class StoreTheme(models.Model):
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
 theme = models.ForeignKey(Theme, on_delete=models.SET_NULL,
null=True)
 active = models.BooleanField(default=True)

 # Product
class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Inventory
class Inventory(models.Model):
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 stock = models.PositiveIntegerField()
 restock_date = models.DateField(null=True, blank=True)
# Orders
class Order(models.Model):
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 status = models.CharField(max_length=20)
 total = models.DecimalField(max_digits=10, decimal_places=2)
 created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
        return self.name

# Shipping
class ShippingMethod(models.Model):
 name = models.CharField(max_length=50)
 price = models.DecimalField(max_digits=6, decimal_places=2)
 estimated_days = models.IntegerField()

class ShippingDetail(models.Model):
 order = models.ForeignKey(Order, on_delete=models.CASCADE)
 method = models.ForeignKey(ShippingMethod,
on_delete=models.SET_NULL, null=True)
 tracking_number = models.CharField(max_length=100, null=True)

 def __str__(self):
        return self.name
 
# Customer Management
class Customer(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
 phone = models.CharField(max_length=15)
 address = models.TextField()
# Email Marketing
class EmailCampaign(models.Model):
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
 subject = models.CharField(max_length=100)
 content = models.TextField()
 sent_at = models.DateTimeField(null=True)
# Analytics
class StoreAnalytics(models.Model):
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
 date = models.DateField()
 total_sales = models.DecimalField(max_digits=10, decimal_places=2)
 total_visitors = models.IntegerField()
# Reviews
class Review(models.Model):
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 rating = models.IntegerField()
 comment = models.TextField()
 created_at = models.DateTimeField(auto_now_add=True)
# Wishlist
class Wishlist(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
# Promotions
class Promotion(models.Model):
 code = models.CharField(max_length=20)
 discount_percentage = models.PositiveIntegerField()
 valid_from = models.DateField()
 valid_to = models.DateField()
# Gift Cards
class GiftCard(models.Model):
 code = models.CharField(max_length=20, unique=True)
 amount = models.DecimalField(max_digits=8, decimal_places=2)
 issued_to = models.ForeignKey(User, on_delete=models.CASCADE,
null=True)
 redeemed = models.BooleanField(default=False)
 expiration_date = models.DateField()
# Security
class TermsAgreement(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 accepted_at = models.DateTimeField(auto_now_add=True)
 version = models.CharField(max_length=10)
# Vendor Management
class Vendor(models.Model):
 name = models.CharField(max_length=100)
 email = models.EmailField()
 phone = models.CharField(max_length=15)
 address = models.TextField()
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
# Refund Policy
class RefundPolicy(models.Model):
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
 policy_text = models.TextField()
 updated_at = models.DateTimeField(auto_now=True)
# Notification Center
class Notification(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 message = models.TextField()
 is_read = models.BooleanField(default=False)
 created_at = models.DateTimeField(auto_now_add=True)
# Audit Logs & Activity Tracking
class AuditLog(models.Model):
 user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
 action = models.CharField(max_length=255)
 timestamp = models.DateTimeField(auto_now_add=True)
 ip_address = models.GenericIPAddressField(null=True, blank=True)
# Feedback & Issue Reporting
class Feedback(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
 message = models.TextField()
 submitted_at = models.DateTimeField(auto_now_add=True)
# Knowledge Base & Help Center
class HelpArticle(models.Model):
 title = models.CharField(max_length=255)
 content = models.TextField()
 category = models.CharField(max_length=100)
 created_at = models.DateTimeField(auto_now_add=True)
# Legal & Compliance Center
class LegalDocument(models.Model):
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
 doc_type = models.CharField(max_length=100)
 content = models.TextField()
 version = models.CharField(max_length=10)
 effective_date = models.DateField()
 updated_at = models.DateTimeField(auto_now=True)
# Tax and Duties
class TaxRule(models.Model):
 store = models.ForeignKey(Store, on_delete=models.CASCADE)
 country = models.CharField(max_length=100)
 state = models.CharField(max_length=100, blank=True, null=True)
 tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
 is_active = models.BooleanField(default=True)
class TaxTransaction(models.Model):
 order = models.OneToOneField(Order, on_delete=models.CASCADE)
 tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
 tax_rule_applied = models.ForeignKey(TaxRule,
on_delete=models.SET_NULL, null=True)
 created_at = models.DateTimeField(auto_now_add=True)