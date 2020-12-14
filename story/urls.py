from django.urls import path


from . import views

app_name = 'story'
urlpatterns = [
    path('api/books/', api_views)
]
