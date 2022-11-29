#include <stdio.h>

int main()
{
    int A, B, X, Y, Hasil;
    A = 9;
    B = 5;
    X = 8;
    Y = 8;
    printf("Variabel A bernilai %d\n", A);
    printf("Variabel B bernilai %d\n", B);
    printf("Variabel X bernilai %d\n", X);
    printf("Variabel Y bernilai %d\n", Y);

    Hasil = ((A%B)+(X%Y));

    printf("Total sisa bagi dari A dibagi B dan X dibagi Y adalah %d\n", Hasil);
    return 0;
}
