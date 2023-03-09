/*
 * File:   Micro_Aula03.c
 * Author: 20.00333-0
 *
 * Created on 9 de Março de 2023, 15:15
 */
// 'C' source line config statements
// CONFIG
#pragma config FOSC = INTOSCIO  // Oscillator Selection bits (INTOSC oscillator: I/O function on RA6/OSC2/CLKOUT pin, I/O function on RA7/OSC1/CLKIN)
#pragma config WDTE = OFF       // Watchdog Timer Enable bit (WDT disabled)
#pragma config PWRTE = OFF      // Power-up Timer Enable bit (PWRT disabled)
#pragma config MCLRE = ON       // RA5/MCLR/VPP Pin Function Select bit (RA5/MCLR/VPP pin function is MCLR)
#pragma config BOREN = ON       // Brown-out Detect Enable bit (BOD enabled)
#pragma config LVP = OFF        // Low-Voltage Programming Enable bit (RB4/PGM pin has digital I/O function, HV on MCLR must be used for programming)
#pragma config CPD = OFF        // Data EE Memory Code Protection bit (Data memory code protection off)
#pragma config CP = OFF         // Flash Program Memory Code Protection bit (Code protection off)

// #pragma config statements should precede project file includes.
// Use project enums instead of #define for ON and OFF.


#include <xc.h>

#define _XTAL_FREQ 4000000
#define AM1 PORTBbits.RB1
#define AM2 PORTBbits.RB4

#define VM1 PORTBbits.RB0
#define VM2 PORTBbits.RB3

#define VD1 PORTBbits.RB2
#define VD2 PORTBbits.RB5

void estado(int vm1, int vm2, int am1, int am2, int vd1, int vd2);

void main(void) {
    CMCON = 0x07;
    TRISB = 0;
    AM1 = 0;
    AM2 = 0;
    VM1 = 0;
    VM2 = 0;
    VD1 = 0;
    VD2 = 0;
    
    /*
    while(1)
    {   
        AM1 ^= 1;
        AM2 ^= 1;
        VM1 ^= 1;
        VM2 ^= 1;
        VD1 ^= 1;
        VD2 ^= 1;
        __delay_ms(500);
    }
    */
    while(1)
    {
        estado(0,0,1,1,0,0);
        estado(0,1,0,1,0,0);
        estado(1,0,0,0,0,1);
        estado(1,0,0,0,1,0);
    }
}


void estado(int vm1, int am1, int vd1, int vm2, int am2, int vd2){
    AM1 = am1;
    AM2 = am2;
    VM1 = vm1;
    VM2 = vm2;
    VD1 = vd1;
    VD2 = vd2;
    __delay_ms(5000);
}

