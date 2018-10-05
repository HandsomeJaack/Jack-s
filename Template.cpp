#include <iostream>
#include <cmath>

using namespace std;

//инициализация констант
const double E = 2.71828; // постоянная E
const double TSum = 1.0 / 2.71828; //точная сумма
// обЪявление переменных
int N; // количество просуммированных членов бесконечного ряда
double Eps; // заданная точность вычислений
double Sum; // сумма слагаемых
double Diff; // разность суммы и точной суммы
int Znak; // знак слагаемого
double Slag; //слагаемое суммы
double NFack; // n-фактариал(знаменатель слагаемого)


int main()
    {cin >> Eps; // ввод точности
    if (Eps > 0) // проверка условия работы программы
    { // обЪявление и инициализация переменных
        N = 1;
        Sum = 0;
        Diff = abs(TSum - Sum);
        Znak = -1;
        NFack = 1;
    } // end if
    else {
        cout << "Eps";
        setlocale(LC_ALL, "Russian");
        cout << "Должно быть больше нуля";
    } // end else
    while (Diff > Eps)
    { // действия над переменными
        N = N + 1; // номер слагаемого
        Znak = -Znak; // знак слагаемого
        NFack = NFack * N; // знаменатель слагаемого
        Slag = Znak / NFack; // значение слагаемого
        Sum = Sum + Slag; // сумма n-слагаемых
        Diff = abs(TSum - Sum); // разность суммы и точной суммы
    } // end while

    cout << N << "\n" << Diff << "\n" << Sum; // вывод данных
    while(1)
    return(0);
    } // end main
