from django.db import models


# =====================================================
# QUESTION MODEL
# =====================================================

class Question(models.Model):

    qno = models.AutoField(primary_key=True)

    qtext = models.TextField()

    op1 = models.CharField(max_length=200)

    op2 = models.CharField(max_length=200)

    op3 = models.CharField(max_length=200)

    op4 = models.CharField(max_length=200)

    corr_answer = models.CharField(max_length=200)

    subject = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.qtext


# =====================================================
# USER MODEL
# =====================================================

class UserInfo(models.Model):

    username = models.CharField(max_length=100)

    password = models.CharField(max_length=100)

    mobile_no = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.username


# =====================================================
# RESULT MODEL
# =====================================================

class Result(models.Model):

    username = models.CharField(max_length=100)

    subject = models.CharField(max_length=100)

    total_questions = models.IntegerField()

    correct_answers = models.IntegerField()

    wrong_answers = models.IntegerField()

    score = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.username