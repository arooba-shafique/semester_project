from django import forms
from .models import *
from .models import Store, Product, Theme, Order, ShippingMethod, Plan

class SomeForm(forms.Form):
    store = forms.ModelChoiceField(queryset=Store.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    theme = forms.ModelChoiceField(queryset=Theme.objects.all())
    order = forms.ModelChoiceField(queryset=Order.objects.all())
    shipping_detail = forms.ModelChoiceField(queryset=ShippingDetail.objects.all())
    plan = forms.ModelChoiceField(queryset=Plan.objects.all())


# User Management Forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'login_method', 'passkey_enabled']

class TrialForm(forms.ModelForm):
    class Meta:
        model = Trial
        fields = ['user' , 'end_date', 'is_active']

# Subscription Forms
class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'price', 'features', 'duration_days']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['user', 'plan', 'is_active']

# Payment Forms
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'amount', 'method', 'status', 'transaction_id']

# Store Forms
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['owner', 'name', 'logo', 'domain']

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'file']

class StoreThemeForm(forms.ModelForm):
    class Meta:
        model = StoreTheme
        fields = ['store', 'theme', 'active']

# Product Forms
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['store', 'name', 'description', 'price', 'image', 'is_published']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'stock', 'restock_date']

# Order Forms
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['store', 'user', 'status', 'total']

class ShippingMethodForm(forms.ModelForm):
    class Meta:
        model = ShippingMethod
        fields = ['name', 'price', 'estimated_days']

class ShippingDetailForm(forms.ModelForm):
    class Meta:
        model = ShippingDetail
        fields = ['order', 'method', 'tracking_number']

# Customer Forms
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'store', 'phone', 'address']

# Marketing Forms
class EmailCampaignForm(forms.ModelForm):
    class Meta:
        model = EmailCampaign
        fields = ['store', 'subject', 'content']

# Analytics Forms
class StoreAnalyticsForm(forms.ModelForm):
    class Meta:
        model = StoreAnalytics
        fields = ['store', 'date', 'total_sales', 'total_visitors']

# Review Forms
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'user', 'rating', 'comment']

# Wishlist Forms
class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['user', 'product']

# Promotion Forms
class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['code', 'discount_percentage', 'valid_from', 'valid_to']

# Gift Card Forms
class GiftCardForm(forms.ModelForm):
    class Meta:
        model = GiftCard
        fields = ['code', 'amount', 'issued_to', 'expiration_date']

# Legal Forms
class TermsAgreementForm(forms.ModelForm):
    class Meta:
        model = TermsAgreement
        fields = ['user', 'version']

class RefundPolicyForm(forms.ModelForm):
    class Meta:
        model = RefundPolicy
        fields = ['store', 'policy_text']

# Vendor Forms
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'email', 'phone', 'address', 'store']

# Notification Forms
class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['user', 'message', 'is_read']

# Audit Forms
class AuditLogForm(forms.ModelForm):
    class Meta:
        model = AuditLog
        fields = ['user', 'action', 'ip_address']

# Feedback Forms
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user', 'store', 'message']

# Help Center Forms
class HelpArticleForm(forms.ModelForm):
    class Meta:
        model = HelpArticle
        fields = ['title', 'content', 'category']

# Legal Forms
class LegalDocumentForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['store', 'doc_type', 'content', 'version', 'effective_date']

# Tax Forms
class TaxRuleForm(forms.ModelForm):
    class Meta:
        model = TaxRule
        fields = ['store', 'country', 'state', 'tax_rate', 'is_active']

class TaxTransactionForm(forms.ModelForm):
    class Meta:
        model = TaxTransaction
        fields = ['order', 'tax_amount', 'tax_rule_applied']