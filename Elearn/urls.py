"""Elearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from accounts import views as account_views
from django.contrib.auth import views as auth_views
from Courses import views as course_views
from Books import views as book_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',account_views.home,name='home'),
    path('courses/recommend/',course_views.recommend,name='recommend'),
    path('courses/external/<clubname>',course_views.external,name='external'),
    path('books/',book_views.books,name='books'),
    path('books/upload/',book_views.bookupload,name='bookupload'),
    path('books/verification/',book_views.verifyourself,name='verifyourself'),
    path('books/verification/otp/',book_views.otp,name='otp'),
    path('<clubname>/courses/<int:pk>/<videoname>/',course_views.playcourse,name='playcourse'),
    path('select/',account_views.select,name='select'),
    path('<clubname>/courses/',course_views.courses,name='courses'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)