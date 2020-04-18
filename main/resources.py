from import_export import resources
from .models import *

class CustomEntryResource(resources.ModelResource):
    class Meta:
        model = CustomEntry