/************************************************************************
Avalon-MM Interface VGA Text mode display
Register Map:
0x000-0x0257 : VRAM, 80x30 (2400 byte, 600 word) raster order (first column then row)
0x258        : control register
VRAM Format:
X->
[ 31  30-24][ 23  22-16][ 15  14-8 ][ 7    6-0 ]
[IV3][CODE3][IV2][CODE2][IV1][CODE1][IV0][CODE0]
IVn = Draw inverse glyph
CODEn = Glyph code from IBM codepage 437
Control Register Format:
[[31-25][24-21][20-17][16-13][ 12-9][ 8-5 ][ 4-1 ][   0    ] 
[[RSVD ][FGD_R][FGD_G][FGD_B][BKG_R][BKG_G][BKG_B][RESERVED]
VSYNC signal = bit which flips on every Vsync (time for new frame), used to synchronize software
BKG_R/G/B = Background color, flipped with foreground when IVn bit is set
FGD_R/G/B = Foreground color, flipped with background when Inv bit is set
************************************************************************/
`define NUM_REGS 601 //80*30 characters / 4 characters per register
`define CTRL_REG 600 //index of control register

module vga_text_avl_interface (
	// Avalon Clock Input, note this clock is also used for VGA, so this must be 50Mhz
	// We can put a clock divider here in the future to make this IP more generalizable
	input logic CLK,
	
	// Avalon Reset Input
	input logic RESET,
	
	// Avalon-MM Slave Signals
	input  logic AVL_READ,					// Avalon-MM Read
	input  logic AVL_WRITE,					// Avalon-MM Write
	input  logic AVL_CS,					// Avalon-MM Chip Select
	input  logic [3:0] AVL_BYTE_EN,			// Avalon-MM Byte Enable
	input  logic [9:0] AVL_ADDR,			// Avalon-MM Address
	input  logic [31:0] AVL_WRITEDATA,		// Avalon-MM Write Data
	output logic [31:0] AVL_READDATA,		// Avalon-MM Read Data
	
	// Exported Conduit (mapped to VGA port - make sure you export in Platform Designer)
	output logic [3:0]  red, green, blue,	// VGA color channels (mapped to output pins in top-level)
	output logic hs, vs						// VGA HS/VS
);

logic [31:0] LOCAL_REG  [`NUM_REGS]; // Registers
//put other local variables here

logic [9:0] drawxl, drawyl; // current x and y position on screen

logic [7:0] rom_out; // font rom output

logic blank, pixel_clk; // used to blank the sreen and clock the pixel input
logic VSYNC; // used for sync
//Declare submodules..e.g. VGA controller, ROMS, etc
logic [6:0] cx,cy; // value of the x and y index

logic [11:0] index; // current char index

logic [6:0] char; // current character
logic iv; // inverse bit

logic [1:0] offsetX; // offset of what x position we are in

logic [10:0] font_addr; // font address

logic [3:0] FGD_B, FGD_G, FGD_R, BKG_B, BKG_G, BKG_R;
logic out;


vga_controller vga_controller ( .Clk(CLK),
							.Reset(RESET),
							.hs(hs),
							.vs(vs),
							.pixel_clk(pixel_clk),
							.blank(blank),
							.sync(VSYNC),
							.DrawX(drawxl),
							.DrawY(drawyl)

							);		

font_rom font_rom ( .addr(font_addr),
					.data(rom_out)
					);

// ocm on_chip (.address_a(AVL_ADDR),
// 			 .address_b(index),
// 			 .byteena_a(AVL_BYTE_EN),
// 			 .byteena_b(AVL_BYTE_EN),
// 			 .clock(CLK),
// 			 .data_a(AVL_WRITEDATA),
// 			 .data_b(AVL_WRITEDATA),//doesnt matter
// 			 .rden_a(AVL_READ & AVL_CS),
// 			 .rden_b(1),
// 			 .wren_a(AVL_WRITE & AVL_CS),
// 			 .wren_b(0),
// 			 .q_a(AVL_READDATA),
// 			 .q_b(q_b)
// 			);

//Read and write from AVL interface to register block, note that READ waitstate = 1, so this should be in always_ff
always_ff @(posedge CLK) begin
	if(RESET)begin
		for(int i = 0; i <= 600; i++)
				begin 
					LOCAL_REG[i][31:0] <= 32'h0;
				end 
			end
	else if (AVL_WRITE && AVL_CS) begin
		unique case(AVL_BYTE_EN)
		
			4'b1111: LOCAL_REG[AVL_ADDR][31:0] <= AVL_WRITEDATA[31:0];
			4'b1100: LOCAL_REG[AVL_ADDR][31:16] <= AVL_WRITEDATA[31:16];
			4'b0011: LOCAL_REG[AVL_ADDR][15:0] <= AVL_WRITEDATA[15:0];
			4'b1000: LOCAL_REG[AVL_ADDR][31:24] <= AVL_WRITEDATA[31:24];
			4'b0100: LOCAL_REG[AVL_ADDR][23:16] <= AVL_WRITEDATA[23:16];
			4'b0010: LOCAL_REG[AVL_ADDR][15:8] <= AVL_WRITEDATA[15:8];
			4'b0001: LOCAL_REG[AVL_ADDR][7:0] <= AVL_WRITEDATA[7:0];
			default: ;
		endcase
	end
	else if(AVL_READ && AVL_CS)
		AVL_READDATA[31:0] = LOCAL_REG[AVL_ADDR][31:0] ; 
end

assign cx = drawxl >> 3;
assign cy = drawyl >> 4;
assign index = ((cy * 80) + cx)  >> 2;

assign offsetX = cx[1:0];

//used for setting iv and char for indexing into the font


always_comb
begin
unique case(offsetX)

	2'b00: begin 
			char = LOCAL_REG[index][6:0];
		   	iv = LOCAL_REG[index][7];
			end		
	2'b01: begin
			char = LOCAL_REG[index][14:8];
			iv = LOCAL_REG[index][15];
			end
	2'b10: begin 
			char = LOCAL_REG[index][22:16];
			iv = LOCAL_REG[index][23];
			end
	2'b11: begin 
			char = LOCAL_REG[index][30:24];
			iv = LOCAL_REG[index][31];
			end
	default: ;

	endcase


 font_addr = (char << 4) + drawyl[3:0];



 FGD_B[3:0] = LOCAL_REG[600][16:13];
 FGD_G[3:0] = LOCAL_REG[600][20:17];
 FGD_R[3:0] = LOCAL_REG[600][24:21];
 BKG_B[3:0] = LOCAL_REG[600][4:1];
 BKG_G[3:0] = LOCAL_REG[600][8:5];
 BKG_R[3:0] = LOCAL_REG[600][12:9];
end

//handle drawing (may either be combinational or sequential - or both). not sure which one
assign out = rom_out[-drawxl[2:0]];

always_ff @ (posedge pixel_clk) 
begin
	if (blank == 1'b0)
	begin
		red[3:0] = 4'h0;
		blue[3:0] = 4'h0;
		green[3:0] = 4'h0;

	end
	else if (out ^ iv)
	begin 
		red[3:0] = FGD_R;
		blue[3:0] = FGD_B;
		green[3:0] = FGD_G;
	end
	else
	begin
		red[3:0] = BKG_R;
		blue[3:0] = BKG_B;
		green[3:0] = BKG_G;
	end
end


endmodule