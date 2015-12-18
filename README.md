[title]: - "CRAB 2 example to run via condor scheduler"

Please, read the [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrab2) for general instructions on how to use CRAB 2.
The following tutorial, is an example of how to use CRAB 2 on CMS-Connect with the condor scheduler.

### Setup the CMSSW release to use

Example:
	$ mkdir ~/releases
	$ cd ~/releases
	$ export SCRAM_ARCH=slc6_amd64_gcc481
	$ cmsrel CMSSW_7_0_5
	$ cd CMSSW_7_0_5/src 
	$ cmsenv

### Setup CRAB 2

	$ source /usr/local/CRAB_2_11_1_patch1/crab.sh

### Setup tutorial

	$ tutorial 
	usage: tutorial name-of-tutorial 
	       tutorial info name-of-tutorial
	
	Available tutorials: 
	quickstart     Basic HTCondor job submission tutorial
	crab2          CRAB 2 example to run via condor scheduler

Now, run the quickstart tutorial:

	$ tutorial crab2
	$ cd tutorial-crab2 

### Create the jobs 
	$ crab -cfg crab_cmsconnect.cfg -create
        Output example:
        --------------
	crab:  Version 2.11.1_patch1 running on Fri Dec 18 06:20:22 2015 CST (12:20:22 UTC)
	
	crab. Working options:
		scheduler           condor
		job type            CMSSW
		server              OFF
		working directory   /home/khurtado/tutorials_github/tutorial-crab2/crab_0_151218_062022/
	
	crab:  Your se_white_list is set to T2_CH_CERN: only local dataset will be considered
	crab:  PSN black list: TAPE,srm-cms.cern.ch,cmssrm.fnal.gov,T1_RU,T1_TW,cmseos.fnal.gov,cmsdca2.fnal.gov,T2_PK_NCP,T3_US_Vanderbilt_EC2
	crab:  Contacting Data Discovery Services ...
	crab:  Accessing DBS at: https://cmsweb.cern.ch/dbs/prod/global/DBSReader
	crab:  DBS3 lookup took  2.10 sec
	crab:  Datatype is mc
	crab:  Requested dataset: /GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO has 300000 events in 1 blocks.
	
	crab:  100 job(s) can run on 1000 events.
	
	crab:  List of jobs and available destination sites:
	
	Block     1: jobs                1-100: sites: T2_CH_CERN
	
	crab:  Creating 100 jobs, please wait...
	crab:  Total of 100 jobs created.
	
	Log file is /home/khurtado/tutorials_github/tutorial-crab2/crab_0_151218_062022/log/crab.log

### Select the Sites to run

You can select any site you wish and export your list via CONDOR_DESIRED_SITES

	$ export +CONDOR_DESIRED_SITES="T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Vanderbilt,T2_US_Wisconsin,T3_US_Baylor,T3_US_Colorado,T3_US_Cornell,T3_US_FIT,T3_US_FIU,T3_US_NotreDame,T3_US_Omaha_Long,T3_US_OSU,T3_US_PuertoRico,T3_US_Rutgers,T3_US_TAMU,T3_US_TTU,T3_US_UCD,T3_US_UCR,T3_US_UCSB,T3_US_UMD,T3_US_UMiss"

# Disable CMS Dashboard integrated in condor
CRAB already has its own implementation to report to the CMS Dashboard, so you have to disable the CMS-Connect integrated version first.
	$ export CONDOR_CMS_DASHBOARD='False'

## Submit the jobs
	$ crab -submit

# Check status of jobs
	$ crab -status


# Dashboard
You can also check your jobs status at the [CMS Dashboard](http://dashboard.cern.ch/cms/)
