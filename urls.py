
from django.urls import path

from .views import custom_login_view , dashboard
from django.contrib.auth.views import LogoutView
from . import views
from .views import create_product, product_detail, product_list, update_product, delete_product


urlpatterns = [
    
    path('', views.home, name='home'),
    path('create_user/', views.create_user, name='create_user'),
    path('login/', custom_login_view, name='login'),
path('dashboard/', dashboard, name='dashboard'),
path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('user/create/', views.create_user, name='create_user'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/update/', views.update_user, name='update_user'),
    path('users/<int:pk>/delete/', views.delete_user, name='delete_user'),

    path('trial/create/', views.create_trial, name='create_trial'),
    path('trial/<int:pk>/', views.trial_detail, name='trial_detail'),
    path('trials/', views.trial_list, name='trial_list'),
    path('trials/<int:pk>/update/', views.update_trial, name='update_trial'),
path('trials/<int:pk>/delete/', views.delete_trial, name='delete_trial'),

    path('store-theme/create/', views.create_store_theme, name='create_store_theme'),
    path('store-theme/<int:pk>/', views.store_theme_detail, name='store_theme_detail'),
    path('store-theme/', views.store_theme_list, name='store_theme_list'),
    path('store-theme/<int:pk>/update/', views.update_store_theme, name='update_store_theme'),
path('store-theme/<int:pk>/delete/', views.delete_store_theme, name='delete_store_theme'),

    path('inventory/create/', views.create_inventory, name='create_inventory'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('inventory/', views.inventory_list, name='inventory_list'),
      path('inventory/<int:pk>/update/', views.update_inventory, name='update_inventory'),
    path('inventory/<int:pk>/delete/', views.delete_inventory, name='delete_inventory'),

    path('shipping-method/create/', views.create_shipping_method, name='create_shipping_method'),
    path('shipping-method/<int:pk>/', views.shipping_method_detail, name='shipping_method_detail'),
    path('shipping-method/', views.shipping_method_list, name='shipping_method_list'),
    path('shipping-method/<int:pk>/update/', views.update_shipping_method, name='update_shipping_method'),
    path('shipping-method/<int:pk>/delete/', views.delete_shipping_method, name='delete_shipping_method'),

    path('shipping-detail/create/', views.create_shipping_detail, name='create_shipping_detail'),
    path('shipping-detail/<int:pk>/', views.shipping_detail_detail, name='shipping_detail_detail'),
    path('shipping-detail/', views.shipping_detail_list, name='shipping_detail_list'),
    path('shipping-detail/<int:pk>/update/', views.update_shipping_detail, name='update_shipping_detail'),
    path('shipping-detail/<int:pk>/delete/', views.delete_shipping_detail, name='delete_shipping_detail'),

    path('store-analytics/create/', views.create_store_analytics, name='create_store_analytics'),
    path('store-analytics/<int:pk>/', views.store_analytics_detail, name='store_analytics_detail'),
    path('store-analytics/', views.store_analytics_list, name='store_analytics_list'),
    path('store-analytics/<int:pk>/update/', views.update_store_analytics, name='update_store_analytics'),
    path('store-analytics/<int:pk>/delete/', views.delete_store_analytics, name='delete_store_analytics'),

    path('create_plan/', views.create_plan, name='create_plan'),
    path('plan/<int:pk>/', views.plan_detail, name='plan_detail'),
    path('plans/', views.plan_list, name='plan_list'),
    path('plans/<int:pk>/update/', views.update_plan, name='update_plan'),
    path('plans/<int:pk>/delete/', views.delete_plan, name='delete_plan'),


    path('subscription/create/', views.create_subscription, name='create_subscription'),
    path('subscription/<int:pk>/', views.subscription_detail, name='subscription_detail'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('subscriptions/<int:pk>/update/', views.update_subscription, name='update_subscription'),
    path('subscriptions/<int:pk>/delete/', views.delete_subscription, name='delete_subscription'),

    path('payment/create/', views.create_payment, name='create_payment'),
    path('payment/<int:pk>/', views.payment_detail, name='payment_detail'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payment/<int:pk>/update/', views.update_payment, name='update_payment'),
    path('payment/<int:pk>/delete/', views.delete_payment, name='delete_payment'),

    path('store/create/', views.create_store, name='create_store'),
    path('store/<int:pk>/', views.store_detail, name='store_detail'),
    path('stores/', views.store_list, name='store_list'),
     path('store/<int:pk>/update/', views.update_store, name='update_store'),
    path('store/<int:pk>/delete/', views.delete_store, name='delete_store'),

    path('theme/create/', views.create_theme, name='create_theme'),
    path('theme/<int:pk>/', views.theme_detail, name='theme_detail'),
    path('themes/', views.theme_list, name='theme_list'),
    path('theme/<int:pk>/update/', views.update_theme, name='update_theme'),
    path('theme/<int:pk>/delete/', views.delete_theme, name='delete_theme'),


    path('product/create/', views.create_product, name='create_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/update/', update_product, name='update_product'),
    path('products/<int:pk>/delete/', delete_product, name='delete_product'),

    path('order/create/', views.create_order, name='create_order'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/', views.order_list, name='order_list'),
     path('order/<int:pk>/update/', views.update_order, name='update_order'),
    path('order/<int:pk>/delete/', views.delete_order, name='delete_order'),

    path('customer/create/', views.create_customer, name='create_customer'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/update/', views.update_customer, name='update_customer'),
    path('customer/<int:pk>/delete/', views.delete_customer, name='delete_customer'),

    path('email-campaign/create/', views.create_email_campaign, name='create_email_campaign'),
    path('email-campaign/<int:pk>/', views.email_campaign_detail, name='email_campaign_detail'),
    path('email_campaigns/', views.email_campaign_list, name='email_campaign_list'),
    path('email-campaign/<int:pk>/update/', views.update_email_campaign, name='update_email_campaign'),
    path('email-campaign/<int:pk>/delete/', views.delete_email_campaign, name='delete_email_campaign'),

    path('review/create/', views.create_review, name='create_review'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),
    path('reviews/', views.review_list, name='review_list'),
    path('review/<int:pk>/update/', views.update_review, name='update_review'),
    path('review/<int:pk>/delete/', views.delete_review, name='delete_review'),

    path('wishlist/create/', views.create_wishlist, name='create_wishlist'),
    path('wishlist/<int:pk>/', views.wishlist_detail, name='wishlist_detail'),
    path('wishlists/', views.wishlist_list, name='wishlist_list'),
    path('wishlist/<int:pk>/update/', views.update_wishlist, name='update_wishlist'),
    path('wishlist/<int:pk>/delete/', views.delete_wishlist, name='delete_wishlist'),

    path('promotion/create/', views.create_promotion, name='create_promotion'),
    path('promotion/<int:pk>/', views.promotion_detail, name='promotion_detail'),
    path('promotions/', views.promotion_list, name='promotion_list'),
    path('promotion/<int:pk>/update/', views.update_promotion, name='update_promotion'),
    path('promotion/<int:pk>/delete/', views.delete_promotion, name='delete_promotion'),
    

    path('gift-card/create/', views.create_gift_card, name='create_gift_card'),
    path('gift-card/<int:pk>/', views.gift_card_detail, name='gift_card_detail'),
    path('gift-card/', views.gift_card_list, name='gift_card_list'),
    path('gift-card/<int:pk>/update/', views.update_gift_card, name='update_gift_card'),
    path('gift-card/<int:pk>/delete/', views.delete_gift_card, name='delete_gift_card'),

    path('terms-agreement/create/', views.create_terms_agreement, name='create_terms_agreement'),
    path('terms-agreement/<int:pk>/', views.terms_agreement_detail, name='terms_agreement_detail'),
    path('terms-agreement/', views.terms_agreement_list, name='terms_agreement_list'),
    path('terms-agreement/<int:pk>/update/', views.update_terms_agreement, name='update_terms_agreement'),
    path('terms-agreement/<int:pk>/delete/', views.delete_terms_agreement, name='delete_terms_agreement'),

    path('refund-policy/create/', views.create_refund_policy, name='create_refund_policy'),
    path('refund-policy/<int:pk>/', views.refund_policy_detail, name='refund_policy_detail'),
    path('refund-policy/', views.refund_policy_list, name='refund_policy_list'),
    path('refund-policy/<int:pk>/update/', views.update_refund_policy, name='update_refund_policy'),
    path('refund-policy/<int:pk>/delete/', views.delete_refund_policy, name='delete_refund_policy'),
    
    path('vendor/create/', views.create_vendor, name='create_vendor'),
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('vendor/', views.vendor_list, name='vendor_list'),
    path('vendor/<int:pk>/update/', views.update_vendor, name='update_vendor'),
    path('vendor/<int:pk>/delete/', views.delete_vendor, name='delete_vendor'),

    path('notification/create/', views.create_notification, name='create_notification'),
    path('notification/<int:pk>/', views.notification_detail, name='notification_detail'),
    path('notification/', views.notification_list, name='notification_list'),
    path('notification/<int:pk>/update/', views.update_notification, name='update_notification'),
    path('notification/<int:pk>/delete/', views.delete_notification, name='delete_notification'),

    path('audit-log/create/', views.create_audit_log, name='create_audit_log'),
    path('audit-log/<int:pk>/', views.audit_log_detail, name='audit_log_detail'),
    path('audit-log/', views.audit_log_list, name='audit_log_list'),
    path('audit-log/<int:pk>/update/', views.update_audit_log, name='update_audit_log'),
    path('audit-log/<int:pk>/delete/', views.delete_audit_log, name='delete_audit_log'),

    path('feedback/create/', views.create_feedback, name='create_feedback'),
    path('feedback/<int:pk>/', views.feedback_detail, name='feedback_detail'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('feedback/<int:pk>/update/', views.update_feedback, name='update_feedback'),
    path('feedback/<int:pk>/delete/', views.delete_feedback, name='delete_feedback'),

    path('help-article/create/', views.create_help_article, name='create_help_article'),
    path('help-article/<int:pk>/', views.help_article_detail, name='help_article_detail'),
    path('help-article/', views.help_article_list, name='help_article_list'),
    path('help-article/<int:pk>/update/', views.update_help_article, name='update_help_article'),
    path('help-article/<int:pk>/delete/', views.delete_help_article, name='delete_help_article'),


    path('legal-document/create/', views.create_legal_document, name='create_legal_document'),
    path('legal-document/<int:pk>/', views.legal_document_detail, name='legal_document_detail'),
    path('legal-document/', views.legal_document_list, name='legal_document_list'),
    path('legal-document/<int:pk>/update/', views.update_legal_document, name='update_legal_document'),
    path('legal-document/<int:pk>/delete/', views.delete_legal_document, name='delete_legal_document'),


    path('tax-rule/create/', views.create_tax_rule, name='create_tax_rule'),
    path('tax-rule/<int:pk>/', views.tax_rule_detail, name='tax_rule_detail'),
    path('tax-rule/', views.tax_rule_list, name='tax_rule_list'),
    path('tax-rule/<int:pk>/update/', views.update_tax_rule, name='update_tax_rule'),
    path('tax-rule/<int:pk>/delete/', views.delete_tax_rule, name='delete_tax_rule'),


    path('tax-transaction/create/', views.create_tax_transaction, name='create_tax_transaction'),
    path('tax-transaction/<int:pk>/', views.tax_transaction_detail, name='tax_transaction_detail'),
    path('tax-transaction/', views.tax_transaction_list, name='tax_transaction_list'),
    path('tax-transaction/<int:pk>/update/', views.update_tax_transaction, name='update_tax_transaction'),
    path('tax-transaction/<int:pk>/delete/', views.delete_tax_transaction, name='delete_tax_transaction'),
]