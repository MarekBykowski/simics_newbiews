# -*- makefile -*-
#
# Sample makefile for the DML device: "empty-dml-device"
# See Simics Model Builder User's Guide for more details on what to put here.
#

MODULE_CLASSES = plugin_device
SRC_FILES = plugin_device.dml
PYTHON_FILES = module_load.py

SIMICS_API := 6
THREAD_SAFE := yes

ifeq ($(MODULE_MAKEFILE),)
$(error Make sure you compile your module from the project directory)
else
include $(MODULE_MAKEFILE)
endif

DMLC_FLAGS += -I$(SIMICS_PROJECT)/include
