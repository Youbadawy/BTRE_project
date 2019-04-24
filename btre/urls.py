from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from oscar.app import application

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    # url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),  # > Django-2.0

    # url(r'', application.urls),
    path('', application.urls),  # > Django-2.0
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This file is part of Shuup.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
# from django.conf import settings

# from django.conf.urls.static import static

# urlpatterns = [
#     url(r'^sa/', include('shuup.admin.urls', namespace="shuup_admin", app_name="shuup_admin")),
#     url(r'^api/', include('shuup.api.urls')),
#     url(r'^', include('shuup.front.urls', namespace="shuup", app_name="shuup")),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)