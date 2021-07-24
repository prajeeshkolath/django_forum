from django.urls import path
from django.conf.urls import re_path
from rest_framework.routers import DefaultRouter

from . import views


# router = DefaultRouter()
# router.register(r'category', views.CategoryViewSet, basename='category')
# urlpatterns = router.urls

urlpatterns = [
    re_path(r'^$', views.ForumHomeView.as_view(), name='home-page'),
    path('thread_list/<int:topic_id>/', views.ThreadListView.as_view(), name='thread-list-view'),
    # re_path(r'^$', HomeView.as_view(), {'view_type': 'html'}, name='home-page'),
    path('contact', views.ContactFormView.as_view(), name='contact')
]
