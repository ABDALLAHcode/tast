from django import forms 
from .models import ProductReview , Product , Brand 
from django.core.exceptions import ValidationError


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['user','product','rate','review','date']

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        if rate > 5:
            raise ValidationError("⚠️ لا يمكن أن يكون التقييم أكثر من 5.")
        if rate <= 0:
            raise ValidationError("⚠️ لا يمكن أن يكون التقييم 0 او اقل ")
        return rate   
    
    

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name','image','slug']

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if Brand.objects.filter(name=name).exists():
            raise ValidationError("⚠️ هذا الاسم موجود بالفعل. يرجى اختيار اسم آخر.")

        return name



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product     
        fields = ['name','image','price','sku','subtitle','description','flag','brand','tags','slug',]
        
    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price <= 0:
            raise ValidationError("⚠️ لا يمكن ان يكون السعر  0 او اقل")
        return price   