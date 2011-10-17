"""Creates a new database but only if the database doesn't exist yet"""
from __future__ import with_statement
import os
try:
    import settings
except ImportError:
    settings = None
from simblin.extensions import db
from simblin import create_app

app = create_app(settings)

with app.test_request_context():
    # The context is needed so db can access the configuration of the app
    db.create_all()

print "Initialized new empty database in %s" % app.config['SQLALCHEMY_DATABASE_URI']

