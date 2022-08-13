"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import backend_meta.views
from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view

schema_url_patterns = [
    path("version", backend_meta.views.VersionAPIView.as_view()),
    path("slots/", include("backend_slots.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "openapi",
        get_schema_view(
            title="My API",
            description="My API",
            version="1.0.0",
            patterns=schema_url_patterns,
        ),
        name="openapi-schema",
    ),
    path("api/", include(schema_url_patterns)),
]
