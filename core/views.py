from django.shortcuts import render
import pandas as pd
import os
from django.http import HttpResponse

# Create your views here.
def index(request):
    current_directory = os.path.dirname(__file__)
    csv_file_path = os.path.join(current_directory, 'data.csv')
    df = pd.read_csv(csv_file_path)

    institute_options = df['Institute'].unique()
    academic_program_options = df['Academic Program Name'].unique()
    quota_options = df['Quota'].unique()
    seat_type_options = df['Seat Type'].unique()
    gender_options = df['Gender'].unique()
    opening_rank_options = df['Opening Rank'].unique()
    closing_rank_options = df['Closing Rank'].unique()
    year_options = df['Year'].unique()
    round_options = df['Round'].unique()

    return render(request, "core/index.html", {
        'institute_options': institute_options,
        'academic_program_options': academic_program_options,
        'quota_options': quota_options,
        'seat_type_options': seat_type_options,
        'gender_options': gender_options,
        'opening_rank_options': opening_rank_options,
        'closing_rank_options': closing_rank_options,
        'year_options': year_options,
        'round_options': round_options,
    })

def college(request):
    if request.method == 'POST':
        institute = request.POST.get('institute')
        academic_program = request.POST.get('academic_program')
        quota = request.POST.get('quota')
        seat_type = request.POST.get('seat_type')
        gender = request.POST.get('gender')
        year = request.POST.get('year')
        round = request.POST.get('round')

        current_directory = os.path.dirname(__file__)
        csv_file_path = os.path.join(current_directory, 'data.csv')

        df = pd.read_csv(csv_file_path)

        filtered_colleges = df[(df['Institute'] == institute) &
                               (df['Academic Program Name'] == academic_program) &
                               (df['Quota'] == quota) &
                               (df['Seat Type'] == seat_type) &
                               (df['Gender'] == gender) &
                               (df['Round'] == round)]

        if not filtered_colleges.empty:
            colleges = filtered_colleges['Institute'].tolist()
            return render(request, 'college.html', {'colleges': colleges})
        else:
            return HttpResponse("No colleges found for the submitted criteria.")
    else:
        return HttpResponse("This view only accepts POST requests.")