from django.contrib import admin
from django.urls import include, path
from TastyCakes.views import signup
from TastyCakes.views import index
from TastyCakes.views import normal_cake
from TastyCakes.views import eggless
from TastyCakes.views import contact
from TastyCakes.views import birth
from TastyCakes.views import anniversary
from TastyCakes.views import design
from TastyCakes.views import trend
from TastyCakes.views import photo
from TastyCakes.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('TastyCakes', include('TastyCakes.urls')),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('index/', index, name='index'),
    path('normal_cake/', normal_cake, name='normal_cake'),
    path('eggless/', eggless, name='eggless'),
    path('contact/', contact, name='contact'),
    path('birth/', birth, name='birth'),
    path('anniversary/', anniversary, name='anniversary'),
    path('design/', design, name='design'),
    path('trend/', trend, name='trend'),
    path('photo/', photo, name='phot0'),
    path('passion/', passion, name='passion'),
    path('cartoon/', cartoon, name='cartoon'),
    path('filmy/', filmy, name='filmy'),
    path('chocolate/', chocolate, name='chocolate'),
    path('venilla/', venilla, name='venilla'),
    path('black_cur/', black_cur, name='black_cur'),
    path('pine/', pine, name='pine'),
    path('red/', red, name='red'),
    path('blue/', blue, name='blue'),
    path('order/', order, name='order'),
    path('login/', login, name='login'),
    
    path('SignInSuccess/', SignInSuccess, name='SignInSuccess'),
    path('SignUnSuccess/', SignUnSuccess, name='SignUnSuccess'),
    path('', welcome, name='welcome'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
