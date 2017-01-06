from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from .utils import reading_time, word_count

from django.contrib.auth.models import User


def upload_location(post, filename):
    return "%s/%s" % (post.id, filename)


class Post(models.Model):
    author = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to=upload_location,
                              height_field="height_field",
                              width_field="width_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    is_favorite = models.BooleanField(default=False)
    word_count = models.IntegerField(null=True)
    read_time = models.IntegerField(default=0)  # assuming read time is in minutes

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def get_read_time(self):
        if self.text:
            self.read_time = reading_time(self.text)
            return self.read_time

    def count_words(self):
        if self.text:
            self.word_count = word_count(self.text)
            return self.word_count


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')  # linked to Post model via the name 'comments'
    author = models.CharField(max_length=200)
    comment = models.TextField(default=None)
    created_time = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment
