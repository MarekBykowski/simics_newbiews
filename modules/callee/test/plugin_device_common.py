import simics

# Extend this function if your device requires any additional attributes to be
# set. It is often sensible to make additional arguments to this function
# optional, and let the function create mock objects if needed.
def create_plugin_device(name = None):
    '''Create a new plugin_device object'''
    plugin_device = simics.pre_conf_object(name, 'plugin_device')
    simics.SIM_add_configuration([plugin_device], None)
    return simics.SIM_get_object(plugin_device.name)
