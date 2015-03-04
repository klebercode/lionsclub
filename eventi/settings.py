"""
Django settings for eventi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
BASE_DIR = Path(__file__).parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '.localhost',
    '127.0.0.1',
    '.ow7.com.br',
]


# Application definition

INSTALLED_APPS = (
    # 'grappelli_extensions',
    # 'grappelli',
    # 'filebrowser',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # other apps
    'south',
    'bootstrap3',

    # my apps
    'eventi.core',
    'eventi.subscriptions',
    'eventi.receipts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eventi.urls'

WSGI_APPLICATION = 'eventi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url),
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # False = Brazil / True = World


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'Lions Clube Garanhuns <convencao@lionsclubegaranhuns.org.br>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtpi.kinghost.net'
EMAIL_HOST_USER = 'convencao@lionsclubegaranhuns.org.br'
EMAIL_HOST_PASSWORD = 't8w4q7e3'
EMAIL_PORT = 587


# django-tinymce
# TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    # General options
    'mode': "textareas",
    'theme': "advanced",
    'plugins': "autolink,lists,spellchecker,pagebreak,style,layer,table,save, \
                advhr,advimage,advlink,emotions,iespell,inlinepopups, \
                insertdatetime,preview,media,searchreplace,print,contextmenu, \
                paste,directionality,fullscreen,noneditable,visualchars, \
                nonbreaking,xhtmlxtras,template",

    # Theme options
    'theme_advanced_buttons1': "save,newdocument,|,bold,italic,underline, \
        strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull, \
        |,styleselect,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "cut,copy,paste,pastetext,pasteword,|,search, \
        replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo, \
        |,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime, \
        preview,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid, \
        |,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr, \
        rtl,|,fullscreen",
    'theme_advanced_buttons4': "insertlayer,moveforward,movebackward, \
        absolute,|,styleprops,spellchecker,|,cite,abbr,acronym,del,ins, \
        attribs,|,visualchars,nonbreaking,template,blockquote, \
        pagebreak,|,insertfile,insertimage",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': "true",

    # Skin options
    # 'skin': "o2k7",
    # 'skin_variant': "silver",

    # Example content CSS (should be your site CSS)
    # 'content_css' : "css/example.css",

    # Drop lists for link/image/media/template dialogs
    # 'template_external_list_url' : "js/template_list.js",
    # 'external_link_list_url' : "js/link_list.js",
    # 'external_image_list_url' : "js/image_list.js",
    # 'media_external_list_url' : "js/media_list.js",

    # Replace values for the template plugin
    # 'template_replace_values' : {
    #         'username' : "Some User",
    #         'staffid' : "991234"
    # }

    'height': '400',
}


# grappelli
GRAPPELLI_ADMIN_TITLE = 'OW7 | CMS'

# GRAPPELLI_EXTENSIONS_NAVBAR = 'eventi.extensions.Navbar'

# GRAPPELLI_EXTENSIONS_SIDEBAR = 'eventi.extensions.Sidebar'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


# south {taggit}
SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}


TAGGIT_AUTOSUGGEST_CSS_FILENAME = 'autoSuggest-grappelli.css'


BOOTSTRAP3 = {
    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',
}
