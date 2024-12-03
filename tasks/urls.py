# tasks/urls.py

# tasks/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LoginView, LogoutView
from .views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView
from .views import ProfileView, UpdateProfilePhotoView, UpdateUsernameView, UpdatePasswordView, AdminLoginView, SuperuserDashboardView


urlpatterns = [
    # Register view (user signup)
    path('register/', RegisterView.as_view(), name='register'),
    
    # Login and Get Access & Refresh tokens
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Refresh JWT Access Token
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Logout view (invalidate session)
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Endpoint for creating a new task
    path('tasks/', TaskCreateView.as_view(), name='task-create'),
    
    # Endpoint to list tasks with search filters
    path('tasks/list/', TaskListView.as_view(), name='task-list'),
    
    # Endpoint to update a task by ID
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    
    # Endpoint to delete a task by ID
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),

     path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update-photo/', UpdateProfilePhotoView.as_view(), name='update-profile-photo'),
    path('profile/update-username/', UpdateUsernameView.as_view(), name='update-username'),
    path('profile/update-password/', UpdatePasswordView.as_view(), name='update-password'),

    #Admin Login
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('admin/dashboard/',SuperuserDashboardView.as_view(),name='admin-dashboard')
]
