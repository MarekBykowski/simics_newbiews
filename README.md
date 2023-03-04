marek@marek-server:~/simics-projects/my-simics-project-1$ cat ./targets/vacuum/my-targets.simics
run-command-file "%script%/vacuum.simics"
@SIM_create_object("callee", "ifc", [])         #-> create interface
@SIM_create_object("callee", "callee_dev", [])  #-> create callee
@SIM_create_object("caller", "caller_dev", [])  #-> create caller
phys_mem.add-map caller_dev.bank.regs 0x1000 0x100

marek@marek-server:~/simics-projects/my-simics-project-1$ ./simics targets/vacuum/my-vacuum.simics  

simics> caller_dev->who_i_connect_to = callee_dev # connnect caller to callee
simics> phys_mem.read 0x1000 -l
[callee_dev info] Hi there!
[caller_dev.bank.regs info] read from counter
42 (LE)
simics> 
