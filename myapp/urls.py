from django.urls import path
from . import views
from myapp.views import custom_logout
urlpatterns =[
    path('',views.landing_page),
    path('signup',views.signup),
    path('register',views.register),
    path('logout',views.logout),
    path('login',views.login),
    path('after_login',views.login_check),
    path('booking',views.booking),
    path('booking_confirm',views.booking_confirm),
    path('view-bookings',views.view_bookings),
    path('track-bookings',views.track_bookings),
    path('generate_pdf/<str:tracking_id>/<str:sender_name>/<str:receiver_name>/<str:pickup_address>/<str:delivery_address>/<str:package_description>/', views.generate_pdf, name='generate_pdf'),
    path('custom_logout/', custom_logout, name='custom_logout'),
    path('verify_otp', views.verify_otp, name='verify_otp'),
    path('Forgotpwd',views.forgot_password),
    path('forgotpwd_verify',views.forgot_verify),
    path('verify_otp_forgot',views.verify_otp_forgot),
    path('changepwd',views.change_password)

]



