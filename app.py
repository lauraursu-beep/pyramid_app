from wsgiref.simple_server import make_server
from pyramid.config import Configurator # pyright: ignore[reportMissingImports]
from pyramid.view import view_config # pyright: ignore[reportMissingImports]    

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {}

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_debugtoolbar') 
        config.add_route('index', '/')
        app = config.make_wsgi_app()
        config.scan()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()