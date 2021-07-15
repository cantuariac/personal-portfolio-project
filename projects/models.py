from django.db import models
from django.core import validators
from django.utils.translation import gettext as _

class Technology(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=20)
    roles = models.TextField()
    about = models.TextField()
    # picture = models.ImageField(upload_to='image/', blank=True, null=True)
    picture = models.FilePathField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    level = models.FloatField(validators=[validators.MinValueValidator(0.0), validators.MaxValueValidator(1.0)])
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return "%s : %d%%"%(self.technology.name, int(self.level *100))

class SocialLink(models.Model):

    name = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    icon = models.ImageField(upload_to='image/', blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("sociallink")
        verbose_name_plural = _("sociallinks")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("sociallink_detail", kwargs={"pk": self.pk})
