from django.urls import path


from employer.views import EmployerListAPIView, EmployerDepListAPIView, EmployerCreateAPIView, EmployerDeleteAPIView

urlpatterns = [
    path('', EmployerListAPIView.as_view(), name='employers-list'),
    path('<int:department_id>/', EmployerDepListAPIView.as_view(), name='employers-list-by-dep'),
    path('add/', EmployerCreateAPIView.as_view(), name='create-employer'),
    path('delete/<int:id>/', EmployerDeleteAPIView.as_view(), name='delete-employer'),


]