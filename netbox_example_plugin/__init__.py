from django.apps import AppConfig


class PluginApp(AppConfig):
    name = 'netbox_example_plugin'
    verbose_name = 'Example Policy'

    class NetBoxPluginMeta:
        name = 'Example Policy'
        author = 'John Anderson'
        description = 'Example plugin to show plugin features'
        version = '1.0.0'
        required_settings = []
        default_settings = {
            'foo': 'bar'
        }
        url_slug = 'hello-world'
        middleware = ['netbox_example_plugin.middleware.TestMiddleware']

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'netbox_example_plugin.PluginApp'
