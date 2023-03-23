/*
 * File:   Aula05.c
 * Author: 20.01383-3
 *
 * Created on 23 de Março de 2023, 17:10
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

//Entradas
#define B1 PORTAbits.RA1
#define B2 PORTAbits.RA0

//Saídas
#define in1 PORTBbits.RB0
#define in2 PORTBbits.RB1
#define in3 PORTBbits.RB2
#define in4 PORTBbits.RB3

void delay(unsigned int tempo) {
    unsigned int i;
    for (i = 0; i < tempo; i++) {
        __delay_ms(1);
    }
}

void move(int i) {
    switch (i) {
        case 0:
            in1 = 1;
            in2 = 0;
            in3 = 0;
            in4 = 0;
            break;
        case 1:
            in1 = 1;
            in2 = 1;
            in3 = 0;
            in4 = 0;
            break;
        case 2:
            in1 = 0;
            in2 = 1;
            in3 = 0;
            in4 = 0;
            break;
        case 3:
            in1 = 0;
            in2 = 1;
            in3 = 1;
            in4 = 0;
            break;
        case 4:
            in1 = 0;
            in2 = 0;
            in3 = 1;
            in4 = 0;
            break;
        case 5:
            in1 = 0;
            in2 = 0;
            in3 = 1;
            in4 = 1;
            break;
        case 6:
            in1 = 0;
            in2 = 0;
            in3 = 0;
            in4 = 1;
            break;
        case 7:
            in1 = 1;
            in2 = 0;
            in3 = 0;
            in4 = 1;
            break;        
    }
}

void main(void) {
    CMCON = 0x07;
    TRISA = 0b00000011;
    TRISB = 0b00000000;
    PORTA = 0x00;
    PORTB = 0x00;
    
    if (B1 == 1) {
        for (int j=0;j<128;j++) {
            for (int i=0;i<8;i++) {
                move(i);
                delay(10);
            }
        }
    }

    if (B2 == 1) {  
       for (int j=0;j<128;j++) {
            for (int i=8;i>-1;i--) {
                move(i);
                delay(10);
            }
        }
    }
    return;
}
