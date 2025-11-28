from django.shortcuts import redirect, render
from .models import Quize, Question, Answer, UserSubmission, UserAnswer 
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.

def register(request):
    if request.method == 'POST':  
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            auth.login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('quize_list')
        else:
            messages.error(request, 'Registration failed')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('quize_list')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')   
    return render(request, 'login.html')

@login_required(login_url='login')
def quize_list(request):
    quizes = Quize.objects.all()
    return render(request, 'quize_list.html', {'quizes': quizes})

@login_required(login_url='login')
def quize_detail(request, quize_id):
    quize = Quize.objects.get(id=quize_id)
    questions = Question.objects.filter(quize=quize)
    answers = Answer.objects.filter(question__in=questions)
    if request.method == 'POST':
        user_submission = UserSubmission.objects.create(
            quize=quize,
            user_name=request.user.username,
            score=0
        )
        for question in questions:
            sel_ans_id = request.POST.get('question_' + str(question.id))
            if sel_ans_id:
                answer = Answer.objects.get(id=sel_ans_id)
                user_answer = UserAnswer.objects.create(
                    submission=user_submission,
                    question=question,
                    answer=answer,
                    is_correct=answer.is_correct
                )   
                user_answer.save()
                if answer.is_correct:
                    user_submission.score += 1
        user_submission.save()
        return redirect('quize_result', submission_id = user_submission.id)
    return render(request, 'quize.html', {'quize': quize, 'questions': questions, 'answers': answers})       
@login_required(login_url='login')
def quize_result(request, submission_id):
    submission = UserSubmission.objects.get(id=submission_id)
    return render(request, 'quize_result.html', {'submission': submission})

@login_required(login_url='login')
def log_out(request):
    auth.logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('home')