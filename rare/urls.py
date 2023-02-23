
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rareapi.views import CategoryView


router=routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category' )
from rareapi.views import register_user, login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
