from django.template import Context, Template, TemplateSyntaxError
from .models import SearchEngineOptimizableEntity as SeoEntity
from .utils import ModelMixinTestCase


class SeoTemplateTagsTest(ModelMixinTestCase):
    mixin = SeoEntity

    def setUp(self):
        self.seo_obj = self.model.objects.create(
            meta_description_override='Test description',
            title_override='Custom title',
            block_indexing=True
        )

        self.empty_seo_obj = self.model.objects.create(
            meta_description_override='',
            title_override='',
            block_indexing=False
        )

    def render_template(self, string, context):
        context = Context(context)
        return Template(string).render(context)

    def assert_template_renders_to(self, template_str, result, context):
        rendered = self.render_template(
            '{% load seo_tags %}' + template_str, context)
        self.assertEqual(rendered, result)

    def test_title_override(self):
        self.assert_template_renders_to('{% override_title None default="test_title" %}', 'test_title', {})
        self.assert_template_renders_to('{% override_title seo_obj default="Test" %}', 'Custom title',
                                        context={'seo_obj': self.seo_obj})

    def test_description_override(self):
        self.assert_template_renders_to('{% override_description None default="test_description" %}',
                                        'test_description', {})
        self.assert_template_renders_to('{% override_description seo_obj default="description"%}',
                                        'Test description',
                                        context={'seo_obj': self.seo_obj})

    def test_block_indexing(self):
        self.assert_template_renders_to('{% block_indexing False default=False%}', '', {})
        self.assert_template_renders_to('{% block_indexing None default=False%}', '', {})
        self.assert_template_renders_to('{% block_indexing "yes" default=False%}', '', {})
        self.assert_template_renders_to('{% block_indexing True default=False%}', '', {})
        self.assert_template_renders_to('{% block_indexing "yes" default=True%}',
                                        '<meta name="robots" content="noindex"/>', {})
        self.assert_template_renders_to('{% block_indexing seo_obj default=False%}',
                                        '<meta name="robots" content="noindex"/>',
                                        context={'seo_obj': self.seo_obj})

    def test_errors(self):
        with self.assertRaises(TemplateSyntaxError):
            self.render_template('{% load seo_tags %}{% block_indexing %}', {})
        with self.assertRaises(TemplateSyntaxError):
            self.render_template('{% load seo_tags %}{% override_description seo_obj %}',
                                 context={'seo_obj': self.seo_obj})
        with self.assertRaises(TemplateSyntaxError):
            self.render_template("{% load seo_tags %}{% override_title 'my_title' %}",
                                 context={'seo_obj': self.seo_obj})
