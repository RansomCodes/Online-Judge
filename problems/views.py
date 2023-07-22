from django.shortcuts import render,redirect,reverse
from .models import questions,testcases,totsubmission
import subprocess,os
from django.contrib.auth.models import User,auth
from datetime import datetime

def home(request):
    ques=questions.objects.all()
    return render(request,'index.html',{'ques':ques})

def question_detail(request,question_id):
    try:
        ques=questions.objects.get(id=question_id)
        ques.statement.lstrip()
        return render(request,'submission.html',{'ques':ques})
    except questions.DoesNotExist:
        return render(request,'verdict.html')


def submit(request):
    
    # Getting hold of every data
    code=request.POST["code"]
    language=request.POST["language"]
    ques_id=request.POST["ques_id"]
    ques_name=questions.objects.get(id=ques_id).name
    curr_time=datetime.now()
    curr_lang=""
    # Extracting testcases from the data which has the question id sam as the problem id
    tc=testcases.objects.filter(question_id=ques_id)
    verdict="Wrong Answer"
    
    # option1 --> C++
    # option2 --> Java
    # option3 --> Python
    if language== "option1":
        # Path where the file is stored and needs to be rewritten
        file_path="assets/user_code.cpp"
        curr_lang="C++"
        # Rewriting the file
        with open(file_path,'w') as file:
            file.write(code)
        verdict="Accepted"
        
        # Getting hold of every testcase
        for test in tc:
            input_data=test.input
            print(input_data)
            output=run_cpp_file("user_code.cpp",input_data)
            print(output)
            # Comparing if the output of the user input function matched with current input
            if output.strip()!=test.expected_output.strip():
                verdict="Wrong answer"
                break
            
    elif language=="option2":
        
        file_path="assets/AddTwoNumbers.java"
        verdict="Accepted"
        curr_lang="Java"
        
        with open(file_path,"w") as file:
            file.write(code)
            
        for test in tc:
            input_data=test.input
            output=run_java_file("AddTwoNumbers.java",input_data)
            
            if output.strip()!=test.expected_output.strip():
                verdict="Wrong Answer"
                break
    
    elif language=="option3":
        
        file_path="assets/python_code.py"
        verdict="Accepted"
        curr_lang="Python"
        
        with open(file_path,"w") as file:
            file.write(code)
            
        for test in tc:
            input_data=test.input
            output=run_python_file("python_code.py",input_data)
            if output.strip()!=test.expected_output.strip():
                verdict="Wrong Answer"
                break
    
    currsubmission=totsubmission(user=request.user.first_name,verdict=verdict,time_of_submission=curr_time,problem=ques_name,language=curr_lang,date_of_submission=curr_time)
    currsubmission.save()
    sub=totsubmission.objects.all()
    return render(request,'verdict.html',{'subs':sub})


def run_cpp_file(file_name,input_data):
    # connect the file name to its correct path
    file_path=os.path.join("assets",file_name)
        
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


def run_java_file(file_name,input_data):
    file_path=os.path.join("assets",file_name)
    
    compile_result=subprocess.run(["javac",file_path],capture_output=True,text=True)
    if compile_result.returncode==0:
        class_name= os.path.splitext(file_name)[0] #Extract the class name from the file name
        run_result=subprocess.run(["java","-classpath","assets",class_name],input=input_data,capture_output=True,text=True)
        if run_result.returncode==0:
            return run_result.stdout
        else:
            return run_result.stderr
    else:
        return compile_result.stderr


def run_python_file(file_name,input_data):
    file_path=os.path.join("assets",file_name)
    
    run_result= subprocess.run(["python",file_path],input=input_data,capture_output=True,text=True)
    
    if run_result.returncode==0:
        return run_result.stdout
    else: 
        return run_result.stderr