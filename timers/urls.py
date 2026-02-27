from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_account/', views.add_account, name='add_account'),
    path('set_timer/<int:account_id>/', views.set_timer, name='set_timer'),
    
    # New V1.1 Routes for Modification
    path('delete_account/<int:account_id>/', views.delete_account, name='delete_account'),
    path('edit_account/<int:account_id>/', views.edit_account, name='edit_account'),

    # New Reset Timer Route
    path('reset_timer/<int:account_id>/<str:model_type>/', views.reset_timer, name='reset_timer'),
]
