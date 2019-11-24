from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from examtool.models import Category, Question
import random
import urllib.request

# Create your views here.


class IndexTemplateView(TemplateView):

    template_name = "index.html"
    # qid = Category

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # items = self.qid.objects.values_list('category_id', flat=True)

        # print(random.choice(items))

        # context['question_id'] = random.randint(items)

        return context


class QuestionTemplateView(TemplateView):

    template_name = "question.html"

    c = Category

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        categoryid = random.choice(self.c.objects.values_list('category_id', flat=True))

        q = random.choice(Question.objects.filter(category_id=categoryid))

        context['question'] = q.question
        context['answer1'] = q.answer1
        context['answer2'] = q.answer2
        context['answer3'] = q.answer3
        context['answer4'] = q.answer4
        context['seikai'] = categoryid
        context['pid'] = q.id

        return context


def answer(request):

    kaitou = request.POST['kaitou']
    answer = request.POST['answerid']
    q = Question.objects.filter(id=answer)
    kotae = list(q)[0].seikai

    if int(kaitou) == kotae:
        return render(request, 'result.html', {'result': '正解'})
    else:
        return render(request, 'result.html', {'result': '間違い'})
