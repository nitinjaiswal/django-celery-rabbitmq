from django.shortcuts import render
from .tasks import saveindb


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

        saveindb(name, email, mobile_number, address)

        context = {
            "method": "post"
        }

    else:
        context = {
            "method": "get"
        }

    return render(request, "home.html", context)
