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
    if not account:
        return 100
    if model_type == 'flash':
        return account.gemini_flash_percent
    elif model_type == 'pro':
        return account.gemini_pro_percent
    elif model_type == 'opus':
        return account.opus_sonnet_percent
    return 100

@register.filter
def get_percent_color(value):
    try:
        pct = int(value)
        # HSL: 0 is red, 120 is green.
        hue = (pct / 100.0) * 120
        return f"hsl({hue}, 70%, 50%)"
    except (ValueError, TypeError):
        return "hsl(120, 70%, 50%)"
