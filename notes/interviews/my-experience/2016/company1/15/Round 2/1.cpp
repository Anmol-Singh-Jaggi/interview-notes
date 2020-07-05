// Memoization solution
#include "options/default_code"
using namespace std;


typedef unsigned long long ULL;
typedef pair<int, int> Coordinate;
// State is a triplet <first, second, third> where
// first => Index of the coordinate of P1 in the list of coordinates
// second => Index of the coordinate of P2 in the list of coordinates
// third => Index of the coordinate of the next gem to be collected in the list of coordinates
// Initial state -> <0, 1, 2>
// Final states -> <x, y, n+2>, where n is the number of gems
typedef vector<int> State;


vector<Coordinate> allCoordinates;
// A map used to cache the answer for every state
map<State, int> minDistance;


size_t ChessboardDistance ( const Coordinate& coordinate1,
                            const Coordinate& coordinate2 )
{
	return max ( abs ( coordinate1.first - coordinate2.first ),
	             abs ( coordinate1.second - coordinate2.second ) );
}


size_t ChessboardDistance ( const State& state1,
                            const State& state2 )
{
	size_t coordinate1Index, coordinate2Index;

	if ( state1[0] != state2[0] )
	{
		coordinate1Index = state1[0];
		coordinate2Index = state2[0];
	}
	else
	{
		coordinate1Index = state1[1];
		coordinate2Index = state2[1];
	}

	const Coordinate& coordinate1 = allCoordinates[coordinate1Index];
	const Coordinate& coordinate2 = allCoordinates[coordinate2Index];

	return ChessboardDistance ( coordinate1, coordinate2 );
}


// Returns all the states whose next state is 'parentState'
// To understand, work out on paper the following example -:
// p1 = (1,1)
// p2 = (3,4)
// GemCoordinates = [(2,2), (3,2), (4,2), (1,1)]
vector<State> GetChildrenStates ( const State& parentState )
{
	vector<State> childrenStates;

	if ( parentState[0] == parentState[2] - 1 )
	{
		if ( parentState[1] == parentState[2] - 2 )
		{
			State childState ( parentState );
			childState[2]--;
			childState[0] -= 2;
			while ( childState[0] >= 0 )
			{
				if ( childState[0] == 1 )
				{
					childState[0]--;
				}
				childrenStates.push_back ( childState );
				childState[0]--;
			}
		}
		else
		{
			State childState ( parentState );
			childState[2]--;
			childState[0]--;
			childrenStates.push_back ( childState );
		}
	}
	else
	{
		if ( parentState[0] == parentState[2] - 2 )
		{
			State childState ( parentState );
			childState[2]--;
			childState[1] -= 2;
			while ( childState[1] >= 1 )
			{
				childrenStates.push_back ( childState );
				childState[1]--;
			}
		}
		else
		{
			State childState ( parentState );
			childState[2]--;
			childState[1]--;
			childrenStates.push_back ( childState );
		}
	}

	return childrenStates;
}


// Is the state valid?
bool IsValidState ( const State& state )
{
	return
	  // The coordinate indices cannot be negative
	  ( state[0] >= 0 )
	  // P1 cannot go to the inital location of P2
	  && ( state[0] != 1 )
	  // P1 cannot go to the inital location of P1
	  && ( state[1] >= 1 )
	  // The coordinates of the gems' locations start at index 2 in the allCoordinates array
	  && ( state[2] >= 2 )
	  // The coordinate-index of P1 cannot be equal or greater than that of the gem to be collected next (duh!)
	  && ( state[0] < state[2] )
	  // Same as above, but for P2
	  && ( state[1] < state[2] )
	  // P1 and P2 cannot be both cannot be at same coordinate-index simultaneously
	  && ( state[0] != state[1] )
	  // The coordinate-index of the gem to be collected next has to be less then allCoordinates's size (duh!)
	  && ( state[2] <= ( int ) allCoordinates.size() )
	  // Either one of the two persons' had moved to collect the gem in the previous transition
	  && ( ( state[0] + 1 == state[2] ) || ( state[1] + 1 == state[2] ) ) );
}


// Main function to calculate the answer corresponding to a state recursively
int Ans ( const State& state )
{
	assert ( IsValidState ( state ) );

	// Return the answer if it is cached
	if ( minDistance.find ( state ) != minDistance.end() )
	{
		return minDistance[state];
	}

	// Find the shortest path from this state to the initial state
	int ans = INT_MAX;
	const vector<State>& childrenStates = GetChildrenStates ( state );
	for ( size_t i = 0; i < childrenStates.size(); i++ )
	{
		const State& childState = childrenStates[i];
		ans = min ( ans, ( int ) ChessboardDistance ( state,
		            childState ) + Ans ( childState ) );
	}

	// Base case
	// Current state is the initial state
	if ( childrenStates.empty() )
	{
		ans = 0;
	}

	minDistance[state] = ans;
	return ans;
}

int main()
{
	int t;
	cin >> t;

	while ( t-- )
	{
		minDistance.clear();
		size_t gemCoordsSize;
		cin >> gemCoordsSize;

		vector<Coordinate> gemCoords ( gemCoordsSize );
		for ( size_t i = 0; i < gemCoordsSize; i++ )
		{
			cin >> gemCoords[i].first >> gemCoords[i].second;
		}

		Coordinate p1, p2;
		cin >> p1.first >> p1.second;
		cin >> p2.first >> p2.second;

		allCoordinates = gemCoords;
		allCoordinates.insert ( allCoordinates.begin(), p2 );
		allCoordinates.insert ( allCoordinates.begin(), p1 );

		int ans = INT_MAX;

		// Calculate the answers for all the final states
		// and return the smallest of them
		const int locationCount = allCoordinates.size();
		for ( int i = 0; i <= locationCount; i++ )
		{
			for ( int j = 0; j <= locationCount; j++ )
			{
				State state {locationCount - i, locationCount - j, locationCount};
				if ( IsValidState ( state ) )
				{
					ans = min ( ans, Ans ( state ) );
				}
			}
		}

		cout << ans << "\n";
		//print ( minDistance );
	}
}
