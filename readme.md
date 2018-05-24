# Solidity Compiler Verification

Verify the functionality of the Solidity Contract compiler by generating various code snippets and inserting into certain positions in the code.

Currently the verifier performs:
1. Conditional augmentation in 'if conditions'
2. Insertion of dead code

## Running 

1. Create folders 'contracts', which contains the contracts to be mutated, and 'contracts/mutants', which contains the generated contracts.

2. Run the following command

```
python3 runner.py
```

### NB: 
For later use: The bash script runStuff.sh can call truffle compile on the contracts, and copy the resulting 'json' and 'sol' files to the relevant folders. 

## Functionalty of the Components

### ineq_gen:
Define depth and boolean value to generate inequalities with operations: '{+, -, *, /}' and comparisons '{<, > , >== , <==, ==}'. Randomly makes use of 'uint' and 'int' variables throughout the generated inequalities.

