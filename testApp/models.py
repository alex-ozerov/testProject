from django.db import models
from cms.models.fields import PlaceholderField
from cms.models.pluginmodel import CMSPlugin
import base64

class Section_1(CMSPlugin):
    background_image = models.ImageField(upload_to="images/", blank=True, null=True)
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    buttom_text = models.CharField(max_length=50, blank=True)
    buttom_link = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    base_64_image = models.CharField(max_length=1000000, default="", blank=True, null=True )
    base_64_background_image = models.CharField(max_length=1000000, default="", blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.base_64_image = base64.b64encode(self.image.read()).decode('utf-8')
        self.base_64_background_image = base64.b64encode(self.background_image.read()).decode('utf-8')
        super(Section_1, self).save(*args, **kwargs)

class Section_2(CMSPlugin):
    buttom_text_1 = models.CharField(max_length=50, blank=True)
    buttom_link_1 = models.URLField(max_length=200, blank=True)
    buttom_text_2 = models.CharField(max_length=50, blank=True)
    buttom_link_2 = models.URLField(max_length=200, blank=True)
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

class Section_3(CMSPlugin):
    title_1 = models.CharField(max_length=50, blank=True)
    description_1 = models.CharField(max_length=1000, blank=True)
    title_2 = models.CharField(max_length=50, blank=True)
    description_2 = models.CharField(max_length=1000, blank=True)
    buttom_text = models.CharField(max_length=50, blank=True, null=True)
    buttom_link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    base_64_image = models.CharField(max_length=1000000, default="", blank=True, null=True )

    def __str__(self):
        return self.title_1

    def save(self, *args, **kwargs):
        self.base_64_image = base64.b64encode(self.image.read()).decode('utf-8')
        super(Section_3, self).save(*args, **kwargs)

class Section_4(CMSPlugin):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    buttom_text_1 = models.CharField(max_length=50, blank=True)
    buttom_link_1 = models.URLField(max_length=200, blank=True)
    buttom_text_2 = models.CharField(max_length=50, blank=True)
    buttom_link_2 = models.URLField(max_length=200, blank=True)
    link_video = models.URLField(max_length=10000, blank=True)
    image_id = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if "=" in self.link_video:
            self.image_id = self.link_video[self.link_video.rindex('=')+1:]
        else:
            self.image_id = self.link_video.split('/')[-1]
        self.link_video = ""+self.link_video[:self.link_video.rindex("/")+1]+"embed/"+self.link_video[self.link_video.rindex("/")+9:]
        super(Section_4, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Section_5(CMSPlugin):
    icon = models.ImageField(upload_to="images/", blank=True, null=True)
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    text_link = models.CharField(max_length=1000, blank=True)
    link = models.URLField(max_length=2000, blank=True)
    base_64_image = models.CharField(max_length=1000000, default="", blank=True, null=True )


    def save(self, *args, **kwargs):
        self.base_64_image = base64.b64encode(self.icon.read()).decode('utf-8')
        super(Section_5, self).save(*args, **kwargs)


class Section_6(CMSPlugin):
    check_box = models.BooleanField(blank=True,null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    list_line_1 = models.CharField(max_length=50, blank=True, null=True)
    list_line_2 = models.CharField(max_length=50, blank=True, null=True)
    list_line_3 = models.CharField(max_length=50, blank=True, null=True)
    list_line_4 = models.CharField(max_length=50, blank=True, null=True)
    list_line_5 = models.CharField(max_length=50, blank=True, null=True)
    list_line_6 = models.CharField(max_length=50, blank=True, null=True)
    text_link = models.CharField(max_length=1000, blank=True)
    link = models.URLField(max_length=2000, blank=True)
    users_text = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class Section_7(CMSPlugin):
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    background_image = models.ImageField(upload_to="images/", blank=True, null=True)
    base_64_image = models.CharField(max_length=1000000, default="", blank=True, null=True)
    base_64_background_image = models.CharField(max_length=1000000, default="", blank=True, null=True)
    buttom_text = models.CharField(max_length=50, blank=True, null=True)
    buttom_link = models.URLField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.base_64_image = base64.b64encode(self.image.read()).decode('utf-8')
        self.base_64_background_image = base64.b64encode(self.background_image.read()).decode('utf-8')
        super(Section_7, self).save(*args, **kwargs)


class Section_8(CMSPlugin):
    title = models.CharField(max_length=50, blank=True, null=True)
    text_link_1 = models.CharField(max_length=1000, blank=True)
    link_1 = models.URLField(max_length=2000, blank=True)
    text_link_2 = models.CharField(max_length=1000, blank=True)
    link_2 = models.URLField(max_length=2000, blank=True)
    text_link_3 = models.CharField(max_length=1000, blank=True)
    link_3 = models.URLField(max_length=2000, blank=True)
    text_link_4 = models.CharField(max_length=1000, blank=True)
    link_4 = models.URLField(max_length=2000, blank=True)

    def __str__(self):
        return self.title