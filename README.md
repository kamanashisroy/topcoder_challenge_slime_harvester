

Marathon match 160
====================


- [topcoder challenge link](https://www.topcoder.com/challenges/80d19de8-91f2-47fa-b08d-af71e4ca2fbb)
- [BioSlime.py](BioSlime.py) is the solution.

#### Java tester link

- [binary link](https://cdn.filestackcontent.com/DlY6u5g0RcGK2J3gbgt6)
- [source link](https://cdn.filestackcontent.com/MhzDbabpS1qbzBMoSpfz)

For simplicity added the latest Java tester source.

```
java -jar tester.jar -exec 'python3 BioSlime.py -X 4' -seed 10 -N 14 -C 4 -D 2 -H 5 -delay 100 -S 0.5 -P 0.5 -W 0.5 -novis
```

#### Discussion 

- [Approach](https://discussions.topcoder.com/discussion/35937/post-your-approach)


What was my approach
========================

#### Observation

- More slimes harvested = more score
- The Slimes are spwaning only when there are some slimes left.
    - If we harvest all slimes quickly
        - then there is less slimes harvested = less score.
    - Otherwise if we wait before we harvest slimes and let slimes grow
        - More slimes harvested = more score

#### Questions

- How long should we wait before we start harvesting ?
    - This is calculated based on equestion `H*C*CAPACITY_MULTIPLIER`,
        - where 'H' = number of harvester
        - where 'C' = Maximum capacity of the harvester
    - What should be the value of `CAPACITY_MULTIPLIER` ?
        - We need to train the algorithm for different parameters and find the best score.
    - Please refer to `calculateApplicableCapacity` for waiting logic.
        - `applicableCapacity` being the minimum-load of a harvester that will make it return to the depot.
        - During waiting time, the `applicableCapacity` is 0.

#### Other tricks

- Using Depot-affinity of harvester(Just like thread affinity of a processor)
    - Please refer to `buildShortestPathFromDepot`
    - Benefits
        - Depot affinity makes harvester assigned to a single depot.
        - It allows more protection to harvester getting surrounded/stuck by slimes.
    - Enhancements
        - While selecting depots we should select a depot with more free-space.

- Avoid getting surrounded/stuck by slimes
    - When harvestor gets stuck, it cannot collect slimes. Please refer to `isSurroundedBySlime` for the implementation.

You are welcome to try some cases.

```
java -jar tester.jar -exec 'python3 BioSlime.py -G -X 1 --cleanupTurn=750 ' -seed 10 -N 30 -D 10 -H 20 -C 30 -delay 100 -S 0.5 -P 0.5 -W 0.5 -novis
```

Also there are other tuning parameters.

```
BioSlime.py -h
```


