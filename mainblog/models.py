from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .middleware import get_current_user
from django.db.models import Q
from PIL import Image


def get_upload_path(instance, filename):
    return 'content_img/{author}/{title}/{file}'.format(author=instance.author.username, title=instance.title, file=filename)


class Articles(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True, default='default_article_pixel.jpg', verbose_name='Изображение заголовка статьи', upload_to='article_img')
    # contentimg = models.ImageField(null=True, blank=True, verbose_name='Изображение для контента статьи', upload_to=get_upload_path)


    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        # if image.height > 288 or image.width > 512:
        #     resize = (512, 1024)
        #     image.thumbnail(resize)
        #     image.save(self.img.path)


    def __str__(self):                      #
        return f'Пост: {self.title}'      # всё это
                                            #         для норм
                                            #                 отображения
    class Meta:                             #                             в админке
        verbose_name = 'Пост'             #
        verbose_name_plural = 'Посты'      #


def get_image_filename(instance, filename):
    title = instance.articles.title
    slug = slugify(title)
    return "article_img/%s-%s" % (slug, filename)


# class Images(models.Model):
#     article = models.ForeignKey(Articles, default=None, on_delete = models.CASCADE)
#     image = models.ImageField(upload_to='content_img', verbose_name='Image')



class ActiveFilterComments(models.Manager):
    def get_queryset(self):
        user = get_current_user()
        administrator = User.objects.get(username='admin')
        if user == administrator:
            return super().get_queryset().filter(Q(active=False) | Q(active=True))
        if not user.is_authenticated:
            return super().get_queryset().filter(active=True)
        return super().get_queryset().filter(Q(active=False, author = get_current_user()) | Q(active=False, article__author = get_current_user()) | Q(active=True))


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True, related_name='comments_articles')
    # author = models.CharField(verbose_name='Автор комментария', max_length=50)
    author = models.ForeignKey(User, verbose_name='Автор комментария', max_length=50, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='E-mail')
    text = models.TextField(verbose_name='Текст комментария')
    date = models.DateTimeField(verbose_name='Дата публикации комментария', default=timezone.now)
    active = models.BooleanField(default=False)
    objects = ActiveFilterComments()


    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})


    def __str__(self):
        return f'Комментарий пользователя {self.author} на "{self.article}"'


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('date',)


class ProductsBorsch(models.Model):
    name = models.CharField(verbose_name='Наименование продукта', max_length=20)
    price = models.IntegerField(verbose_name='Стоимость продукта за кг', null=True)
    grammovka = models.IntegerField(verbose_name='Граммовка для литра борща', null=True)
    kilo = models.IntegerField(verbose_name='Килограмм', default=1000, null=True)

    def get_absolute_url(self):
        return reverse('all_products')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)