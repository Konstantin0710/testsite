from django.test import TestCase

# Create your tests here.

dirty_json = "{'agent_class': ADTWebAgent, 'station_class': SoftphoneStation, 'browser': WebBrowser.CHROME, 'is_floating_mode_enabled': False, 'tc_type': 'Autoanswer disabled; Cold transfer, no answer', 'check_vp': True}"


dirty_json = dirty_json[1:-1].split(", '")
normal_json = dict()
for i in dirty_json:
    k, v = i.split(": ")
    k = k.replace("'", "")
    v = v.replace("'", "")
    normal_json[k] = v

print(normal_json)
