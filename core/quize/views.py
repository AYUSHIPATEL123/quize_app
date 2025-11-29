from django.shortcuts import redirect, render
from .models import Quize, Question, Answer, UserSubmission, UserAnswer 
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import auth
from .decorators import not_logged_in
# Create your views here.
@not_logged_in  # Decorator to restrict access to views for logged-in users
def register(request):   # View for user registration
    if request.method == 'POST':  
        form = UserForm(request.POST)
        if form.is_valid():  # Check if the form data is valid
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')  # Get the password from cleaned data
            user = authenticate(username=username, password=password) # Authenticate the user
             # If the user is successfully created, log them in and redirect to the quiz list page
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('home')
            else:
                messages.error(request, 'Registration failed. User was not created.')
                return redirect('register')
        else:
            messages.error(request, 'Registration data is not valid. Registration failed')
    else:  # If the request method is not POST, then render the registration form
        form = UserForm()
    return render(request, 'register.html', {'form': form})

@not_logged_in  # Decorator to restrict access to views for logged-in users
def login(request):
    # If the request method is POST, then try to authenticate the user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        
        # If the user is not None, then log in the user and redirect to the quiz list page
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        # If the user is None, then show an error message and redirect to the login page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')   
    # If the request method is not POST, then render the login.html page
    return render(request, 'login.html')

@login_required(login_url='login') # Decorator to ensure the user is logged in
def quize_list(request):  # View to display the list of quizzes
    quizes = Quize.objects.all()
    return render(request, 'quize_list.html', {'quizes': quizes})

@login_required(login_url='login')
def quize_detail(request, quize_id):  # View to display the details of a specific quiz
    quize = Quize.objects.get(id=quize_id) 
    questions = Question.objects.filter(quize=quize)
    answers = Answer.objects.filter(question__in=questions) # Get answers for the questions in the quiz
    if request.method == 'POST':
        # Create a new UserSubmission object
        user_submission = UserSubmission.objects.create(
            quize=quize,
            user_name=request.user.username,
            score=0
        )
        # Get the selected answers from the form submission
        for question in questions:
            sel_ans_id = request.POST.get('question_' + str(question.id))   # Get the selected answer ID for the question
            if sel_ans_id:
                answer = Answer.objects.get(id=sel_ans_id)  # Get the Answer object for the selected answer ID
                # Create a new UserAnswer object for the selected answer
                user_answer = UserAnswer.objects.create(
                    submission=user_submission,
                    question=question,
                    answer=answer,
                    is_correct=answer.is_correct
                )   
                user_answer.save()
                if answer.is_correct:   # If the answer is correct, increment the score
                    user_submission.score += 1
        user_submission.save()
        return redirect('quize_result', submission_id = user_submission.id)
    return render(request, 'quize.html', {'quize': quize, 'questions': questions, 'answers': answers})       
@login_required(login_url='login')
def quize_result(request, submission_id):  # View to display the result of a quiz submission
    submission = UserSubmission.objects.get(id=submission_id)  
    return render(request, 'quize_result.html', {'submission': submission})

@login_required(login_url='login')
def log_out(request):  # logout user view
    auth.logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('home')