from django.shortcuts import render,redirect,HttpResponse,reverse
from .forms import  CreatePollForm
from .models import Poll

# Create your views here.

def home(request):
    polls = Poll.objects.all()
    
    context = {
        'polls':polls,
    }
    
    return render(request,'main/home.html',context)



def create(request):
    
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    
    context = {
        'form':form,
    }
    return render(request,'main/create.html',context)


def vote(request,id):
    poll = Poll.objects.get(id=id)
    
    if request.method == 'POST':
        select_answer = request.POST['ses']
        
        if select_answer == 'option1':
            poll.option_one_count += 1
        elif select_answer == 'option2':
            poll.option_two_count += 1
        elif select_answer == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400,'Error')
        
        poll.save()
        return redirect(reverse('results',kwargs={'id':id}))
    
    
    context = {
        'poll':poll
    }
    return render(request,'main/vote.html',context)


def results(request,id):
    poll = Poll.objects.get(id=id)
    
    context = {
        'poll':poll
    }
    
    return render(request,'main/results.html',context)


