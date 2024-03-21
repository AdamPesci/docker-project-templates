from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from celery import Celery, chain, group
from .tasks import debug_task, add, sub

from .forms import DebugForm

import random

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class DebugFormView(FormView):
    template_name = 'debug_form.html'
    form_class = DebugForm
    success_url = 'debug-form'

    def form_valid(self, form):
        # define chain of tasks -  add some numbers, substract something from the result, then say hello!
        g = group(chain(add.s(random.randint(0, 9), random.randint(
            0, 9)), sub.s(random.randint(0, 9))), debug_task.s())
        try:
            result = g.apply_async().get(timeout=10)
        except TimeoutError as error:
            print(error)  # do something with error idk
            result = None
        context = self.get_context_data(form=form)
        context['success'] = True
        context['form_result'] = form.say_hello()
        context['celery_result'] = result
        return self.render_to_response(context=context)
