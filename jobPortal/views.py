from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        candidates=Candidates.objects.filter(company__name=request.user.username)
        context={
            'candidates':candidates,
        }
        return render(request,'hr.html',context)
    else:
        companies=Company.objects.all()
        context={
            'companies':companies,
        }
        return render(request,'Jobseeker.html',context)