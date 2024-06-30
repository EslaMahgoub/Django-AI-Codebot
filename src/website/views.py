from django.shortcuts import render
from django.contrib import messages
from . import utils

LANG_LIST = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'git', 'go', 'java', 'javascript', 'jsx', 'markup', 'markup-templating', 'matlab', 'mongodb', 'perl', 'php', 'powershell', 'python', 'ruby', 'rust', 'sass', 'sql', 'swift', 'tsx', 'typescript', 'yaml']

def handle_code_submission(request, template_name, label):
    if request.method == 'POST':
        code = request.POST.get('code')
        lang = request.POST.get('lang')
        
        if lang == "Select Programming Language":
            messages.error(request, "Please select a programming language")
        else:
            try:
                message = f"Respond with code only, {label} the following {code} {lang}"
                response = utils.chat_with_openai(message, raw=False)
                return render(request, template_name, {"lang_list": LANG_LIST, "response": response, "code": code, "lang": lang})
                
            except Exception as e:
                return render(request, template_name, {"lang_list": LANG_LIST, "response": str(e), "code": code, "lang": lang})
            
    return render(request, template_name, {"lang_list": LANG_LIST})

def home(request):
    return handle_code_submission(request, "home.html", label="Fix")

def suggest(request):
    return handle_code_submission(request, "suggest.html", label="Suggest")