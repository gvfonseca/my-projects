transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 4.1/Multiplier {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 4.1/Multiplier/Synchronizers.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 4.1/Multiplier {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 4.1/Multiplier/ripple_adder.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 4.1/Multiplier {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 4.1/Multiplier/Reg_4.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 4.1/Multiplier {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 4.1/Multiplier/HexDriver.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 4.1/Multiplier {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 4.1/Multiplier/full_adder.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 4.1/Multiplier {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 4.1/Multiplier/control.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 4.1/Multiplier {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 4.1/Multiplier/Processor.sv}

vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 4.1/Multiplier {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 4.1/Multiplier/testbench_8.sv}

vsim -t 1ps -L altera_ver -L lpm_ver -L sgate_ver -L altera_mf_ver -L altera_lnsim_ver -L fiftyfivenm_ver -L rtl_work -L work -voptargs="+acc"  testbench_8

add wave *
view structure
view signals
run 2000 ns
