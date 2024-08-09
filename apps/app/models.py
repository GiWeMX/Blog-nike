from django.db import models
from apps.user.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} -> {self.post.title}'
    
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} -> {self.post.title}'
    

    def children(self):
        return Comment.objects.filter(parent=self)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} -> {self.comment.text[:30]}'
    
    class Meta:
        verbose_name = 'Лайк комментария'
        verbose_name_plural = 'Лайки комментариев'
