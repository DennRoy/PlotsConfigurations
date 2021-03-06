#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/user/m/mlizzo/work/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
workdir=/afs/cern.ch/work/m/mlizzo/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_OS/Full2016_v6/FitDir 
workspaceDir=workspaces

cd $workdir

echo "mjj_vs_mTi:" "" > ${workspaceDir}/significance_mjj_vs_mTi.txt
combine -M Significance ${workspaceDir}/mjj_vs_mTi.root -t -1 --setParameters r_vbs=1 --redefineSignalPOIs=r_vbs >> ${workspaceDir}/significance_mjj_vs_mTi.txt

