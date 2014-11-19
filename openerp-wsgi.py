# WSGI Handler sample configuration file.
#
# Change the appropriate settings below, in order to provide the parameters
# that would normally be passed in the command-line.
# (at least conf['addons_path'])
#
# For generic wsgi handlers a global application is defined.
# For uwsgi this should work:
#   $ uwsgi_python --http :9090 --pythonpath . --wsgi-file openerp-wsgi.py
#
# For gunicorn additional globals need to be defined in the Gunicorn section.
# Then the following command should run:
#   $ gunicorn openerp:service.wsgi_server.application -c openerp-wsgi.py

import openerp
from os import sep
from os.path import dirname, realpath
import inspect


#>>> import os
#>>> import inspect
#>>> inspect.getfile(os)
#'/usr/lib64/python2.7/os.pyc'
#>>> inspect.getfile(inspect)
#'/usr/lib64/python2.7/inspect.pyc'
#>>> os.path.dirname(inspect.getfile(inspect))
#'/usr/lib64/python2.7'


#----------------------------------------------------------
# Common
#----------------------------------------------------------
openerp.multi_process = True # Nah!

# Equivalent of --load command-line option
openerp.conf.server_wide_modules = ['web']
conf = openerp.tools.config

# Path to the OpenERP Addons repository (comma-separated for
# multiple locations)

#base_path = realpath(dirname(__file__))
base_path = realpath(dirname(inspect.getfile(inspect.currentframe())))

addons_path_base = sep.join((base_path, "addons"))

addons_path_include = ",".join(sep.join((base_path, "include", path)) for path in (
    "account-analytic",
#    "account-closing",
    "account-financial-reporting",
    "account-financial-tools",
    "account-invoicing",
    "acsone-addons",
    "bank-statement-reconcile",
    "custom/8.0",
))

conf["addons_path"] = ",".join((addons_path_base, addons_path_include))

# Optional database config if not using local socket
#conf['db_name'] = 'mycompany'
#conf['db_host'] = 'localhost'
#conf['db_user'] = 'foo'
#conf['db_port'] = 5432
#conf['db_password'] = 'secret'

#----------------------------------------------------------
# Generic WSGI handlers application
#----------------------------------------------------------
application = openerp.service.wsgi_server.application

openerp.service.server.load_server_wide_modules()

#----------------------------------------------------------
# Gunicorn
#----------------------------------------------------------
# Standard OpenERP XML-RPC port is 8069
#bind = '127.0.0.1:8069'
#pidfile = '.gunicorn.pid'
#workers = 4
#timeout = 240
#max_requests = 2000

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
