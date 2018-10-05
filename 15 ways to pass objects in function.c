#include <iostream>
#include <conio.h>

using namespace std;

class Complex
{
    private:
        double Re, Im;
    public:
        Complex(double,double);
        Complex(){};
        double GetRe();
        double GetIm();
        void PutIm(double);
        void PutRe(double);
        void PrintComplex();
        void DivComp(Complex, Complex&); //1
        void pDivComp_(Complex, Complex*); //2
        Complex* pDivComp(Complex); //3
        void DivComp_P(Complex*,Complex&); //7
        void pDivComp_P(Complex*, Complex*); //8
        Complex* pDvComp(Complex*); //9

        Complex DivComplex(Complex); //12
        Complex operator*(Complex); //13
        friend void DivComp(Complex,Complex,Complex&); //14
        friend void DivComp2(Complex,Complex,Complex*); //15
};

void DivC(Complex, Complex,Complex&); //4

Complex* pDivCmp(Complex,Complex); //5

void DivCom(Complex,Complex, Complex*); //6

void DvCmp(Complex*,Complex*, Complex&); //10

Complex* pDvCmp(Complex*,Complex*); //11

Complex::Complex(double Re, double Im)
{
    this -> Re = Re;
    this -> Im = Im;
}

double Complex::GetRe() { return Re;}

double Complex::GetIm() { return Im;}

void Complex::PutRe(double Re)
{ this -> Re = Re; }

void Complex::PutIm(double Im)
{ this -> Im = Im; }

void Complex::PrintComplex()
{
    cout<<"Re = "<<Re<<", Im = "<<Im<<endl;
}

void Complex::DivComp(Complex B, Complex& CR)//1
{
    CR.Re = (Re*B.Re + Im*B.Im)/(Im*Im + B.Im*B.Im);
    CR.Im = (Im*B.Re - Re*B.Im)/(Im*Im + B.Im*B.Im);
}

void Complex::pDivComp_(Complex B, Complex* pC) //2
{
    pC -> Re = (Re*B.Re + Im*B.Im)/(Im*Im + B.Im*B.Im);
    pC -> Im = (Im*B.Re - Re*B.Im)/(Im*Im + B.Im*B.Im);
}

Complex* Complex::pDivComp(Complex B)//3
{
    Complex* pC;
    pC -> Re = (Re*B.Re + Im*B.Im)/(Im*Im + B.Im*B.Im);
    pC -> Im = (Im*B.Re - Re*B.Im)/(Im*Im + B.Im*B.Im);
    return pC;
}

void DivC(Complex A, Complex B,Complex& C) //4
{
    C.PutRe((A.GetRe()*B.GetRe() + A.GetIm()*B.GetIm())/
        (A.GetIm()*A.GetIm() + B.GetIm()*B.GetIm()));
    C.PutIm((A.GetIm()*B.GetRe() - A.GetRe()*B.GetIm())/
        (A.GetIm()*A.GetIm() + B.GetIm()*B.GetIm()));
}

Complex* pDivCmp(Complex A, Complex B) //5
{
    Complex *pC;
    pC -> PutRe((A.GetRe()*B.GetRe() + A.GetIm()*B.GetIm())/
        (A.GetIm()*A.GetIm() + B.GetIm()*B.GetIm()));
    pC -> PutIm((A.GetIm()*B.GetRe() - A.GetRe()*B.GetIm())/
        (A.GetIm()*A.GetIm() + B.GetIm()*B.GetIm()));
    return pC;
}

void DivCom(Complex A,Complex B, Complex* pC) //6
{
    pC -> PutRe((A.GetRe()*B.GetRe() + A.GetIm()*B.GetIm())/
        (A.GetIm()*A.GetIm() + B.GetIm()*B.GetIm()));
    pC -> PutIm((A.GetIm()*B.GetRe() - A.GetRe()*B.GetIm())/
        (A.GetIm()*A.GetIm() + B.GetIm()*B.GetIm()));
}

void Complex::DivComp_P(Complex* pB,Complex &C) //7
{
    C.PutRe((Re* pB -> GetRe() + Im* pB -> GetIm())/
        (Im*Im + (pB -> GetIm()) * (pB -> GetIm())));
    C.PutIm((Im*pB -> GetRe() - Re*(pB -> GetIm()))/
        (Im*Im + (pB -> GetIm()) * (pB -> GetIm())));
}

void Complex::pDivComp_P(Complex* pB, Complex* pC) //8
{
    pC -> PutRe((Re* pB -> GetRe() + Im* pB -> GetIm())/
        (Im*Im + (pB -> GetIm()) * (pB -> GetIm())));
    pC -> PutIm((Im*pB -> GetRe() - Re*(pB -> GetIm()))/
        (Im*Im + (pB -> GetIm()) * (pB -> GetIm())));
}

Complex* Complex::pDvComp(Complex* pB) //9
{
    Complex* pR;
    pR -> PutRe((Re* pB -> GetRe() + Im* pB -> GetIm())/
        (Im*Im + (pB -> GetIm()) * (pB -> GetIm())));
    pR -> PutIm((Im*pB -> GetRe() - Re*(pB -> GetIm()))/
        (Im*Im + (pB -> GetIm()) * (pB -> GetIm())));
    return pR;
}

void DvCmp(Complex* pA, Complex* pB, Complex& CR) //10
{
    CR.PutRe((pA -> GetRe() * pB -> GetRe() + pA -> GetIm() * pB -> GetIm())/
        (pA -> GetIm()*pA -> GetIm() + (pB -> GetIm()) * (pB -> GetIm())));
    CR.PutIm(( pA -> GetIm() *pB -> GetRe() - pA -> GetRe()*(pB -> GetIm()))/
        (pA -> GetIm()*pA -> GetIm() + (pB -> GetIm()) * (pB -> GetIm())));
}

Complex* pDvCmp(Complex* pA,Complex* pB) //11
{
    Complex* pC;
    pC -> PutRe((pA -> GetRe() * pB -> GetRe() + pA -> GetIm() * pB -> GetIm())/
        (pA -> GetIm()*pA -> GetIm() + (pB -> GetIm()) * (pB -> GetIm())));
    pC -> PutIm(( pA -> GetIm() *pB -> GetRe() - pA -> GetRe()*(pB -> GetIm()))/
        (pA -> GetIm()*pA -> GetIm() + (pB -> GetIm()) * (pB -> GetIm())));
    return pC;
}

Complex Complex::DivComplex(Complex B) //12
{
    Complex R;
    R.Re = (Re*B.Re + Im*B.Im)/(Im*Im + B.Im*B.Im);
    R.Im = (Im*B.Re - Re*B.Im)/(Im*Im + B.Im*B.Im);
    return R;
}

Complex Complex::operator*(Complex B) //13
{
    Complex R;
    R.Re = (Re*B.Re + Im*B.Im)/(Im*Im + B.Im*B.Im);
    R.Im = (Im*B.Re - Re*B.Im)/(Im*Im + B.Im*B.Im);
    return R;
}

void DivComp(Complex A, Complex B, Complex &C) //14
{
    C.Re = (A.Re*B.Re + A.Im*B.Im)/(A.Im*A.Im + B.Im*B.Im);
    C.Im = (A.Im*B.Re - A.Re*B.Im)/(A.Im*A.Im + B.Im*B.Im);
}

void DivComp2(Complex A ,Complex B, Complex *pC) //15
{
    pC -> Re = (A.Re*B.Re + A.Im*B.Im)/(A.Im*A.Im + B.Im*B.Im);
    pC -> Im = (A.Im*B.Re - A.Re*B.Im)/(A.Im*A.Im + B.Im*B.Im);
}

void main()
{
    clrscr();
    Complex A(-5,4);
    Complex B(-5,4);
    Complex C1,C4,C7,C8,C10,C12,C13,C14,C15;
    Complex *pC2, *pC3, *pC5, *pC6, *pC8, *pC9, *pC11;

    A.DivComp(B, C1);//1
    cout<<"C1 Division A.DivComp(B, C1): ";
    C1.PrintComplex();
    getch();

    A.pDivComp_(B, pC2); //2
    cout<<"C2 Division A.pDivComp_(B, pC2): ";
    pC2 -> PrintComplex();
    getch();

    pC3 = A.pDivComp(B); //3
    cout<<"C3 Division pC3 = A.pDivComp(B): ";
    pC3 -> PrintComplex();
    getch();

    DivC(A,B,C4); //4
    cout<<"C4 Division DivC(A,B,C4): ";
    C4.PrintComplex();
    getch();

    pC5 = pDivCmp(A,B); //5
    cout<<"C5 Division pC5 = pDivCmp(A,B): ";
    pC5 -> PrintComplex();
    getch();

    DivCom(A,B, pC6); //6
    cout<<"C6 Division DivCom(A,B, pC6): ";
    pC6 -> PrintComplex();
    getch();

    A.DivComp_P(&B, C7); //7
    cout<<"C7 Division A.DivComp_P(&B, C7): ";
    C7.PrintComplex();
    getch();

    A.pDivComp_P(&B, pC8); //8
    cout<<"C8 Division A.pDivComp_P(&B, pC8): ";
    pC8 -> PrintComplex();
    getch();

    A.pDivComp_P(&B, &C8); //8
    cout<<"C8 Division A.pDivComp_P(&B, &C8): ";
    C8.PrintComplex();
    getch();

    pC9 = A.pDvComp(&B); //9
    cout<<"C9 Division pC9 = A.pDvComp(&B): ";
    pC9 -> PrintComplex();
    getch();

    DvCmp(&A,&B,C10); //10
    cout<<"C10 Division DvCmp(&A,&B,C10): ";
    C10.PrintComplex();
    getch();

    pC11 = pDvCmp(&A, &B); //11
    cout<<"C11 Division pC11 = pDvCmp(&A, &B): ";
    pC11 -> PrintComplex();
    getch();

    C12 = A.DivComplex(B); //12
    cout<<"C12 Division A.DivComplex(B): ";
    C12.PrintComplex();
    getch();

    cout<<"C12 Division A.DivComplex(B).PrintComplex: "; //12
    A.DivComplex(B).PrintComplex();
    getch();

    C13=A*B; //13
    cout<<"C13 Division Overload C13=A*B: ";
    C13.PrintComplex();
    getch();

    DivComp(A,B,C14); //14
    cout<<"C14 Division DivComp(A,B,C14): ";
    C14.PrintComplex();
    getch();

    DivComp2(A,B,&C15); //15
    cout<<"C15 Division DivComp2(A,B,&C15): ";
    C15.PrintComplex();
    getch();
}
