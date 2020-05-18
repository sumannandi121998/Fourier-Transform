#include <stdio.h>
#include <math.h>
#include <complex.h>
#include <gsl/gsl_fft_complex.h>

#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])

float f(float x) //given sinc function
 { 
   if (x==0)
    return 1;
   else
    return sin(x)/x;
 }
int main ()
{
  int i,n;
  float dx,pi,k[128],xmin,xmax; 
  double data[2*128];
  double complex z1,z2,z;
  xmin=-50; //minimum value of x
  xmax=50; //maximum value of x
  n=128; //no of discrete points
  pi=3.141;
  dx=(xmax-xmin)/(n-1); //distance between two consecutive points
  

  for (i = 0; i < n; i++)
    {
       REAL(data,i) = f(xmin+i*dx); IMAG(data,i) = 0.0; //sampling the function in n discrete points
    }


  gsl_fft_complex_radix2_forward (data, 1, n); //dft of n points using gsl function

  for (i = 0; i < n; i++) //defining values of k in fourier space
  {
    if (i<n/2)
    k[i]=2*pi*i/(n*dx);
    else if (i==n/2)
    k[i]=-pi/dx;
    else
    k[i]=-k[n-i];
  }
  for (i = 0; i <n; i++)
  { 
   z1=cos(xmin*k[i])-sin(xmin*k[i])*I; //real and imaginary part of phase factor
   z2=REAL(data,i)+IMAG(data,i)*I; //real and imaginary part of dft
   z=dx*z1*z2/sqrt(2*pi); //FT of the sinc function

   printf ("%f %e %e\n",k[i],creal(z),cimag(z)); //printing the result
  }

  return 0;
}
