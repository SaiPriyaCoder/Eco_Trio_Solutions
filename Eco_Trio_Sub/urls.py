from django.urls import path
from django.shortcuts import redirect
from .views import home_view, agri_services_view, signup_view, signin_view,send_otp,logout_view,register_view,submit_form,global_view, digital_grow, team_view,contact_view,collab_view,apply_view,subscribe_view  # Import your views here
 # Make sure to import your actual view function
urlpatterns = [
    # path('', lambda request: redirect('home')),  # 👈 Redirect root to /home
    path('home/', home_view, name='home'),
    #path('send-otp/', send_otp, name='send_otp'),
    path('register/',register_view, name='register'),  # ✅ Use the function, not a string
    path('send-otp-email/', send_otp, name='send_otp_email'),
    path('submit/', submit_form, name='submit_form'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path("logout/", logout_view, name="logout"),
    path('agri_services/', agri_services_view, name='agri_services'),  # ✅ Add the new view
    path('go_global/', global_view, name='go_global'),  # ✅ Add the new view
    path('digital_grow/', digital_grow, name='dital_grow'),  # ✅ Add the new view
    path('team/', team_view, name='team'),  # ✅ Add the new view
    path('contact/',contact_view,name='contact'),
    path('collab/', collab_view, name='collab'),  # ✅ Add the new view
    # path('careers/', careers_view, name='careers'),
    path('apply/<int:job_id>/', apply_view, name='apply_job'),
    path('subscribe/', subscribe_view, name='subscribe'),

]
