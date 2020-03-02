from django.conf.urls import url
from registerApp import views
# SET THE NAMESPACE!
app_name = 'registerApp'

urlpatterns = [
	url(r'^register/$',views.register,name='register'),
	url(r'^user_login/$',views.user_login,name='user_login'),
]