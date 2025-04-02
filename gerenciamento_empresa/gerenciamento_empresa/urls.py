
from django.contrib import admin
from django.urls import path
from empresa import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.login_view, name='home'),
    path('cadastro/projeto/', views.cadastro_projeto, name='cadastro_projeto'),
    path('cadastro/trainee/', views.cadastro_trainee, name='cadastro_trainee'),
    path('cadastro/meta/', views.cadastro_meta, name='cadastro_meta'),
    path('cadastro/membro/', views.cadastro_membro, name='cadastro_membro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('reset_senha/', auth_views.PasswordResetView.as_view(), name='reset_senha'),
    path('reset_senha/done/', auth_views.PasswordResetDoneView.as_view(), name='reset_senha_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('projetos/', views.projetos, name='projetos'),
    path('metas/', views.metas, name='metas'),
    path('setores/', views.setores, name='setores'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
]

