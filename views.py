from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from webapp.utils import  handle_delete_view




User = get_user_model()

from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    UserForm, TrialForm, StoreThemeForm, InventoryForm, ShippingMethodForm, ShippingDetailForm, StoreAnalyticsForm, PlanForm, SubscriptionForm, PaymentForm, StoreForm, ThemeForm,
    ProductForm, OrderForm, CustomerForm, EmailCampaignForm, ReviewForm,
    WishlistForm, PromotionForm, GiftCardForm, TermsAgreementForm, RefundPolicyForm,
    VendorForm, NotificationForm, AuditLogForm, FeedbackForm, HelpArticleForm,
    LegalDocumentForm, TaxRuleForm, TaxTransactionForm
)
from .models import (
    Trial, StoreTheme, Inventory, ShippingMethod, ShippingDetail, StoreAnalytics, Plan, Subscription, Payment, Store, Theme,
    Product, Order, Customer, EmailCampaign, Review,
    Wishlist, Promotion, GiftCard, TermsAgreement, RefundPolicy,
    Vendor, Notification, AuditLog, Feedback, HelpArticle,
    LegalDocument, TaxRule, TaxTransaction
)


def home(request):
    return render(request, 'home.html')
# views.py




def handle_form_view(request, form_class, template_name, instance=None, redirect_url_name=None, detail_redirect=None):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save()
            if detail_redirect:
                return redirect(detail_redirect, pk=obj.pk)  # only detail views get a pk
            elif redirect_url_name:
                return redirect(redirect_url_name)  # list views don't get a pk
    else:
        form = form_class(instance=instance)

    return render(request, template_name, {'form': form})










def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # redirect here!
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# UserForm (user creation/management)
def create_user(request):
    return handle_form_view(request, UserForm, 'create_user.html', redirect_url_name='user_list')



def user_detail(request, pk):
    return render(request, 'user_detail.html', {'user_obj': get_object_or_404(User, pk=pk)})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'update_user.html', {'form': form})

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'delete_user.html', {'user': user})

# TrialForm
def create_trial(request):
    return handle_form_view(request, TrialForm, 'create_trial.html', redirect_url_name='trial_list')

def trial_detail(request, pk):
    return render(request, 'trial_detail.html', {'trial': get_object_or_404(Trial, pk=pk)})

def trial_list(request):
    from .models import Trial
    trials = Trial.objects.all()
    return render(request, 'trial_list.html', {'trials': trials})

def update_trial(request, pk):
    trial = get_object_or_404(Trial, pk=pk)
    form = TrialForm(request.POST or None, instance=trial)
    if form.is_valid():
        form.save()
        return redirect('trial_list')
    return render(request, 'update_trial.html', {'form': form})

def delete_trial(request, pk):
    trial = get_object_or_404(Trial, pk=pk)
    if request.method == "POST":
        trial.delete()
        return redirect('trial_list')
    return render(request, 'delete_trial.html', {'trial': trial})


# StoreThemeForm
def create_store_theme(request):
    return handle_form_view(request, StoreThemeForm, 'create_store_theme.html', redirect_url_name='store_theme_list')


def store_theme_detail(request, pk):
    return render(request, 'store_theme_detail.html', {'store_theme': get_object_or_404(StoreTheme, pk=pk)})

def store_theme_list(request):
    themes = StoreTheme.objects.all()
    return render(request, 'store_theme_list.html', {'themes': themes})

def update_store_theme(request, pk):
    theme = get_object_or_404(StoreTheme, pk=pk)
    if request.method == 'POST':
        form = StoreThemeForm(request.POST, instance=theme)
        if form.is_valid():
            form.save()
            return redirect('store_theme_list')
    else:
        form = StoreThemeForm(instance=theme)
    return render(request, 'update_store_theme.html', {'form': form})


def delete_store_theme(request, pk):
    return handle_delete_view(
        request, 
        StoreTheme, 
        pk, 
        redirect_url_name='store_theme_list',
        template_name='delete_store_theme.html' 
    )


# InventoryForm
def create_inventory(request):
    return handle_form_view(request, InventoryForm, 'create_inventory.html', redirect_url_name='inventory_list')

def inventory_detail(request, pk):
    return render(request, 'inventory_detail.html', {'inventory': get_object_or_404(Inventory, pk=pk)})

def inventory_list(request):
    inventories = Inventory.objects.select_related('product').all()
    return render(request, 'inventory_list.html', {'inventories': inventories})

def update_inventory(request, pk):
    return handle_form_view(
        request,
        InventoryForm,
        'update_inventory.html',
        instance=Inventory.objects.get(pk=pk),
        redirect_url_name='inventory_list'
    )


def delete_inventory(request, pk):
    return handle_delete_view(request, Inventory, pk, redirect_url_name='inventory_list', template_name='delete_inventory.html')

# ShippingMethodForm
def create_shipping_method(request):
    return handle_form_view(request, ShippingMethodForm, 'create_shipping_method.html', redirect_url_name='shipping_method_list')

def shipping_method_detail(request, pk):
    return render(request, 'shipping_method_detail.html', {'shipping_method': get_object_or_404(ShippingMethod, pk=pk)})

def shipping_method_list(request):
    methods = ShippingMethod.objects.all()
    return render(request, 'shipping_method_list.html', {'methods': methods})

def update_shipping_method(request, pk):
    instance = get_object_or_404(ShippingMethod, pk=pk)
    return handle_form_view(
        request,
        ShippingMethodForm,
        'update_shipping_method.html',
        instance=instance,
        redirect_url_name='shipping_method_list'
    )
def delete_shipping_method(request, pk):
    return handle_delete_view(request, ShippingMethod, pk, redirect_url_name='shipping_method_list', template_name='delete_shipping_method.html')

# ShippingDetailForm
def create_shipping_detail(request):
    return handle_form_view(request, ShippingDetailForm, 'create_shipping_detail.html', redirect_url_name='shipping_detail_list')

def shipping_detail_detail(request, pk):
    return render(request, 'shipping_detail_detail.html', {'shipping_detail': get_object_or_404(ShippingDetail, pk=pk)})

def shipping_detail_list(request):
    details = ShippingDetail.objects.select_related('order').all()
    return render(request, 'shipping_detail_list.html', {'details': details})

# Update
def update_shipping_detail(request, pk):
    instance = get_object_or_404(ShippingDetail, pk=pk)
    return handle_form_view(
        request,
        ShippingDetailForm,
        'update_shipping_detail.html',
        instance=instance,
        redirect_url_name='shipping_detail_list'
    )

# Delete
def delete_shipping_detail(request, pk):
    return handle_delete_view(
        request,
        ShippingDetail,
        pk,
        redirect_url_name='shipping_detail_list',
        template_name='delete_shipping_detail.html'
    )

# StoreAnalyticsForm
def create_store_analytics(request):
    return handle_form_view(request, StoreAnalyticsForm, 'create_store_analytics.html', redirect_url_name='store_analytics_list')

def store_analytics_detail(request, pk):
    return render(request, 'store_analytics_detail.html', {'store_analytics': get_object_or_404(StoreAnalytics, pk=pk)})

def store_analytics_list(request):
    analytics = StoreAnalytics.objects.select_related('store').all()
    return render(request, 'store_analytics_list.html', {'analytics': analytics})


def update_store_analytics(request, pk):
    analytics = get_object_or_404(StoreAnalytics, pk=pk)
    if request.method == 'POST':
        form = StoreAnalyticsForm(request.POST, instance=analytics)
        if form.is_valid():
            form.save()
            return redirect('store_analytics_list')
    else:
        form = StoreAnalyticsForm(instance=analytics)
    return render(request, 'update_store_analytics.html', {'form': form})

def delete_store_analytics(request, pk):
    analytics = get_object_or_404(StoreAnalytics, pk=pk)
    if request.method == 'POST':
        analytics.delete()
        return redirect('store_analytics_list')
    return render(request, 'delete_store_analytics.html', {'analytics': analytics})

# Create + Detail views
def create_plan(request):
    return handle_form_view(request, PlanForm, 'create_plan.html', redirect_url_name='plan_list')

def plan_detail(request, pk):
    return render(request, 'plan_detail.html', {'plan': get_object_or_404(Plan, pk=pk)})

def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'plan_list.html', {'plans': plans})

def update_plan(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('plan_list')
    else:
        form = PlanForm(instance=plan)
    return render(request, 'update_plan.html', {'form': form})

def delete_plan(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'POST':
        plan.delete()
        return redirect('plan_list')
    return render(request, 'delete_plan.html', {'plan': plan})

def create_subscription(request):
    return handle_form_view(request, SubscriptionForm, 'create_subscription.html', redirect_url_name='subscription_list')

def subscription_detail(request, pk):
    return render(request, 'subscription_detail.html', {'subscription': get_object_or_404(Subscription, pk=pk)})

def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'subscription_list.html', {'subscriptions': subscriptions})


def update_subscription(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm(instance=subscription)
    return render(request, 'update_subscription.html', {'form': form})

def delete_subscription(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        subscription.delete()
        return redirect('subscription_list')
    return render(request, 'delete_subscription.html', {'subscription': subscription})


def create_payment(request):
    return handle_form_view(request, PaymentForm, 'create_payment.html', redirect_url_name='payment_list')

def payment_detail(request, pk):
    return render(request, 'payment_detail.html', {'payment': get_object_or_404(Payment, pk=pk)})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def update_payment(request, pk):
    instance = get_object_or_404(Payment, pk=pk)
    return handle_form_view(request, PaymentForm, 'update_payment.html', instance, 'payment_list')

def delete_payment(request, pk):
    return handle_delete_view(request, Payment, pk, 'payment_list', 'delete_payment.html')


def create_store(request):
    return handle_form_view(request, StoreForm, 'create_store.html', redirect_url_name='store_list')

def store_detail(request, pk):
    return render(request, 'store_detail.html', {'store': get_object_or_404(Store, pk=pk)})

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store_list.html', {'stores': stores})

def update_store(request, pk):
    instance = get_object_or_404(Store, pk=pk)
    return handle_form_view(request, StoreForm, 'update_store.html', instance, 'store_list')

def delete_store(request, pk):
    return handle_delete_view(request, Store, pk, 'store_list', 'delete_store.html')


def create_theme(request):
    return handle_form_view(request, ThemeForm, 'create_theme.html', redirect_url_name='theme_list')

def theme_detail(request, pk):
    return render(request, 'theme_detail.html', {'theme': get_object_or_404(Theme, pk=pk)})

def theme_list(request):
    themes = Theme.objects.all()
    return render(request, 'theme_list.html', {'themes': themes})

def update_theme(request, pk):
    instance = get_object_or_404(Theme, pk=pk)
    return handle_form_view(request, ThemeForm, 'update_theme.html', instance, 'theme_list')

def delete_theme(request, pk):
    return handle_delete_view(request, Theme, pk, 'theme_list', 'delete_theme.html')

def create_product(request):
    return handle_form_view(
        request,
        ProductForm,
        'create_product.html',
        redirect_url_name='product_list'  # ✅ list, so no pk
    )


def product_detail(request, pk):
    return render(request, 'product_detail.html', {'product': get_object_or_404(Product, pk=pk)})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
        return redirect('product_list')  # Change this if you have a different list URL
    return render(request, 'update_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})


def create_order(request):
    return handle_form_view(request, OrderForm, 'create_order.html',  redirect_url_name='order_list')

def order_detail(request, pk):
    return render(request, 'order_detail.html', {'order': get_object_or_404(Order, pk=pk)})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def update_order(request, pk):
    instance = get_object_or_404(Order, pk=pk)
    return handle_form_view(request, OrderForm, 'update_order.html', instance, 'order_list')

def delete_order(request, pk):
    return handle_delete_view(request, Order, pk, 'order_list', 'delete_order.html')


def create_customer(request):
    return handle_form_view(request, CustomerForm, 'create_customer.html',  redirect_url_name='customer_list')

def customer_detail(request, pk):
    return render(request, 'customer_detail.html', {'customer': get_object_or_404(Customer, pk=pk)})

def customer_list(request):
    customers = Customer.objects.select_related('user').all()
    return render(request, 'customer_list.html', {'customers': customers})


def update_customer(request, pk):
    instance = get_object_or_404(Customer, pk=pk)
    return handle_form_view(request, CustomerForm, 'update_customer.html', instance, 'customer_list')

def delete_customer(request, pk):
    return handle_delete_view(request, Customer, pk, 'customer_list', 'delete_customer.html')

def create_email_campaign(request):
    return handle_form_view(request, EmailCampaignForm, 'create_email_campaign.html',  redirect_url_name='email_campaign_list')

def email_campaign_detail(request, pk):
    return render(request, 'email_campaign_detail.html', {'email_campaign': get_object_or_404(EmailCampaign, pk=pk)})

def email_campaign_list(request):
    campaigns = EmailCampaign.objects.all()
    return render(request, 'email_campaign_list.html', {'campaigns': campaigns})

def update_email_campaign(request, pk):
    instance = get_object_or_404(EmailCampaign, pk=pk)
    return handle_form_view(request, EmailCampaignForm, 'update_email_campaign.html', instance, 'email_campaign_list')

def delete_email_campaign(request, pk):
    return handle_delete_view(request, EmailCampaign, pk, 'email_campaign_list', 'delete_email_campaign.html')


def create_review(request):
    return handle_form_view(request, ReviewForm, 'create_review.html',  redirect_url_name='review_list')

def review_detail(request, pk):
    return render(request, 'review_detail.html', {'review': get_object_or_404(Review, pk=pk)})

def review_list(request):
    reviews = Review.objects.select_related('product', 'user').all()
    return render(request, 'review_list.html', {'reviews': reviews})


def update_review(request, pk):
    instance = get_object_or_404(Review, pk=pk)
    return handle_form_view(request, ReviewForm, 'update_review.html', instance, 'review_list')

def delete_review(request, pk):
    return handle_delete_view(request, Review, pk, 'review_list', 'delete_review.html')


def create_wishlist(request):
    return handle_form_view(request, WishlistForm, 'create_wishlist.html',  redirect_url_name='wishlist_list')

def wishlist_detail(request, pk):
    return render(request, 'wishlist_detail.html', {'wishlist': get_object_or_404(Wishlist, pk=pk)})

def wishlist_list(request):
    wishlists = Wishlist.objects.select_related('user').all()
    return render(request, 'wishlist_list.html', {'wishlists': wishlists})

def update_wishlist(request, pk):
    instance = get_object_or_404(Wishlist, pk=pk)
    return handle_form_view(request, WishlistForm, 'update_wishlist.html', instance, 'wishlist_list')

def delete_wishlist(request, pk):
    return handle_delete_view(request, Wishlist, pk, 'wishlist_list', 'delete_wishlist.html')


def create_promotion(request):
    return handle_form_view(request, PromotionForm, 'create_promotion.html',  redirect_url_name='promotion_list')

def promotion_detail(request, pk):
    return render(request, 'promotion_detail.html', {'promotion': get_object_or_404(Promotion, pk=pk)})

def promotion_list(request):
    promotions = Promotion.objects.all()
    return render(request, 'promotion_list.html', {'promotions': promotions})

def update_promotion(request, pk):
    instance = get_object_or_404(Promotion, pk=pk)
    return handle_form_view(request, PromotionForm, 'update_promotion.html', instance, 'promotion_list')

def delete_promotion(request, pk):
    return handle_delete_view(request, Promotion, pk, 'promotion_list', 'delete_promotion.html')

def create_gift_card(request):
    return handle_form_view(request, GiftCardForm, 'create_gift_card.html',  redirect_url_name='gift_card_list')

def gift_card_detail(request, pk):
    return render(request, 'gift_card_detail.html', {'gift_card': get_object_or_404(GiftCard, pk=pk)})

def gift_card_list(request):
    gift_card = GiftCard.objects.all()
    return render(request, 'gift_card_list.html', {'gift_card': gift_card})

def update_gift_card(request, pk):
    instance = get_object_or_404(GiftCard, pk=pk)
    return handle_form_view(request, GiftCardForm, 'update_gift_card.html', instance, 'gift_card_list')

def delete_gift_card(request, pk):
    return handle_delete_view(request, GiftCard, pk, 'gift_card_list', 'delete_gift_card.html')

def create_terms_agreement(request):
    return handle_form_view(
        request,
        TermsAgreementForm,
        'create_terms_agreement.html',
        redirect_url_name='terms_agreement_list'  # ✅ This is the list view
    )

def terms_agreement_detail(request, pk):
    return render(request, 'terms_agreement_detail.html', {'terms_agreement': get_object_or_404(TermsAgreement, pk=pk)})

def terms_agreement_list(request):
    terms_agreements = TermsAgreement.objects.all()
    return render(request, 'terms_agreement_list.html', {'terms_agreements': terms_agreements})

def update_terms_agreement(request, pk):
    instance = get_object_or_404(TermsAgreement, pk=pk)
    return handle_form_view(request, TermsAgreementForm, 'update_terms_agreement.html', instance, 'terms_agreement_list')

def delete_terms_agreement(request, pk):
    return handle_delete_view(request, TermsAgreement, pk, 'terms_agreement_list', 'delete_terms_agreement.html')

def create_refund_policy(request):
    return handle_form_view(request, RefundPolicyForm, 'create_refund_policy.html',  redirect_url_name='refund_policy_list')

def refund_policy_detail(request, pk):
    return render(request, 'refund_policy_detail.html', {'refund_policy': get_object_or_404(RefundPolicy, pk=pk)})

def refund_policy_list(request):
  refund_policies = RefundPolicy.objects.all()
  return render(request, 'refund_policy_list.html', {'refund_policies': refund_policies})
 
def update_refund_policy(request, pk):
    instance = get_object_or_404(RefundPolicy, pk=pk)
    return handle_form_view(request, RefundPolicyForm, 'update_refund_policy.html', instance, 'refund_policy_list')

def delete_refund_policy(request, pk):
    return handle_delete_view(request, RefundPolicy, pk, 'refund_policy_list', 'delete_refund_policy.html')

def create_vendor(request):
    return handle_form_view(request, VendorForm, 'create_vendor.html',  redirect_url_name='vendor_detail')

def vendor_detail(request, pk):
    return render(request, 'vendor_detail.html', {'vendor': get_object_or_404(Vendor, pk=pk)})

def update_vendor(request, pk):
    instance = get_object_or_404(Vendor, pk=pk)
    return handle_form_view(request, VendorForm, 'update_vendor.html', instance, 'vendor_list')


def vendor_list(request):
    vendor = Vendor.objects.all()
    return render(request, 'vendor.html', {'vendor': vendor})

def delete_vendor(request, pk):
    return handle_delete_view(request, Vendor, pk, 'vendor_list', 'delete_vendor.html')

def create_notification(request):
    return handle_form_view(request, NotificationForm, 'create_notification.html',  redirect_url_name='notification_detail')

def notification_detail(request, pk):
    return render(request, 'notification_detail.html', {'notification': get_object_or_404(Notification, pk=pk)})


def notification_list(request):
    notification = Notification.objects.all()
    return render(request, 'notification.html', {'notification': notification})

def update_notification(request, pk):
    instance = get_object_or_404(Notification, pk=pk)
    return handle_form_view(request, NotificationForm, 'update_notification.html', instance, 'notification_list')

def delete_notification(request, pk):
    return handle_delete_view(request, Notification, pk, 'notification_list', 'delete_notification.html')


def create_audit_log(request):
    return handle_form_view(request, AuditLogForm, 'create_audit_log.html',  redirect_url_name='audit_log_detail')

def audit_log_detail(request, pk):
    return render(request, 'audit_log_detail.html', {'audit_log': get_object_or_404(AuditLog, pk=pk)})


def audit_log_list(request):
    audit_log = AuditLog.objects.all()
    return render(request, 'audit_log.html', {'audit_log': audit_log})

def update_audit_log(request, pk):
    instance = get_object_or_404(AuditLog, pk=pk)
    return handle_form_view(request, AuditLogForm, 'update_audit_log.html', instance, 'audit_log_list')

def delete_audit_log(request, pk):
    return handle_delete_view(request, AuditLog, pk, 'audit_log_list', 'delete_audit_log.html')

def create_feedback(request):
    return handle_form_view(request, FeedbackForm, 'create_feedback.html',  redirect_url_name='feedback_detail')

def feedback_detail(request, pk):
    return render(request, 'feedback_detail.html', {'feedback': get_object_or_404(Feedback, pk=pk)})


def feedback_list(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback_list.html', {'feedback': feedback})

def update_feedback(request, pk):
    instance = get_object_or_404(Feedback, pk=pk)
    return handle_form_view(request, FeedbackForm, 'update_feedback.html', instance, 'feedback_list')

def delete_feedback(request, pk):
    return handle_delete_view(request, Feedback, pk, 'feedback_list', 'delete_feedback.html')

def create_help_article(request):
    return handle_form_view(request, HelpArticleForm, 'create_help_article.html',  redirect_url_name='help_article_detail')

def help_article_detail(request, pk):
    return render(request, 'help_article_detail.html', {'help_article': get_object_or_404(HelpArticle, pk=pk)})

def help_article_list(request):
    help_article = HelpArticle.objects.all()
    return render(request, 'help_article_list.html', {'help_article': help_article})

def update_help_article(request, pk):
    instance = get_object_or_404(HelpArticle, pk=pk)
    return handle_form_view(request, HelpArticleForm, 'update_help_article.html', instance, 'help_article_list')

def delete_help_article(request, pk):
    return handle_delete_view(request, HelpArticle, pk, 'help_article_list', 'delete_help_article.html')


def create_legal_document(request):
    return handle_form_view(request, LegalDocumentForm, 'create_legal_document.html',  redirect_url_name='legal_document_detail')

def legal_document_detail(request, pk):
    return render(request, 'legal_document_detail.html', {'legal_document': get_object_or_404(LegalDocument, pk=pk)})

def legal_document(request):
    legal_document = LegalDocument.objects.all()
    return render(request, 'legal_document.html', {'legal_document': legal_document})

def legal_document_list(request):
    legal_document = LegalDocument.objects.all()
    return render(request, 'legal_document_list.html', {'legal_document': legal_document})

def update_legal_document(request, pk):
    instance = get_object_or_404(LegalDocument, pk=pk)
    return handle_form_view(request, LegalDocumentForm, 'update_legal_document.html', instance, 'legal_document_list')

def delete_legal_document(request, pk):
    return handle_delete_view(request, LegalDocument, pk, 'legal_document_list', 'delete_legal_document.html')

def create_tax_rule(request):
    return handle_form_view(request, TaxRuleForm, 'create_tax_rule.html',  redirect_url_name='tax_rule_detail')

def tax_rule_detail(request, pk):
    return render(request, 'tax_rule_detail.html', {'tax_rule': get_object_or_404(TaxRule, pk=pk)})

def tax_rule_list(request):
    tax_rule = TaxRule.objects.all()
    return render(request, 'tax_rule_list.html', {'tax_rule': tax_rule})

def update_tax_rule(request, pk):
    instance = get_object_or_404(TaxRule, pk=pk)
    return handle_form_view(request, TaxRuleForm, 'update_tax_rule.html', instance, 'tax_rule_list')

def delete_tax_rule(request, pk):
    return handle_delete_view(request, TaxRule, pk, 'tax_rule_list', 'delete_tax_rule.html')

def create_tax_transaction(request):
    return handle_form_view(request, TaxTransactionForm, 'create_tax_transaction.html',  redirect_url_name='tax_transaction_detail')

def tax_transaction_detail(request, pk):
    return render(request, 'tax_transaction_detail.html', {'tax_transaction': get_object_or_404(TaxTransaction, pk=pk)})

def tax_transaction_list(request):
    tax_transaction = TaxTransaction.objects.all()
    return render(request, 'tax_transaction_list.html', {'tax_transaction': tax_transaction})

def update_tax_transaction(request, pk):
    instance = get_object_or_404(TaxTransaction, pk=pk)
    return handle_form_view(request, TaxTransactionForm, 'update_tax_transaction.html', instance, 'tax_transaction_list')

def delete_tax_transaction(request, pk):
    return handle_delete_view(request, TaxTransaction, pk, 'tax_transaction_list', 'delete_tax_transaction.html')