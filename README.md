# Scheduling Simulator
##### Simulator for `FCFS`, `SPN`, `RR`, `SRT` algorithms
## Input to the program
This program gets the `.xlsx` file name as the timeline of the process' computation or I/O time needed
##### This timeline should follow the following format
<table>
    <tr>
        <td><strong>P <code>1</code></strong></td>
        <td><strong>P <code>2</code></strong></td>
    </tr>
    <tr>
        <td><code>0</code></td>
        <td><code>5</code></td>
    </tr>
    <tr>
        <td>CPU <code>10</code></td>
        <td>CPU <code>2</code></td>
    </tr>
    <tr>
        <td>DISK <code>1</code></td>
        <td>CPU <code>5</code></td>
    </tr>
    <tr>
        <td>NET <code>3</code></td>
        <td>NET <code>2</code></td>
    </tr>
    <tr>
        <td>CPU <code>8</code></td>
        <td>CPU <code>20</code></td>
    </tr>
    <tr>
        <td>NET <code>2</code></td>
    </tr>
</table>

* Every column starts with *P* + *process id*
* Preceding rows contains the *arrival time*
* Next rows represent the timeline of the each process
    * Each rows contains resource label followed by time the resource will be used
    * Supported resources are `CPU`, `DISK`, `NET`

## Output
The program then generates a new `.xlsx` file for every algorithm
##### Output has the following format
<table>
    <tr>
        <td><strong>Process id</strong></td>
        <td><strong>AT</strong></td>
        <td><strong>WT</strong></td>
        <td><strong>CT</strong></td>
        <td><strong>TAT</strong></td>
    </tr>
    <tr>
        <td>P1</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>P2</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>P3</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>P4</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>

`Average waiting time`, `Average running time`, `Average turnaround time`, `CPU utilization` and `throughput`
are prompted in the program as the algorithms runs.

### Algorithm implementation
##### Each algorithm are implemented separately in the `algorithm` folder
To implement a new algorithm 2 methods from `base.py` needs to be overloaded
1. pick_next
2. init_queue
`pick_next` should return the next process as it called
`init_queue` will initiate the queue that might be needed for various scheduling
algorithm, although some algorithm might not require it     
