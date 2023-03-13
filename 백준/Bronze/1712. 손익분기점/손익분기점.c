void breakevenpoint2()
{
	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);
	//printf("%d", sizeof(a));
	long long i;
	if (b == c)
		i = -1;
	else
	{
		i = a / (c - b) + 1;
		if (i < 0)
			i = -1;
	}
	printf("%d", i);
}

int main()
{
	breakevenpoint2();
	return 0;
}