from extras.plugins import PluginNavMenuLink, PluginNavMenuButton
from utilities.choices import ButtonColorChoices


class LinkOne(PluginNavMenuLink):
    link = 'dcim:device_list'
    link_text = 'Hello'
    link_permission = 'foo'


class LinkTwo(PluginNavMenuLink):
    link = 'dcim:device_list'
    link_text = 'Hello again'
    buttons = [
        PluginNavMenuButton('dcim:site_list', 'Sites', 'fa-info', ButtonColorChoices.BLUE, 'bar'),
        PluginNavMenuButton('dcim:site_list', 'Sites', 'fa-plus', ButtonColorChoices.GREEN),
    ]
