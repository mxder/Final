#include <iostream>
using namespace std;



int main()
{
	int p;
	int n;
	int* rest = new int[n];
	int* locallst = new int[p];
	int* local = new int[p];
	cin >> n >> p;
	for (int i = 0; i < p; i++)
		locallst[i] = i;
	for (int i = 0; i < n; i++)
	{
		cin >> rest[i];
	}
	

}
