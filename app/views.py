from django.shortcuts import render, redirect
from .models import Users, category, Staffs, Tickets, Feedback, Emergency_support

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
    categories = category.objects.all()
    return render(request, "homepage.html", {'msg': msg, 'categories': categories})


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


def ticket(request):
    msg = request.GET.get("msg", "")
    return render(request, 'ticket.html', {'msg': msg})


def raise_ticket(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        issue = request.POST['issue']
        user = Users.objects.get(id=request.session.get('id'))
        Tickets.objects.create(
            user=user, name=name, email=email, phone_number=phone_number, issue=issue)
        return redirect('/ticket?msg=Ticket raised successfully')
    return redirect('/ticket?msg=something wenr wrong! Please try again')


def ticketspage(request):
    user = Users.objects.get(id=request.session.get('id'))
    tickets = Tickets.objects.filter(user=user)
    return render(request, 'ticketspage.html', {'tickets': tickets})


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
    user = Users.objects.get(id=request.session.get('id'))
    tickets = Tickets.objects.filter(user=user)
    return render(request, 'feedbackpage.html', {"msg": msg, 'tickets': tickets})


def submit_feedback(request):
    if request.POST:
        ticket_id = request.POST['ticket']
        rating = request.POST['rating']
        comment = request.POST['comment']
        ticket = Tickets.objects.get(id=ticket_id)
        if Feedback.objects.filter(ticket=ticket).exists():
            return redirect('/feedbackpage?msg=Feedback for the ticket is already submitted')
        Feedback.objects.create(ticket=ticket, rating=rating, comment=comment)
        return redirect('/feedbackpage?msg=Feedback submitted successfully')
    return redirect('/feedbackpage?msg=Something went wrong! Try again')


def forgotpasswordpage(request):
    msg = request.GET.get("msg", "")
    return render(request, 'forgotpassword.html', {"msg": msg})


def emergencysupport(request):
    msg = request.GET.get("msg", "")
    return render(request, 'emergencysupport.html', {'msg': msg})


def submit_emergency(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        issue = request.POST['issue']
        user = Users.objects.get(id=request.session.get('id'))
        Emergency_support.objects.create(
            user=user, name=name, email=email, phone_number=phone_number, description=issue)
        return redirect('/emergencysupport?msg=Emergency reported successfully')
    return redirect('/emergencysupport?msg=Something went wrong. Please try again')


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
