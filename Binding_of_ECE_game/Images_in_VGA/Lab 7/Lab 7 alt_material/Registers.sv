module reg_16 (input  logic Clk, Reset, Load, 
              input  logic [15:0]  Din,
              output logic [15:0]  Dout);

    always_ff @ (posedge Clk)
    begin
	 	 if (Reset) //notice, this is a sycnrhonous reset, which is recommended on the FPGA
			  Dout <= 16'h0000;
		 else if (Load)
			  Dout <= Din;
    end

endmodule


module reg_1 (input  logic Clk, Reset, Load, 
              input  logic  Din,
              output logic  Dout);

    always_ff @ (posedge Clk)
    begin
	 	 if (Reset) //notice, this is a sycnrhonous reset, which is recommended on the FPGA
			  Dout <= 1'b0;
		 else if (Load)
			  Dout <= Din;
    end

endmodule


module reg_3 (input  logic Clk, Reset, Load, 
              input  logic [2:0]  Din,
              output logic [2:0]  Dout);

    always_ff @ (posedge Clk)
    begin
	 	 if (Reset) //notice, this is a sycnrhonous reset, which is recommended on the FPGA
			  Dout <= 3'b000;
		 else if (Load)
			  Dout <= Din;
    end

endmodule

module reg_4 (input  logic Clk, Reset, Load, 
              input  logic [3:0]  Din,
              output logic [3:0]  Dout);

    always_ff @ (posedge Clk)
    begin
	 	 if (Reset) //notice, this is a sycnrhonous reset, which is recommended on the FPGA
			  Dout <= 4'b0000;
		 else if (Load)
			  Dout <= Din;
    end

endmodule



module reg_2 (input  logic Clk, Reset, Load, 
              input  logic [2:0]  Din,
              output logic [2:0]  Dout);

    always_ff @ (posedge Clk)
    begin
	 	 if (Reset) //notice, this is a sycnrhonous reset, which is recommended on the FPGA
			  Dout <= 2'b00;
		 else if (Load)
			  Dout <= Din;
    end

endmodule