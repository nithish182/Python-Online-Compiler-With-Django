"""
WSGI config for OnlineCompiler project.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
---------------------------NITHISH--KUMARAN-S--------------------------------
MADE BY : ------ NITHISH KUMARAN .K.C.S ------
20BCAR0116
NITHISHKUMARAN1@GMAIL.COM
PROJECT @ JU(20BCAR0116)-PCL 2022-2023 copyright-c.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineCompiler.settings')

application = get_wsgi_application()
