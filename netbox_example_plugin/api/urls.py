from django.urls import path
from rest_framework import routers

from . import views


class ExampleRootView(routers.APIRootView):
    """
    Example API root view
    """
    def get_view_name(self):
        return 'Example'


router = routers.DefaultRouter()
router.APIRootView = ExampleRootView

app_name = 'netbox_example_plugin-api'
urlpatterns = router.urls

urlpatterns += [
    path('test/', views.TestView.as_view())
]
