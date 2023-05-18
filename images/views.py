from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from .forms import ProductForm
from django.urls import reverse_lazy
from .models import Images, Product


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productlist'] = Product.objects.all()
        return context


# add product
class CreatePoductView(CreateView):
    template_name = "add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('home')


# product detail
class ProductDetailView(TemplateView):
    template_name = "productdetails.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productobj'] = Product.objects.get(id=self.kwargs['pk'])
        return context
#
#
# # add immages of product
class AddProductImages(TemplateView):
    template_name = "add_images.html"

    def post(self,  *args, **kwargs):
        try:
            images = self.request.FILES.getlist('images')
            product = Product.objects.get(id=self.kwargs['pk'])
            for image in images:
                product_images = Images.objects.create(
                    product=product,
                    images=image
                )
            return redirect('home')
        except Exception as e:
            print(e)