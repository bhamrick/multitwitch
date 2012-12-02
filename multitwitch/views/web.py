from multitwitch.lib.session import web, ajax

class WebView:
    @web(template="web/home.tmpl")
    def home(request):
        return {'project' : 'multitwitch'}

    @ajax()
    def ajax_test(request):
        return [1, {'a' : 2, 'b' : 4}, 3]
