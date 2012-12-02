from multitwitch.lib.session import web, ajax

class WebView:
    @web(template="web/home.tmpl")
    def home(request):
        streams = request.matchdict[streams]
        return {'project' : 'multitwitch',
                'args' : 'streams'}
