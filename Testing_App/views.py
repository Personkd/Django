from django.shortcuts import render, redirect
from .forms import Registration,Login,PostForm,Comments,UpdateProfile
from  django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Posts,Comments,User
from django.views.generic.base import TemplateView
from render_block import render_block_to_string
from django.http import JsonResponse, HttpResponse
import datetime

#Головна сторінка з постами
class HomePage(TemplateView):
        template_name="home.html"
        def post(self,request):
            data = request.POST
            print(data)
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["posts"] = Posts.objects.all()
            return context

#def usersreg (request):
    #if request.method == 'POST':
        #form = User(request.POST)
        #if form.is_valid():
            #name = form.cleaned_data['name']
            #password = form.cleaned_data['password']
            #age = form.cleaned_data['age']
            #print (name,password,age)
    #else:
        #return render(request, 'Userform.html', {"form":User()})

#Стара реєстрація
#def register (request):
   # if request.method == 'POST':
        #form = Registration(request.POST)
        #if form.is_valid():
           #name = form.cleaned_data['username']
           #email = form.cleaned_data['email']
           # password = form.cleaned_data['password1']
            #user= User.objects.create_user(username=name,email=email,password=password)
            #user.save()
           # return redirect("/")
       # else:
      #      print(form.errors.as_data())
   # else:
       # return render(request, 'Reg.html', {"form":Registration()})

#Реєстрація
class RegistrationPage(CreateView):
    template_name = "Reg.html"
    #model = User
    #fields = ["username","email","password1","password2"]
    form_class = Registration
    success_url = reverse_lazy("home")
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["user"]=self.request.user
        return context

#Старий логін
def logining (request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=name,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                return redirect("/login")
    else:
        return render(request, 'Login.html', {"form":Login()})

#Старе створення поста
@login_required
def createpost (request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            post= Posts(text=text, added_at=datetime.datetime.now(),user=request.user)
            post.save()
            return redirect("/")
    else:
        return render(request, 'Postcreate.html', {"form":PostForm()})

#Старе оновлення поста
#@login_required
#def post(request,**kwargs):
    #certainpost = Posts.objects.get(id=kwargs["id"])
    #certainuser=certainpost.user
    #certaintime=certainpost.added_at
    #certaintext=certainpost.text
    #if request.method == 'POST':
        #change=Changepost(request.POST)
        #if change.is_valid():
            #new_text=change.cleaned_data["new_text"]
            #Posts.objects.filter(id = kwargs["id"]).update(text=new_text)
            #return redirect("/")
    #return render(request, 'Post.html', {"text":certaintext,"user":certainuser,"time":certaintime,"form":Changepost()})

#Старе оновлення поста
class  PostFormPage(TemplateView):
    template_name="Post.html"
    form_class=PostForm
    model=Posts
    def get_success_url(self):
        return f'/'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["post"]=Posts.objects.get(id=self.kwargs["pk"])
        context["comments"]=Comments.objects.filter(post=Posts.objects.get(id=self.kwargs["pk"]))
        return context


#Створення коментарів
class  CommentPage(TemplateView):
    template_name="Post.html"
    def  post(self,request,**kwargs):
        data=request.POST
        user=User.objects.get(id=self.kwargs["pk"])
        post=Posts.objects.get(id=self.kwargs["pk"])
        text = data.get('text')
        comment = Comments(text=text, added_at=datetime.datetime.now(), user=user, post=post)
        comment.save()
        response = render_block_to_string("Post.html","comments", {"comments" : Comments.objects.filter(post=post)})
        return HttpResponse(response)

#Оновлення поста
class  UpdatePostPage(TemplateView):
    template_name="Post.html"
    def  post(self,request,**kwargs):
        data=request.POST
        new_text=data.get("post")
        post =  Posts.objects.filter(id=kwargs["pk"])
        post.update(text=new_text)
        response = render_block_to_string("Post.html","text",{"post":post.first()})
        return HttpResponse(response)

#сторінка профілю та його оновлення
class  UpdateProfile(UpdateView):
    template_name="Profile.html"
    form_class=UpdateProfile
    model=User
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["username"]=User.objects.get(id=self.kwargs["pk"])
        context["posts"]=Posts.objects.filter(user=User.objects.get(id=self.kwargs["pk"]))
        return context
    def get_initial(self):
        user=self.request.user
        return {"username":user.username,"email":user.email,"bio":user.bio,"picture":user.profile_photo}
    def get_success_url(self):
        return f'/profile/{self.kwargs["pk"]}'

#Логаут
def loggingout(request):
    logout(request)
    return redirect("/")

def JStest (request):
       return render(request, "jstest.html")


def JStesting(request):
    return render(request, "jstest1.html")

class ajaxtestpage(TemplateView):
    template_name = 'ajaxtestpage.html'

    def post(self,request):
        print(request.POST)
        return JsonResponse({'status': 'Ви успішно ввели дані'})


