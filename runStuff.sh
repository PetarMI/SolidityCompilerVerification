#!/bin/bash
cd /home/ali/Documents/MSc1/ProgAnalysis/Project/projTruffle/contracts
truffle compile 
echo =========================================
echo Compilation complete, copying files...
cp /home/ali/Documents/MSc1/ProgAnalysis/Project/projTruffle/contracts/* /home/ali/GitHub/SolidityCompilerVerification/contracts
cp /home/ali/Documents/MSc1/ProgAnalysis/Project/projTruffle/build/contracts/* /home/ali/GitHub/SolidityCompilerVerification/contracts
echo =========================================
echo Running runner.py
cd /home/ali/GitHub/SolidityCompilerVerification/
python3 runner.py
