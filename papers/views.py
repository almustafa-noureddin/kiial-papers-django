from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .tables import PaperTable
#from .forms import SearchForm
from .models import (
	Paper,
	Researcher,
    Supervisor,
	
	)
from django.core.paginator import Paginator
from django.views import generic
from django.views.generic.edit import ModelFormMixin
from .filters import PapersFilter
from .forms import PaperModelForm, ResearcherModelForm, SupervisorModelForm, CustomUserCreationForm
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
#from guest_user.mixins import AllowGuestUserMixin
from .mixins import OrganisorAndLoginRequiredMixin
#class IndexView(generic.TemplateView):
#	template_name = "papers/index.html"
#
#	def get_context_data(self, **kwargs):
#		context = super().get_context_data(**kwargs)
#		
#		papers = Paper.objects.all()[:10]
#		researchers = Researcher.objects.all()[:10]
#		papersupervisors = PaperSupervisor.objects.all()
#		degrees = Degree.objects.all()[:10]
#		
#		context["papers"] = papers
#		context["researchers"] = researchers
#		context["papersupervisors"] = papersupervisors
#		context["degrees"] = degrees
#		return context
#

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class IndexListView(SingleTableMixin, FilterView):
    table_class = PaperTable
    model = Paper
    template_name = "papers/index.html"

    filterset_class = PapersFilter


#class IndexListView(SingleTableView):
#    model = Paper
#    table_class = PaperTable
#    template_name = 'papers/index.html'

class PaperListView(generic.ListView):
    template_name = 'papers/papers_list.html'
    context_object_name = 'papers'
    model = Paper
    paginate_by = 5
    ordering = ['title']
    
    def get_queryset(self):
        order = self.request.GET.get('orderby', 'title')
        d_or_a = self.request.GET.get('desc_or_asc', '')
        return super().get_queryset().all().order_by(f'{d_or_a}{order}')
    

    def get_context_data(self, **kwargs):
        context = super(PaperListView, self).get_context_data(**kwargs)
        context['orderby'] = self.request.GET.get('orderby', 'title')
        context['desc_or_asc'] = self.request.GET.get('desc_or_asc', '')
        return context
	
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)
    


class PaperDetailView(generic.DetailView):
    model = Paper
    template_name = "papers/paper_detail.html"
    context_object_name = 'paper'


class PaperCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "papers/create_paper.html"
    form_class = PaperModelForm

    def get_success_url(self):
        return reverse("papers:index")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "You have successfully created a paper")
        return super(PaperCreateView, self).form_valid(form)


class PaperUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    template_name = "papers/update_paper.html"
    form_class = PaperModelForm
    def get_queryset(self):
        return Paper.objects.all()

    def get_success_url(self):
        return reverse("papers:index")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully updated this paper")
        return super(PaperUpdateView, self).form_valid(form)


class PaperDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    template_name = "papers/delete_paper.html"
    context_object_name = "paper"


    def get_success_url(self):
        return reverse("papers:index")

    def get_queryset(self):
        return Paper.objects.all()




class ResearcherListView(generic.ListView):
    template_name = 'papers/researchers_list.html'
    context_object_name = 'researchers'
    model = Researcher
    paginate_by = 10
    ordering = ['first_name', 'second_name', 'third_name', 'fourth_name', 'alternative_name']
    
    def get_queryset(self):
        return super().get_queryset().all()

    def get_context_data(self, **kwargs):
        context = super(ResearcherListView, self).get_context_data(**kwargs)
        return context
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class ResearcherDetailView(generic.DetailView):
    model = Researcher
    template_name = "papers/researcher_detail.html"
    context_object_name = 'researcher'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        papers = Paper.objects.all()
        
        context["papers"] = papers
        return context


class ResearcherCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "papers/create_researcher.html"
    form_class = ResearcherModelForm

    def get_success_url(self):
        return reverse("papers:index")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "You have successfully created a researcher")
        return super(ResearcherCreateView, self).form_valid(form)


class ResearcherUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    template_name = "papers/update_researcher.html"
    form_class = ResearcherModelForm
    def get_queryset(self):
        return Researcher.objects.all()

    def get_success_url(self):
        return reverse("papers:index")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully updated this researcher")
        return super(ResearcherUpdateView, self).form_valid(form)


class ResearcherDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    template_name = "papers/delete_researcher.html"
    context_object_name = "researcher"

    def get_success_url(self):
        return reverse("papers:index")

    def get_queryset(self):
        return Researcher.objects.all()



class SupervisorListView(generic.ListView):
    template_name = 'papers/supervisors_list.html'
    context_object_name = 'supervisors'
    model = Supervisor
    paginate_by = 10
    ordering = ['first_name', 'second_name', 'third_name', 'fourth_name', 'alternative_name']
    
    def get_queryset(self):
        return super().get_queryset().all()

    def get_context_data(self, **kwargs):
        context = super(SupervisorListView, self).get_context_data(**kwargs)
        return context
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class SupervisorDetailView(generic.DetailView):
    model = Supervisor
    template_name = "papers/supervisor_detail.html"
    context_object_name = 'supervisor'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        papers = Paper.objects.all()
        
        context["papers"] = papers
        return context



class SupervisorCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "papers/create_supervisor.html"
    form_class = SupervisorModelForm

    def get_success_url(self):
        return reverse("papers:index")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "You have successfully created a supervisor")
        return super(SupervisorCreateView, self).form_valid(form)


class SupervisorUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    template_name = "papers/update_supervisor.html"
    form_class = SupervisorModelForm
    def get_queryset(self):
        return Supervisor.objects.all()

    def get_success_url(self):
        return reverse("papers:index")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully updated this Supervisor")
        return super(SupervisorUpdateView, self).form_valid(form)


class SupervisorDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    template_name = "papers/delete_supervisor.html"
    context_object_name = "supervisor"
    
    def get_success_url(self):
        return reverse("papers:index")

    def get_queryset(self):
        return Supervisor.objects.all()



#
#class PaperUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
#    template_name = "leads/lead_update.html"
#    form_class = PaperModelForm
#
#    def get_queryset(self):
#        user = self.request.user
#        # initial queryset of leads for the entire organisation
#        return Paper.objects.filter(organisation=user.userprofile)
#
#    def get_success_url(self):
#        return reverse("Papers:Papers-list")
#
#    def form_valid(self, form):
#        form.save()
#        messages.info(self.request, "You have successfully updated this lead")
#        return super(PaperUpdateView, self).form_valid(form)
#
#
#

#
#
#class LandingPageView(generic.TemplateView):
#    template_name = "index.html"
#    def get_context_data(self, **kwargs):
#		context = super().get_context_data(**kwargs)
#        papers = Paper.objects.all()
#        context["papers"] = papers
#        return context