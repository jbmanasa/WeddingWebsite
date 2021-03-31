from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
from .models import Guest, Family


class GuestAdmin(admin.ModelAdmin):
    list_display = ['name','attending_haldi', 'attending_mehendi', 'attending_pre_wedding_party', 'attending_wedding']
    list_filter = [('attending_haldi', DropdownFilter),
                    ('attending_mehendi', DropdownFilter),
                    ('attending_pre_wedding_party', DropdownFilter),
                    ('attending_wedding', DropdownFilter)]


class FamilyAdmin(admin.ModelAdmin):
    list_display = ['family','email_id', 'code']
    readonly_fields = ('rsvp_date', 'code')
    def get_form(self, request, obj=None, **kwargs):
        form = super(FamilyAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['comments'].widget.attrs['style'] = 'width: 50em; height: 1em;'
        return form


admin.site.register(Guest, GuestAdmin)
admin.site.register(Family, FamilyAdmin)