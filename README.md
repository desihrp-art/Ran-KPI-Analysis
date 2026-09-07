# RAN Performance & Optimization Analysis

## About This Project

This project demonstrates a practical 4G LTE RAN performance analysis workflow.

The main objective is to identify network performance issues, classify problematic cells, assess potential root causes, and define appropriate optimization directions based on KPI relationships.

The analysis focuses on **RAN performance and optimization**, while data processing is used only as a supporting tool.

## Key KPIs

* PRB Utilization
* DL Throughput
* UL Throughput
* CQI
* EUT
* Payload
* Cell Availability
* Rank

## Analysis Approach

The analysis follows a practical RAN optimization workflow:

**KPI Data → Performance Assessment → Issue Classification → Root Cause Investigation → Optimization Direction**

The analysis includes:

* Overall network KPI assessment
* Identification of worst-performing cells
* High PRB utilization analysis
* Low DL throughput analysis
* Low CQI analysis
* KPI relationship analysis
* Performance issue classification
* Root cause investigation
* Optimization recommendations

## KPI Summary

| KPI             |    Average | Initial Assessment           |
| --------------- | ---------: | ---------------------------- |
| PRB Utilization |     72.50% | Moderate                     |
| DL Throughput   | 15.99 Mbps | Requires cell-level analysis |
| UL Throughput   |  4.63 Mbps | Relatively stable            |
| CQI             |       9.60 | Moderate                     |
| EUT             | 14.58 Mbps | Requires cell-level analysis |
| Availability    |     99.67% | Good                         |

Overall network availability is good. However, several L1800 cells show high resource utilization combined with reduced throughput and CQI.

## Issue Classification

| Cell    | PRB Utilization | DL Throughput | CQI | Rank | Payload | Issue Classification       | RAN Indication                           |
| ------- | --------------: | ------------: | --: | ---: | ------: | -------------------------- | ---------------------------------------- |
| Cell001 |             72% |     18.5 Mbps |  10 |    2 | 42.5 GB | Normal                     | Performance relatively healthy           |
| Cell002 |             91% |      8.2 Mbps |   7 |    2 | 68.2 GB | Congestion + Radio Quality | High load with low CQI                   |
| Cell003 |             65% |     12.4 Mbps |  11 |    2 | 35.7 GB | Normal                     | No major performance issue indicated     |
| Cell004 |             88% |      9.5 Mbps |   8 |    2 | 61.4 GB | Congestion                 | High resource utilization                |
| Cell005 |             45% |     32.6 Mbps |  13 |    4 | 28.3 GB | Excellent                  | Good radio quality and capacity          |
| Cell006 |             95% |      5.8 Mbps |   6 |    2 | 75.6 GB | Critical                   | High load + poor radio quality           |
| Cell007 |             58% |     15.7 Mbps |  11 |    2 | 31.8 GB | Normal                     | Performance relatively healthy           |
| Cell008 |             83% |     11.2 Mbps |   9 |    2 | 55.2 GB | High Utilization           | Resource utilization requires monitoring |
| Cell009 |             39% |     38.4 Mbps |  14 |    4 | 24.6 GB | Excellent                  | Strong radio and capacity performance    |
| Cell010 |             89% |      7.6 Mbps |   7 |    2 | 64.8 GB | Congestion + Radio Quality | High load with low CQI                   |

### Performance Priority

1. **Cell006** — highest priority: high PRB, highest payload, low CQI and low DL throughput.
2. **Cell002** — high utilization combined with low CQI and low throughput.
3. **Cell010** — high utilization combined with low CQI and low throughput.
4. **Cell004** — high PRB utilization with relatively moderate CQI.
5. **Cell008** — high utilization but less severe performance degradation.

> Classification is based on simulated KPI data and represents performance indications requiring further investigation rather than confirmed root causes.

## Root Cause Analysis

### Cell006 — Critical Performance Issue

#### KPI Condition

* PRB Utilization: **95%**
* DL Throughput: **5.8 Mbps**
* CQI: **6**
* Rank: **2**
* Payload: **75.6 GB**
* Availability: **99.2%**

#### Performance Assessment

Cell006 shows a potential capacity and radio performance issue.

The combination of very high PRB utilization, high payload, low DL throughput, and low CQI indicates that the cell is heavily loaded while users are experiencing relatively poor radio conditions.

The high availability value indicates that the issue is not primarily related to cell availability.

#### Possible Root Causes

1. High traffic load / cell congestion
2. Poor radio quality affecting spectral efficiency
3. Interference or degraded radio conditions
4. Limited effective capacity on the serving cell
5. Potential traffic imbalance with neighboring cells

#### Recommended Investigation

* Traffic and active user trend
* PRB utilization trend
* CQI distribution
* DL/UL resource utilization
* Neighboring cell load
* Handover performance
* Coverage and radio quality indicators
* Rank distribution and MIMO performance

#### Initial Optimization Direction

Potential optimization actions include:

* Load balancing between neighboring cells
* Neighbor and handover optimization
* Radio parameter optimization
* Investigation of interference conditions
* Capacity expansion if sustained congestion is confirmed
* MIMO performance investigation if Rank distribution indicates degradation

The final optimization action should be based on the confirmed root cause rather than KPI threshold results alone.

---

### Cell002 — Congestion + Radio Quality

#### KPI Condition

* PRB Utilization: **91%**
* DL Throughput: **8.2 Mbps**
* CQI: **7**
* Rank: **2**
* Payload: **68.2 GB**
* Availability: **99.5%**

#### Performance Assessment

Cell002 shows a potential congestion condition combined with degraded radio quality.

High PRB utilization and high payload indicate significant traffic load, while low CQI and low DL throughput indicate reduced radio performance.

#### Possible Root Causes

* High traffic load
* Poor radio conditions
* Interference
* Traffic imbalance with neighboring cells
* Limited effective capacity

#### Recommended Investigation

* Traffic and active user trend
* CQI distribution
* Neighboring cell load
* Handover performance
* PRB utilization trend
* Radio quality indicators

#### Initial Optimization Direction

Investigate load balancing, neighbor and handover optimization, and radio conditions. Capacity enhancement should be considered if sustained congestion is confirmed.

---

### Cell010 — Congestion + Radio Quality

#### KPI Condition

* PRB Utilization: **89%**
* DL Throughput: **7.6 Mbps**
* CQI: **7**
* Rank: **2**
* Payload: **64.8 GB**
* Availability: **99.4%**

#### Performance Assessment

Cell010 shows a performance pattern similar to Cell002.

High PRB utilization and high payload indicate significant traffic load, while low CQI and low DL throughput indicate degraded radio performance.

#### Possible Root Causes

* High traffic load
* Poor radio conditions
* Interference
* Traffic imbalance
* Limited effective capacity

#### Recommended Investigation

* Traffic and active user trend
* CQI distribution
* Neighboring cell load
* Handover performance
* PRB utilization trend
* Radio quality indicators

#### Initial Optimization Direction

Investigate load balancing, neighbor optimization, handover performance, and radio conditions. Capacity enhancement should be considered if congestion remains persistent.

---

### Cell004 — Capacity / Congestion Indication

#### KPI Condition

* PRB Utilization: **88%**
* DL Throughput: **9.5 Mbps**
* CQI: **8**
* Rank: **2**
* Payload: **61.4 GB**
* Availability: **99.6%**

#### Performance Assessment

Cell004 shows high resource utilization with reduced DL throughput.

The CQI is relatively moderate, therefore the initial indication is more toward capacity or resource limitation than a severe radio quality problem.

#### Recommended Investigation

* Traffic trend
* Active users
* PRB utilization trend
* Neighboring cell capacity
* Load distribution
* CQI and throughput distribution

#### Initial Optimization Direction

Investigate load balancing and neighboring cell utilization before considering capacity expansion.

---

### Cell008 — High Utilization / Monitoring

#### KPI Condition

* PRB Utilization: **83%**
* DL Throughput: **11.2 Mbps**
* CQI: **9**
* Rank: **2**
* Payload: **55.2 GB**
* Availability: **99.7%**

#### Performance Assessment

Cell008 shows elevated resource utilization but does not demonstrate the same severity as Cell006, Cell002, or Cell010.

The cell should be monitored for increasing traffic load and further throughput degradation.

#### Recommended Investigation

* Traffic growth trend
* PRB utilization trend
* Active users
* CQI distribution
* Neighboring cell load

#### Initial Optimization Direction

Continue monitoring and consider preventive load balancing if traffic continues to increase.

## Healthy Cell Benchmark

### Cell005

Cell005 demonstrates strong performance with:

* PRB Utilization: **45%**
* DL Throughput: **32.6 Mbps**
* CQI: **13**
* Rank: **4**
* Availability: **99.9%**

The cell can be used as a performance benchmark for comparison with degraded L1800 cells.

### Cell009

Cell009 also demonstrates excellent performance with:

* PRB Utilization: **39%**
* DL Throughput: **38.4 Mbps**
* CQI: **14**
* Rank: **4**
* Availability: **99.9%**

The combination of low PRB utilization, high CQI, high throughput, and Rank 4 indicates strong radio resource efficiency.

## Overall RAN Assessment

The analyzed network shows generally good availability, with an average availability of **99.67%**.

However, several L1800 cells show high resource utilization combined with degraded throughput and CQI.

The most significant performance concerns are concentrated on:

1. **Cell006**
2. **Cell002**
3. **Cell010**
4. **Cell004**
5. **Cell008**

The KPI relationships indicate that performance degradation should not be assessed using a single KPI alone.

High PRB utilization combined with Payload, DL Throughput, CQI, and Rank provides a stronger basis for prioritizing cells and defining further investigation.

The recommended RAN optimization workflow is:

**KPI Monitoring → Problem Identification → Issue Classification → Root Cause Investigation → Optimization Action → Post-Optimization Monitoring**

## Tools

* Python
* Pandas

Python is used as a supporting tool for KPI data processing and analysis. The primary focus of this project is **RAN performance assessment, problem identification, root cause investigation, and optimization strategy**.

## Data

The dataset used in this project is simulated/anonymized and does not contain confidential operator data.


