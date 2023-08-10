/*
 * File:   Aula09.c
 * Author: 20.01383-3
 *
 * Created on 10 de Agosto de 2023, 16:56
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

void liga(int);


void delay(unsigned int tempo) {
    unsigned int i;
    for (i = 0; i < tempo; i++) {
        __delay_ms(1);
    }
}

int n = 0;
int segundos = 0;
int led = 0;

void main(void) {
    CMCON = 0x07;
    TRISA = 0b00000000;
    TRISB = 0b00000001;
    PORTA = 0b00010000;
    PORTB = 0b00000000;
    TMR0 = 131;
    OPTION_REG = 0b00000101;
    T0IE = 1;
    GIE = 1;
    for(;;){  
    } 
}

void __interrupt() myi(void){
    if(n == 125){
        n = 0 ;
        segundos++;
        liga(led);
        if(segundos / 2 == 1){
            PORTA = 0b00010000;
            PORTB = 0b00000000;
            led++;
            segundos = 0;
            if(led == 12){
                led = 0;
            }
        }
    }
    else{
        n++;
    }
    TMR0 = 131;
    T0IF = 0;
}

void liga(int led){
    switch(led){
        case 0:
            PORTA = 0b00010001;
            PORTB = 0b00000000;
            break;
        case 1:
            PORTA = 0b00010000;
            PORTB = 0b10000000;
            break;
        case 2:
            PORTA = 0b00010000;
            PORTB = 0b01000000;
            break;
        case 3:
            PORTA = 0b00010000;
            PORTB = 0b00100000;
            break;
        case 4:
            PORTA = 0b00010000;
            PORTB = 0b00010000;
            break;
        case 5:
            PORTA = 0b00010000;
            PORTB = 0b00001000;
            break;
        case 6:
            PORTA = 0b00010000;
            PORTB = 0b00000100;
            break;
        case 7:
            PORTA = 0b00010000;
            PORTB = 0b00000010;
            break;
        case 8:
            PORTA = 0b00000000;
            PORTB = 0b00000000;
            break;
        case 9:
            PORTA = 0b00011000;
            PORTB = 0b00000000;
            break;
        case 10:
            PORTA = 0b00010100;
            PORTB = 0b00000000;
            break;
        case 11:
            PORTA = 0b00010010;
            PORTB = 0b00000000;
            break;
    }
}
