- Check if 2 binary trees are mirror or not.
- <https://www.geeksforgeeks.org/puzzle-9-find-the-fastest-3-horses/>
- <https://puzzling.stackexchange.com/questions/1959/candle-timing-measurement>
- 2 eggs and 100 floors puzzle.
- Interval scheduling.
- <https://stackoverflow.com/questions/43715207/how-to-prove-this-greedy-algorithm-as-optimal-rod-connection>
- Consistent hashing.
- Double checked singleton.
- Design a transaction system in which there is a class `Account`:

```java
class Account{
    public credit(int amt){
        // Credit money to account.
    }
    public debit(int amt){
        // Debit money from account.
    }
    public getBalance(){
        // Return current balance.
        // This should be non-blocking. Dirty read is allowed.
        // Dirty read meaning that some older value is also acceptable.
    }
    public getMiniStatement(){
        // Return the last 5 transactions in reverse time-sorted order.
        // Should be non blocking.. dirty read allowed.
    }
}
```
- How this was solved:

```java
class Transaction{
    public Transaction(int amount, Timestamp time, boolean isCredit){
        ...
    }
}

class TransactionBuffer{
    List<Transaction> txns = new ArrayList<>();
    // next is either the index of the next empty(null) cell
    // or the index of the oldest transaction (if the buffer gets full).
    // Note that the buffer will always remain full once its full.
    int next = 0;
    public TransactionBuffer(){
        for (int i=0;i<5;i++){
            txns.add(null);
        }
    }
    public addTxn(Transaction txn){
        txns[next] = txns;
        next = (next + 1) % 5
    }
    public getTxns(){
        // Return all transactions in time sorted order.
        List<> copy = new ArrayList<>(txns);
        copy.sort(timestamp)
        return copy;
        // Note that we could also have started iterating from next and get 5 elements but what if bufferis being modified
        // when this function is called.
        // The next pointer could be pointing to the wrong transaction (not necessarily the oldest).
    }
}
class Account{
    private int balance = 0;
    private TransactionBuffer buffer;
    public synchronized credit(int amt){
        balance += amt;
        buffer.addTxn(new Transaction(amt, time, 0));
    }
    public synchronized debit(int amt){
        if(amt > balance){
            throw error;
        }
        buffer.addTxn(new Transaction(amt, time, 0));
    }
    public getBalance(){
        return balance.
    }
    public getMiniStatement(){
        // Dirty read possible.
        // Note that even though this is not synchronized
        // But still there will be no inconsistency.
        // Lets say this function is called while the buffer is being modified.
        // any write operation on the list is a microprocessor load isntruction which is atomic.
        return buffer.getTxns();
    }
}
```