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

    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def custom_assert_equal(self, template_str, result, context=None):
        rendered = self.render_template(
            '{% load seo_tags %}' + template_str, context)
        self.assertEqual(rendered, result)

    def test_title_override(self):
        self.custom_assert_equal('{% override_title "test_title" %}', 'test_title')
        self.custom_assert_equal('{% override_title seo_obj %}', 'Custom title', context={'seo_obj': self.seo_obj})

    def test_description_override(self):
        self.custom_assert_equal('{% override_description "test_description" %}', 'test_description')
        self.custom_assert_equal('{% override_description seo_obj %}', 'Test description',
                                 context={'seo_obj': self.seo_obj})

    def test_block_indexing(self):
        self.custom_assert_equal('{% block_indexing False %}', '')
        self.custom_assert_equal('{% block_indexing None %}', '')
        self.custom_assert_equal('{% block_indexing "yes" %}', '<meta name="robots" content="noindex"/>')
        self.custom_assert_equal('{% block_indexing True %}', '<meta name="robots" content="noindex"/>')
        self.custom_assert_equal('{% block_indexing seo_obj %}', '<meta name="robots" content="noindex"/>',
                                 context={'seo_obj': self.seo_obj})

    def test_errors(self):
        with self.assertRaises(TemplateSyntaxError):
            self.render_template('{% load seo_tags %}{% block_indexing %}')
        with self.assertRaises(TemplateSyntaxError):
            self.render_template('{% load seo_tags %}{% override_description seo_obj None %}',
                                 context={'seo_obj': self.seo_obj})
        with self.assertRaises(TemplateSyntaxError):
            self.render_template("{% load seo_tags %}{% override_title seo_obj 'my_title' %}",
                                 context={'seo_obj': self.seo_obj})
