#include <stdio.h>

void insertionSort(int arr[], int n);
void printArray(int arr[], int n);

int main()
{
    int n = 8;
    int arr[] = {5, 17, 3, 8, 1, 45, 2, 7};
    
    insertionSort(arr, n);
    printArray(arr, n);
    
    return 0;
}

void insertionSort(int arr[], int n)
{
   for(int i = 1; i < n; i++)
   {
       int curr = arr[i];
       int prev = i-1;
       
       while(prev >= 0 && arr[prev] > curr)
       {
           arr[prev+1] = arr[prev];
           prev--;
       }
       arr[prev+1] = curr;
   }
}

void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

------------------------------------------------------------------------------------------------------------------
output:-

1 2 3 5 7 8 17 45
--------------------------------
