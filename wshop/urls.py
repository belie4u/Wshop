from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.apps import apps


urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),

    # PayPal Express integration...
    path('checkout/paypal/', include('paypal.express_checkout.urls')),
    # Dashboard views for Payflow Pro
    path('dashboard/paypal/payflow/',apps.get_app_config("payflow_dashboard").urls),
         
    # Dashboard views for Express
    path('dashboard/paypal/express/',apps.get_app_config("express_dashboard").urls),
         
    # Dashboard views for Express Checkout
    path('dashboard/paypal/express-checkout/',apps.get_app_config('express_checkout_dashboard').urls),
         


    path("", include(apps.get_app_config('oscar').urls[0])),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
