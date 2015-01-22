from django.db import models
from django.contrib.auth.models import User


class Paper(models.Model):
    doi_suffix = models.CharField(max_length=128, unique=True, primary_key=True)
    gigasci_url = models.URLField()
    title = models.CharField(max_length=128, unique=True)
    authors = models.TextField()
    RESEARCH_ARTICLE = 'RA'
    COMMENTARY = 'CO'
    DATA_NOTE = 'DA'
    REVIEW = 'RE'
    TECHNICAL_NOTE = 'TN'
    ARTICLE_TYPE_CHOICES = (
        (RESEARCH_ARTICLE, 'Research Article'),
        (COMMENTARY, 'Commentary'),
        (DATA_NOTE, 'Data Note'),
        (REVIEW, 'Review'),
        (TECHNICAL_NOTE, 'Technical Note'),
    )
    article_type = models.CharField(max_length=2, choices=ARTICLE_TYPE_CHOICES, default=RESEARCH_ARTICLE)
    short_name = models.CharField(max_length=128, unique=True)
    journal = models.CharField(max_length=40, default='GigaScience')
    year = models.CharField(max_length=4, default='2014')
    volume = models.CharField(max_length=5)
    page = models.CharField(max_length=5)
    image_url = models.URLField()
    background = models.TextField()
    results = models.TextField()
    conclusions = models.TextField()

    def __unicode__(self):
        return self.doi_suffix


class Figure(models.Model):
    paper = models.ForeignKey(Paper)
    figure_num = models.CharField(max_length=2)
    title = models.CharField(max_length=128)
    url = models.URLField()
    tbn_file = models.CharField(max_length=128)
    wf_js = models.CharField(max_length=128)
    wf_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class Table(models.Model):
    paper = models.ForeignKey(Paper)
    table_num = models.CharField(max_length=2)
    title = models.CharField(max_length=128)
    url = models.URLField()
    tbn_file = models.CharField(max_length=128)
    wf_js = models.CharField(max_length=128)
    wf_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class Workflow(models.Model):
    paper = models.ForeignKey(Paper)
    figure = models.ForeignKey(Figure, blank=True, null=True)
    table = models.ForeignKey(Table, blank=True, null=True)
    url = models.URLField()
    title = models.CharField(max_length=128)
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    orcid = models.CharField(blank=True, max_length=16)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
