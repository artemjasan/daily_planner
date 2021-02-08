from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('todo_list/', include('todolist_app.urls')),
    path('admin/', admin.site.urls),
]
