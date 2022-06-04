from django.shortcuts import render,redirect
from .models import Account,interior
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages

def main_page(request):
    user_id = request.session.get('user')
    data = {'login':False} 
    if user_id:
        data['login'] = True
        n = Account.objects.get(user_id=user_id)
        data['name'] = n.name
        data['id'] = n.user_id
        data['star_address'] = n.star_address.split(',')
        inte = interior.objects.all()
        data['interior'] = inte
        lst = interior.objects.filter(user_id = user_id)
        data['my_interior'] = lst
        go_lst =[]
        idx = n.interior.split(',')
        user_inte = []
        for i in idx:
            if i =='' or i ==' ':
                continue
            go_lst.append(interior.objects.get(id = i))
            user_inte.append(int(i))
        data['go_interior'] = go_lst
        data['user_inte'] = user_inte
        return render(request,'chaeum_app/main.html',data)
    else:
        return render(request,'chaeum_app/login.html',{'error':False})


def verify(request):
    if request.method =="POST":
        uid = request.POST.get("userid",None)
        pw = request.POST.get("password",None)
        if Account.objects.filter(user_id=uid).exists():
            n = Account.objects.get(user_id=uid)
            if n.password == pw:
                request.session['user'] = uid
                return redirect('')
            else:
                return render(request,'chaeum_app/login.html',{'error':True})
        else:
            return render(request,'chaeum_app/login.html',{'error':True})
    else:
        return render(request,'chaeum_app/login.html',{'error':True})

def login(request):
    return render(request, 'chaeum_app/login.html',{'error':False})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/Main')

def go_to_create_interior(request):
    return render(request,'chaeum_app/create_interior.html',{})


def create_interior(request):
    if request.method =="POST":
        user_id = request.session['user']
        title = request.POST.get("title",None)
        start_date = request.POST.get("start",None)
        end_date = request.POST.get("end",None)
        address = request.POST.get("address",None)
        job_list = [request.POST.get("job_1",''), request.POST.get("job_2",''), request.POST.get("job_3",''), request.POST.get("job_4",'')]
        job =[]
        for i in job_list:
            if i =='':
                continue
            else:
                job.append(i)
                
        job =",".join(job)
        interior.objects.create(user_id = user_id,interior_name = title,start_date=start_date,end_date=end_date, address=address,job =job)

        
    return redirect('/Main')
def register(request):
    return render(request,'chaeum_app/register.html',{'perror':True,'ierror':True})
#회원가입 확인
def create_account(request):
    data = {"perror":True, "ierror":True}
    if request.method =="POST":
        if request.POST.get("InputPassword") != request.POST.get("RepeatPassword"):
            data["perror"] = False
            return render(request,'chaeum_app/register.html',data)
        if Account.objects.filter(user_id=request.POST.get("Inputid")).exists():
            data["ierror"]=False
            return render(request,'chaeum_app/register.html',data)
        name= request.POST.get("FirstName") +request.POST.get("LastName")
        email = request.POST.get("InputEmail")
        id =request.POST.get("Inputid")
        password = request.POST.get("InputPassword")
        Account.objects.create(user_id=id,password = password,email=email,name =name)
        return redirect('/login')

def admit(request):
    if request.method =="GET":
        user_id = request.GET.get("user_id")
        inte_id = request.GET.get("inte_id")
        acc = Account.objects.get(user_id=user_id)
        acc.interior = acc.interior+inte_id+", "
        acc.save()
        inte =interior.objects.get(id =inte_id)
        inte.admit_user = user_id
        inte.save()
        messages.warning(request, "신청되었습니다.")
        return redirect('/Main')

def show_profile(request):
    data = dict()
    if request.method =="GET":
        print(request.GET)
        user_id = request.GET.get("user_id")
        inte_id = request.GET.get("inte_id")
        print(user_id)
        user =Account.objects.get(user_id = user_id)
        data['user'] = user
        data['time'] = str(len(user.interior.split(',')))
        data['inte_id'] = inte_id
    return render(request,'chaeum_app/show_profile.html',data)

def select(request):
    if request.method =="GET":
        print(request.GET)
        user_id = request.GET.get("user_id")
        inte_id = request.GET.get("inte_id")
        inte =interior.objects.get(id = inte_id)
        inte.matching = True
        inte.save()
    return redirect('/Main')

def send_to_mobile(request):
    data = []
    lst = interior.objects.all()
    for item in lst:
        dic = dict()
        dic['location']=item.address
        dic['jobGroup']=item.job
        dic['endDate']=item.end_date
        dic['startDate']=item.start_date
        data.append(dic)

    return JsonResponse(data,safe=False)