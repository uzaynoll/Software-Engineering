#include<stdio.h>
#include<math.h>
float Cmean(int list[],int b)
{
    int i;
    float mean,s;
    for(i=0;i<b;i++)
    {
        s+=list[i];
    }
    mean=s/b;
    return(mean);
}

float Csd(int list[], int b)
{
    float sum = 0.0, mean, SD = 0.0;
    mean= Cmean(list,8);
    for (int i = 0; i < b; i++)
        SD += pow(list[i] - mean, 2);
    return sqrt(SD / 8);
}

void testMean(float input,float output)
{
 if(input == output)
 printf("\nMean Function is working properly");
 else
 printf("\nMean Function is not working properly");
}

void testSD(float input,float output)
{
 if(input == output)
 printf("\nStandard Deviation Function is working properly");
 else
 printf("\nStandard Deviation Function is not working properly");
}

int main()
{
    int list[8]={10, 12, 23, 23, 16, 23, 21, 16};
    float mean= Cmean(list,8);
    float sd=Csd(list,8);
    printf("The mean of the provided numbers is %.3f\n",mean);
    printf("The Standard deviation of the provided numbers is %.3f\n",sd);
    testMean(mean,18.000);
    testSD(sd,sqrt(24));
}
