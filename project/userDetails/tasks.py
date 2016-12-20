from __future__ import absolute_import, unicode_literals
from celery import Celery
from .models import UserDetail, UserAddress


app = Celery('tasks', backend='amqp', broker='pyamqp://guest@localhost//')

app.conf.task_serializer = 'json'
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
    result_expires=60,
    task_acks_late=True,
    broker_url='pyamqp://',

)


@app.task
def saveindb(name, email, mobile_number, address):
    """

    :param name: stores user name entered in the form
    :param email: stores user email id entered in the form
    :param mobile_number: stores user mobile number entered in the form
    :param address: stores user address entered in the form

    This function saves user details asynchronously in UserDetail and UserAddress Model
    """
    # saving name, email and mobile_number in UserDetail model
    userdetail = UserDetail(name=name, email_id=email, mobile_number=mobile_number)
    userdetail.save()

    # saving address in UserAddress model
    useraddress = UserAddress(address=address)
    useraddress.save()


