from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db import connection
# Create your views here.
def index(request):
    x=request.session.get('auserid')
    m=mcart.objects.all().filter(userid=x).count()
    return render(request,'user/index.html',{"n":m})
def home(request):
    x=request.session.get('auserid')
    m=mcart.objects.all().filter(userid=x).count()
    return render(request,'user/home.html',{"n":m})
def login(request):
    x=request.session.get('auserid')
    m=mcart.objects.all().filter(userid=x).count()
    if request.method=="POST":
        Email=request.POST.get('e')
        Password=request.POST.get('p')
        x=register.objects.all().filter(email=Email,passwd=Password).count()
        if x==1:
            request.session['userid']=Email
            return HttpResponse("<script>alert('You Are Login Successfully..');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('Your userid or password is incorrect !!!');location.href='/user/login/'</script>")    

    return render(request,'user/login.html',{"n":m})    
def signup(request):
    x=request.session.get('auserid')
    m=mcart.objects.all().filter(userid=x).count()
    if request.method=="POST":
        Name=request.POST.get('name')
        Mobile=request.POST.get('mob')
        Email=request.POST.get('email')
        Password=request.POST.get('passwd')
        Cpassword=request.POST.get('cpasswd')
        Picture=request.FILES.get('ig')
        Address=request.POST.get('msg')
        x=register.objects.all().filter(email=Email).count()
        if x==0:
            register(name=Name,email=Email,mobile=Mobile,ppic=Picture,passwd=Password,cpasswd=Cpassword,address=Address).save()
            return HttpResponse("<script>alert('You are Register Successfully ..');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('You are already Register !!');location.href='/user/index/'</script>")    
    return render(request,'user/signup.html',{"n":m})    
def contact(request):
    x=request.session.get('auserid')
    m=mcart.objects.all().filter(userid=x).count()
    return render(request,'user/contact.html',{"n":m})        
def plumber(request):
    x=request.session.get('auserid')
    k=mcart.objects.all().filter(userid=x).count()
    m=category.objects.all()
    dict={"data":m,"n":k}
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('aadhar')
        d=request.POST.get('pancard')
        e=request.POST.get('phone')
        f=request.POST.get('aphone')
        g=request.POST.get('job')
        h=request.POST.get('date')
        i=request.POST.get('city')
        j=request.FILES.get('igg')
        x=worker.objects.all().filter(email=b).count()
        if x==0:
            worker(name=a,email=b,aadhar=c,pan=d,phone=e,aphone=f,job=g,date=h,city=i,pic=j).save()
            return HttpResponse("<script>alert('Joined Successfully ');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('You are already Joined');location.href='/user/index/'</script>")    
    return render(request,'user/plumber.html',context=dict)
def blog(request):
    x=request.session.get('auserid')
    k=mcart.objects.all().filter(userid=x).count()
    m=category.objects.all()
    dict={"data":m,"n":k}
    return render(request,'user/blog.html',context=dict) 

################################################################################################

def team(request):
    x=request.session.get('auserid')
    k=mcart.objects.all().filter(userid=x).count()
    m=worker.objects.all().filter(job="Plumber").order_by('-id')
    e=worker.objects.all().filter(job="Electrician").order_by('-id')
    b=worker.objects.all().filter(job="Bikes").order_by('-id')
    t=worker.objects.all().filter(job="Bus and Truck").order_by('-id')
    a=worker.objects.all().filter(job="Auto").order_by('-id')
    tr=worker.objects.all().filter(job="Tractor").order_by('-id')
    c=worker.objects.all().filter(job="Cars").order_by('-id')
    dic={"data":m,"edata":e,"bdata":b,"tdata":t,"adata":a,"trdata":tr,"cdata":c,"n":k}
    return render(request,'user/team.html',context=dic)

########################################################################################################
def help(request):
    m=category.objects.all()
    dict={"data":m}
    if request.method=="POST":
        Name=request.POST.get('name')
        Mobile=request.POST.get('mobile')
        Amobile=request.POST.get('amobile')
        City=request.POST.get('city')
        Address=request.POST.get('address')
        Job=request.POST.get('job')
        userdata(name=Name,mobile=Mobile,amobile=Amobile,city=City,address=Address,job=Job).save()
        return HttpResponse("<script>alert('Your Request Successfully Submited !!!!');location.href='/user/help/'</script>")
    return render(request,'user/help.html',context=dict)    
##########################################################################################################

def signout(request):
    if request.session.get('userid'):
        del request.session['userid']
    return HttpResponse("<script>alert('You are singout');location.href='/user/index/'</script>")
#############################################################################################################    
def work(request):
    x=request.session.get('auserid')
    k=mcart.objects.all().filter(userid=x).count()
    m=userdata.objects.all().order_by('-id')
    dict={"udata":m,"n":k,"id":id}
    return render(request,'user/work.html',context=dict)  
##############################################################################################################    
def alogin(request):
    if request.method=="POST":
        Email=request.POST.get('ee')
        x=worker.objects.all().filter(email=Email).count()
        if request.session.get('userid'):
            return HttpResponse("<script>alert('You Are Already Login As User 12345');location.href='/user/index/'</script>")
        if x==1:
            request.session['auserid']=Email
            return HttpResponse("<script>alert('You Are Login Successfully !!!');location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('Your Email Id Invalid !!!!');location.href='/user/index/'</script>")    
    return render(request,'user/index.html')        
#######################################################################################################################################

def asignout(request):
    if request.session.get('auserid'):
        del request.session['auserid'] 
    return HttpResponse("<script>alert('You are singout');location.href='/user/index/'</script>")

######################################################################################################################

def pricing(request):
    return render(request,'user/pricing.html')
###################################################################################################################
def cart(request):
    p=request.GET.get('uid')
    user=request.session.get('auserid')
    if user:
        if p is not None:
            mcart(userid=user,pid=p,cdate=datetime.now().date(),status=True).save()
            return HttpResponse("<script>alert('Your item added...5656');location.href='/user/work/'</script>")
    else:
        return HttpResponse("<script>alert('You have login first as a mate partner !!!!!!');location.href='/user/signin/'</script>")
    return render(request,'user/cart.html') 

################################################################################################################################################
def showauser(request):
    x=request.session.get('auserid')
    k=mcart.objects.all().filter(userid=x).count()
    auser=request.session.get('auserid')
    if auser:
        cursor=connection.cursor()
        cursor.execute("select u.*,c.* from user_userdata u, user_mcart c where u.id=c.pid and c.userid='"+str(auser)+"'")
        cdata=cursor.fetchall()
    return render(request,'user/showauser.html',{"cdata":cdata,"n":k})
