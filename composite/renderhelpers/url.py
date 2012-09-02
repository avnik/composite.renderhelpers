"""
Useful example of renderhelper

Use:
    config.include('composite.renderhelper')
    config.include('composite.renderhelper.url')

then in templates (for example)
    <a href="${url(context)}">context</a>

(this code is example! May not work properly)
"""
from zope.interface import Interface
from pyramid.interfaces import IRequest
from pyramid.traversal import resource_path
from . import IRenderHelper

class url_helper(object):
    """This helper expose pyramid.traversal.resource_path into rendering"""
    def __init__(self, request, context):
        self.request = request
        self.context = context

    def __call__(self, ob, args):
        return resource_path(ob, *args)

def includeme(configurator):
    configurator.registry.registerAdapter(
        url_helper,
        (IRequest, Interface),
        IRenderHelper,
        name="url")
