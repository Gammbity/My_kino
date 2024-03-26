from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AktyorModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.DateField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Aktyor'
        verbose_name_plural = 'Aktyors'

class FilmModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField()
    actors = models.ManyToManyField(AktyorModel, related_name='kinolar')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

class CommentModel(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self) -> str:
        return self.comment
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

# class AddAktyorModel(models.Model):
#     aktyor = models.ForeignKey(AktyorModel, related_name='add_aktyor', on_delete=models.CASCADE)
#     film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='add_film')

    