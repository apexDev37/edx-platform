"""
Django admin for Video Pipeline models.
"""

from django.contrib import admin

from config_models.admin import ConfigurationModelAdmin
from openedx.core.djangoapps.video_config.admin import CourseSpecificEnabledFlagBaseAdmin
from openedx.core.djangoapps.video_pipeline.forms import (
    CourseVideoUploadsEnabledByDefaultAdminForm,
    VEMPipelineIntegrationAdminForm
)
from openedx.core.djangoapps.video_pipeline.models import (
    CourseVideoUploadsEnabledByDefault,
    VEMPipelineIntegration,
    VideoUploadsEnabledByDefault
)


@admin.register(CourseVideoUploadsEnabledByDefault)
class CourseVideoUploadsEnabledByDefaultAdmin(CourseSpecificEnabledFlagBaseAdmin):
    """
    Admin of video uploads enabled by default feature on course-by-course basis.
    Allows searching by course id.
    """
    form = CourseVideoUploadsEnabledByDefaultAdminForm


@admin.register(VEMPipelineIntegration)
class VEMPipelineIntegrationAdmin(ConfigurationModelAdmin):
    """
    Admin of VEM Pipeline integration config model.
    """
    form = VEMPipelineIntegrationAdminForm


admin.site.register(VideoUploadsEnabledByDefault, ConfigurationModelAdmin)
