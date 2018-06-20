#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int* a = new int [n];
	for (int i = 0; i < n; i++)
		cin >> a[i];
	int w[3]; //当前等待人数
	int time[3]; //等待总时长
	w[0] = w[1] = w[2] = 0;
	time[0] = time[1] = time[2] = 0;
	//传统
	for (int i = 0; i < n; i++)
	{
		int min;
		if (w[0] <= w[1] && w[0] <= w[2])
			min = 0;
		else if (w[1] <= w[0] && w[1] <= w[2])
			min = 1;
		else
			min = 2;
		w[min]++;
		time[min] += a[i];
	}
	int w1 = time[0] + time[1] + time[2];
	int t1;
	//新的
	int w2, t2[3];
	int now[3];
	now[0] = now[1] = now[2] = 0;
	t2[0] = t2[1] = t2[2] = 0;
	for (int i = 0; i < n; i++)
	{
		if (now[0] <= now[1] && now[0] <= now[2])
		{
			w2 += now[0];
			t2[0] += now[0];
			now[0] = a[i];
		}
		else if (now[1] <= now[2] && now[1] <= now[0])
		{
			w2 += now[1];
			t2[1] += now[1];
			now[1] = a[i];
		}
		else if (now[2] <= now[1] && now[2] <= now[0])
		{
			w2 += now[2];
			t2[2] += now[2];
			now[2] = a[2];
		}
	}
	//t2=min(t2)
}
