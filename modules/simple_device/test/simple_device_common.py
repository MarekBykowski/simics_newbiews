import simics

# Extend this function if your device requires any additional attributes to be
# set. It is often sensible to make additional arguments to this function
# optional, and let the function create mock objects if needed.
def create_simple_device(name = None):
    '''Create a new simple_device object'''
    simple_device = simics.pre_conf_object(name, 'simple_device')
    simics.SIM_add_configuration([simple_device], None)
    return simics.SIM_get_object(simple_device.name)
