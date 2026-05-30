from django.db import models

# Create your models here.


class PredictionHistory(models.Model):
    study_hours = models.FloatField()
    attendance = models.FloatField()
    previous_marks = models.FloatField()
    assignment_score = models.FloatField()

    prediction = models.CharField(max_length=20)
    probability = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} - {self.created_at}"
