from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import ListView,DetailView
from .models import Questions
from django.contrib import messages
from django.contrib.auth.decorators  import login_required

# Create your views here.

def home(request):
    return render(request,"home.html")



    # crud functionality of the website 
class QuestionsListView(ListView):
    model = Questions
    template_name = "questions.html"
    context_object_name="questions"
    ordering=["-dateCreated"]
class DetailedCreateView(DetailView):
    model = Questions
    template_name = "ReadQuestions.html"
    context_object_name="question"
@login_required
def askquestions(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        description = request.POST.get('description').strip()
        
        # Validate form input
        if not title or not description:
            messages.error(request, "Title and description cannot be empty or whitespace.")
            return render(request, "Askquestion.html")
        
        # Create question
        question = Questions.objects.create(
            title=title,
            description=description,
            user=request.user
        )
        messages.success(request, "Your question has been successfully created")
        return redirect('questions')  # Ensure 'questions' is a valid URL name in your urls.py
    
    return render(request, "Askquestion.html")
@login_required
def update_question(request, question_id):
    question = get_object_or_404(Questions, id=question_id, user=request.user)
    
    if request.method == "POST":
        title = request.POST.get("title").strip()
        description = request.POST.get("description").strip()
        
        # Validate form input
        if not title or not description:
            messages.error(request, "Title and description cannot be empty or whitespace.")
            return render(request, "updatequestion.html", {"question": question})
        
        # Update question
        question.title = title
        question.description = description
        question.save()
        
        messages.success(request, "Your question has been successfully updated.")
        return redirect("questions")
    
    return render(request, "updatequestion.html", {"question": question})
    
def delete_question(request,question_id):
    question=get_object_or_404(Questions,id=question_id,user=request.user)
    
    if request.method=="POST":
        question.delete()
        messages.success(request, "Your question has been successfully deleted.")
        return redirect("questions")
    return render(request,"ReadQuestions.html")