from django.apps import AppConfig


class PluginApp(AppConfig):
    name = 'netbox_firewall_policy'
    verbose_name = 'Firewall Policy'

    class NetBoxPluginMeta:
        name = 'Firewall Policy'
        author = 'John Anderson'
        description = 'Example plugin to manage firewall policy'
        version = '1.0.0'
        required_settings = []
        default_settings = {
            'foo': 'bar'
        }
        url_slug = 'hello-world'
        middleware = ['netbox_firewall_policy.middleware.TestMiddleware']

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'netbox_firewall_policy.PluginApp'
