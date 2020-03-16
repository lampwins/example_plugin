from django.dispatch import receiver

from extras.plugins import PluginTemplateContent
from extras.plugins.signals import register_detail_page_content_classes


@receiver(register_detail_page_content_classes)
def template_content_classes(**kwargs):
    return [TestButtonOne, TestButtonTwo]


class TestButtonOne(PluginTemplateContent):
    model = 'virtualization.virtualmachine'

    def buttons(self):
        return self.render('test_button_1.html')

    def left_page(self):
        return self.render('panel_left_1.html')

    def right_page(self):
        return self.render('panel_right_1.html')

    def full_width_page(self):
        return self.render('panel_full_width_1.html')


class TestButtonTwo(PluginTemplateContent):
    model = 'dcim.cable'

    def buttons(self):
        return self.render('test_button_2.html')

    def left_page(self):
        return self.render('panel_left_2.html')

    def right_page(self):
        return self.render('panel_right_2.html')

    def full_width_page(self):
        return self.render('panel_full_width_2.html')
