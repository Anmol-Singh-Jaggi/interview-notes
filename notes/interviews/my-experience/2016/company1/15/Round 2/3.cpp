#include "options/default_code"
using namespace std;

// Generate test cases
int main()
{
  srand ( time ( NULL ) );
  int t = 10000;
  cout << t << "\n";
  while ( t-- )
  {
    int gemCoordsSize = 10;
    cout << gemCoordsSize << "\n";
    while ( gemCoordsSize-- )
    {
      for ( size_t i = 0; i < 2; i++ )
      {
        int pos = rand() % 101;
        cout << pos << " ";
      }
      cout << "\n";
    }
    for ( size_t i = 0; i < 4; i++ )
    {
      int pos = rand() % 101;
      cout << pos << " ";
    }
    cout << "\n";
  }
}
