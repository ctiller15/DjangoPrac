from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	# this leads to /polls/
	url(r'^$', views.index, name='index'),
	# this leads to polls/(int)/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# this leads to the polls results page
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# this leads to the polls vote page
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]