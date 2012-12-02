from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .config import routes

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    globals()['DBEngine'] = engine
    config = Configurator(settings=settings)
    config.include(routes)
    return config.make_wsgi_app()

