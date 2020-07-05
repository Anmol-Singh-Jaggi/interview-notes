import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedDeque;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class CriticalSection {
    public static void main(String[] args) throws Exception{
        // Make Account.inc() function as synchronized to get correct result!
        Account acc = new Account();
        List<Thread> threads = new ArrayList<>();
        for (int i = 0; i < 100; i++) {
            Thread t1 = new Thread(new Task(acc));
            threads.add(t1);
            t1.start();
        }
        for(Thread t1: threads){
            t1.join();
        }
        System.out.println(acc.elem);
    }
}

class Account {
    public Integer elem = 0;

    public void inc() {
        elem++;
    }
}

class Task implements Runnable {
    private Account acc;

    public Task(Account acc) {
        this.acc = acc;
    }

    public void run() {
        for (int i = 0; i < 1000; i++) {
            acc.inc();
        }

    }
}