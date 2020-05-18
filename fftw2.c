#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <fftw3.h>
#include <complex.h>

float f(float x) //given gaussian function
 { 
    return exp(-x*x);
 }

void main () 
{
  int i,n;
  float dx,pi,k[256],xmin,xmax;
  double complex z1,z2,z;
  xmin=-50; //minimum value of x
  xmax=50; //maximum value of x
  n=256; //no of discrete points
  pi=3.141;
  dx=(xmax-xmin)/(n-1); //distance between two consecutive points
  fftw_complex data[n], dft[n];
  fftw_plan p;

  for(i=0; i<n; i++) //sampling the function in n discrete points 
    {
      data[i][0] = f(xmin+i*dx); 
      data[i][1] = 0.0;
    }

  p = fftw_plan_dft_1d(n,data, dft,FFTW_FORWARD, FFTW_ESTIMATE); //dft of n points using FFTW
  fftw_execute(p);

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
    z2=dft[i][0]+dft[i][1]*I; //real and imaginary part of dft
    z=dx*z1*z2/sqrt(2*pi); //FT of the sinc function

    printf ("%f %e %e\n",k[i],creal(z),cimag(z)); //printing the result
  }

  fftw_destroy_plan(p);
}
