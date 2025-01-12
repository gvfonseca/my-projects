// Main.c - makes LEDG0 on DE2-115 board blink if NIOS II is set up correctly
// for ECE 385 - University of Illinois - Electrical and Computer Engineering
// Author: Zuofu Cheng

#include <stdio.h>
int main()
{
	int i = 0;
	volatile unsigned int *LED_PIO = (unsigned int*)0x80; //make a pointer to access the PIO block
	volatile unsigned int *SW_PIO = (unsigned int*)0x60; //pointer to the switches block
	volatile unsigned int *accumulate_PIO = (unsigned int*)0x50; //pointer to accumulate

	//local variables
	int x = 0;

	//*LED_PIO |= 0x1

	*LED_PIO = 0; //clear all LEDs

	//display all the LEDS 5 times
	while (x < 5){
		for (i = 0; i < 100000; i++); //software delay
				*LED_PIO |= 0xFF; //set LSB
		for (i = 0; i < 100000; i++); //software delay
				*LED_PIO &= ~0xFF; //clear LSB
		x++;
	}


	*LED_PIO = 0; //reset just in case

	//blinking LED

	int dummy = 0;
	 //edge detection
	while (1 == 1) //infinite loop
	{

		dummy = *accumulate_PIO;

		while(dummy == *accumulate_PIO);
		if(dummy){
			*LED_PIO = *SW_PIO + *LED_PIO;
		}


	}


	return 1; //never gets here
}
