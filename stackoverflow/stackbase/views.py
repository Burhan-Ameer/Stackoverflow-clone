from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import ListView, DetailView
from .models import Questions, Answers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):
    return render(request, "home.html")



# crud functionality of the website 
class QuestionsListView(ListView):
    model = Questions
    template_name = "questions.html"
    context_object_name = "questions"
    ordering = ["-dateCreated"]

class DetailedCreateView(DetailView):
    model = Questions
    template_name = "ReadQuestions.html"
    context_object_name = "question"

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
            title = title,
            description = description,
            user = request.user
        )
        messages.success(request, "Your question has been successfully created")
        return redirect('questions')  # Ensure 'questions' is a valid URL name in your urls.py
    
    return render(request, "Askquestion.html")

@login_required
def update_question(request, question_id):
    question = get_object_or_404(Questions, id = question_id, user = request.user)
    
    if request.method == "POST":
        title = request.POST.get("title").strip()
        description = request.POST.get("description").strip()
        
        # Validate form input
        if not title or not description:
            messages.error(request, "Title and description cannot be empty or whitespace.")
            return render(request, "update_question.html", {"question": question})
        
        # Update question
        question.title = title
        question.description = description
        question.save()
        
        messages.success(request, "Your question has been successfully updated.")
        return redirect("questions")
    
    return render(request, "update_question.html", {"question": question})

@login_required 
def delete_question(request, question_id):
    question = get_object_or_404(Questions, id = question_id, user = request.user)
    
    if request.method == "POST":
        question.delete()
        messages.success(request, "Your question has been successfully deleted.")
        return redirect("questions")
    
    return render(request, "ReadQuestions.html", {"question": question})

@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Questions, id=question_id)
    
    if request.method == "POST":
        answer_content = request.POST.get('answer').strip()
        
        # Validate form input
        if not answer_content:
            messages.error(request, "Answer cannot be empty or whitespace.")
            return render(request, "ReadQuestions.html", {"question": question, "answers": question.answers.all()})
        
        # Create answer
        try:
            Answers.objects.create(
                user=request.user,
                questions=question,
                answer=answer_content
            )
            messages.success(request, "Your answer has been successfully submitted.")
        except Exception as e:
            messages.error(request, f"Error submitting answer: {str(e)}")
            return render(request, "ReadQuestions.html", {"question": question, "answers": question.answers.all()})
        
        return redirect('question_detail', question.id)  # Use positional argument for the URL parameter
    
    return render(request, "ReadQuestions.html", {"question": question, "answers": question.answers.all()})

@login_required
def edit_answer(request, answer_id):
    answer = get_object_or_404(Answers, id=answer_id, user=request.user)
    
    if request.method == "POST":
        answer_content = request.POST.get('answer').strip()
        
        # Validate form input
        if not answer_content:
            messages.error(request, "Answer cannot be empty or whitespace.")
            return render(request, "edit_answer.html", {"answer": answer})
        
        # Update answer
        try:
            answer.answer = answer_content
            answer.save()
            messages.success(request, "Your answer has been successfully updated.")
        except Exception as e:
            messages.error(request, f"Error updating answer: {str(e)}")
            return render(request, "edit_answer.html", {"answer": answer})
        
        return redirect('question_detail', answer.questions.id)  # Use positional argument for the URL parameter
    
    return render(request, "edit_answer.html", {"answer": answer})

@login_required
def delete_answer(request, answer_id):
    answer = get_object_or_404(Answers, id=answer_id, user=request.user)
    
    if request.method == "POST":
        question_id = answer.questions.id
        answer.delete()
        messages.success(request, "Your answer has been successfully deleted.")
        return redirect('question_detail', question_id)  # Use positional argument for the URL parameter
    
    return render(request, "delete_answer.html", {"answer": answer})