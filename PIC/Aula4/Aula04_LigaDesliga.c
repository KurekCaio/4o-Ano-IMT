/*
 * File:   Aula04_Ativ2.c
 * Author: 20.00730-2
 *
 * Created on 16 de Março de 2023, 17:08
 */

// PIC16F628A Configuration Bit Settings
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

#define Gre PORTBbits.RB0
#define Yel PORTBbits.RB1
#define Red PORTBbits.RB2

#define B1 PORTAbits.RA0
#define B2 PORTAbits.RA1

void delay(unsigned int tempo) {
    unsigned int i;
    for (i = 0; i < tempo; i++) {
        __delay_ms(1);
    }
}

void main(void) {
    CMCON = 0x07;
    TRISA = 0b00000011;
    TRISB = 0b00000000;
    PORTB = 0x00;
   
    while(1) {
        if (B1 == 0 && Gre == 0) {
            Gre = 1;
            delay(500);
        }
        
        if (B1 == 0 && Gre == 1) {
            Yel = 1;
            delay(500);
        }
        
        if (B1 == 0 && Yel == 1) {
            Red = 1;
            delay(500);
        }
            
        if (B2 == 0 && Red == 1) {
            Red = 0;
            delay(500);
        }
        
        if (B2 == 0 && Yel == 1 && Red == 0) {
            Yel = 0;
            delay(500);
        }
        
        if (B2 == 0 && Gre == 1 && Yel == 0) {
            Gre = 0;
            delay(500);
        }
    }
}
