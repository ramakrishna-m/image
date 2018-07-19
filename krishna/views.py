from django.shortcuts import render

def index(request):
    ram = []
    for i in range(6):
        ram.append(i)
    return render(request, 'index.html', {'ram': ram})


