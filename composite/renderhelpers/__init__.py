from zope.interface import Interface
from pyramid.interfaces import IBeforeRender

class IRenderHelper(Interface):
    """\
    Provide named adapter for request and context to IRenderHelper,
    and this named object appears in rendering context
    """

def before_render_hook(event):
    request = event["request"]
    context = event["context"]
    registry = request.registry
    helpers = registry.getAdapters((request, context), IRenderHelper)
    event.update(helpers)

def includeme(configurator):
    configurator.add_subscriber(before_render_hook, IBeforeRender)
