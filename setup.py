from setuptools import setup

setup(
    name='ee-seo-mixin',
    version='0.1',
    description='Django app which provides abstract SEO mixin and a corresponding template to override.',
    author='Laboratorium EE',
    packages=['ee_seo_mixin'],  # same as name
    install_requires=['django==1.11'],  # external packages as dependencies
)
