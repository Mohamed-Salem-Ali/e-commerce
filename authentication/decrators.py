from django.shortcuts import redirect

# Decorator to restrict authenticated users from accessing specific views
# If the user is already logged in, they are redirected to the home page.
def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect logged-in users to home
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func

# Decorator to restrict access to specific user groups
# Only users belonging to the allowed_roles can access the view
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group=None

            # Check if the user belongs to any group
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            # Allow access only if the user's group is in the allowed_roles list
            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return redirect('register') # Redirect unauthorized users to profile page
                
        return wrapper_func
    return decorator