#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;
vector<string> elements;

int main()
{
	string exp;
	cin >> exp;
	int index = 0;
	if (!exp.empty())
	{
		while ((index = exp.find(' ', index)) != string::npos)
		{
			exp.erase(index, 1);
		}
	}
	int len = exp.length();
	int i = 0;
	char temp[20];
	while (i < len)
	{
		switch (exp[i])
		{
		case '+':
		case '*':
		case '/':
		case '(':
		case ')':
		{
			temp[0] = exp[i];
			temp[1] = '\0';
			elements.push_back(temp);
			strcpy_s(temp, "");
			++i;
			break;
		}
		case '-':
		{
			if (i == 0 || elements.back() == "(")
			{
				elements.push_back("0");
				elements.push_back("-");
			}
			else
			{
				elements.push_back("-");
			}
			++i;
			break;
		}
		case '0':case'1':case'2':case'3':case'4':case'5':case'6':case'7':case'8':case'9':
		{
			int j = 0;
			while (i<len && exp[i] >= '0' && exp[i] <= '9')
			{
				temp[j] = exp[i];
				++j;
				++i;
			}
			temp[j] = '\0';
			elements.push_back(temp);
			strcpy_s(temp, "");
			break;
		}
		default:
			return -1;
		}
	}
	for (int i = 0; i<elements.size(); ++i)
		cout << elements[i];
	system("PAUSE");
	return 0;
}
