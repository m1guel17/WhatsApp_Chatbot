from django.urls import path

from apps.webhook.views import chatbotRoutes

urlpatterns = [
    path('', chatbotRoutes, name="webhook_"),
]
