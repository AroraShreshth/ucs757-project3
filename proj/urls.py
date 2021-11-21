"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from .settings import website_name
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# Admin.py Stuff 
admin.site.site_header = f'{website_name} Admin'
admin.site.site_title = f'{website_name} Admin'
admin.site.index_title = f'{website_name} System Administration'
admin.autodiscover()
admin.site.enable_nav_sidebar = False


urlpatterns = [
    path('', include('users.urls')),
    path('', include('mlmod.urls')),
    path('admin/', admin.site.urls),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset',
         ),
]

if settings.DEBUG:
    import debug_toolbar
    # Django Debug Toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    # Media Data
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
