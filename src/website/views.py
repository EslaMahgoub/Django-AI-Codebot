from django.shortcuts import render
from django.contrib import messages


def home(request):
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'git', 'go', 'java', 'javascript', 'jsx', 'markup', 'markup-templating', 'matlab', 'mongodb', 'perl', 'php', 'powershell', 'python', 'ruby', 'rust', 'sass', 'sql', 'swift', 'tsx', 'typescript', 'yaml']
    
    if request.method == 'POST':
        code = request.POST.get('code')
        lang = request.POST.get('lang')
        
        if lang == "Select Programming Language":
            messages.error(request, "Please select a programming language")
            
        return render(request, "home.html", {"lang_list": lang_list, "code": code, "lang": lang})
    return render(request, "home.html", {"lang_list": lang_list})