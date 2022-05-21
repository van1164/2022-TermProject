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
        return render(request,'chaeum_app/main.html',data)
    else:
        return render(request,'chaeum_app/login.html',{'error':False})

    if request.method =="POST":
        uid = request.POST.get("userid",None)
        pw = request.POST.get("password",None)
        user_data = verify(uid,pw)
        if user_data == False:
            return render(request, 'chaeum_app/login.html',{})
        data['name'] = user_data['name']
        data['id'] = user_data['id']
        print(data['name'])
        data['login'] = True
        star_address = Account.objects.get(user_id=uid).star_address
        star_address = star_address.split(',')
        data['star_address'] = star_address 
    return render(request,'chaeum_app/main.html',data)
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
    return render('chaeum_app/create_interior.html')


def create_interior(request):
    data =[{
    'category': '김시환',
    'profileImgUrl': 'https://placeimg.com/200/100/people/grayscale',
    'userName': '김시환',
    'vote': '예민한 개도 미용할 수 있는 곳이나 동물 병원 어디 있을까요?\n'
        '내일 유기견을 데려오기로 했는데 아직 성향을 잘 몰라서 걱정이 돼요 ㅜㅜ.',
    'voteImgUrl': 'https://placeimg.com/200/100/tech/grayscale',
    'heartCount': 48,
    'date': '7시간전',
    },
     {
    'category': '이윤우',
    'profileImgUrl': 'https://placeimg.com/200/100/people/grayscale',
    'userName': '이윤우',
    'vote': '예민한 개는 무섭다ㅠㅠ?\n'
        '걱정이 돼요 ㅜㅜ.',
    'voteImgUrl': 'https://placeimg.com/200/100/tech/grayscale',
    'heartCount': 514,
    'date': '1시간전',
    },      
           
           ]
    print("vote!!")
    return JsonResponse(data,safe=False)