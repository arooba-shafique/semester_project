from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, Trial, Plan, Subscription, Payment, Store,
    Theme, StoreTheme, Product, Inventory, Order,
    ShippingMethod, ShippingDetail, Customer, EmailCampaign,
    StoreAnalytics, Review, Wishlist, Promotion, GiftCard,
    TermsAgreement, Vendor, RefundPolicy, Notification,
    AuditLog, Feedback, HelpArticle, LegalDocument,
    TaxRule, TaxTransaction
)

admin.site.register(User, UserAdmin)
admin.site.register(Trial)
admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Payment)
admin.site.register(Store)
admin.site.register(Theme)
admin.site.register(StoreTheme)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(ShippingMethod)
admin.site.register(ShippingDetail)
admin.site.register(Customer)
admin.site.register(EmailCampaign)
admin.site.register(StoreAnalytics)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Promotion)
admin.site.register(GiftCard)
admin.site.register(TermsAgreement)
admin.site.register(Vendor)
admin.site.register(RefundPolicy)
admin.site.register(Notification)
admin.site.register(AuditLog)
admin.site.register(Feedback)
admin.site.register(HelpArticle)
admin.site.register(LegalDocument)
admin.site.register(TaxRule)
admin.site.register(TaxTransaction)
