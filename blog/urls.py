from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from . import views
from .views import HomeView,ArticleDetailView,CreatBlogView,UpdateBlogView,DeleteBlogView

urlpatterns = [
    #path('',views.home,name='home'),    
    # path('resume/',views.resume,name='resume'),
    path('',HomeView.as_view(),name='home'),
    path('details/<int:pk>',ArticleDetailView.as_view(),name='details'),
    path('addpost/',CreatBlogView.as_view(),name='addPost'),
    path('details/edit/<int:pk>',UpdateBlogView.as_view(),name='editpost'),
    path('details/<int:pk>/delete',DeleteBlogView.as_view(),name='deletepost'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)