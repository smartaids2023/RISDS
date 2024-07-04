from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('index.html/', views.index, name='index_html'),
    path('index.html/index.html', views.index_html, name='nested_index_html'),
    path('index.html/quote.html', views.quote_html, name='quote_html'),
    path('index.html/contact.html', views.contact_html, name='contact_html'),
    path('index.html/about.html', views.about_html, name='about_html'),
    path('index.html/service.html', views.service_html, name='service_html'),
    path('index.html/trainings.html', views.trainings_html, name='trainings_html'),
    path('index.html/quote.html', views.quote_html, name='quote_html'),
    path('index.html/team.html', views.team_html, name='team_html'),
    path('index.html/careers.html', views.careers_html, name='careers_html'),
    path('index.html/feature.html', views.feature_html, name='feature_html'),
    path('index.html/detail.html', views.detail_html, name='detail_html'),
    path('index.html/blog.html', views.blog_html, name='blog_html'),
    path('index.html/privacy.html', views.privacy_html, name='privacy_html'),
    path('index.html/terms.html', views.terms_html, name='terms_html'),
    path('index.html/technology.html', views.technology_html, name='technology_html'),
    path('index.html/innovative.html', views.innovative_html, name='innovative_html'),
    path('index.html/userexp.html', views.userexp_html, name='userexp_html'),
    path('index.html/leveraging.html', views.leveraging_html, name='leveraging_html'),
    path('index.html/applications.html', views.applications_html, name='applications_html'),
    path('index.html/ai.html', views.ai_html, name='ai_html'),
    path('index.html/integration.html', views.integration_html, name='integration_html'),
    path('index.html/cookie_policy.html', views.cookie_policy_html, name='cookie_policy_html'),
    path('index.html/developments.html', views.developments_html, name='developments_html'),
    
    path('about/', views.about, name='about'),
    path('about.html', views.about, name='about_html'),
    path('service/', views.service, name='service'),
    path('service.html', views.service, name='service_html'),
    path('blog/', views.blog, name='blog'),
    path('blog.html', views.blog, name='blog_html'),
    path('detail/', views.detail, name='detail'),
    path('detail.html', views.detail, name='detail_html'),
    path('contact/', views.contact, name='contact'),
    path('contact.html', views.contact, name='contact_html'),
    path('feature/', views.feature, name='feature'),
    path('feature.html', views.feature, name='feature_html'),
    path('careers/', views.careers, name='careers'),
    path('careers.html', views.careers, name='careers_html'),
    path('quote/', views.quote, name='quote'),
    path('quote.html', views.quote, name='quote_html'),
    path('team/', views.team, name='team'),
    path('team.html', views.team, name='team_html'),
    path('trainings/', views.trainings, name='trainings'),
    path('trainings.html', views.trainings, name='trainings_html'),
    path('privacy/', views.privacy, name='privacy'),
    path('privacy.html', views.privacy, name='privacy_html'),
    path('terms/', views.terms, name='terms'),
    path('terms.html', views.terms, name='terms_html'),
    path('technology/', views.technology, name='technology'),
    path('technology.html', views.technology, name='technology_html'),
    path('innovative/', views.innovative, name='innovative'),
    path('innovative.html', views.innovative, name='innovative_html'),
    path('userexp/', views.userexp, name='userexp'),
    path('userexp.html', views.userexp, name='userexp_html'),
    path('leveraging/', views.leveraging, name='leveraging'),
    path('leveraging.html', views.leveraging, name='leveraging_html'),
    path('applications/', views.applications, name='applications'),
    path('applications.html', views.applications, name='applications_html'),
    path('ai/', views.ai, name='ai'),
    path('ai.html', views.ai, name='ai_html'),
    path('integration/', views.integration, name='integration'),
    path('integration.html', views.integration, name='integration_html'),
    path('cookie_policy/', views.cookie_policy, name='cookie_policy'),
    path('cookie_policy.html', views.cookie_policy, name='cookie_policy_html'),
    path('developments/', views.developments, name='developments'),
    path('developments.html', views.developments, name='developments_html'),
    

]

# from django.urls import path
# from .views import check_firebase_connection

# urlpatterns = [
#     # Your other URL patterns here

#     # Add a URL pattern for checking Firebase connection
#     path('', check_firebase_connection, name='check_firebase_connection'),
# ]


# from django.urls import path
# from .views import read_data_from_firebase

# urlpatterns = [
#     # Your other URL patterns here

#     path('', read_data_from_firebase, name='read_data_from_firebase'),
# ]
