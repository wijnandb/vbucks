from django.http import HttpResponse
from django.shortcuts import render
from .models import Chore, User

def index(request):
    list_of_chores = Chore.objects.all().order_by('chore_text')
    context = { 'list_of_chores': list_of_chores }
    return render(request, 'chores/index.html', context)
    
def detail(request, chore_id):
    return HttpResponse("Details van klusje %s." % chore_id)

def user(request, user_id):
    return HttpResponse("Behaalde punten en voltooide klussen van %s." % user_id)

#@login_required(login_url='/admin')
def claim(request, chore_id):
    return HttpResponse("Claim klus %s door zoon." % chore_id)

#def claim_chore(request, chore_id):
#    if request.method == 'POST':
#        form = ThoughtForm(request.POST)
#        if form.is_valid():
#            thought = form.save(commit=False)
#            thought.user = request.user
#            thought.save()
#            return HttpResponse('Hurray, saved!')
#    else:
#        form = ThoughtForm()
#    return render(request, 'lala/add_new_thought.html', {
#        'form': form
#    })
