How to run: 
    - Experiments: simply run the main method in ExperimentSetup.py (with no arguments). Results will be saved as pngs in current directory.
    - Correctness tests: run the main method in CorrectnessTests.py (with no arguments). Results will print.

Contents of package:
    SA.py - code for constructing SA, PLCP, LCP from PLCP, and encoded versions
        - SAs are objects, the actual SA indices are stored in sa.ranks 
        - other values stored are n, and the actually T for testing and validation purposes
    ExperimentsSetup.py - resources and methods to run and plot experiments for presentation
    TestingUtils.py - resources for random test generation and correctness tests