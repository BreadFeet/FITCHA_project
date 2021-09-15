from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

# Create your views here.
from config import settings
from frame.custdb import CustDB
from frame.error import ErrorCode
from frame.linkdb import LinkDB
from myanalysis.myanalysis import Analysis


def home(request):
    # print(dir(request.session))
    # print(request.session.keys())         # ['logininfo']
    # print(request.session.values())       # [{'id':'id01', 'name':'김영희'}]
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sign(request):
    return render(request, 'signup_in.html')


def signupimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    age = int(request.POST['age'])
    height = float(request.POST['ht'])
    weight = int(request.POST['wt'])

    try:
        CustDB().insert(id, pwd, name, age, height, weight)
        return render(request, 'signupsuccess.html')
    except Exception as err:
        print('에러:', err)
        context = {'msg': ErrorCode.e01}
        return render(request, 'signupfail.html', context)



def signinimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']

    try:
        cust = CustDB().selectOne(id)
        if pwd == cust.getPwd():
            request.session['signininfo'] = {'id': cust.getId(), 'name': cust.getName()}
            print(request.session['signininfo'])
            next = 'home.html'
            context = None
        else:
            raise Exception
    except:
        next = 'signinfail.html'
        context = {'msg': ErrorCode.e02}

    return render(request, next, context)


def signout(request):
    if request.session['signininfo'] != None:
        del request.session['signininfo']
    return render(request, 'home.html')


def myinfo(request):
    id = request.session['signininfo']['id']
    cust = CustDB().selectOne(id)
    context = {'cust': cust}
    return render(request, 'myinfo.html', context)

def updateinfo(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    age = int(request.POST['age'])
    height = float(request.POST['ht'])
    weight = int(request.POST['wt'])
    size = request.POST['size']

    if size == 'None':    # 실제 사이즈 정보가 입력되지 않은 경우
        CustDB().update6(id, pwd, name, age, height, weight)
        return redirect('home')
    else:       # 실제 사이즈 정보가 입력된 경우
        CustDB().update7(id, pwd, name, age, height, weight, size)
        return redirect('home')


def deleteinfo(request):
    id = request.session['signininfo']['id']
    CustDB().delete(id)
    return redirect('home')


def recommend(request):
    id = request.session['signininfo']['id']
    cust = CustDB().selectOne(id)
    age = cust.getAge()
    height = cust.getHt()
    weight = cust.getWt()
    size = cust.getSize()   # Null인 경우 None으로 출력됨

    # 1. Right size가 있는 경우
    if size != None:
        links = LinkDB().selectOne(size)
        context = {
            'size': size,
            'msg': 'actual',
            'mf': links[0],
            'yoox': links[1]
        }

    # 2. Right size가 없는 경우
    # 분석내용이랑 연결해야 함
    else:
        size = Analysis().sizeRecomm(age, height, weight)
        # 해당 사이즈에 맞는 웹사이트 링크 가져오기
        links = LinkDB().selectOne(size)
        context = {
            'size': size,
            'msg': 'recommended',
            'mf': links[0],
            'yoox': links[1]
        }
    return render(request, 'findsize.html', context)

def explore(request):
    return render(request, 'explore.html')


def contact(request):
    return render(request, 'contact.html')

def contactimpl(request):
    if request.method == 'POST':
        name = request.POST['name']
        email_from = request.POST['email']
        sender = '"' + name + '"' + ' <' + email_from + '>'
        print(name, email_from, sender, type(sender))

        subject = request.POST['subject']
        message = request.POST['message']

        email_to = settings.EMAIL_HOST_USER
        email = EmailMessage(subject, message, to=[email_to], reply_to=[sender])
        email.send()
    return render(request, 'thanks.html')