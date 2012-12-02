from APPNAME.views.web import WebView
from APPNAME.views.split import SplitView

def routes(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('root', '')
    config.add_view(WebView.home, route_name='root')

    config.add_route('home', '/home')
    config.add_view(WebView.home, route_name='home')

    config.add_route('ajax_test', '/ajax_test')
    config.add_view(WebView.ajax_test, route_name='ajax_test')

    config.add_route('split_test', '/split_test')
    config.add_view(SplitView.test, route_name='split_test')
