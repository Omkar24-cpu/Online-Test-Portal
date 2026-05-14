from django.shortcuts import render, redirect
from .models import *
import re


# =====================================================
# QUESTION CRUD
# =====================================================

def QuestionCrudPage(request):

    return render(request,
                  "Questions/questioncrud.html")


# CREATE QUESTION
def CreateQuestion(request):

    if request.method == "POST":

        qtext = request.POST.get('qtext')

        op1 = request.POST.get('op1')

        op2 = request.POST.get('op2')

        op3 = request.POST.get('op3')

        op4 = request.POST.get('op4')

        corr_answer = request.POST.get('corr_answer')

        subject = request.POST.get('subject')

        Question.objects.create(

            qtext=qtext,

            op1=op1,

            op2=op2,

            op3=op3,

            op4=op4,

            corr_answer=corr_answer,

            subject=subject
        )

        return redirect('/showallquestion/')

    return render(request,
                  "Questions/createquestion.html")


# SHOW ALL QUESTIONS
def ShowAllQuestion(request):

    questions = Question.objects.all()

    return render(request,
                  "Questions/showallquestion.html",
                  {'questions': questions})


# SHOW QUESTION FOR UPDATE
def ShowQuestionforUpdate(request, id):

    question = Question.objects.get(qno=id)

    return render(request,
                  "Questions/updatequestion.html",
                  {'question': question})


# UPDATE QUESTION
def UpdateQuestion(request, id):

    question = Question.objects.get(qno=id)

    if request.method == "POST":

        question.qtext = request.POST.get('qtext')

        question.op1 = request.POST.get('op1')

        question.op2 = request.POST.get('op2')

        question.op3 = request.POST.get('op3')

        question.op4 = request.POST.get('op4')

        question.corr_answer = request.POST.get('corr_answer')

        question.subject = request.POST.get('subject')

        question.save()

        return redirect('/showallquestion/')

    return render(request,
                  "Questions/updatequestion.html",
                  {'question': question})


# SHOW QUESTION FOR DELETE
def ShowQuestionforDelete(request, id):

    question = Question.objects.get(qno=id)

    return render(request,
                  "Questions/deletequestion.html",
                  {'question': question})


# DELETE QUESTION
def DeleteQuestion(request, id):

    question = Question.objects.get(qno=id)

    question.delete()

    return redirect('/showallquestion/')


# =====================================================
# USER CRUD
# =====================================================

def UserCrudPage(request):

    return render(request,
                  "User/usercrud.html")


# CREATE USER
def CreateUser(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        mobile_no = request.POST.get('mobile_no')

        # MOBILE VALIDATION
        if not re.fullmatch(r'[0-9]{10}', mobile_no):

            return render(request,
                          "User/createuser.html",
                          {
                              'error':
                              'Mobile number must contain exactly 10 digits'
                          })

        # PASSWORD VALIDATION
        if len(password) < 7 or len(password) > 12:

            return render(request,
                          "User/createuser.html",
                          {
                              'error':
                              'Password must be between 7 and 12 characters'
                          })

        UserInfo.objects.create(

            username=username,

            password=password,

            mobile_no=mobile_no
        )

        return redirect('/showalluser/')

    return render(request,
                  "User/createuser.html")


# SHOW ALL USERS
def ShowAllUser(request):

    users = UserInfo.objects.all()

    return render(request,
                  "User/showalluser.html",
                  {'users': users})


# SHOW USER FOR UPDATE
def ShowUserforUpdate(request, id):

    user = UserInfo.objects.get(id=id)

    return render(request,
                  "User/updateuser.html",
                  {'user': user})


# UPDATE USER
def UpdateUser(request, id):

    user = UserInfo.objects.get(id=id)

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        mobile_no = request.POST.get('mobile_no')

        # MOBILE VALIDATION
        if not re.fullmatch(r'[0-9]{10}', mobile_no):

            return render(request,
                          "User/updateuser.html",
                          {
                              'user': user,
                              'error':
                              'Mobile number must contain exactly 10 digits'
                          })

        # PASSWORD VALIDATION
        if len(password) < 7 or len(password) > 12:

            return render(request,
                          "User/updateuser.html",
                          {
                              'user': user,
                              'error':
                              'Password must be between 7 and 12 characters'
                          })

        user.username = username

        user.password = password

        user.mobile_no = mobile_no

        user.save()

        return redirect('/showalluser/')

    return render(request,
                  "User/updateuser.html",
                  {'user': user})


# SHOW USER FOR DELETE
def ShowUserforDelete(request, id):

    user = UserInfo.objects.get(id=id)

    return render(request,
                  "User/deleteuser.html",
                  {'user': user})


# DELETE USER
def DeleteUser(request, id):

    user = UserInfo.objects.get(id=id)

    user.delete()

    return redirect('/showalluser/')


# =====================================================
# LOGIN SYSTEM
# =====================================================

# LOGIN USER
def LoginUser(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        try:

            user = UserInfo.objects.get(
                username=username,
                password=password
            )

            request.session['username'] = user.username

            return redirect('/subject/')

        except:

            return render(request,
                          "User/login.html",
                          {
                              'error':
                              'Invalid Username or Password'
                          })

    return render(request,
                  "User/login.html")


# LOGOUT USER
def LogoutUser(request):

    request.session.flush()

    return redirect('/login/')


# =====================================================
# TEST SYSTEM
# =====================================================

# SUBJECT PAGE
def SubjectPage(request):

    return render(request,
                  "subject.html")


# START TEST
def StartTest(request):

    subject = request.GET.get('subject')

    questions = Question.objects.filter(
        subject=subject
    )

    return render(request,
                  "starttest.html",
                  {
                      'questions': questions,
                      'subject': subject
                  })


# SUBMIT TEST
def SubmitTest(request):

    # CHECK USER LOGIN
    if not request.session.get('username'):

        return redirect('/login/')

    if request.method == "POST":

        # GET USERNAME
        username = request.session.get(
            'username'
        )

        # GET SUBJECT
        subject = request.POST.get('subject')

        # GET QUESTIONS
        questions = Question.objects.filter(
            subject=subject
        )

        total_questions = questions.count()

        correct_answers = 0

        wrong_answers = 0

        # CHECK ANSWERS
        for q in questions:

            selected_answer = request.POST.get(
                str(q.qno)
            )

            if selected_answer == q.corr_answer:

                correct_answers += 1

            else:

                wrong_answers += 1

        # CALCULATE SCORE
        score = int(
            (correct_answers / total_questions) * 100
        )

        # SAVE RESULT
        Result.objects.create(

            username=username,

            subject=subject,

            total_questions=total_questions,

            correct_answers=correct_answers,

            wrong_answers=wrong_answers,

            score=score
        )

        # SHOW RESULT PAGE
        return render(request,
                      "result.html",
                      {
                          'username': username,
                          'subject': subject,
                          'total_questions': total_questions,
                          'correct_answers': correct_answers,
                          'wrong_answers': wrong_answers,
                          'score': score
                      })

    return redirect('/subject/')