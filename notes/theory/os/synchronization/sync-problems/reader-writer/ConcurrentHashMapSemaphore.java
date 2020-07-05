import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Semaphore;

public class ConcurrentHashMapSemaphore {
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
    private final Semaphore write_access = new Semaphore(1);
    private final Semaphore read_access = new Semaphore(1);
    private Integer numReaders = 0;
    private Map<Integer, Integer> mapping = new HashMap<>();

    public void put(Integer key, Integer value) throws Exception {
        write_access.acquire();
        mapping.put(key, value);
        write_access.release();
    }

    public Integer get(Integer key) throws Exception {
        Integer ret = null;
        read_access.acquire();
        numReaders++;
        if(numReaders == 1){
            write_access.acquire();
        }
        read_access.release();
        ret = mapping.get(key);
        read_access.acquire();
        numReaders--;
        if(numReaders == 0){
            write_access.release();
        }
        read_access.release();
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