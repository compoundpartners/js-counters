from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CounterModel, CountersContainerModel

@plugin_pool.register_plugin
class CountersContainerPlugin(CMSPluginBase):

    module = 'Jumpsuite'
    model = CountersContainerModel
    name = _('Counters Container')
    child_classes = ['CounterPlugin']

    render_template = 'js-counters/counters_container.html'

    allow_children = True



    def render(self, context, instance, placeholder):
        context.update({
            'object': instance
        })
        return context

@plugin_pool.register_plugin
class CounterPlugin(CMSPluginBase):

    module = 'Jumpsuite'
    model = CounterModel
    name = _('Counter')
    parent_classes = ['CountersContainerPlugin']

    render_template = 'js-counters/counter.html'

    #child_count = CountersContainerPlugin.get(cmsplugin_ptr=instance.parent.child_count)

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance
        })
        return context
