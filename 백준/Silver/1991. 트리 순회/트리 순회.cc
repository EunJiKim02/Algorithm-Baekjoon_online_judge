#include<iostream>

using namespace std;

bool alphaempty[26] = { 0 };
typedef struct tree {
	char data;
	struct tree* leftchild;
	struct tree* rightchild;
}Tree;

void inorder(Tree* ptr)
{
	if (ptr)
	{
		inorder(ptr->leftchild);
		cout << ptr->data;
		inorder(ptr->rightchild);
	}
}

void preorder(Tree* ptr)
{
	if (ptr)
	{
		cout << ptr->data;
		preorder(ptr->leftchild);
		preorder(ptr->rightchild);
	}
}

void postorder(Tree* ptr)
{
	if (ptr)
	{
		postorder(ptr->leftchild);
		postorder(ptr->rightchild);
		cout << ptr->data;
	}
}

int main(void)
{
	int repeat;
	cin >> repeat;
	Tree* r;
	Tree** node = (Tree**)malloc(sizeof(Tree*) * repeat);
	for (int i = 0; i < repeat; i++)
	{
		node[i] = (Tree*)malloc(sizeof(Tree));
		node[i]->data = i + 'A';
		node[i]->leftchild = NULL;
		node[i]->rightchild = NULL;
	}
	r = node[0];
	for (int i = 0; i < repeat; i++)
	{
		char data, left, right;
		cin >> data >> left >> right;
		if (left != '.')
			node[data - 'A']->leftchild = node[left - 'A'];
		if (right != '.')
			node[data - 'A']->rightchild = node[right - 'A'];
	}

	preorder(r);
	cout << "\n";
	inorder(r);
	cout << "\n";
	postorder(r);

	return 0;
}
