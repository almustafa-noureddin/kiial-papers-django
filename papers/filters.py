from django.db.models import Q
import django_filters
from .models import Paper, Degree, Researcher,Supervisor
from django import forms
#class PapersFilter(django_filters.FilterSet):
#    q = django_filters.CharFilter(method='get',label="search")
#
#    class Meta:
#        model = Paper
#        fields =  ['q']
#
#    def get(self, queryset,name, value):
#        return queryset.filter(
#            Q(title__icontains=value) | Q(supervisor__first_name__icontains=value)
#        )
#
class PapersFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains',label='العنوان')
    researcher = django_filters.CharFilter(field_name='researcher',method='getresearcher',label='الباحث')
    supervisor = django_filters.CharFilter(field_name='supervisor',method='getsupervisor',label='المشرف')
    date_of_publishing = django_filters.NumberFilter(lookup_expr='exact',label='تاريخ النشر')
    paper_number = django_filters.NumberFilter(lookup_expr='exact',label='رقم الورقة')
    degree = django_filters.ModelMultipleChoiceFilter(queryset=Degree.objects.all(),
        widget=forms.CheckboxSelectMultiple,label='الدرجة العلمية')
    
    class Meta:
        model = Paper
        fields = ['title', 'researcher', 'supervisor','degree','date_of_publishing','paper_number' ]
    
    def getresearcher(self, queryset,name, value):
        return queryset.filter(
            Q(researcher__first_name__icontains=value) 
            | Q(researcher__second_name__icontains=value)
            | Q(researcher__third_name__icontains=value)
            | Q(researcher__fourth_name__icontains=value)
            | Q(researcher__alternative_name__icontains=value)
        )
    def getsupervisor(self, queryset,name, value):
        return queryset.filter(
            Q(supervisor__first_name__icontains=value) 
            | Q(supervisor__second_name__icontains=value)
            | Q(supervisor__third_name__icontains=value)
            | Q(supervisor__fourth_name__icontains=value)
        )