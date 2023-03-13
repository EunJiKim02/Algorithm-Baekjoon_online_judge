#include<iostream>
#include<vector>
#define SWAP(x, y, temp) temp=x,x=y,y=temp

using namespace std;

typedef struct node{
	int data;
	struct node* rlink;
	struct node* llink;
}Node;

void postorder(Node * h)
{
	if (h!=NULL){
		postorder(h->llink);
		postorder(h->rlink);
		cout << h->data << '\n';
	}
}

Node * insert(Node* h, int dd)
{
	Node* k = (Node*)malloc(sizeof(Node));
	k->data = dd;
	k->llink = NULL;
	k->rlink = NULL;
	Node* p = h;
	if (!h) 
		h = k;
	else {
		while (1) {
			if (p->data > k->data) {
				if (!p->llink) {
					p->llink = k;
					break;
				}
				p = p->llink;
			}
			else if (p->data < k->data) {
				if (!p->rlink) {
					p->rlink = k;
					break;
				}
				p = p->rlink;
			}
		}
	}
	return h;
}

int main() {
	int n;
	Node* k = NULL;
	while (cin >> n){
		k = insert(k, n);
	}
	postorder(k);
}