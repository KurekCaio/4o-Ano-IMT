/*
 * File:   aula1.c
 * Author: 20.00080-4
 *
 * Created on 2 de Março de 2023, 15:18
 */

// PIC16F628A Configuration Bit Settings
// 'C' source line config statements
// CONFIG
#pragma config FOSC = INTOSCIO  // Oscillator Selection bits (INTOSC oscillator: I/O function on RA6/OSC2/CLKOUT pin, I/O function on RA7/OSC1/CLKIN)
#pragma config WDTE = OFF       // Watchdog Timer Enable bit (WDT disabled)
#pragma config PWRTE = OFF      // Power-up Timer Enable bit (PWRT disabled)
#pragma config MCLRE = ON       // RA5/MCLR/VPP Pin Function Select bit (RA5/MCLR/VPP pin function is MCLR)
#pragma config BOREN = OFF      // Brown-out Detect Enable bit (BOD disabled)
#pragma config LVP = OFF        // Low-Voltage Programming Enable bit (RB4/PGM pin has digital I/O function, HV on MCLR must be used for programming)
#pragma config CPD = OFF        // Data EE Memory Code Protection bit (Data memory code protection off)
#pragma config CP = OFF         // Flash Program Memory Code Protection bit (Code protection off)

// #pragma config statements should precede project file includes.
// Use project enums instead of #define for ON and OFF.

#include <xc.h>

#define _XTAL_FREQ 4000000

void main(void) {
    CMCON = 0x07; //pinos RA sao digitais
    TRISA = 0b00001111; // TRIS = 1 entrada, e TRIS = 0 saída
    //TRISAbits.TRISA0 = ...
    TRISB = 0b00000000;
    
    PORTB = 0b00000000;
    
    int tempo = 400;
    int i;
    
    while(1){
        
        
        if(PORTAbits.RA1==0){
            tempo = 200;
        }
        else if(PORTAbits.RA2==0){
            tempo = 100;
        }
        else if(PORTAbits.RA3==0){
            tempo = 50;
        }
        else{
            tempo = 400;
        }
        
        if(PORTAbits.RA0==0){
            for(i=0;i<tempo;i++){
               PORTBbits.RB0=1;
            __delay_ms(1); 
            }
            
            for(i=0;i<tempo;i++){
               PORTBbits.RB1=1;
            __delay_ms(1); 
            }
            
            for(i=0;i<tempo;i++){
               PORTBbits.RB2=1;
            __delay_ms(1); 
            }
            
            for(i=0;i<tempo;i++){
               PORTBbits.RB3=1;
            __delay_ms(1); 
            }
            
            for(i=0;i<tempo;i++){
               PORTBbits.RB4=1;
            __delay_ms(1); 
            }
            
            for(i=0;i<tempo;i++){
               PORTBbits.RB5=1;
            __delay_ms(1); 
            }
            
            for(i=0;i<tempo;i++){
               PORTBbits.RB6=1;
            __delay_ms(1); 
            }
            
            for(i=0;i<tempo;i++){
               PORTBbits.RB7=1;
            __delay_ms(1); 
            }
            
            for(i=0;i<tempo;i++){
                PORTB = 0b00000000;
                __delay_ms(1); 
            }  
        }
    }
}
