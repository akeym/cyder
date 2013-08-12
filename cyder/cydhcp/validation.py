from django.core.exceptions import ValidationError
import re


mac_match = "[0-9a-f]{12}$"
is_mac = re.compile(mac_match)

MAC_ERR = "Mac Address not of valid type."

def validate_mac(mac):
    mac = mac.lower()
    if not isinstance(mac, basestring) or not is_mac.match(mac):
        raise ValidationError(MAC_ERR)
