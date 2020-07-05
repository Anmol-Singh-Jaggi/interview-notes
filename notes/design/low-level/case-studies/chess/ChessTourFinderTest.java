import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.lang.Math;

public class ChessTourFinderTest {
    private static boolean isValidMove(Pair newPosition, Pair oldPosition) {
        int newX = newPosition.getFirst();
        int newY = newPosition.getSecond();
        int oldX = oldPosition.getFirst();
        int oldY = oldPosition.getSecond();
        int deltaX = newX - oldX;
        int deltaY = newY - oldY;
        if (Math.abs(deltaX) == 2 && Math.abs(deltaY) == 2) {
            return true;
        }
        if ((Math.abs(deltaX) == 3 && deltaY == 0) || (deltaX == 0 && Math.abs(deltaY) == 3)) {
            return true;
        }
        return false;
    }

    public static boolean isTourValid(Pair boardDimensions, List<Pair> tour) {
        // Check if size of tour is as expected.
        int rows = boardDimensions.getFirst();
        int cols = boardDimensions.getSecond();
        if (tour.size() != rows * cols) {
            return false;
        }
        // Check if every position is within the board.
        for (Pair position : tour) {
            int posX = position.getFirst();
            int posY = position.getSecond();
            if (posX < 0 || posY < 0 || posX >= rows || posY >= cols) {
                return false;
            }
        }
        // Check if pos[i+1] can be reached from pos[i] through valid rules.
        for (int i = 1; i < tour.size(); i++) {
            Pair newPosition = tour.get(i);
            Pair oldPosition = tour.get(i - 1);
            if (!isValidMove(newPosition, oldPosition)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Pair boardDimensions = new Pair(10, 10);
        Pair startPosition = new Pair(0, 0);
        ChessTourFinder tourFinder = new ChessTourFinder();
        // First test
        List<Pair> tour = tourFinder.findTour(boardDimensions, startPosition);
        assert (isTourValid(boardDimensions, tour));
        startPosition = new Pair(5, 5);
        // Second test
        tour = tourFinder.findTour(boardDimensions, startPosition);
        assert (isTourValid(boardDimensions, tour));
        System.out.println("Tests succeeded!");
    }
}