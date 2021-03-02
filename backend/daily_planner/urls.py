from django.contrib import admin
from django.urls import include, path

api_v1_patterns = [
    path('todo_list/', include('todolist_app.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_v1_patterns)),
]
