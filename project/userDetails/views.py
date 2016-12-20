from django.shortcuts import render
from .models import UserDetail, UserAddress


def home(request):
    """
    view function for home page. Functionality :
    1. if method is post, it saves name, email, mobile_number in UserDetail model and print acknowldgement on home page
    2. if method is get, it opens home.html showing the form

    """
    if request.method == "POST":

        # retrieving data from form
        name = request.POST.get("myName")
        address = request.POST.get("myAddress")
        email = request.POST.get("myEmail")
        mobile_number = request.POST.get("myMobileNumber")

        # saving name, email and mobile_number in UserDetail model
        userdetail = UserDetail(name=name, email_id=email, mobile_number=mobile_number)
        userdetail.save()

        # saving address in UserAddress model
        useraddress = UserAddress(address=address)
        useraddress.save()

        context = {
            "method": "post"
        }

    else:
        context = {
            "method": "get"
        }

    return render(request, "home.html", context)
