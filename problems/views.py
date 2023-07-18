from django.shortcuts import render
from .models import questions
import subprocess,os

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
    code=request.POST["code"]
    language=request.POST["language"]
    file_path="assets/user_code.cpp"
    output=""
    with open(file_path,'w') as file:
        file.write(code)
    input_data="50"
    output=run_cpp_file("user_code.cpp",input_data)
    return render(request,'verdict.html',{'output':output})

def run_cpp_file(file_name,input_data):
    # connect the file name to its correct path
    file_path=os.path.join("assets",file_name)
    
    # Check if the file actually exists or not
    if not os.path.exists(file_path):
        print("File not found")
    with open(file_path, 'r') as file:
        content = file.read()
        print("$$$$$$$$", content)
        
    # Compiling the file with user input
    output_file_name="compiled_output"
    compile_result=subprocess.run(["g++",file_path,"-o",output_file_name],capture_output=True,text=True)
    if compile_result.returncode == 0:
        run_result=subprocess.run(["./"+output_file_name],input=input_data,capture_output=True,text=True)
        if run_result.returncode==0:
            return run_result.stdout
        else:
            return run_result.stderr
    else:
        return compile_result.stderr