from django.contrib import admin
from django.urls import path
from dashboard.views import dashboard
from dashboard.auth_views import login_view, logout_view
from chatbot_app.views import chat
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_required(dashboard), name="dashboard"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("chat/", chat, name="chat"),
]
