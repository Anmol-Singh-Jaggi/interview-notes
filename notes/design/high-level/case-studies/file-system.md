- Distributed file system:
  - Each file is divided into fixed-size partitions.
  - Partitions are stored on different machines.
  - A partition is replicated across the cluster.
  - All the metadata is stored on a "Master" node.
  - It stores `<fileName, map<chunkId, machineUrl>>`.
    