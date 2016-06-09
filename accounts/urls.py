from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
    url(r'gracias/(?P<username>[\w]+)/$',views.gracias_view,name='accounts.gracias'),
    url(r'perfil/$', views.index_view, name='accounts.perfil'),
    url(r'^login/$', views.login_view, name='accounts.login'),
    url(r'^logout/$', views.logout_view, name='accounts.logout'),
    url(r'^$.', views.index_view),

]