from pyramid.config import Configurator

from .config import routes

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include(routes)
    return config.make_wsgi_app()

