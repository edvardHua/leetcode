#include<iostream>
#include<malloc.h>

using namespace std;

class Solution{
    public:

};

static float calc_c(const float* data, int size)
{
    float sum = 0.f;
    
    for (int i = 0; i < size; ++i) {
        sum += data[i];
    }
    
    return sum;
}


int main()
{
    int c = 1000000;
    float* d = (float *)malloc(sizeof(float)*c);
    for (int i = 0; i < 10; i ++){
        cout << d[i] << endl;
    }
    return 0;
}