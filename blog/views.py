
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
from django.views.generic import ListView, DetailView, View
from django.utils import timezone


# def home(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("blog/templates/home.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    print('........111')
    try:
        print(".......222")
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        print("..........3333")
        return render(
            request, 'returnblog/templates/detail.html',
            {'question': question, "error_message":
             "you didn't selected any choice"}
        )
    else:
        print("........222")
        selected_choice.votes +=1
        selected_choice.save()



        return HttpResponseRedirect(reverse("blog:results", args=[question.pk,])) 
    

# def results(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     return render(request, "blog/templates/results.html",
#                   {"question": question})


# def about(request, pk):
#     print('.........')
#     try:
#         print(pk)
#         question = Question.objects.get(pk=pk)

#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "blog/templates/detail.html", {"question": question})


class PollListView(ListView):
    template_name = 'blog/templates/home.html'
    context_object_name = 'latest_question_list'
 
    def get_queryset(self):

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class PollDetailView(DetailView):
    model = Question
    template_name = 'blog/templates/detail.html'


class PollResultView(DetailView):
    model = Question
    template_name = "blog/templates/results.html"
    success_url = '/'
    

# class PollVoteView(View):
#     def get(request):   
#         return render(request, 'blog/templates/detail.html')

#     def post(request, pk):
#         question = get_object_or_404(Question, pk=pk)
#         print('........111')
#         try:
#             print(".......222")
#             selected_choice = question.choice_set.get(pk=request.POST['choice'])
#         except (KeyError, Choice.DoesNotExist):
#             print("..........3333")
#             return render(
#                 request, 'returnblog/templates/detail.html',
#                 {'question': question, "error_message":
#                 "you didn't selected any choice"}
#             )
#         else:
#             print("........222")
#             selected_choice.votes +=1
#             selected_choice.save()
#             return HttpResponseRedirect(reverse("blog:results", args=[question.pk,])) 
