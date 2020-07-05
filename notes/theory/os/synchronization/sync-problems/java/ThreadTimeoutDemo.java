import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public class ThreadTimeoutDemo {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Future<String> future = executor.submit(new Task2());

        try {
            System.out.println("Started..");
            System.out.println(future.get(1, TimeUnit.SECONDS));
            System.out.println("Finished!");
        } catch (TimeoutException e) {
            future.cancel(true);
            System.out.println("Terminated!");
        }

        executor.shutdownNow();
        System.out.println("Finished!!");
        // Note that JVM might not exit because of the thread still working...
        // There is no way to stop it apart from continuously checking inside the task.
    }
}

class Task implements Callable<String> {
    @Override
    public String call() throws Exception {
        int i = 9;
        while (i < 10) {
            i = i - 1;
            i = i + 1;
            // There is no way to kill this thread.
        }
        int j = i / 2;
        System.out.println(j);
        return "Ready!";
    }
}

class Task2 implements Callable<String> {
    @Override
    public String call() throws Exception {
        int i = 9;
        while (i < 10) {
            i = i - 1;
            i = i + 1;
            if(Thread.currentThread().isInterrupted()){
                break;
            }
        }
        int j = i / 2;
        System.out.println(j);
        return "Ready!";
    }
}