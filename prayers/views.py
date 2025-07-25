from django.shortcuts import render

# Create your views here.
def prayer_tracker(request):
    prayers = [
        {'name': 'Fajar', 'id': 'fajar'},
        {'name': 'Zohar', 'id': 'zohar'},
        {'name': 'Asar', 'id': 'asar'},
        {'name': 'Magrib', 'id': 'magrib'},
        {'name': 'Isha', 'id': 'isha'}
    ]
    return render(request, 'tracker.html', {'prayers': prayers})