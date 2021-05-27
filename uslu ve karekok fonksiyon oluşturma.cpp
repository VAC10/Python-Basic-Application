//üslü işlem ve karekok fonksiyonları olusturalım
#include <iostream>
#include <cmath>
using namespace std;
int usal(int taban, int us)
{
	return pow(taban,us);
}
int karekok(int deger)
{
	return sqrt(deger);
}
int main(){
	int t,u,s;
cout<<"********us ve islemi*********"<<endl;
cout<<"lutfen bir taban degeri giriniz = ";
	cin>>t;
	cout<<"lutfen bir us degeri giriniz = ";
	cin>>u;
	cout<<"******karekok alma islemi*****"<<endl;
		cout<<"lutfen sayı degerini giriniz = ";
	cin>>s;
	cout<<"uslu sayi sonucu = "<< usal(t,u)<<endl;
	cout<<"karekok islemi sonucu ="<<karekok (s)<<endl;
	return 0;
	
	
}












	
	
	
	

	
