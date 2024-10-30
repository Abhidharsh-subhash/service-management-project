from django.shortcuts import render, redirect
from .models import Users

# Create your views here.


def index(request):
    return render(request, 'index.html')


def loginpage(request):
    msg = request.GET.get("msg", "")
    return render(request, "loginpage.html", {"msg": msg})


def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Users.objects.get(email=email, password=password)
        except Users.DoesNotExist:
            return redirect('/loginpage?msg=Invalid Email or Password!')
        request.session['email'] = email
        request.session['id'] = user.id
        request.session['username'] = user.username
        return redirect('/homepage?msg=You are logged in successfully')


def homepage(request):
    msg = request.GET.get("msg", "")
    return render(request, "homepage.html", {'msg': msg})


def profilepage(request):
    msg = request.GET.get("msg", "")
    if request.session.get('email'):
        try:
            user_id = request.session.get('id')
            user_data = Users.objects.filter(id=user_id).first()
            return render(request, 'profile.html', {"msg": msg, 'data': user_data})
        except Users.DoesNotExist:
            return redirect('/loginpage?msg=Login again!')
    return redirect('/loginpage?msg=Something went wrong, try again!')


def logout(request):
    try:
        del request.session['email']
        del request.session['full_name']
        del request.session['id']
        return redirect('/loginpage?msg=You are logged out successfully!')
    except:
        return redirect('/loginpage?msg=You are logged out successfully!')


def update_profile(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        Users.objects.filter(id=request.session.get('id')).update(
            username=username, email=email)
        return redirect('/profilepage?msg=Profile updated successfully')


def signuppage(request):
    msg = request.GET.get("msg", "")
    return render(request, 'signup.html', {"msg": msg})


def signup(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if Users.objects.filter(email=email).exists():
            return redirect('/signuppage?msg=Email already exists!')
        Users.objects.create(username=username, email=email, password=password)
        return redirect('/loginpage?msg=You are registered successfully!')
    return redirect('/signuppage?msg=Something went wrong, Please try again!')


def feedbackpage(request):
    msg = request.GET.get("msg", "")
    return render(request, 'feedback.html', {"msg": msg})


def forgotpasswordpage(request):
    msg = request.GET.get("msg", "")
    return render(request, 'forgotpassword.html', {"msg": msg})


def verify_email(request):
    if request.POST:
        email = request.POST['email']
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return redirect('/forgotpasswordpage?msg=Email does not exist!')
        return render(request, 'setpasswordpage.html', {'data': user})


def setpasswordpage(request):
    msg = request.GET.get("msg", "")
    return render(request, 'setpassword.html', {"msg": msg})


def setpassword(request):
    if request.POST:
        id = request.POST['user']
        password = request.POST['password']
        try:
            user = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return redirect('/forgotpasswordpage?msg=Something went wrong!')
        user.password = password
        user.save()
        return redirect('/loginpage?msg=Password changed successfully!')
