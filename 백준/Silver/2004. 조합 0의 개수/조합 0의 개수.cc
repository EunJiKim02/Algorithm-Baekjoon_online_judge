#include <iostream>


void getnumber(unsigned long k, int* count, unsigned long n)
{
	unsigned long tem = k;
	while (1)
	{
		if ((n / k) == 0)
			break;
		*count += (n / k);
		k *= tem;
	}
}

int main()
{
	unsigned long n, m;
	std::cin >> n >> m;

	if (m > (n / 2))
		m = n - m;
	int cnt2_1=0, cnt5_1=0;
	int cnt2_2=0, cnt5_2=0;

	//분자 : n!
	getnumber(2, &cnt2_1, n);
	getnumber(5, &cnt5_1, n);
	
	//분모 : m!(n-m)!
	getnumber(2, &cnt2_2, m);
	getnumber(2, &cnt2_2, (n - m));
	getnumber(5, &cnt5_2, m);
	getnumber(5, &cnt5_2, (n - m));


	int a = cnt2_1 - cnt2_2;
	int b = cnt5_1 - cnt5_2;
	//printf("%d %d / %d %d\n", cnt2_1, cnt5_1, cnt2_2, cnt5_2);
	printf("%d",(a > b) ? b : a);
}