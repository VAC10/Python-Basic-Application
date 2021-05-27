#include <iostream>
using namespace std;
const double pi =3.14;
double alan(int r){
	return pi*r*r;
	cout<<"dairenin alani =";
}


double cevre(int r){
	return 2*pi*r;
	cout<<"dairenin cevresi =";
	
}

int main(){
	int yaricap;
	cout<<"lutfen yaricap degiskenini giriniz:";
	cin>>yaricap;
	cout<<"dairenin alani:"<<alan(yaricap)<<endl;
	cout<<"dairenin cevresi:"<<cevre(yaricap);
	
	
	
	
	
	
}
