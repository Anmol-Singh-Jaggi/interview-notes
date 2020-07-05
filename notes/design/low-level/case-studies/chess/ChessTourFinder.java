import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.lang.Math;

public class ChessTourFinder {
    private List<Pair> getNeighbours(Pair boardDimensions, Pair position) {
        int positionX = position.getFirst();
        int positionY = position.getSecond();
        List<Pair> neighbours = new ArrayList<>();
        // 4 straight
        neighbours.add(new Pair(positionX - 3, positionY));
        neighbours.add(new Pair(positionX, positionY + 3));
        neighbours.add(new Pair(positionX + 3, positionY));
        neighbours.add(new Pair(positionX, positionY - 3));
        // 4 diagonal
        neighbours.add(new Pair(positionX - 2, positionY + 2));
        neighbours.add(new Pair(positionX + 2, positionY + 2));
        neighbours.add(new Pair(positionX + 2, positionY - 2));
        neighbours.add(new Pair(positionX - 2, positionY - 2));
        // Filter out all the positions which are not inside the board.
        int rows = boardDimensions.getFirst();
        int cols = boardDimensions.getSecond();
        List<Pair> validNeighbours = new ArrayList<>();
        for (Pair neighbour : neighbours) {
            int posX = neighbour.getFirst();
            int posY = neighbour.getSecond();
            if (posX >= 0 && posY >= 0 && posX < rows && posY < cols) {
                validNeighbours.add(neighbour);
            }
        }
        return validNeighbours;
    }

    private boolean findTour(Pair boardDimensions, Pair position, Set<Pair> visited, List<Pair> tour) {
        visited.add(position);
        tour.add(position);
        if (tour.size() == boardDimensions.getFirst() * boardDimensions.getSecond()) {
            return true;
        }
        for (Pair neighbour : getNeighbours(boardDimensions, position)) {
            if (!visited.contains(neighbour)) {
                boolean isTourFound = findTour(boardDimensions, neighbour, visited, tour);
                if (isTourFound) {
                    return true;
                }
            }
        }
        visited.remove(position);
        tour.remove(tour.size() - 1);
        return false;
    }

    public List<Pair> findTour(Pair boardDimensions, Pair startPosition) {
        List<Pair> tour = new ArrayList<>();
        findTour(boardDimensions, startPosition, new HashSet<>(), tour);
        return tour;
    }

    public static void main(String[] args) {
        Pair boardDimensions = new Pair(10, 10);
        Pair startPosition = new Pair(0, 0);
        ChessTourFinder tourFinder = new ChessTourFinder();
        List<Pair> tour = tourFinder.findTour(boardDimensions, startPosition);
        // The tour will be empty if no tour possible.
        System.out.println(tour);
    }
}
