
## Now

*   metrics
    +   accumulation vs raw metrics, i.e. calculate now or later

*   implementation
    +   metric sampling and aggregation
    +   role execution: base node launches other role, communication

### done

*   implementation
    +   discovery, config, data protocols and message structures

*   design
    +   design goals: simple, minimal network traffic
    +   fault tolerance

*   future work
    +   split-brain syndrome is not handled; assumed network topology set up appropriately
    +   multiple-level branches
    +   auto-split large groups into multiple branches
    +   use events instead of polling

*   configuration

## Later

*   implementation
    +   recovery protocol

*   zeromq primer
    +   why zmq
    +   socket types
    +   message patterns

*   replace recovery algorithms with pseudo code and algorithm package
