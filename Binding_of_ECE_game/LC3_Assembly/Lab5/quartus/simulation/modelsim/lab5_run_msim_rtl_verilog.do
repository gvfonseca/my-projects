transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/ALU.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/test_memory.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/synchronizers.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/SLC3_2.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/Registers.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/register_file.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/Mux.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/Mem2IO.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/ISDU.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/HexDriver.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/Datapath.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/slc3.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/memory_contents.sv}
vlog -sv -work work +incdir+C:/ECE385/Lab5/slc3 {C:/ECE385/Lab5/slc3/slc3_testtop.sv}

vlog -sv -work work +incdir+C:/ECE385/Lab5/quartus/../slc3 {C:/ECE385/Lab5/quartus/../slc3/testbench_16.sv}

vsim -t 1ps -L altera_ver -L lpm_ver -L sgate_ver -L altera_mf_ver -L altera_lnsim_ver -L fiftyfivenm_ver -L rtl_work -L work -voptargs="+acc"  testbench_16

add wave *
view structure
view signals
run 10000 ns
