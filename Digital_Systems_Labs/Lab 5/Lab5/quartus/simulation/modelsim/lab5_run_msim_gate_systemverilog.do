transcript on
if {[file exists gate_work]} {
	vdel -lib gate_work -all
}
vlib gate_work
vmap work gate_work

vlog -sv -work work +incdir+. {lab5.svo}

vlog -sv -work work +incdir+C:/ECE385/Lab5/quartus/../Lc3/Lab5provided_sp2023 {C:/ECE385/Lab5/quartus/../Lc3/Lab5provided_sp2023/testbench_16.sv}

vsim -t 1ps +transport_int_delays +transport_path_delays -L altera_ver -L altera_lnsim_ver -L fiftyfivenm_ver -L gate_work -L work -voptargs="+acc"  testbench_16

add wave *
view structure
view signals
run 10000 ns
