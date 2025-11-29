from django.shortcuts import redirect

def not_logged_in(view_func):  # Decorator to restrict access to views for logged-in users
    def wrapper(request, *args, **kwargs): # Wrap the view function
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to home if user is already logged in
        return view_func(request, *args, **kwargs) 
    return wrapper # Return the wrapper function