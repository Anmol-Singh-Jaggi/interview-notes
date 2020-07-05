// Brute force
#include "options/default_code"
using namespace std;


typedef unsigned long long ULL;
typedef pair<int, int> Coordinate;


Coordinate p1Coord;
Coordinate p2Coord;
vector<Coordinate> gemCoords;


size_t ChessboardDistance ( const Coordinate& coordinate1,
                            const Coordinate& coordinate2 )
{
  return max ( abs ( coordinate1.first - coordinate2.first ),
               abs ( coordinate1.second - coordinate2.second ) );
}


// bitmask is a binary string where the value at index 'i' denotes which of p1 and p2 moved to collect gemCoords[i]
// '0' means p1 moved and '1' means p2 moved
size_t ComputeDistance ( const ULL& bitmask )
{
  // The distance travelled by both p1 and p2
  size_t distance = 0;
  Coordinate p1 = p1Coord;
  Coordinate p2 = p2Coord;

  // gemIndex = The index of the gem we have to collect next
  for ( size_t gemIndex = 0; gemIndex < gemCoords.size(); gemIndex++ )
  {
    if ( bitmask & ( ( ULL ) 1 << gemIndex ) )
    {
      // Move p2 to the next gem and update the distance travelled so far
      distance += ChessboardDistance ( p2, gemCoords[gemIndex] );
      p2 = gemCoords[gemIndex];
    }
    else
    {
      // Move p1 to the next gem and update the distance travelled so far
      distance += ChessboardDistance ( p1, gemCoords[gemIndex] );
      p1 = gemCoords[gemIndex];
    }
  }

  // Make sure that one of the two persons have collected the last gem
  assert ( p1 == gemCoords[gemCoords.size() - 1]
           || p2 == gemCoords[gemCoords.size() - 1] );

  return distance;
}


// Extracts the subset indices from the bitmask
string DecodeMask ( ULL bitMask )
{
  string decodedMask;

  for ( size_t i = 0; i < gemCoords.size(); i++ )
  {
    if ( bitMask & ( ( ULL ) 1 << i ) )
    {
      decodedMask.push_back ( '1' );
    }
    else
    {
      decodedMask.push_back ( '0' );
    }
  }

  return decodedMask;
}


int main()
{
  int t;
  cin >> t;

  while ( t-- )
  {
    size_t gemCoordsSize;
    cin >> gemCoordsSize;

    gemCoords.resize ( gemCoordsSize );
    for ( size_t i = 0; i < gemCoordsSize; i++ )
    {
      cin >> gemCoords[i].first >> gemCoords[i].second;
    }

    cin >> p1Coord.first >> p1Coord.second;
    cin >> p2Coord.first >> p2Coord.second;

    const ULL number_of_possibilities = ( ULL ) 1 << gemCoords.size();
    size_t minDistance = INT_MAX;
    ULL answerBitmask = 0;

    for ( ULL bitmask = 0; bitmask < number_of_possibilities; bitmask++ )
    {
      size_t currentDistance = ComputeDistance ( bitmask );
      //print ( bitmask );
      //print ( currentDistance );
      if ( currentDistance < minDistance )
      {
        minDistance = currentDistance;
        answerBitmask = bitmask;
      }
    }

    cout << minDistance << "\n";
    //print ( answerBitmask );
    //print ( DecodeMask ( answerBitmask ) );
  }
}
