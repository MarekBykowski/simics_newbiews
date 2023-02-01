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


# Additional tests that do not "fit" in the main flow 

import dev_util
import conf
import stest
import m_compute_common
import simics 

# Create an instance of the device to test
[dev, clock, mem, stub_done, stub_notified] = m_compute_common.create_m_compute()

cli.global_cmds.log_level(object=dev,level=2)

##
## Testing the is_threaded pseudo attribute
##
# Can we read it?
stest.expect_true(dev.is_threaded in [True, False])
# And do we get an exception on trying to write it?
with stest.expect_exception_mgr(simics.SimExc_AttrNotWritable):
    dev.is_threaded = False

