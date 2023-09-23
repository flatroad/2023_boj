#include <iostream>
#include <list>

void	get_number(int *arr, int count, int n, int cucl, std::list<int> stk)
{
	if (count == 6)
	{
		std::list<int>::iterator it;
		std::list<int>::iterator end = --stk.end();
		for (it = stk.begin(); it != end; it++)
			std::cout << *it << " ";
		std::cout << *it << std::endl;
		return ;
	}
	for (int i = n;  i < cucl + 6 && i <= n + cucl; i++)
	{
		stk.push_back(arr[i]);
		get_number(arr, count + 1, i + 1, cucl, stk);
		stk.pop_back();
	}
	return ;
}

int main()
{
	std::list<int> stk;
	while (1)
	{
		int num = 0;
		std::cin >> num;
		if (num == 0)
			break ;
		int arr[num];
		for (int i = 0; i < num; i++)
			std::cin >> arr[i];
		get_number(arr, 0, 0, num - 6, stk);
		std::cout << std::endl;
	}
}