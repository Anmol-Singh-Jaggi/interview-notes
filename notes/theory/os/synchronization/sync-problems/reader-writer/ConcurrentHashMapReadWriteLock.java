import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class ConcurrentHashMapReadWriteLock {
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
    private final ReadWriteLock lock = new ReentrantReadWriteLock();
    private Map<Integer, Integer> mapping = new HashMap<>();

    public void put(Integer key, Integer value) throws Exception {
        lock.writeLock().lock();
        mapping.put(key, value);
        lock.writeLock().unlock();
    }

    public Integer get(Integer key) throws Exception {
        Integer ret = null;
        lock.readLock().lock();
        ret = mapping.get(key);
        lock.readLock().unlock();
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