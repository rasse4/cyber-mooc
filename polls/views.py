from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic



import logging
logger = logging.getLogger('pollsLogger')
logger.debug("Activity:")


from .models import Question, Choice



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
    else:

#   The following needs to be commented out to fix flaw:
        cursor = conn.cursor()
        command = """UPDATE Choice SET (vote) WHERE id=(id) VALUES (?,?= ;"""
        data_tuple=(selected_choice.votes.id)
        cursor.execute(command,data_tuple)
        conn.commit()


#        The following needs to be uncommented to fix the flaw:
#        selected_choice.votes += 1

        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

