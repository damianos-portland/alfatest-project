import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput

from .models import *

class OrderFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date", lookup_expr='gte')
	# end_date = DateFilter(field_name="date", lookup_expr='lte')
	# note = CharFilter(field_name='note', lookup_expr='icontains')
	customer = CharFilter(field_name='customer__name', lookup_expr='icontains')
	date = DateFilter(
        widget=DateInput(
            attrs={
                'type': 'date'
            }
        )
    )



	class Meta:
		model = Application
		fields = '__all__'
		exclude = ['protocol_number','ergo','trials']



class CustomerFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date", lookup_expr='gte')
	# end_date = DateFilter(field_name="date", lookup_expr='lte')
	# note = CharFilter(field_name='note', lookup_expr='icontains')
	afm = CharFilter(field_name='afm', lookup_expr='startswith')
	name = CharFilter(field_name='name', lookup_expr='icontains')
	address = CharFilter(field_name='address', lookup_expr='icontains')



	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['phone', 'email', 'engineer']
