from django.conf import settings


def compatible_staticpath(path):
    '''
    Try to return a path compatible all the way back to Django 1.2. If anyone
    has a cleaner or better way to do this let me know!
    '''
    try:
        # >= 1.4 or Using staticfiles
        if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
            from django.contrib.staticfiles.storage import staticfiles_storage
            return staticfiles_storage.url(path)
    except ImportError:
        pass
    try:
        # >= 1.3
        return '%s/%s' % (settings.STATIC_URL.rstrip('/'), path)
    except AttributeError:
        pass
    try:
        return '%s/%s' % (settings.PAGEDOWN_URL.rstrip('/'), path)
    except AttributeError:
        pass
    return '%s/%s' % (settings.MEDIA_URL.rstrip('/'), path)
