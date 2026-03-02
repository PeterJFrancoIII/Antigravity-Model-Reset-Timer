# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# We need to collect all Django components, templates, and static files.
added_files = [
    ('timers/templates', 'timers/templates'),
    ('manage.py', '.'),
    ('antigravity_timer', 'antigravity_timer'),
    ('timers', 'timers'),
    ('requirements.txt', '.'),
]

a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        'django.core.management',
        'django.core.management.commands.runserver',
        'django.core.wsgi',
        'django.core.handlers.wsgi',
        'django.db.backends.sqlite3', # Standard backup
        'djongo',
        'pymongo',
        'webview',
        'clr', # For Windows support if needed
        'timers.templatetags.timer_extras',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AntigravityTimer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False, # Set to False for graphical interface
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AntigravityTimer',
)

app = BUNDLE(
    coll,
    name='AntigravityTimer.app',
    icon='icon.png', # Add path to .icns file if available
    bundle_identifier='com.antigravity.timer',
)
