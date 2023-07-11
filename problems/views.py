from django.shortcuts import render
from .models import questions

# Create your views here.
def home(request):
    ques=questions.objects.all()
    return render(request,'index.html',{'ques':ques})

def question_detail(request,question_id):
    try:
        ques=questions.objects.get(id=question_id)
        print("IDHAR HU MAI")
        return render(request,'submission.html',{'ques':ques})
    except questions.DoesNotExist:
        print("JALDI WAHAAN SE HATO")
        return render(request,'verdict.html')


def submit(request):
    return render(request,'verdict.html')