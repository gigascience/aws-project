from django.db import models


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