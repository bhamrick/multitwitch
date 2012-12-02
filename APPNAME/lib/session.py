from pyramid.response import Response
import jinja2

import simplejson as json

env = jinja2.Environment(loader=jinja2.FileSystemLoader('APPNAME/templates'))

def web(template=None, content_type='text/html', *args, **kwargs):
    """
    Decorator for web routes

    TODO - permissions
    """
    def decorator(f):
        def wrapper(request):
            body = ''
            data = f(request)
            if template is not None:
                tmpl = env.get_template(template)
                body = tmpl.render(data)
            else:
                body = data
            return Response(body, content_type=content_type)
        return staticmethod(wrapper)
    return decorator

def ajax(*args, **kwargs):
    """
    Decorator for ajax routes

    Returns a response with a JSON version of the return value of f

    TODO - permissions
    """
    def decorator(f):
        def wrapper(request):
            retval = f(request)
            return Response(
                    body=json.dumps(retval),
                    content_type='application/json'
                    )
        return staticmethod(wrapper)
    return decorator
