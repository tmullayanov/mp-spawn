# README #

mp_spawn is a toy project for implementing and testing out computation on non-daemon processes in Python.

The "sample task" is to calculate value of pi using BBP algorithm which perfectly suits for parallelization


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

