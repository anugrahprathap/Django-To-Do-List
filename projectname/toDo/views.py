# In your app's views.py file
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

from django.contrib import messages

from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')



# In your app's views.py file
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import CustomUserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a UserProfile for the newly registered user
            UserProfile.objects.create(user=user, full_name=form.cleaned_data['full_name'])
            messages.success(request, f'Account created successfully for {form.cleaned_data["full_name"]}!')

            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            

            login(request, user)  # Log in the user
            return redirect('home')  # Redirect to the user profile page
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})




@login_required
def home_view(request):
    tasks = Task.objects.filter(user=request.user)  # Filter tasks by the logged-in user
    return render(request, 'home.html', {'tasks': tasks})
    
def logout_view(request):
    logout(request)
    return redirect('landing_page')





# In your app's views.py file
def user_profile(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    return render(request, 'user_profile.html', {'user': user, 'tasks': tasks})

# Implement similar views for listing, updating, and deleting tasks




from .models import Task  # Import your Task model

# View for adding a to-do list item
def add_task(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        user = request.user
        completed = request.POST.get('completed', False)
        due_date_str = request.POST.get('due_date', None)
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str.strip() else None
        category = request.POST['category']  # Get the selected category
        
        task = Task(name=name, description=description, user=user, completed=completed, due_date=due_date, category=category)
        task.save()
        return redirect('home')
    return render(request, 'add_task.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})


from .forms import CustomUserCreationForm, UserProfileForm

@login_required
def edit_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {'form': form}
    return render(request, 'edit_profile.html', context)



# View for viewing a list of to-do list items
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Filter tasks by the logged-in user
    return render(request, 'task_list.html', {'tasks': tasks})

# View for editing a to-do list item
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        task.name = request.POST['name']
        task.description = request.POST['description']
        task.save()
        return redirect('home')  # Redirect to the task list page
    
    return render(request, 'edit_task.html', {'task': task})

# View for deleting a to-do list item
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('home')  # Redirect to the task list page
    
    return render(request, 'delete_task.html', {'task': task})




def toggle_task_status(request, task_id):
    # Get the task object by its ID
    task = get_object_or_404(Task, id=task_id)

    # Toggle the task's completed status
    task.completed = not task.completed
    task.save()

    # Redirect back to the task list page
    return redirect('home')




def search_task(request):
    query = request.GET.get('q')
    

    if query:
        # Perform a case-insensitive search for tasks that contain the query string
        tasks = Task.objects.filter(name__icontains=query)
    else:
        tasks = Task.objects.all()

    return render(request, 'home.html', {'tasks': tasks, 'query': query})