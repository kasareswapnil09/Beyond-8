from django.shortcuts import render, redirect
from .models import Schedule,Nurse,Shift
from .forms import ScheduleForm
from ortools.sat.python import cp_model
from django.views import View
from django.shortcuts import render


def nurse_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            nurse = form.cleaned_data['nurse']
            shift = form.cleaned_data['shift']
            day = form.cleaned_data['day']
            
            # TODO: Add code to optimize and schedule the nurse using Google OR-Tools
            
            # For now, save the schedule without optimization
            Schedule.objects.create(nurse=nurse, shift=shift, day=day)
            return redirect('nurse_schedule')
    else:
        form = ScheduleForm()

    schedules = Schedule.objects.all()
    return render(request, 'nurse_schedule.html', {'form': form, 'schedules': schedules})


# from ortools.sat.python import cp_model

def optimize_schedule(nurses, shifts, days):
    model = cp_model.CpModel()
    shifts_worked = {}

    for nurse in nurses:
        for day in days:
            for shift in shifts:
                shifts_worked[(nurse.id, day, shift.id)] = model.NewBoolVar(f'nurse_{nurse.id}_day_{day}_shift_{shift.id}')

    # TODO: Add constraints based on the problem statement

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Apply the optimized schedule
    if status == cp_model.OPTIMAL:
        for nurse in nurses:
            for day in days:
                for shift in shifts:
                    if solver.Value(shifts_worked[(nurse.id, day, shift.id)]) == 1:
                        Schedule.objects.create(nurse=nurse, shift=shift, day=day)

def nurse_schedule(request):
    nurses = Nurse.objects.all()
    shifts = Shift.objects.all()
    days = [1, 2, 3, 4, 5, 6, 7]  # Example days, adjust accordingly

    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            nurse = form.cleaned_data['nurse']
            shift = form.cleaned_data['shift']
            day = form.cleaned_data['day']

            Schedule.objects.create(nurse=nurse, shift=shift, day=day)
            return redirect('nurse_schedule')
    else:
        form = ScheduleForm()

    optimize_schedule(nurses, shifts, days)

    schedules = Schedule.objects.all()
    return render(request, 'nurse_schedule.html', {'form': form, 'schedules': schedules})



# from django.views import View
# from django.shortcuts import render

class CustomAdminView(View):
    def get(self, request, *args, **kwargs):
        nurses = Nurse.objects.all()
        return render(request, 'custom_admin_view.html', {'nurses': nurses})
