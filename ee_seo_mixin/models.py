from django.db import models
from django.utils.translation import ugettext_lazy as _


class SearchEngineOptimizableEntity(models.Model):
    class Meta:
        abstract = True

    meta_description_override = models.TextField(
        verbose_name=_("SEO: Meta description override"),
        blank=True,
        max_length=500)
    title_override = models.CharField(
        verbose_name=_("SEO: Title override"),
        blank=True,
        max_length=120)
    block_indexing = models.BooleanField(
        verbose_name=_("SEO: Block indexing by search engine robots"),
        default=False)
