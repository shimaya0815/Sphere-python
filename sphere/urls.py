# sphere/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from offices.views import SignUpView, DashboardView, CustomLoginView
from offices.forms import CustomAuthenticationForm
from offices.views import UserListView, UserInviteView
from .views import HomeView
path
from chat import views as chat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', CustomLoginView.as_view(form_class=CustomAuthenticationForm), name='login'),
    # ログアウト時にトップページにリダイレクト
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('<str:office_id>/todo/', include('todos.urls')),
    path('<str:office_id>/dashboard/', DashboardView.as_view(), name='dashboard'),
    path('<str:office_id>/client/', include('tax_clients.urls')),
    path('<str:office_id>/users/', UserListView.as_view(), name='user_list'),
    path('<str:office_id>/users/invite/', UserInviteView.as_view(), name='user_invite'),
    path('chat/', chat_views.chat_room, name='chat_room'),
]
