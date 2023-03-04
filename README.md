marek@marek-server:~/simics-projects/my-simics-project-3/simple-devices$ cat targets/vacuum/my-vacuum.simics  
run-command-file "%script%/vacuum.simics"  
@SIM_create_object("simple_device", "sim_dev", [])  #-> create one object  
phys_mem.add-map sim_dev.bank.regs 0x1000 0x100  
@SIM_create_object("plugin_device", "plugin_dev", [])  #-> create another  

marek@marek-server:~/simics-projects/my-simics-project-3/simple-devices$./bin/simics targets/vacuum/my-vacuum.simics  

simics> sim_dev->connect2 = plugin_dev  #-> connect the objects  
simics> phys_mem.read 0x1000 -l  
[plugin_dev info] Hi there!  #-> sim_dev object calls into plugin_device  
[sim_dev.bank.regs info] read from counter  
42 (LE)  
