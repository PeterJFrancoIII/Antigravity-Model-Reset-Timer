from django import template

register = template.Library()

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter
def get_reset_time(account, model_type):
    if model_type == 'flash':
        return account.gemini_flash_reset
    elif model_type == 'pro':
        return account.gemini_pro_reset
    elif model_type == 'opus':
        return account.opus_sonnet_reset
    return None

@register.filter
def get_percent(account, model_type):
    if model_type == 'flash':
        return account.gemini_flash_percent
    elif model_type == 'pro':
        return account.gemini_pro_percent
    elif model_type == 'opus':
        return account.opus_sonnet_percent
    return 100

@register.filter
def get_percent_color(percent):
    try:
        val = float(percent)
        if val >= 80:
            return '#00ff88' # Green
        elif val >= 40:
            return '#ffaa00' # Yellow
        else:
            return '#ff3b30' # Red
    except (ValueError, TypeError):
        return '#00ff88'
