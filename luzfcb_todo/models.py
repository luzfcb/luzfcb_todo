from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class BaseModel(models.Model):
    created_date = models.DateTimeField(default=timezone.now, blank=True, editable=False)
    created_by = models.ForeignKey(to=USER_MODEL,
                                   related_name="%(app_label)s_%(class)s_created_by", null=True,
                                   blank=True, on_delete=models.SET_NULL, editable=False)

    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True, editable=False)
    modified_by = models.ForeignKey(to=USER_MODEL,
                                    related_name="%(app_label)s_%(class)s_modified_by", null=True,
                                    blank=True, on_delete=models.SET_NULL, editable=False)

    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True, editable=False)

    expire_date = models.DateTimeField(blank=True, null=True)
    is_expired = models.BooleanField(default=False, editable=False)

    is_active = models.BooleanField(default=True)

    priority = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        now_datetime = timezone.now()
        if self.is_completed:
            self.completed_date = now_datetime
        else:
            self.completed_date = None

        if now_datetime > self.expire_date:
            self.is_expired = True
        else:
            self.is_expired = False

        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class TodoList(BaseModel):
    name = models.CharField(max_length=60)
    name_slug = models.SlugField(max_length=60, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.name_slug = slugify(self.name)
        super(TodoList, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)


class Task(BaseModel):
    title = models.CharField(max_length=60)
    title_slug = models.SlugField(max_length=60, editable=False)

    content = models.TextField()

    todolist = models.ForeignKey(to=TodoList)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug_title = slugify(self.title)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)
