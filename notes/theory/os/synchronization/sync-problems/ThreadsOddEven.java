import java.util.concurrent.Semaphore;

public class ThreadsOddEven {
    public static void main(String[] args) {
        Semaphore semOdd = new Semaphore(1);
        Semaphore semEven = new Semaphore(0);
        Thread oddThread = new Thread(new ThreadOdd(semOdd, semEven));
        Thread evenThread = new Thread(new ThreadEven(semOdd, semEven));
        oddThread.start();
        evenThread.start();
    }
}

class ThreadOdd implements Runnable {
    private int num = 1;
    private final Semaphore semOdd;
    private final Semaphore semEven;

    public ThreadOdd(Semaphore semOdd, Semaphore semEven) {
        this.semEven = semEven;
        this.semOdd = semOdd;
    }

    @Override
    public void run() {
        while (true) {
            try {
                semOdd.acquire();
                System.out.println(num);
                System.out.println("Odd");
                Thread.sleep(2000);
                num += 2;
                semEven.release();
            } catch (Exception e) {

            }
        }
    }
}

class ThreadEven implements Runnable {
    private int num = 2;
    private final Semaphore semOdd;
    private final Semaphore semEven;

    public ThreadEven(Semaphore semOdd, Semaphore semEven) {
        this.semEven = semEven;
        this.semOdd = semOdd;
    }

    @Override
    public void run() {
        while (true) {
            try {
                semEven.acquire();
                System.out.println(num);
                System.out.println("Even");
                Thread.sleep(2000);
                num += 2;
                semOdd.release();
            } catch (Exception e) {

            }
        }
    }
}