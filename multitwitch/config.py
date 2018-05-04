from multitwitch.views.web import WebView

def routes(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('favicon', '/favicon.ico')
    config.add_view(WebView.favicon, route_name='favicon')

    config.add_route('twitch_api_test', '/twitch_api_test')
    config.add_view(WebView.twitch_api_test, route_name='twitch_api_test')

    config.add_route('view', '/view')
    config.add_view(WebView.view, route_name='view')

    config.add_route('edit', '/edit/*streams')
    config.add_view(WebView.edit, route_name='edit')

    config.add_route('root', '')
    config.add_view(WebView.home, route_name='root')

    config.add_route('multitwitch', '*streams')
    config.add_view(WebView.streams, route_name='multitwitch')
