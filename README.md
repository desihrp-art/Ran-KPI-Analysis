## Issue Classification

| Cell | PRB Utilization | DL Throughput | CQI | Rank | Payload | Issue Classification | RAN Indication |
|---|---:|---:|---:|---:|---:|---|---|
| Cell001 | 72% | 18.5 Mbps | 10 | 2 | 42.5 GB | Normal | Performance relatively healthy |
| Cell002 | 91% | 8.2 Mbps | 7 | 2 | 68.2 GB | Congestion + Radio Quality | High load with low CQI |
| Cell003 | 65% | 12.4 Mbps | 11 | 2 | 35.7 GB | Normal | No major performance issue indicated |
| Cell004 | 88% | 9.5 Mbps | 8 | 2 | 61.4 GB | Congestion | High resource utilization |
| Cell005 | 45% | 32.6 Mbps | 13 | 4 | 28.3 GB | Excellent | Good radio quality and capacity |
| Cell006 | 95% | 5.8 Mbps | 6 | 2 | 75.6 GB | Critical | High load + poor radio quality |
| Cell007 | 58% | 15.7 Mbps | 11 | 2 | 31.8 GB | Normal | Performance relatively healthy |
| Cell008 | 83% | 11.2 Mbps | 9 | 2 | 55.2 GB | High Utilization | Resource utilization requires monitoring |
| Cell009 | 39% | 38.4 Mbps | 14 | 4 | 24.6 GB | Excellent | Strong radio and capacity performance |
| Cell010 | 89% | 7.6 Mbps | 7 | 2 | 64.8 GB | Congestion + Radio Quality | High load with low CQI |

### Performance Priority

1. **Cell006** — highest priority: high PRB, highest payload, low CQI and low DL throughput.
2. **Cell002** — high utilization combined with low CQI and low throughput.
3. **Cell010** — high utilization combined with low CQI and low throughput.
4. **Cell004** — high PRB utilization with relatively moderate CQI.
5. **Cell008** — high utilization but less severe performance degradation.

> Classification is based on simulated KPI data and represents performance indications requiring further investigation rather than confirmed root causes.

