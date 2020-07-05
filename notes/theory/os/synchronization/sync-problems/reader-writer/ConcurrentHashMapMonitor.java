import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Semaphore;

public class ConcurrentHashMapMonitor {
    public static void main(String[] args) {
        ConcurrentHashMap mapping = new ConcurrentHashMap();
        for (int i = 0; i < 50; i++) {
            Thread t1 = new Thread(new Task(mapping, i, i + 1));
            t1.start();
        }
        for (int i = 0; i < 50; i++) {
            Thread t1 = new Thread(new Task(mapping, i, null));
            t1.start();
        }
    }
}

class ConcurrentHashMap {
    private final Semaphore exclusiveAccess = new Semaphore(1);
    private final Semaphore numReadersAccess = new Semaphore(1);
    // serviceQueue is to ensure fairness (FIFO).
    private final Semaphore serviceQueue = new Semaphore(1, true);
    private Integer numReaders = 0;
    private Map<Integer, Integer> mapping = new HashMap<>();

    public void put(Integer key, Integer value) throws Exception {
        serviceQueue.acquire();
        exclusiveAccess.acquire();
        serviceQueue.release();
        mapping.put(key, value);
        exclusiveAccess.release();
    }

    public Integer get(Integer key) throws Exception {
        serviceQueue.acquire();
        Integer ret = null;
        numReadersAccess.acquire();
        numReaders++;
        if(numReaders == 1){
            exclusiveAccess.acquire();
        }
        serviceQueue.release();
        numReadersAccess.release();
        ret = mapping.get(key);
        numReadersAccess.acquire();
        numReaders--;
        if(numReaders == 0){
            exclusiveAccess.release();
        }
        numReadersAccess.release();
        return ret;
    }
}

class Task implements Runnable {
    private ConcurrentHashMap mapping;
    private Integer key;
    private Integer value;

    public Task(ConcurrentHashMap mapping, Integer key, Integer value) {
        this.mapping = mapping;
        this.key = key;
        this.value = value;
    }

    public void run() {
        try {
            if (value == null) {
                System.out.println(key.toString() + " = " + mapping.get(key).toString());
            } else {
                mapping.put(key, value);
            }
        } catch (Exception e) {
        }
    }
}