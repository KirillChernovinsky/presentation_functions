from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewsForm, UserForm, CommentForm
from .models import News, Comment, Person


class GetNews(ListView):
    model = News
    template_name = 'zadanie/main.html'
    context_object_name = 'posts'


class GetDetail(DetailView):
    model = News
    template_name = 'zadanie/post_list.html'


class CreateNews(CreateView):
    model = News
    fields = '__all__'
    template_name = 'zadanie/create.html'
    success_url = '/zadanie'


class CreatePerson(CreateView):
    model = Person
    fields = '__all__'
    template_name = 'zadanie/create.html'
    success_url = '/zadanie'


class CreateComment(CreateView):
    model = Comment
    fields = '__all__'
    template_name = 'zadanie/create.html'
    success_url = '/zadanie'


class UpdateNews(UpdateView):
    model = News
    fields = '__all__'
    template_name = 'zadanie/create.html'
    success_url = '/zadanie'



#Как удалять ?????
class DeletePost(DeleteView):
    model = News
    template_name = 'zadanie/main.html'
    success_url = 'zadanie/main.html'








# def makeMen():
#     p, try5lekuihr5jou = Person.objects.get_or_create(name='Tomeygdtrhj', surname='Tvhgfnhfsv', age=18, gender=True, birthDay='2011-12-12')
#     p, _ = Person.objects.get_or_create(name='Tom1', surname='fgv', age=28, gender=True, birthDay='2011-12-12')
#     p, _ = Person.objects.get_or_create(name='Tom2', surname='Tvhfjmdsv', age=38, gender=True, birthDay='2011-02-02')
#     p, _ = Person.objects.get_or_create(name='Tom3', surname='Tvhhmsv', age=19, gender=True, birthDay='2011-05-12')
#     p, _ = Person.objects.get_or_create(name='Tom4', surname='Tvhhfmnjsv', age=25, gender=True, birthDay='2011-12-05')
#

#
#
# def create(request):
#     if request.method == "POST":
#         form = AddForm(request.POST)
#         if form.is_valid():
#             post_name = form.cleaned_data['post_name']
#             post_description = form.cleaned_data['post_description']
#             post_img = form.cleaned_data['post_img']
#             men, _ = News.objects.get_or_create(post_img=post_img,post_name=post_name,post_description=post_description)
#
#             return redirect('home')
#         else:
#             form = AddForm()
#             return render(request, 'zadanie/create.html', context={'form': form})
#     else:
#         form = AddForm()
#         return render(request, 'zadanie/create.html', context={'form': form})
#
#
# def update(request, id):
#     try:
#         men = News.objects.get(id=id)
#         if request.method == "POST":
#             men.post_name = request.POST.get('post_name')
#             men.post_description = request.POST.get('post_description')
#             men.post_img = request.POST.get('post_img')
#             men.popular = request.POST.get('popular')
#             men.save()
#             return redirect('home')
#         else:
#             return render(request, 'zadanie/update.html', context={'men': men})
#     except:
#         return redirect('create')
#
#
#
# def comm(request, id):
#     try:
#         men = Comment.objects.get(id=id)
#         if request.method == "POST":
#             men.Comment = request.POST.get('Comment')
#             men.save()
#             return redirect('home')
#         else:
#             men = Comment.objects.get(id=id)
#             men, _ = Comment.objects.get_or_create()
#             return redirect('home', context={'men':men})
#     except:
#         return redirect('create')
#
#
# def delete(request, id):
#     try:
#         men = News.objects.get(id=id)
#         men.delete()
#         return redirect('home')
#     except:
#         return redirect('create')
#
#
#
# def popular(request, id):
#
#     men = News.objects.get(id=id)
#
#     men, _ = News.objects.get_or_create(post_img=post_img, post_name=post_name, post_description=post_description)
#
#     return redirect('home')
#
#
#
#
#
#
# # Выводит даже не списком, а переменными Queryset вообще нет
# def popular_posts(request):
#     men = News.objects.get(popular="ДА")
#     print(men)
#     post_img = men.post_img
#     post_name = men.post_name
#     post_description = men.post_description
#     popular = men.popular
#     men, _ = News.objects.get_or_create(post_img=post_img,post_name=post_name,post_description=post_description)
#     return render(request, 'zadanie/popular_posts.html', context={'men': men})
#
# def lastpost(request):
#     # Получаем последний пост
#     latest_post = News.objects.latest('id')
#
#     post_img = latest_post.post_img
#     post_name = latest_post.post_name
#     post_description = latest_post.post_description
#     men, _ = News.objects.get_or_create(post_img=post_img,post_name=post_name,post_description=post_description)
#     return render(request, 'zadanie/popular_posts.html', context={'men': men})
#
#
#
#
#
#
#
#
#
#
#
#
# peoples = []
#
#
# def registr(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             men, _ = Person.objects.get_or_create(email=email)
#
#             # if email == 'User1@y.1' and password == '12345678':
#             return render(request, 'ZADANIE/beforeentrance.html', context={"men": men})
#
#             # else:
#             #     HttpResponse('отказано в доступе')
#         else:
#             HttpResponse('Данные не валидны')
#     else:
#         form = UserForm()
#         # form2 = UserForm2
#         return render(request, 'ZADANIE/ZADANIE.html', context={'form': form})
#
#
# def vhod(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             men, _ = Person.objects.get_or_create(email=email)
#
#             #проверка не работает Почему?
#             if men.password == "admin" and men.email == 'admin@yandex.ru':
#                 return render(request, 'ZADANIE/admin.html')
#             else:
#                 return render(request, 'ZADANIE/beforeentrance.html', context={"men": men})
#             # men, _ = News.objects.get_or_create(name=name, email=email,
#             #                                     )
#             # return render(request, 'ZADANIE/beforeregistr.html', context={'men':men})
#         else:
#             HttpResponse('Данные не валидны')
#     else:
#         form = UserForm()
#         # form2 = UserForm2
#         return render(request, 'ZADANIE/vhod.html', context={'form': form})
#
#     # news = News.objects.all()
#     # post_name = request.POST.get('post_name')
#     # post_description = request.POST.get('post_description')
#     # post_img = request.POST.get('post_img')
#     # print(post_img)
#     # popular = request.POST.get('popular')
#     # print(popular)
#     # if post_name and post_description and post_img and popular == 'ДА':
#     #     post = News.objects.filter(
#     #
#     #         post_name=post_name,
#     #         post_description=post_description,
#     #         post_img=post_img,
#     #         popular="ДА",
#     #     )
#     #     if post.exists():
#     #         return redirect('popular_posts')
#     #
#     #
#     # all_records = News.objects.all()
#     # for record in all_records:
#     #     if record.popular == "ДА":
#     #         post_name = request.POST.get('post_name')
#     #         post_description = request.POST.get('post_description')
#     #         post_img = request.POST.get('post_img')
#     #         popular = request.POST.get('popular')
#     #         if post_name and post_description and post_img and popular == 'ДА':
#     #             post = News.objects.filter(
#     #
#     #                 post_name=post_name,
#     #                 post_description=post_description,
#     #                 post_img=post_img,
#     #                 popular="ДА",
#     #             )
#     #             if post.exists():
#     #                 return redirect('popular_posts')
#     #             else:
#     #                 pass
#     #         else:
#     #             pass
#     #     else:
#     #         return redirect("home")
