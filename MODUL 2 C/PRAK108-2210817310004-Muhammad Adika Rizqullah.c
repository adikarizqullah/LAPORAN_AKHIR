#include <stdio.h>
#include <stdlib.h>

void main (){
    float mengelilingiTaman = 5, jarakTempuh = 14, keliling, jarijari;

    printf("Diketahui :\n");
    printf("Pak Dengklek mengelilingi taman = %.f Putaran\n", mengelilingiTaman);
    printf("Jarak tempuh Pak Dengklek =  %.f Kilometer\n", jarakTempuh);
    printf("Jawaban :\n");
    keliling = jarakTempuh / mengelilingiTaman;
    jarijari = (keliling * 7) / (2 * 22);
    printf("Jari-jari taman yang dikelilingi Pak Dengklek adalah %.2f Kilometer\n", jarijari);
}
