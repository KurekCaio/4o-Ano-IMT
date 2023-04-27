// #pragma config statements should precede project file includes.
// Use project enums instead of #define for ON and OFF.
    // PIC16F628A Configuration Bit Settings
// 'C' source line config statements
// CONFIG
#pragma config FOSC = INTOSCIO  // Oscillator Selection bits (INTOSC oscillator: I/O function on RA6/OSC2/CLKOUT pin, I/O function on RA7/OSC1/CLKIN)
#pragma config WDTE = OFF        // Watchdog Timer Enable bit (WDT enabled)
#pragma config PWRTE = OFF      // Power-up Timer Enable bit (PWRT disabled)
#pragma config MCLRE = OFF      // RA5/MCLR/VPP Pin Function Select bit (RA5/MCLR/VPP pin function is digital input, MCLR internally tied to VDD)
#pragma config BOREN = ON       // Brown-out Detect Enable bit (BOD enabled)
#pragma config LVP = OFF        // Low-Voltage Programming Enable bit (RB4/PGM pin has digital I/O function, HV on MCLR must be used for programming)
#pragma config CPD = OFF        // Data EE Memory Code Protection bit (Data memory code protection off)
#pragma config CP = OFF         // Flash Program Memory Code Protection bit (Code protection off)

// #pragma config statements should precede project file includes.
// Use project enums instead of #define for ON and OFF.

#include <xc.h>

#define _XTAL_FREQ 4000000

#define BT1 PORTBbits.RB0
#define BT2 PORTBbits.RB1
#define BT3 PORTBbits.RB2
#define BT4 PORTBbits.RB3

#define A PORTAbits.RA0
#define B PORTAbits.RA1
#define C PORTAbits.RA2
#define D PORTAbits.RA3

#define LE1 PORTBbits.RB5
#define LE2 PORTBbits.RB4
#define LE3 PORTAbits.RA6
#define LE4 PORTAbits.RA7

void delay(unsigned int tempo) {
    unsigned int i;
    for (i = 0; i < tempo; i++) {
        __delay_ms(1);
    }
}

void contador(int valor){
    switch(valor){
        case 0:
            A = 0;
            B = 0;
            C = 0;
            D = 0;
            break;
        case 1:
            A = 1;
            B = 0;
            C = 0;
            D = 0;
            break;
        case 2:
            A = 0;
            B = 1;
            C = 0;
            D = 0;
            break;
        case 3:
            A = 1;
            B = 1;
            C = 0;
            D = 0;
            break;
        case 4:
            A = 0;
            B = 0;
            C = 1;
            D = 0;
            break;
        case 5:
            A = 1;
            B = 0;
            C = 1;
            D = 0;
            break;
        case 6:
            A = 0;
            B = 1;
            C = 1;
            D = 0;
            break;
        case 7:
            A = 1;
            B = 1;
            C = 1;
            D = 0;
            break;
        case 8:
            A = 0;
            B = 0;
            C = 0;
            D = 1;
            break;
        case 9:
            A = 1;
            B = 0;
            C = 0;
            D = 1;
            break;
    }
}

int d1 = 0;
int d2 = 0;
int d3 = 0;
int d4 = 0;

void main(void) {
    CMCON = 0x07;
    TRISA = 0b00000000;
    TRISB = 0b00001111;
    PORTA = 0x00;
    PORTB = 0x00;
    
    LE1 = 1;
    LE2 = 1;
    LE3 = 1;
    LE4 = 1;
    
    while(1){
        //incrementa placar 1
        if (BT1 == 1){
            delay(250);
            if (d1 < 9){
                LE1 = 0;
                d1++;
                contador(d1);
                LE1 = 1;
            } else{
                LE1 = 0;
                d1 = 0;
                contador(d1);
                LE1 = 1;
                LE2 = 0;
                d2++;
                contador(d2);
                LE2 = 1;
            }
        } 
        //decrementa placar 1
        if (BT2 == 1){
            delay(250);
            if (d1 > 0){
                LE1 = 0;
                d1--;
                contador(d1);
                LE1 = 1;
            } else{
                if (d2 > 0){
                    LE1 = 0;
                    d1 = 9;
                    contador(d1);
                    LE1 = 1;
                    LE2 = 0;
                    d2--;
                    contador(d2);
                    LE2 = 1;
                }
            }
        } 
        
        //incrementa placar 2
        if (BT3 == 1){
        delay(250);
        if (d3 < 9){
                LE3 = 0;
                d3++;
                contador(d3);
                LE3 = 1;
            } else{
                LE3 = 0;
                d3 = 0;
                contador(d3);
                LE3 = 1;
                LE4 = 0;
                d4++;
                contador(d4);
                LE4 = 1;
            }
        } 
        
        //decrementa placar 2
        if (BT4 == 1){
        delay(250);
        if (d3 > 0){
                LE3 = 0;
                d3--;
                contador(d3);
                LE3 = 1;
            } else{
                if (d4 > 0){
                    LE3 = 0;
                    d3 = 9;
                    contador(d3);
                    LE3 = 1;
                    LE4 = 0;
                    d4--;
                    contador(d4);
                    LE4 = 1;
                }
            }
        } 
    }
        
    return;
}
