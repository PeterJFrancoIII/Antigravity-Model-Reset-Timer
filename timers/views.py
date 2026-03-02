from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import AntigravityAccount

def dashboard(request):
    # Enforces maximum 20 accounts rendered - slice in-memory to avoid subqueries
    accounts = list(AntigravityAccount.objects.all().order_by('created_at'))[:20]
    return render(request, 'index.html', {'accounts': accounts, 'account_count': len(accounts)})

def add_account(request):
    # Creates account only if limit < 20
    if request.method == 'POST':
        account_name = request.POST.get('account_name')
        if account_name and AntigravityAccount.objects.count() < 20:
            AntigravityAccount.objects.get_or_create(name=account_name)
    return redirect('dashboard')

def set_timer(request, account_id):
    # Calculates exact future timestamp and saves to MongoDB
    if request.method == 'POST':
        account = get_object_or_404(AntigravityAccount, id=account_id)
        model_type = request.POST.get('model_type')
        hours_raw = request.POST.get('hours', '')
        minutes_raw = request.POST.get('minutes', '')
        percent_raw = request.POST.get('percent', '')
        
        # Only update timer if hours or minutes are provided and non-zero
        if hours_raw or minutes_raw:
            hours = int(hours_raw or 0)
            minutes = int(minutes_raw or 0)
            if hours > 0 or minutes > 0:
                future_time = timezone.now() + timedelta(hours=hours, minutes=minutes)
                if model_type == 'flash': account.gemini_flash_reset = future_time
                elif model_type == 'pro': account.gemini_pro_reset = future_time
                elif model_type == 'opus': account.opus_sonnet_reset = future_time
        
        # Only update percent if a value was provided
        if percent_raw:
            percent = int(percent_raw)
            if model_type == 'flash': account.gemini_flash_percent = percent
            elif model_type == 'pro': account.gemini_pro_percent = percent
            elif model_type == 'opus': account.opus_sonnet_percent = percent
            
        account.save()
    return redirect('dashboard')

# --- V1.1 Upgrade Functions ---

def delete_account(request, account_id):
    """Locates the account by ID and drops it from MongoDB."""
    if request.method == 'POST':
        account = get_object_or_404(AntigravityAccount, id=account_id)
        account.delete()
    return redirect('dashboard')

def edit_account(request, account_id):
    """Overwrites the existing account name in MongoDB."""
    if request.method == 'POST':
        account = get_object_or_404(AntigravityAccount, id=account_id)
        new_name = request.POST.get('new_name')
        if new_name:
            account.name = new_name
            account.save()
    return redirect('dashboard')

def reset_timer(request, account_id, model_type):
    """Clears a specific timer by setting the reset timestamp to None."""
    if request.method == 'POST':
        account = get_object_or_404(AntigravityAccount, id=account_id)
        
        if model_type == 'flash': account.gemini_flash_reset = None
        elif model_type == 'pro': account.gemini_pro_reset = None
        elif model_type == 'opus': account.opus_sonnet_reset = None
            
        account.save()
    return redirect('dashboard')

def update_percent(request, account_id):
    """Updates the remaining percentage for a specific model."""
    if request.method == 'POST':
        account = get_object_or_404(AntigravityAccount, id=account_id)
        model_type = request.POST.get('model_type')
        percent = int(request.POST.get('percent', 100))
        
        if model_type == 'flash': account.gemini_flash_percent = percent
        elif model_type == 'pro': account.gemini_pro_percent = percent
        elif model_type == 'opus': account.opus_sonnet_percent = percent
            
        account.save()
    return redirect('dashboard')
