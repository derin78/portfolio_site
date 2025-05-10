from portfolio_site.wsgi import application
from vercel_wsgi import handle_request

def handler(request, context):
    return handle_request(application, request, context)
