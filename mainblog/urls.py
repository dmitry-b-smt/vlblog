from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #  path('', views.home, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('borsch_index', views.AllProducts.as_view(), name='all_products'),
    path('borsch_index/product/add', views.createProducts, name='create_product'),
    path('borsch_index/product/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('borsch_index/product/<int:pk>/update', views.UpdateProducts.as_view(), name='product_update'),
    path('borsch_index/product/<int:pk>/delete', views.DeleteProduct.as_view(), name='product_delete'),
    path('', views.AllArticles.as_view(), name = 'home'),
    path('articles/<int:pk>', views.ArticleDetail.as_view(), name = 'article_detail'),
    path('articles/add', views.createarticle, name = 'article_add'),
    path('articles/<int:pk>/update', views.UpdateArticle.as_view(), name = 'article_update'),
    path('articles/<int:pk>/delete', views.DeleteArticle.as_view(), name = 'article_delete'),
    path('user/<str:username>', views.UserAllArticles.as_view(), name = 'user_articles'),

    #ajax
    path('update_comment_status/<int:pk>/<slug:type>', views.update_comment_status, name='update_comment_status'),
]