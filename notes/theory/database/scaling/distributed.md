# 2-Phase Commit Protocol

- Lets say we have a replication-enabled db cluster.
- For example, 3 machines and the write request can come to any machine.
- All the 3 databases need to always be in sync.
- For distributed atomicity, we use protocols like 2-phase protocol.
- In 2PC, there is one **Transaction Coordinator (TC)** and multiple **Transaction Participants (TP)**.
- Phase 1:
  - TC sends `preCommit` message to all TPs.
  - A TP will try to execute the transaction and commit it.
  - But it will not unlock the resources/locks etc at this point.
  - If successful, then reply back 'yes' to TC.
- Phase 2:
  - If TC got yes from all TP's, then send `doCommit` message to all TPs.
  - All TP's will then finally unlock the resources/locks etc.
  - On the other hand, even if one TP replied back with 'No', then TC will send `rollback` message to all TPs.
  - The TPs will then rollback their transactions (using journalling for example).
- Note that this is a **blocking** protocol since if the TC or TP fails, then all TP's/TC will be blocked and we will need manual intervention to resolve the transaction.   .

# 3-Phase Commit Protocol

- Similar to 2PC, but one more phase is introduced.
- TODO
