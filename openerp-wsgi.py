# -*- coding: utf-8 -*-

"""
WSGI Handler sample configuration file.
=======================================

Change the appropriate settings below, in order to provide the parameters
that would normally be passed in the command-line.

* For uwsgi this should work:

    $ uwsgi_python --http :9090 --pythonpath . --wsgi-file openerp-wsgi.py

For gunicorn additional globals need to be defined in the Gunicorn section.

    $ gunicorn openerp:service.wsgi_server.application -c openerp-wsgi.py
"""

import openerp

#----------------------------------------------------------
# Common
#----------------------------------------------------------
openerp.multi_process = True

# Equivalent of --load command-line option
openerp.conf.server_wide_modules = ['web']
conf = openerp.tools.config

# Path to the OpenERP Addons repository (comma-separated for
# multiple locations)

conf['addons_path'] = '/opt/odoo/addons,/opt/odoo/include/custom/8.0'

#conf['admin_passwd'] = 'TrucSuperCompliquéEtVachementSecret'

# Optional database config if not using local socket
#conf['db_name'] = 'TODO'
#conf['dbfilter'] = 'TODO'
#conf['list_db'] = 'TODO'
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
