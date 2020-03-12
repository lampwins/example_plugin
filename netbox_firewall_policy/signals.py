from django.dispatch import receiver

from extras.plugins.signals import register_detail_page_buttons


@receiver(register_detail_page_buttons)
def device_buttons(sender, **kwargs):
    if sender._meta.model.__name__ == 'Device':
        return [
            'test_device_button.html',
            'test_device_button2.html'
        ]
