"""
ASGI config for OnlineCompiler project.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
---------------------------NITHISH--KUMARAN-S--------------------------------
MADE BY : ------ NITHISH KUMARAN .K.C.S ------
20BCAR0116
NITHISHKUMARAN1@GMAIL.COM
PROJECT @ JU(20BCAR0116)-PCL 2022-2023 copyright-c.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file,
MADE BY : ------ NITHISH KUMARAN .K.C.S ------
20BCAR0116
NITHISHKUMARAN1@GMAIL.COM
PROJECT @ JU(20BCAR0116)-PCL 2022-2023 copyright-c.
also see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineCompiler.settings')

application = get_asgi_application()
