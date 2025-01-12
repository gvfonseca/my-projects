transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 3/385_lab3_adders_provided_sp23 {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 3/385_lab3_adders_provided_sp23/full_adder.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 3/385_lab3_adders_provided_sp23 {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 3/385_lab3_adders_provided_sp23/select_adder.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 3/385_lab3_adders_provided_sp23 {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 3/385_lab3_adders_provided_sp23/reg_17.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 3/385_lab3_adders_provided_sp23 {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 3/385_lab3_adders_provided_sp23/mux2_1_17.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 3/385_lab3_adders_provided_sp23 {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 3/385_lab3_adders_provided_sp23/HexDriver.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 3/385_lab3_adders_provided_sp23 {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 3/385_lab3_adders_provided_sp23/control.sv}
vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 3/385_lab3_adders_provided_sp23 {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 3/385_lab3_adders_provided_sp23/adder_toplevel.sv}

vlog -sv -work work +incdir+C:/Users/hunte/OneDrive/Documents/Illinois/Spring\ 2023/ECE\ 385/Labs/Lab\ 3/385_lab3_adders_provided_sp23 {C:/Users/hunte/OneDrive/Documents/Illinois/Spring 2023/ECE 385/Labs/Lab 3/385_lab3_adders_provided_sp23/testbench_adder.sv}

vsim -t 1ps -L altera_ver -L lpm_ver -L sgate_ver -L altera_mf_ver -L altera_lnsim_ver -L fiftyfivenm_ver -L rtl_work -L work -voptargs="+acc"  testbench_adder

add wave *
view structure
view signals
run -all
