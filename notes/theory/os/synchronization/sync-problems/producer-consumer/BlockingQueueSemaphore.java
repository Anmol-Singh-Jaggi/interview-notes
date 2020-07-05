import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class BlockingQueueSemaphore {
    public static void main(String[] args) {
        BlockingQueue bq = new BlockingQueue();
        for (int i = 0; i < 6; i++) {
            Thread t1 = new Thread(new Task(bq, i));
            t1.start();
        }
        for (int i = 0; i < 6; i++) {
            Thread t1 = new Thread(new Task(bq, null));
            t1.start();
        }
    }
}

class BlockingQueue {
    Queue<Integer> queue = new LinkedList<Integer>();
    private final Integer capacity = 3;
    private final Semaphore access = new Semaphore(1);
    private final Semaphore emptySlots = new Semaphore(capacity);
    private final Semaphore occupiedSlots = new Semaphore(0);

    public void add(Integer elem) throws Exception {
        emptySlots.acquire();
        access.acquire();
        queue.add(elem);
        access.release();
        occupiedSlots.release();
    }

    public Integer remove() throws Exception {
        Integer ret = null;
        occupiedSlots.acquire();
        access.acquire();
        ret = queue.remove();
        access.release();
        emptySlots.release();
        return ret;
    }
}

class Task implements Runnable {
    private BlockingQueue bq;
    Integer elem = null;

    public Task(BlockingQueue bq, Integer elem) {
        this.bq = bq;
        this.elem = elem;
    }

    public void run() {
        try {
            if (this.elem != null) {
                bq.add(elem);
            } else {
                System.out.println(bq.remove());
            }
        } catch (Exception e) {

        }
    }
}