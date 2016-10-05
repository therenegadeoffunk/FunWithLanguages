#include <stdio.h>
#include <ctype.h>


int testarray[100];
int i;

int binary_search(int searchme[], int findme)
{
    int begin, mid, size;
    begin = 0;
    size = sizeof(searchme) - 1;
    mid = (size/2);
    while (begin <= size) {
        if (searchme[mid] == findme) {
            printf("We did it!\n");
            return 0;
        }
        else if (searchme[mid] < findme) {
            begin = mid + 1;
        }
        else {
            size = mid - 1;
        }
        mid = (begin + size)/2;
    }
    return 0;
}

int main(int argc, char *argv[])
{
    for (i = 0; i < 100; i++) {
    testarray[i] = i+1;
}
    binary_search(testarray, 7);
    return 0;
}
