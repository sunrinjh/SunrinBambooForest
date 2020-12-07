from django import template

register = template.Library()

@register.filter
def ipProcess(ip):
    try:
        data=str(ip).split('.')[0:2]
        
        ip='.'.join(data)
        return ip
    except Exception:
        return ip