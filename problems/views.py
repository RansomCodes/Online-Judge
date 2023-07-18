from django.shortcuts import render
from .models import questions,testcases
import subprocess,os

# Create your views here.
def home(request):
    ques=questions.objects.all()
    return render(request,'index.html',{'ques':ques})

def question_detail(request,question_id):
    try:
        ques=questions.objects.get(id=question_id)
        # print("IDHAR HU MAI")
        return render(request,'submission.html',{'ques':ques})
    except questions.DoesNotExist:
        # print("JALDI WAHAAN SE HATO")
        return render(request,'verdict.html')


def submit(request):
    
    # Getting hold of every data
    code=request.POST["code"]
    language=request.POST["language"]
    ques_id=request.POST["ques_id"]
    tc=testcases.objects.filter(question_id=ques_id)
    verdict="Accepted"
    if language== "option1":
        # Path where the file is stored and needs to be rewritten
        file_path="assets/user_code.cpp"
        
        # Rewriting the file
        with open(file_path,'w') as file:
            file.write(code)
        
        # Getting hold of every testcase associated with the current question id
        for test in tc:
            input_data=test.input
            # print(test.input)
            output=run_cpp_file("user_code.cpp",input_data)
            if output.strip()!=test.expected_output.strip():
                # print(output,"&&&&&&&&&&",test.expected_output)
                # print(len(output))
                # print(len(test.expected_output))
                verdict="Wrong answer"
                break
            
    elif language=="option2":
        file_path="assets/AddTwoNumbers.java"
        with open(file_path,"w") as file:
            file.write(code)
        for test in tc:
            input_data=test.input
            output=run_java_file("AddTwoNumbers.java",input_data)
            if output.strip()!=test.expected_output.strip():
                verdict="Wrong Answer"
                break
    return render(request,'verdict.html',{'verdict':verdict})


def run_cpp_file(file_name,input_data):
    # connect the file name to its correct path
    file_path=os.path.join("assets",file_name)
    
    # if not os.path.exists(file_path):
    #     print("File not found")
    # else:
    #     with open(file_path,"r") as file:
    #         content=file.read()
    #         print(content)
        
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
    
    # if not os.path.exists(file_path):
    #     print("File not found")
    # else:
    #     with open(file_path,"r") as file:
    #         content=file.read()
    #         print(content)
    
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
    