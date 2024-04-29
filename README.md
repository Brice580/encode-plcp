# Encoding PLCP in 2n bits

This project explores encoding PLCP in 2n bits for space optimization. We test the encoding of PLCP through comparing construction runtimes, average bytes taken, and other runtimes. We utilize the **succinct** library in python for access to succinct data structures and queries such as **rank** and **select**.


How to run: simply run the main method in ExperimentSetup.py (with no arguments)

Contents of package:
    SA.py - code for constructing SA, PLCP, LCP from PLCP, and encoded versions
    ExperimentsSetup.py - resources and methods to run and plot experiments for presentation
    TestingUtils.py - resources for random test generation and validation of results
