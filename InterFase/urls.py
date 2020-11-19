from django.conf.urls import url
from User import user_Views
from project import projectViews,moduleViews,caseViews

urlpatterns = [
    url(r'^register/', user_Views.registerHtml),
    url(r'^registerapi/', user_Views.CreateUser),
    url(r'^login/', user_Views.Login),
    url(r'^logout/', user_Views.logout),
    url(r'^index/', user_Views.Index),
    url(r'^resetpwd/', user_Views.resetPwd),
    url(r'^retrievePassword/', user_Views.retrievePassword),

    url(r'^createProject/', projectViews.createProject),
    url(r'^project/', projectViews.projectAll),
    url(r'^projectById/', projectViews.projectById),
    url(r'^deleteProject/', projectViews.deleteProject),
    url(r'^queryProjectToName/', projectViews.queryProjectToName),
    url(r'^updateProject/', projectViews.updateProject),


    url(r'^module/', moduleViews.modulehtml),
    url(r'^basicInformation/', moduleViews.basicInformation),
    url(r'^queryModuleToName/', moduleViews.queryModuleToName),
    url(r'^moduleAll/', moduleViews.moduleAll),
    url(r'^createModule/', moduleViews.createModule),
    url(r'^deleteModule/', moduleViews.deleteModule),


    url(r'^case/', caseViews.casehtml),
    url(r'^createCase/', caseViews.createCase),
    url(r'^caseAll/', caseViews.caseAll),
    url(r'^deleteCase/', caseViews.deleteCase),
]
