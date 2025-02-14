from django.urls import path
from stackbase import views as stackbase_views
from stackusers.views import register, login_page, logout_page, profile, update_profile

urlpatterns = [
    path("", stackbase_views.home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("profile/", profile, name="profile"),
    path("update_profile/", update_profile, name="update_profile"),
    # CRUD part of app
    path("questions/", stackbase_views.QuestionsListView.as_view(), name="questions"),
    # Details of questions
    path("questions/<int:pk>/", stackbase_views.DetailedCreateView.as_view(), name="question_detail"),
    # Create questions
    path("ask_questions/", stackbase_views.askquestions, name="ask_questions"),   
    # Update questions
    path("questions/<int:question_id>/update/", stackbase_views.update_question, name="update_question"),
    # Delete questions
    path("questions/<int:question_id>/delete/", stackbase_views.delete_question, name="delete_question"),
    # Answer questions
    path("questions/<int:question_id>/answer/", stackbase_views.answer_question, name="answer_question"),
    # Edit answers
    path("answers/<int:answer_id>/edit/", stackbase_views.edit_answer, name="edit_answer"),
    # Delete answers
    path("answers/<int:answer_id>/delete/", stackbase_views.delete_answer, name="delete_answer"),
]
