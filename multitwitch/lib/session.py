from pyramid.response import Response
import jinja2

import simplejson as json

env = jinja2.Environment(loader=jinja2.FileSystemLoader('multitwitch/templates'))

def web(template=None, test_template=None, content_type='text/html', *args, **kwargs):
    """
    Decorator for web routes

    TODO - permissions
    """
    if test_template is None:
        test_template = template
    def decorator(f):
        def wrapper(request):
            body = ''
            data = f(request)
            template_to_use = None
            if request.host.startswith("test."):
                template_to_use = test_template
            else:
                template_to_use = template
            if template_to_use is not None:
                tmpl = env.get_template(template_to_use)
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
