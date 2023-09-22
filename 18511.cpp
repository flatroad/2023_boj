#include <iostream>
#include <deque>

void re_div(int flag, int max_num, int dev, int ans, int l_num, int *arr, int dev_num, int k)
{
	k = k + 1;
	if (dev == 0)
	{
		if (ans > max_num)
			return ;
		else
		{
			std::cout << ans << std::endl;
			exit(0);
		}
	}
	if (flag == 1)
	{
		while (dev != 0)
		{
			ans = ans + (l_num * dev);
			dev = dev / 10;
		}
		std::cout << ans << std::endl;
		exit(0);
	}
	int memo = 0;
	memo = dev_num / dev;
	dev_num = dev_num % dev;
	for (int i = memo; i > 0; i--)
	{
		if (arr[i] == 1)
		{
			if (i < memo)
				flag = 1;
			ans = ans + (i * dev);
			re_div(flag, max_num, dev / 10, ans, l_num, arr, dev_num, k);
			ans = ans - (i * dev);
			flag = 0;
		}
	}
	if (k == 1)
		re_div(1, max_num, dev / 10, ans, l_num, arr, dev_num, k);
	else
		return ;
}


int main(int argc, char **argv)
{
	int max_num;
	int number_list;
	int num;
	int l_num = 0;

	std::cin >> max_num >> number_list;
	
	int arr[10];
	for (int i = 0; i <= 9; i++)
		arr[i] = 0;
	for (int i = 0; i < number_list; i++)
	{
		std::cin >> num;
		if (l_num < num)
			l_num = num;
		arr[num] = 1;
	}

	int dev = 100000000;
	while (dev / max_num != 0)
		dev = dev / 10;
	int ans = 0;
	int flag = 0;

	re_div(0, max_num, dev, ans, l_num, arr, max_num, 0);
}

