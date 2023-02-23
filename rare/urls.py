
from django.contrib import admin
from django.urls import path
from rareapi.views import register_user, login_user
from rest_framework import routers
from rareapi.views import PostView
from django.conf.urls import include
from rareapi.views import CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, 'post')
router.register(r'categories', CategoryView, 'category' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
