from typing import Text
from django.db import reset_queries
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from questions.models import Question, Answer
from result.models import Result


# Create your views here.
class QuizViewList(ListView):
    model = Quiz
    template_name = 'quizes/main.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answer():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def save_quiz_view(request, pk):
    print(request.POST)
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        
        data_.pop('csrfmiddlewaretoken')
        
        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        result = []
        correct_ans = None

        for q in questions:
            a_selected = request.POST.get(q.text)
            
            if a_selected !="":
                question_answer = Answer.objects.filter(question=q)
                for a in question_answer:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_ans = a.text
                    else:
                        if a.correct:
                            correct_ans = a.text
                result.append({str(q): {'Jawaban_benar': correct_ans, 'Terjawab': a_selected}})
            else:
                result.append({str(q): 'Belum dijawab'})
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'Lolos': True, 'Skor': score_, 'Hasil': result})
        else:
            return JsonResponse({'Lolos': False, 'Skor': score_, 'Hasil': result})

    