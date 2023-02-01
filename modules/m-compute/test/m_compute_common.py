# © 2021 Intel Corporation
#
# This software and the related documents are Intel copyrighted materials, and
# your use of them is governed by the express license under which they were
# provided to you ("License"). Unless the License provides otherwise, you may
# not use, modify, copy, publish, distribute, disclose or transmit this software
# or the related documents without Intel's prior written permission.
#
# This software and the related documents are provided as is, with no express or
# implied warranties, other than those that are expressly stated in the License.


import simics
import dev_util
import pyobj


# Test memory 
mem = dev_util.Memory()

## Receiver for notifications
class notify_completion_receiver(pyobj.ConfObject):
    def _initialize(self):
        super()._initialize()  

    class notifier_seen(pyobj.SimpleAttribute(False, 'b')):
        """Have we seen a notifier? Reset to False after each use!"""

    class completion_sender(pyobj.Attribute):
        "Object notifying m-compute-complete"
        attrtype = "o|n"

        def getter(self):
            return self.val

        def setter(self, obj):
            simics.SIM_log_info(1, self._up.obj, 0, 
              f"Setting up notification from {obj}" )
            self.val = obj
            self.handle = simics.SIM_add_notifier(
                    obj, 
                    simics.SIM_notifier_type("m-compute-complete"), 
                    self._up.obj,
                    self._up.notified, None)

    def notified(self, obj, src, data):
        simics.SIM_log_info(2, self.obj, 0, "Notified!" )
        self.notifier_seen.val = True
    

# Interrupt check
class signal_receive(dev_util.iface("signal")):
    def __init__(self):
        self.raise_count = 0
        self.lower_count = 0
        self.raised = False
    def signal_raise(self, sim_obj):
        simics.SIM_log_info(2, self.dev.obj, 0, "Signal raised!" )
        self.raised = True
        self.raise_count += 1
    def signal_lower(self, sim_obj):
        simics.SIM_log_info(2, self.dev.obj, 0, "Signal lowered!" )
        self.raised = False
        self.lower_count += 1

stub_done = dev_util.Dev([signal_receive])

# Extend this function if your device requires any additional attributes to be
# set. It is often sensible to make additional arguments to this function
# optional, and let the function create mock objects if needed.
def create_m_compute(name = "compute"):
    '''Create a new m_compute object'''
    clock = simics.pre_conf_object('clock', 'clock', freq_mhz=1000)
    compute = simics.pre_conf_object(name, 'm_compute', 
                                    queue=clock, 
                                    local_memory=mem.obj,
                                    operation_done=stub_done.obj)
    stub_notified = simics.pre_conf_object("stub_notified",
                                           "notify_completion_receiver",
                                           completion_sender=compute)                                    
    simics.SIM_add_configuration([clock,compute,stub_notified], None)
    cobj = simics.SIM_get_object(compute.name)
    fn = simics.SIM_get_object(stub_notified.name)
    clockobj = simics.SIM_get_object(clock.name)
    return [cobj, clockobj, mem, stub_done, fn]


