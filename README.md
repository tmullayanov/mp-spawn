# README #

mp_spawn is a toy project for implementing and testing out computation on non-daemon processes in Python.

The "demo task" is to calculate value of pi using BBP algorithm which perfectly suits for parallelization.
The scheme of computation is described as follows: main process spawns N number of processes (referred as 1st level processes) and assigns correspondning job to each of them.

Then each 1st level process spawns M number of (2nd level) processes which actually calculate several hexademical digits of PI and signal the sum of it to their master.
The 1st level process waits until all it's children finish the computation, then gathers their results and signals the total result of its job to the main process


### Requirements ###

* Python 3.5+ (though the method should work on python 2.7 as well)
* multicore CPU if one wants to see the speedup

### Usage ###

usage: ./main.py [-h] [--processes PROCESSES] [--spawn-by SPAWN_BY]
               [--pi-prec PI_PREC] [--sequential]

optional arguments:

  -h, --help            show this help message and exit

  --processes PROCESSES
                        number of 1st level processes to spawn

  --spawn-by SPAWN_BY   number of 2nd level processes to spawn

  --pi-prec PI_PREC     number of hex digits of pi that would be calculated

  --sequential          if set, program performs sequential calculation


