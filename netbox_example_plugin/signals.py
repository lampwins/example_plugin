from django.dispatch import receiver

from extras.plugins.signals import register_detail_page_content_classes, register_nav_menu_link_classes

from .nav_bar import LinkOne, LinkTwo
from .template_content import TestButtonOne, TestButtonTwo


@receiver(register_detail_page_content_classes)
def template_content_classes(**kwargs):
    return [TestButtonOne, TestButtonTwo]


@receiver(register_nav_menu_link_classes)
def nav_menu_link_classes(**kwargs):
    return [LinkOne, LinkTwo]
