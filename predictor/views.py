from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import StudentPredictionForm
from .models import PredictionHistory
from .serializers import StudentPredictionSerializer
from .services.ml_service import predict_student_performance


def predict_view(request):
    result = None

    if request.method == "POST":
        form = StudentPredictionForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            result = predict_student_performance(cleaned_data)

            PredictionHistory.objects.create(
                study_hours=cleaned_data["study_hours"],
                attendance=cleaned_data["attendance"],
                previous_marks=cleaned_data["previous_marks"],
                assignment_score=cleaned_data["assignment_score"],
                prediction=result["prediction"],
                probability=result["probability"],
            )
    else:
        form = StudentPredictionForm()

    return render(request, "predictor/predict.html", {
        "form": form,
        "result": result,
    })


def history_view(request):
    histories = PredictionHistory.objects.order_by("-created_at")
    return render(request, "predictor/history.html", {
        "histories": histories,
    })


class StudentPredictionAPIView(APIView):
    def post(self, request):
        serializer = StudentPredictionSerializer(data=request.data)

        if serializer.is_valid():
            cleaned_data = serializer.validated_data

            result = predict_student_performance(cleaned_data)

            PredictionHistory.objects.create(
                study_hours=cleaned_data["study_hours"],
                attendance=cleaned_data["attendance"],
                previous_marks=cleaned_data["previous_marks"],
                assignment_score=cleaned_data["assignment_score"],
                prediction=result["prediction"],
                probability=result["probability"],
            )

            return Response(result, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
