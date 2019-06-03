from django.shortcuts import render


def analysis_list(request):
    return render(request, 'analysis/analysis_index.html')

def analysis_people(request):
    return render(request, 'analysis/jj.html')
