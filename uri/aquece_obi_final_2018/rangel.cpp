#include <iostream>

using namespace std;

int main() {
   int A, B, ai, aj;
   

   cin >> A;
   int numbers[A];
   for (int i=0; i<A; i++ ) {
        cin >> B;
        numbers[i] = B;
    }
   
   
   bool achei;
   for (int i=0; i<A; i++ ) {
        achei = false;
        for (int j=i+1; j<A-1; j++){
            ai = numbers[i];
            aj = numbers[j];
            if (aj>ai){
                cout  << aj << ' ';
                achei = true;
                break;
            }
        }
        if (!achei)
            if (i == A-1)
                cout << '*' << endl;
            else
                cout << '*' << ' ';    
    }
   
  return 0;
}
