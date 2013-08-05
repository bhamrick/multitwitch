from multitwitch.lib.session import web, ajax

class WebView:
    @web(template="web/home.tmpl", test_template="web/test_home.tmpl")
    def home(request):
        streams = request.matchdict['streams']
        return {'project' : 'multitwitch',
                'streams' : streams,
                'unique_streams' : set(streams),
                'nstreams' : len(streams)}
