from django.shortcuts import render,redirect
from .models import Account,interior
from django.http import JsonResponse
# Create your views here.
def main_page(request):
    user_id = request.session.get('user')
    data = {'login':False} 
    print(user_id)   
    if user_id:
        data['login'] = True
        n = Account.objects.get(user_id=user_id)
        data['name'] = n.name
        data['id'] = n.user_id
        print(n.star_address.split(','))
        data['star_address'] = n.star_address.split(',')
        inte = interior.objects.all()
        data['interior'] = inte
        
        return render(request,'chaeum_app/main.html',data)
    else:
        return render(request,'chaeum_app/login.html',{'error':False})


def verify(request):
    if request.method =="POST":
        print("TTT")
        uid = request.POST.get("userid",None)
        pw = request.POST.get("password",None)
        print(uid,pw)
        if Account.objects.filter(user_id=uid).exists():
            n = Account.objects.get(user_id=uid)
            if n.password == pw:
                request.session['user'] = uid
                return redirect('')
            else:
                return render('chaeum_app/login.html',{'error':True})
    else:
        print("none post")
        return render('chaeum_app/login.html',{'error':True})

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
        print(job)
        interior.objects.create(user_id = user_id,interior_name = title,start_date=start_date,end_date=end_date, address=address,job =job)
        
    return redirect('/Main')
def register(request):
    return render(request,'chaeum_app/register.html')
#회원가입 확인
def confirm_register(request):
    pass

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