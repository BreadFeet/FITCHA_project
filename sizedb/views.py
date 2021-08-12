from django.shortcuts import render, redirect

# Create your views here.
from frame.custdb import CustDB
from frame.error import ErrorCode


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def loginimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    print(request.session)

    try:
        cust = CustDB().selectOne(id)
        if pwd == cust.getPwd():
            request.session['logininfo'] = {'id': cust.getId(), 'name': cust.getName()}
            print(request.session['logininfo'])
            next = 'index.html'
            context = None
        else:
            raise Exception
    except:
        next = 'loginfail.html'
        context = {'msg': ErrorCode.e02}

    return render(request, next, context)


def signup(request):
    return render(request, 'signup.html')

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
        print(err)
        context = {'msg': ErrorCode.e01}
        return render(request, 'signupfail.html', context)


def recommend(request):
    id = request.session['logininfo']['id']
    cust = CustDB().selectOne(id)
    age = cust.getAge()
    weight = cust.getWt()
    height = cust.getHt()
    # 분석화면이랑 연결해야 함
    return render(request, 'recommend.html')
