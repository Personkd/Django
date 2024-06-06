from  django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from .views import ajaxtestpage


urlpatterns = [
    path('', views.HomePage.as_view(), name = 'home'),
    path('jstest/', views.JStest, name='jstest'),
    path('jstest1/', views.JStesting, name='jstest1'),
    path('ajaxtest/', ajaxtestpage.as_view(), name='ajaxtest'),
    #path ('usersreg/', views.usersreg, name ='usersreg'),
    path ('registration/', views.RegistrationPage.as_view(), name ='registration'),
    path('login/', views.logining, name='login'),
    path('logout/', views.loggingout, name='logout'),
    path('createpost/', views.createpost, name='createpost'),
    path('post/<int:pk>/',views.PostFormPage.as_view()),
    path('create_comment/<int:pk>/', views.CommentPage.as_view(),name="comment_creation"),
    #path('delete_comment/<int:pk>/', views.CommentDeletion.as_view(),name="comment_deletion"),
    path('update_post/<int:pk>/', views.UpdatePostPage.as_view(),name="post_editing"),
    path('profile/<int:pk>/', views.UpdateProfile.as_view(), name='profileView')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)