from django.urls import path
from .views import predict_view, history_view, StudentPredictionAPIView


urlpatterns = [
    path("", predict_view, name="predict"),
    path("history/", history_view, name="history"),
    path("api/predict/", StudentPredictionAPIView.as_view(), name="api-predict"),
]
