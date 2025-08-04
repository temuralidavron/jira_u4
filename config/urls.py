from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view

from drf_yasg import openapi

from config import settings

schema_view = get_schema_view(

    openapi.Info(

        title="U4",

        default_version='v1',

        description="Test description",

    ),

    public=True,

    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('', include('account.urls')),
        path('task/', include('task.urls')),
        path('notification/', include('notification.urls')),
    ]))
]
if settings.DEBUG:

    import debug_toolbar

    urlpatterns += [

        path('__debug__/', include(debug_toolbar.urls)),

    ]

