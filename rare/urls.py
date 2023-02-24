from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rareapi.views import login_user, register_user
from rest_framework import routers
from rareapi.views import CategoryView, PostView, AuthorView



router=routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, 'category' )
router.register(r'posts', PostView, 'post')
router.register(r'authors', AuthorView, 'author')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
