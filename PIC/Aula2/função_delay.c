void delay(unsigned int tempo) {
    unsigned int i;
    for (i = 0; i < tempo; i++) {
        __delay_ms(1);
    }
}
