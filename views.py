from django.shortcuts import render

from portfolio.models import Global, About, Skills, Experences,Client

# Create your views here.
def hi(request):
    mydata = Global.objects.all()[0]
    about = About.objects.all()[0]
    tecnical_skills = Skills.objects.filter(type="Technical Skills")
    professional_skills = Skills.objects.filter(type="Professional Skills")
    Educations = Experences.objects.filter(type="Education")
    Works = Experences.objects.filter(type="Work")
    client = Client.objects.all()
    context = {
        "mydata":mydata,
        "about":about,
        "tecnical_skills":tecnical_skills,
        "professional_skills":professional_skills,
        "Educations": Educations,
        "Works": Works,
        "client": client
    }
    return render(request,'portfolio/index.html',context)