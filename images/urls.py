from django.urls import path
# import views
from .views import HomeView,CreatePoductView, ProductDetailView,AddProductImages
    #AddPoductView, ProductDetailView, AddProductImagesView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('addproduct', CreatePoductView.as_view(), name="addproduct"),
    path('productdetail/<int:pk>/', ProductDetailView.as_view(), name="productdetail"),
    path('addimages/<int:pk>/', AddProductImages.as_view(), name="addimages"),
]