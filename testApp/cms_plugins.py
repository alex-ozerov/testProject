from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import Section_1, Section_2, Section_3, Section_4, Section_5, Section_6, Section_7, Section_8

@plugin_pool.register_plugin
class Plugin_section_1(CMSPluginBase):
    model = Section_1
    name = _("Section 1")
    render_template = "section_1.html"
    cache = False
    exclude = ['base_64_image', 'base_64_background_image']

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class Plugin_section_2(CMSPluginBase):
    model = Section_2
    name = _("Section 2")
    render_template = "section_2.html"
    cache = False


    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class Plugin_section_3(CMSPluginBase):
    model = Section_3
    name = _("Section 3")
    render_template = "section_3.html"
    cache = False
    exclude = ['base_64_image']


    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class Plugin_section_4(CMSPluginBase):
    model = Section_4
    name = _("Section 4")
    render_template = "section_4.html"
    cache = False
    exclude = ['image_id']


    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class Plugin_section_5(CMSPluginBase):
    model = Section_5
    name = _("Section 5")
    render_template = "section_5.html"
    cache = False
    exclude = ['base_64_image']



    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class Plugin_section_6(CMSPluginBase):
    model = Section_6
    name = _("Section 6")
    render_template = "section_6.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class Plugin_section_7(CMSPluginBase):
    model = Section_7
    name = _("Section 7")
    render_template = "section_7.html"
    cache = False
    exclude = ['base_64_image', 'base_64_background_image']

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class Plugin_section_8(CMSPluginBase):
    model = Section_8
    name = _("Section 8")
    render_template = "section_8.html"
    cache = False


    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context