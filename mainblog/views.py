from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Articles, Comments, ProductsBorsch
from .forms import CommentForm, CreateArticleForm, UpdateArticleForm, BorschForm, UpdateBorschForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template import Context, Template
from random import randint
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.db import models
from django.contrib.auth.decorators import login_required


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


def createarticle(request):
    error = ''
    author = request.user

    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        instance = form.save(commit=False)
        if form.is_valid():
            instance.author = author
            instance.save()
            return redirect('home')
        else:
            error = 'Invalid Form'

    form = CreateArticleForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'mainblog/create_article.html', data)


# class CreateArticle(LoginRequiredMixin, CreateView):
#     model = Articles
#     template_name = 'mainblog/create_article.html'
#
#     fields = ['title', 'img', 'text', 'contentimg']
#
#     def get_context_data(self, **kwargs):
#         ctx = super(CreateArticle, self).get_context_data(**kwargs)
#         ctx['title'] = 'Добавление статьи'
#         ctx['btn_text'] = 'Добавить статью'
#         return ctx
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


class UpdateArticle(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    form_class = UpdateArticleForm
    template_name = 'mainblog/create_article.html'

    # fields = ['title', 'img', 'text']

    def test_func(self):
        articles = self.get_object()
        if self.request.user == articles.author:
            return True

        return False

    def get_context_data(self, **kwargs):
        ctx = super(UpdateArticle, self).get_context_data(**kwargs)
        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteArticle(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    success_url = '/'
    template_name = 'mainblog/delete_article.html'

    def test_func(self):
        articles = self.get_object()
        if self.request.user == articles.author:
            return True

        return False


class AllArticles(ListView):
    model = Articles
    template_name = 'mainblog/home.html'
    context_object_name = 'articles'
    ordering = ['-date']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        ctx = super(AllArticles, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        ctx['last_post'] = Articles.objects.latest('date')
        ctx['rand_post'] = Articles.objects.all()[
            randint((Articles.objects.count() // 2) + 1, Articles.objects.count() - 2)]
        ctx['rand_post_2'] = Articles.objects.all()[randint(0, (Articles.objects.count() // 2))]
        ctx['default_image'] = 'default_article_pixel.jpg'
        ctx['goviadina'] = 90
        ctx['kapusta'] = 65
        ctx['svekla'] = 90
        ctx['kartoshka'] = 90
        ctx['morkov'] = 25
        ctx['luk'] = 45
        ctx['tomaty'] = 25
        ctx['perec'] = 3
        ctx['sol'] = 1
        ctx['smetana'] = 15
        ctx['borsch'] = ProductsBorsch.objects.order_by('-grammovka')

        return ctx


class UserAllArticles(ListView):
    model = Articles
    template_name = 'mainblog/user_articles.html'
    context_object_name = 'articles'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Articles.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(UserAllArticles, self).get_context_data(**kwargs)
        ctx['title'] = f'Статьи пользователя {self.kwargs["username"]}'

        return ctx


class ArticleDetail(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Articles
    template_name = 'mainblog/article_detail.html'
    context_object_name = 'get_article'
    form_class = CommentForm
    success_msg = 'Ваш комментарий отправлен на модерацию. Он будет опубликован сразу после проверки'

    def get_context_data(self, *args, **kwargs):
        ctx = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        ctx['comments_articles'] = self.get_object().comments_articles.all()
        ctx['title'] = Articles.objects.get(pk=self.kwargs['pk'])
        ctx['default_image'] = 'default_article_pixel.jpg'

        return ctx

    def get_success_url(self, **kwargs):
        return reverse_lazy('article_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def update_comment_status(request, pk, type):
    comment = Comments.objects.get(pk=pk)
    administrator = User.objects.get(username='admin')

    if request.user == comment.article.author or request.user == administrator:

        if type == 'public':
            comment.active = True
            comment.save()
            template = Template('''
                    <div class="comments__control">
                        <p>Комментарий опубликован</p>
                        <a class="button comments__button_reject" title="Удалить" data-url="{% url 'update_comment_status' comment.id 'delete' %}" href="#">Удалить</a>
                    </div>
            ''')
            context = Context({'comment': comment})
            return HttpResponse(template.render(context))

        elif type == 'delete':
            comment.delete()
            return HttpResponse('''
                <div class="comments__control">
                    <p>Комментарий был успешно удалён</p>
                </div>
            ''')

    else:
        return HttpResponse('''
            <div class="delcomm_bad">
                deny
            </div>
        ''')

    return HttpResponse('1')


def contacts(request):
    people = [
        {
            'name': 'Дмитрий',
            'role': 'Тех. разработка',
            # 'email': 'tech@vlblog.com',
        },
        {
            'name': 'Владислав',
            'role': 'Автор публикаций',
            'email': 'author@vlblog.com',
        }
    ]

    info = [
        {
            'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis lorem vitae facilisis dapibus. Vestibulum eu nibh quis libero iaculis posuere et sit amet dui. Sed accumsan elementum turpis, in sodales dui semper eu. Etiam consectetur nisl eget lectus porttitor tincidunt eu a magna. Suspendisse ornare elementum nisi, a sodales nisl blandit at. Etiam sit amet tristique justo. In hac habitasse platea dictumst. Donec venenatis velit at nunc vestibulum gravida. Cras quis arcu ac mi porta pulvinar. Fusce ullamcorper mattis est et sollicitudin. Fusce posuere diam nec vehicula tincidunt. In lacinia sit amet leo nec commodo. Pellentesque sed sem ut nisl commodo sollicitudin et non erat. Duis eget pretium lorem, at auctor velit. Pellentesque non felis suscipit, congue felis non, aliquet turpis. Fusce placerat porta velit in placerat. Curabitur eu orci et tortor volutpat faucibus et nec ex. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed ac tortor nulla. Donec lacinia tellus tempus lorem sodales, in vulputate nulla bibendum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget erat posuere, semper neque ac, pulvinar nisi. In eget libero a mi ornare mollis. Curabitur vulputate metus sit amet egestas elementum. Fusce rhoncus porttitor imperdiet. Quisque sagittis condimentum risus, gravida euismod turpis tempus vitae. Nulla convallis metus auctor sodales bibendum.',
        }
    ]

    data = {
        'info': info,
        'people': people,
        'title': 'Наши контакты'
    }
    return render(request, 'mainblog/contacts.html', data)


def about(request):
    info = [
        {
            'text': 'ЭКО Борщ - сайт о повседневности, занудной жизни, рутине и о том куда же бедному '
                    'крестьянину податься!'
                    'Спросите, а почему ЭКО? Да потому что «ЭКО» с греческого переводится просто, '
                    'как дом, а в мире нет боле близких и более отдалённых наук друг от друга как '
                    'ЭКОномика и ЭКОлогия. Первая переводится как наука о ведении домашнего хозяйства, '
                    'а вторая просто наука о доме. Поскольку мы в России то и варимся мы в домашнем '
                    'Борще, где на злобу дня кроме обычных ингредиентов картошки, лука и свёклы будем '
                    'подкидывать крылья летучих мышей, хвосты крыс, яд гадюки и прочие прелести '
                    'повседневности. Одним словом, домашний борщ от Бабы Яги.',
        }
    ]

    data = {
        'info': info,
        'title': 'Наши контакты'
    }
    return render(request, 'mainblog/about.html', data)


def createProducts(request):
    error = ''
    products = ProductsBorsch.objects.all()
    if request.method == 'POST':
        form = BorschForm(request.POST)
        instance = form.save(commit=False)
        if form.is_valid():
            instance.save()
            return redirect('all_products')
        else:
            error = 'Invalid Form'

    form = BorschForm()
    data = {
        'form': form,
        'products': products,
        'error': error,
    }
    return render(request, 'mainblog/create_product.html', data)


class AllProducts(ListView):
    model = ProductsBorsch
    template_name = 'mainblog/borsch_index.html'
    context_object_name = 'products'
    ordering = ['-grammovka']

    def get_context_data(self, **kwargs):
        ctx = super(AllProducts, self).get_context_data(**kwargs)
        ctx['title'] = 'Все продукты'

        return ctx


class ProductDetail(DetailView):
    model = ProductsBorsch
    template_name = 'mainblog/product_detail.html'
    context_object_name = 'get_product'

    def get_context_data(self, *args, **kwargs):
        ctx = super(ProductDetail, self).get_context_data(*args, **kwargs)
        ctx['title'] = ProductsBorsch.objects.get(pk=self.kwargs['pk'])
        return ctx

    def get_success_url(self, **kwargs):
        return reverse_lazy('product_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object.product = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class UpdateProducts(LoginRequiredMixin, UpdateView):
    model = ProductsBorsch
    form_class = UpdateBorschForm
    template_name = 'mainblog/create_product.html'

    def get_context_data(self, **kwargs):
        ctx = super(UpdateProducts, self).get_context_data(**kwargs)
        ctx['title'] = 'Обновление продукта'
        ctx['btn_text'] = 'Обновить продукт'
        return ctx

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = ProductsBorsch
    success_url = '/borsch_index'
    template_name = 'mainblog/delete_product.html'

    def get_context_data(self, **kwargs):
        ctx = super(DeleteProduct, self).get_context_data(**kwargs)
        ctx['title'] = 'Удаление продукта'
        ctx['btn_text'] = 'Удалить продукт'
        return ctx