```bash
pip install virtualenv
mkdir projects
cd projects
mkdir helloapp
virtualenv -p python env
source env/Scripts/activate
pip install django

# create a skeletop project
django-admin startproject helloapp

# create an app
python manage.py startapp howdy

# helloapp
# ├── helloapp
# │        ├── __init__.py
# │        ├── settings.py
# │        ├── urls.py
# │        └── wsgi.py
# ├── howdy
# │        ├── __init__.py
# │        ├── admin.py
# │        ├── apps.py
# │        ├── migrations
# │        ├── models.py
# │        ├── tests.py
# │        └── views.py
# └── manage.py

# Sync your database for the first time
python manage.py migrate

```
We should add the app name (`howdy`) to the Installed Apps list in settings.py file so it gets recognized.  

Edit the `helloapp/urls.py` to include urls.py from howdy app:
```python
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('howdy.urls')),
]
```
create the `howdy/urls.py`:
```python
from django.conf.urls import url
from howdy import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('about/', views.AboutPageView.as_view()),
]
```
create `howdy/views.py`
```python
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# differne way of defining view:
class AboutPageView(TemplateView):
    template_name = "about.html"
```
create a folder `howdy/templates` and create two files `index.html` and `about.html` in it.  
run the server:
```bash
python manage.py runserver
```
Browse http://127.0.0.1:8000/

