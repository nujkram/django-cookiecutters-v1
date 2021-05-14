"""
{{ cookiecutter.project_name }}
{{ cookiecutter.description }}

Author: {{ cookiecutter.author_name }} ({{ cookiecutter.email }})
Version: {{ cookiecutter.version }}
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import Is{{cookiecutter.user_type_verbose}}ViewMixin

from {{cookiecutter.module}}.models.{{cookiecutter.master_module}}.models import {{cookiecutter.model}} as Master
from {{cookiecutter.user}}_dashboard.controllers.views.{{cookiecutter.module}}.{{ cookiecutter.module }}.forms import {{cookiecutter.model}}Form as MasterForm

"""
URLS
# {{ cookiecutter.model_verbose }}

from {{ cookiecutter.user }}_dashboard.controllers.views.{{ cookiecutter.app}}.{{ cookiecutter.module }} import main as {{ cookiecutter.module }}_views

urlpatterns += [
    path(
        '{{cookiecutter.master_module}}/list',
        {{ cookiecutter.module }}_views.{{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}ListView.as_view(),
        name='{{cookiecutter.user}}_dashboard_{{cookiecutter.module}}_list'
    ),
    path(
        '{{cookiecutter.master_module}}/<{{cookiecutter.master_reference}}>/detail',
        {{ cookiecutter.module }}_views.{{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}DetailView.as_view(),
        name='{{cookiecutter.user}}_dashboard_{{cookiecutter.module}}_detail'
    ),
    path(
        '{{cookiecutter.master_module}}/create',
        {{ cookiecutter.module }}_views.{{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}CreateView.as_view(),
        name='{{cookiecutter.user}}_dashboard_{{cookiecutter.module}}_create'
    ),
    path(
        '{{cookiecutter.master_module}}/<{{cookiecutter.master_reference}}>/update',
        {{ cookiecutter.module }}_views.{{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}UpdateView.as_view(),
        name='{{cookiecutter.user}}_dashboard_{{cookiecutter.module}}_update'
    ),
    path(
        '{{cookiecutter.master_module}}/<{{cookiecutter.master_reference}}>/delete',
        {{ cookiecutter.module }}_views.{{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}DeleteView.as_view(),
        name='{{cookiecutter.user}}_dashboard_{{cookiecutter.module}}_delete'
    )
]
"""


class {{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}ListView(LoginRequiredMixin, Is{{cookiecutter.user_type_verbose}}ViewMixin, View):
    """ 
    List view for {{ cookiecutter.model_verbose_plural }}. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - {{ cookiecutter.user_type_verbose }} user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        obj_list = Master.objects.actives()
        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"{{ cookiecutter.model_verbose_plural }}",
            "menu_section": "{{ cookiecutter.menu_section}}",
            "menu_subsection": "{{ cookiecutter.menu_subsection }}",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "{{cookiecutter.module}}/list.html", context)


class {{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}CreateView(LoginRequiredMixin, Is{{cookiecutter.user_type_verbose}}ViewMixin, View):
    """ 
    Create view for {{ cookiecutter.model_verbose_plural }}. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - {{ cookiecutter.user_type_verbose }} user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        form = MasterForm
        context = {
            "page_title": "Create new {{ cookiecutter.model_verbose }}",
            "menu_section": "{{ cookiecutter.menu_section}}",
            "menu_subsection": "{{ cookiecutter.menu_subsection }}",
            "menu_action": "create",
            "form": form
        }

        return render(request, "{{cookiecutter.module}}/form.html", context)
    
    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.created_by = request.user
            data.save()
            messages.success(
                request,
                f'{data} saved!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    '{{cookiecutter.user}}_dashboard_{{cookiecutter.module}}_detail',
                    kwargs={
                        '{{cookiecutter.master_reference}}': data.{{cookiecutter.master_pk}}
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new {{ cookiecutter.model_verbose }}",
                "menu_section": "{{ cookiecutter.menu_section}}",
                "menu_subsection": "{{ cookiecutter.menu_subsection }}",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "{{cookiecutter.module}}/form.html", context)


class {{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}DetailView(LoginRequiredMixin, Is{{cookiecutter.user_type_verbose}}ViewMixin, View):
    """ 
    Create view for {{ cookiecutter.model_verbose_plural }}. 
    
    Allowed HTTP verbs: 
        - GET
    
    Restrictions:
        - LoginRequired
        - {{ cookiecutter.user_type_verbose }} user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, {{ cookiecutter.master_pk }}=kwargs.get('{{ cookiecutter.master_reference }}', None))
        context = {
            "page_title": f"{{ cookiecutter.model_verbose }}: {obj}",
            "menu_section": "{{ cookiecutter.menu_section}}",
            "menu_subsection": "{{ cookiecutter.menu_subsection }}",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "{{cookiecutter.module}}/detail.html", context)


class {{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}UpdateView(LoginRequiredMixin, Is{{cookiecutter.user_type_verbose}}ViewMixin, View):
    """ 
    Create view for {{ cookiecutter.model_verbose_plural }}. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - {{ cookiecutter.user_type_verbose }} user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, {{ cookiecutter.master_pk }}=kwargs.get('{{ cookiecutter.master_reference }}', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": "Update {{ cookiecutter.model_verbose }}: {obj}",
            "menu_section": "{{ cookiecutter.menu_section}}",
            "menu_subsection": "{{ cookiecutter.menu_subsection }}",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "{{cookiecutter.module}}/form.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, {{ cookiecutter.master_pk }}=kwargs.get('{{ cookiecutter.master_reference }}', None))
        form = MasterForm(instance=obj, data=request.POST)

        if form.is_valid():
            data = form.save()
            messages.success(
                request,
                f'{data} saved!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    '{{cookiecutter.user}}_dashboard_{{cookiecutter.module}}_detail',
                    kwargs={
                        '{{cookiecutter.master_reference}}': data.{{cookiecutter.master_pk}}
                    }
                )
            )
        else:
            context = {
                "page_title": "Update {{ cookiecutter.model_verbose }}: {obj}",
                "menu_section": "{{ cookiecutter.menu_section}}",
                "menu_subsection": "{{ cookiecutter.menu_subsection }}",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "{{cookiecutter.module}}/form.html", context)


class {{cookiecutter.user_type_verbose}}Dashboard{{cookiecutter.model}}DeleteView(LoginRequiredMixin, Is{{cookiecutter.user_type_verbose}}ViewMixin, View):
    """ 
    Create view for {{ cookiecutter.model_verbose_plural }}. 
    
    Allowed HTTP verbs: 
        - GET
        - POST
    
    Restrictions:
        - LoginRequired
        - {{ cookiecutter.user_type_verbose }} user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, {{ cookiecutter.master_pk }}=kwargs.get('{{ cookiecutter.master_reference }}', None))
        context = {
            "page_title": "Delete {{ cookiecutter.model_verbose }}: {obj}",
            "menu_section": "{{ cookiecutter.menu_section}}",
            "menu_subsection": "{{ cookiecutter.menu_subsection }}",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "{{cookiecutter.module}}/delete.html", context)
    
    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, {{ cookiecutter.master_pk }}=kwargs.get('{{ cookiecutter.master_reference }}', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                '{{cookiecutter.user}}_dashboard_{{cookiecutter.module}}_list'
            )
        )
