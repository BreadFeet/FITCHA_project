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
    if 'size' in request.session.keys():
        del request.session['size']
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
    size = request.POST.get('size')    # POST['size']: size를 입력하지 않은 경우 값이 없어서 오류난다
    print(size)    # size 입력하지 않은 경우: None

    if size == None:    # 실제 사이즈 정보가 입력되지 않은 경우
        size = 'NULL'
    else:
        size = "'{}'".format(size)
    print(size)

    CustDB().update(id, pwd, name, age, height, weight, size)
    return redirect('home')


def deleteinfo(request):
    # id를 데이터베이스에서 지우기
    id = request.session['signininfo']['id']
    CustDB().delete(id)
    # 로그인 정보(session)도 지우기
    signout(request)
    return redirect('home')


def recommend(request):
    # 로그인 정보가 있는 경우
    if 'signininfo' in request.session.keys():       # request.session['signininfo'] != None: 애초에 signininfo라는 키가 없는 경우 이렇게 불러오면 오류남
        id = request.session['signininfo']['id']
        cust = CustDB().selectOne(id)
        age = cust.getAge()
        height = cust.getHt()
        weight = cust.getWt()
        size = cust.getSize()   # Null인 경우 None으로 출력됨

        # 1. Right size가 있는 경우
        if size != None:
            # 해당 사이즈에 맞는 웹사이트 링크 가져오기
            links = LinkDB().selectOne(size)
            context = {
                'msg': 'actual',
                'size': size,
                'mf': links[0],
                'yoox': links[1],
                'mt': links[2],
                'net': links[3]
            }

        # 2. Right size가 없는 경우 - 분석내용이랑 연결해야 함
        else:
            size = Analysis().sizeRecomm(age, height, weight)
            links = LinkDB().selectOne(size)
            context = {
                'msg': 'recommended',
                'size': size,
                'mf': links[0],
                'yoox': links[1],
                'mt': links[2],
                'net': links[3]
            }

            request.session['size'] = size   # 추천 size 정보를 어디서나 불러올 수 있도록 session에 저장
            # print(request.session.keys())
            # print(request.session.items())

        return render(request, 'findsize.html', context)

    # 로그인 정보가 없는 경우
    else:
        context = {'msg': ErrorCode.e03}
        return render(request, 'signinrequest.html', context)


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