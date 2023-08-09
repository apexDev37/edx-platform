"""
Django admin page for the Agreements app
"""

from django.contrib import admin
from openedx.core.djangoapps.agreements.models import IntegritySignature
from openedx.core.djangoapps.agreements.models import LTIPIITool
from openedx.core.djangoapps.agreements.models import LTIPIISignature
from openedx.core.djangoapps.agreements.models import ProctoringPIISignature


@admin.register(IntegritySignature)
class IntegritySignatureAdmin(admin.ModelAdmin):
    """
    Admin for the IntegritySignature Model
    """
    list_display = ('user', 'course_key', 'created', 'modified')
    readonly_fields = ('user', 'course_key', 'created', 'modified')
    search_fields = ('user__username', 'course_key',)
    ordering = ['-modified']

    class Meta:
        model = IntegritySignature




@admin.register(LTIPIITool)
class LTIPIIToolAdmin(admin.ModelAdmin):
    """
    Admin for the LTIPIITool Model
    """
    readonly_fields = ('course_key', 'lti_tools', 'lti_tools_hash')

    class Meta:
        model = LTIPIITool




@admin.register(LTIPIISignature)
class LTIPIISignatureAdmin(admin.ModelAdmin):
    """
    Admin for the LTIPIISignature Model
    """
    readonly_fields = ('user', 'course_key', 'lti_tools', 'lti_tools_hash')

    class Meta:
        model = LTIPIISignature




@admin.register(ProctoringPIISignature)
class ProctoringPIISignatureAdmin(admin.ModelAdmin):
    """
    Admin for the ProctoringPIISignature Model
    """
    readonly_fields = ('user', 'course_key', 'proctoring_provider')

    class Meta:
        model = ProctoringPIISignature


