# © 2010 Intel Corporation

import simics

# Extend this function if your device requires any additional attributes to be
# set. It is often sensible to make additional arguments to this function
# optional, and let the function create mock objects if needed.
def create_caller(name = None):
    '''Create a new caller object'''
    caller = simics.pre_conf_object(name, 'caller')
    simics.SIM_add_configuration([caller], None)
    return simics.SIM_get_object(caller.name)
