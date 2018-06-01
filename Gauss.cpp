#include <iostream>

int main()
{
    int poryadok, i, j, k;
    double d, s;
    std::cout << "Введите поярдок:\n";
    std::cin >> poryadok;
    double **a = new double *[poryadok];
    for (i = 0; i <= poryadok; i++)
        a[i] = new double [poryadok];

    double **a1 = new double *[poryadok];
    for (i = 0; i <= poryadok; i++)
        a1[i] = new double [poryadok];

    double *b = new double [poryadok]; //свободный член
    double *x = new double [poryadok]; //корни
    std::cout << "Введите коэффициенты и свободные члены: \n";
    for (i = 1; i <= poryadok; i++)
    {
        for (j = 1; j <= poryadok; j++)
        {
            std::cout << "a[ " << i << "," << j << "]= ";
            std::cin >> a[i][j];
            a1[i][j] = a[i][j];
        }
        std::cout << "b,[ " << i << "]= ";
        std::cin >> b[i];
    }
    for (k = 1; k <= poryadok; k++) // прямой ход
    {
        for (j = k + 1; j <= poryadok; j++)
        {
            d = a[j][k] / a[k][k];
            for (i = k; i <= poryadok; i++)
                a[j][i] = a[j][i] - d * a[k][i];
            b[j] = b[j] - d * b[k];
        }
    }

    for (k = poryadok; k >= 1; k--) // обратный ход
    {
        d = 0;
        for (j = k + 1; j <= poryadok; j++)
        {
            s = a[k][j] * x[j];
            d = d + s;
        }
        x[k] = (b[k] - d) / a[k][k];
    }
    std::cout << "Корни системы: \n";
    for( i = 1; i <= poryadok; i++)
        std::cout << "x[" << i << "]=" << x[i] << " \n";
    return 0;
}

