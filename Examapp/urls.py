from django.urls import path
from . import views

urlpatterns = [

    # =====================================================
    # HOME
    # =====================================================

    path('', views.QuestionCrudPage),

    # =====================================================
    # QUESTION CRUD
    # =====================================================

    path('createquestion/',
         views.CreateQuestion),

    path('showallquestion/',
         views.ShowAllQuestion),

    path('showquestionforupdate/<int:id>/',
         views.ShowQuestionforUpdate),

    path('updatequestion/<int:id>/',
         views.UpdateQuestion),

    path('showquestionfordelete/<int:id>/',
         views.ShowQuestionforDelete),

    path('deletequestion/<int:id>/',
         views.DeleteQuestion),

    # =====================================================
    # USER CRUD
    # =====================================================

    path('usercrud/',
         views.UserCrudPage),

    path('createuser/',
         views.CreateUser),

    path('showalluser/',
         views.ShowAllUser),

    path('showuserforupdate/<int:id>/',
         views.ShowUserforUpdate),

    path('updateuser/<int:id>/',
         views.UpdateUser),

    path('showuserfordelete/<int:id>/',
         views.ShowUserforDelete),

    path('deleteuser/<int:id>/',
         views.DeleteUser),

    # =====================================================
    # LOGIN SYSTEM
    # =====================================================

    path('login/',
         views.LoginUser),

    path('logout/',
         views.LogoutUser),

    # =====================================================
    # TEST SYSTEM
    # =====================================================

    path('subject/',
         views.SubjectPage),

    path('starttest/',
         views.StartTest),

    path('submittest/',
         views.SubmitTest),

]