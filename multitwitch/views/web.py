from multitwitch.lib.session import web, ajax

class WebView:
    @web(template="web/home.tmpl")
    def home(request):
        streams = request.matchdict['streams']
        uniq_streams = []
        for s in streams:
            if s not in uniq_streams:
                uniq_streams.append(s)
        return {'project' : 'multitwitch',
                'streams' : streams,
                'unique_streams' : uniq_streams,
                'nstreams' : len(streams)}
