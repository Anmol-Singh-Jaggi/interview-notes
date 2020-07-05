import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class BlockingQueueMonitor {
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
    private final Lock mutex = new ReentrantLock();
    private final Condition notFull = mutex.newCondition();
    private final Condition notEmpty = mutex.newCondition();

    public void add(Integer elem) throws Exception {
        mutex.lock();
        while (queue.size() == capacity) {
            notFull.await();
        }
        queue.add(elem);
        notEmpty.signalAll();
        mutex.unlock();
    }

    public Integer remove() throws Exception {
        mutex.lock();
        Integer ret = null;
        while (queue.isEmpty()) {
            notEmpty.await();
        }
        ret = queue.remove();
        notFull.signalAll();
        mutex.unlock();
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