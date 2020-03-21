from extras.plugins import PluginConfig


class PluginAppConfig(PluginConfig):
    name = 'netbox_example_plugin'
    verbose_name = 'Example Plugin'

    author = 'John Anderson'
    description = 'Example plugin to show plugin features'
    version = '1.0.0'
    required_settings = []
    default_settings = {
        'foo': 'bar'
    }
    url_slug = 'hello-world'
    middleware = ['netbox_example_plugin.middleware.TestMiddleware']
    min_version = '2.8.0-dev'
    #max_version = '2.9.0'
    caching_config = {
        'netbox_example_plugin.*': None
    }

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'netbox_example_plugin.PluginAppConfig'
