# Pipelined vs Nonpipelined Execution Simulator

A Python simulation that compares the execution time of **pipelined** and **nonpipelined** instruction processing, and shows how instruction overlap affects performance as the workload grows.

Built as a Computer Architecture course project.

## How it works

| | Nonpipelined | Pipelined |
|---|---|---|
| File | `nonpipelined_simulator.py` | `pipelined_simulator.py` |
| Model | Instructions run one after another | 5-stage pipeline, one thread per stage |
| Timing | 800 µs per instruction (`time.sleep(0.0008)`) | 200 µs per stage (`time.sleep(0.0002)`) |
| Overlap | None | Several instructions are in different stages at the same time |

The pipelined version uses `threading` and `queue`: each stage is a worker thread that takes an instruction from its queue, waits 200 µs, and passes it to the next stage's queue. Both programs read the input file, count the instructions, run the simulation, and print the number of instructions processed and the total time.

## Results

Measured on 3 workloads (full analysis and graph in [`REPORT.pdf`](REPORT.pdf)):

| Instructions | Pipelined (s) | Nonpipelined (s) | Speedup | Time saved |
|---:|---:|---:|---:|---:|
| 3,000 | 1.709 | 3.125 | 1.83x | 45.3% |
| 10,000 | 5.570 | 10.230 | 1.84x | 45.6% |
| 30,000 | 16.691 | 30.570 | 1.83x | 45.4% |

Pipelined execution was faster in every run, and the gap grew with the number of instructions. Exact timings vary from machine to machine.

## Run it

Requires Python 3 (standard library only).

The scripts read a file named `mips_instructions.asm` from the same folder, one instruction per line. Only the number of lines matters. To generate a test input with 3,000 instructions:

```bash
seq 3000 | sed 's/.*/add $t0, $t1, $t2/' > mips_instructions.asm
```

Then run each simulator:

```bash
python3 nonpipelined_simulator.py
python3 pipelined_simulator.py
```

Example output:

```
====================================
        Pipelined Simulation
====================================

Instructions Processed : 3000

Time taken by Pipelined Execution = 0.95 seconds
```

## Files

```
├── nonpipelined_simulator.py   # sequential execution simulation
├── pipelined_simulator.py      # 5-stage threaded pipeline simulation
├── REPORT.pdf                  # performance report with results and graph
└── README.md
```

## Skills demonstrated

Python, multithreading and queues, computer architecture concepts (pipelining), performance measurement and reporting.
