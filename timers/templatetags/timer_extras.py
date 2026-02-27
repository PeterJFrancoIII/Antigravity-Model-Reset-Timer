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
