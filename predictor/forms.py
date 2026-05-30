from django import forms


class StudentPredictionForm(forms.Form):
    study_hours = forms.FloatField(
        min_value=0,
        max_value=24,
        label="Study Hours Per Day"
    )

    attendance = forms.FloatField(
        min_value=0,
        max_value=100,
        label="Attendence Percentage"
    )
    
    previous_marks = forms.FloatField(
        min_value=0,
        max_value=100,
        label="Previous Marks"
    )
    assignment_score = forms.FloatField(
        min_value=0,
        max_value=100,
        label="Assignment Score"
    )
