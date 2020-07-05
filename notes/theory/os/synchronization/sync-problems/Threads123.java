import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Semaphore;

public class Threads123 {
    // Print 1,2,3,1,2,3.....
    public static void main(String[] args) {
        Semaphore sem1 = new Semaphore(1);
        Semaphore sem2 = new Semaphore(0);
        Semaphore sem3 = new Semaphore(0);
        List<Semaphore> sems = new ArrayList<>();
        sems.add(sem1);
        sems.add(sem2);
        sems.add(sem3);
        Thread t0 = new Thread(new MyThread(sems, 0));
        Thread t1 = new Thread(new MyThread(sems, 1));
        Thread t2 = new Thread(new MyThread(sems, 2));
        t0.start();
        t1.start();
        t2.start();
    }
}

class MyThread implements Runnable {
    private final int idx;
    private final List<Semaphore> sems;

    public MyThread(List<Semaphore> sems, int idx) {
        this.sems = sems;
        this.idx = idx;
    }

    @Override
    public void run() {
        while (true) {
            try {
                sems.get(idx).acquire();
                System.out.println(idx+1);
                Thread.sleep(2000);
                sems.get((idx + 1) % 3).release();
            } catch (Exception e) {

            }
        }
    }
}