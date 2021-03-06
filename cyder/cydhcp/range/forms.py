from django import forms

from cyder.base.eav.forms import get_eav_form
from cyder.base.mixins import UsabilityFormMixin
from cyder.cydhcp.range.models import Range, RangeAV
from cyder.cydns.forms import ViewChoiceForm


class RangeForm(ViewChoiceForm, UsabilityFormMixin):
    class Meta:
        model = Range
        exclude = ('start_upper', 'start_lower', 'end_upper', 'end_lower')
        fields = ('name', 'network', 'ip_type', 'range_type', 'start_str',
                  'end_str', 'domain', 'is_reserved', 'allow', 'views',
                  'dhcpd_raw_include', 'dhcp_enabled', 'description')
        widgets = {'views': forms.CheckboxSelectMultiple,
                   'range_type': forms.RadioSelect,
                   'ip_type': forms.RadioSelect}
        exclude = 'range_usage'

    def __init__(self, *args, **kwargs):
        super(RangeForm, self).__init__(*args, **kwargs)
        self.fields['dhcpd_raw_include'].label = "DHCP Config Extras"
        self.fields['dhcpd_raw_include'].widget.attrs.update(
            {'cols': '80',
             'style': 'display: none;width: 680px'})

        self.fields['network'].widget.attrs.update({'class': 'networkWizard'})

    def filter_by_ctnr_all(self, ctnr):
        super(RangeForm, self).filter_by_ctnr_all(ctnr, skip='network')


RangeAVForm = get_eav_form(RangeAV, Range)
