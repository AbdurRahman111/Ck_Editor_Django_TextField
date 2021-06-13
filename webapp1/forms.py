from .models import Blogs
from django.forms import ModelForm


class add_blog(ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'

