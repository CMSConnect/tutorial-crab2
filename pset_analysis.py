#This analysis code will produce an EDM output file called output.root containing only the recoTracks_*_*_* branches for a maximum of 10 events in the input dataset.

import FWCore.ParameterSet.Config as cms
process = cms.Process('NoSplit')
process.source = cms.Source('PoolSource',
  fileNames = cms.untracked.vstring("root://cms-xrd-global.cern.ch//store/mc/HC/GenericTTbar/GEN-SIM-RECO/CMSSW_5_3_1_START53_V5-v1/0010/00CE4E7C-DAAD-E111-BA36-0025B32034EA.root"),
  skipEvents = cms.untracked.uint32(0),
)

process.dump = cms.EDAnalyzer("EventContentAnalyzer", listContent=cms.untracked.bool(False), getData=cms.untracked.bool(True))
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50)
)

process.Timing = cms.Service("Timing",
    useJobReport = cms.untracked.bool(True),
    summaryOnly = cms.untracked.bool(True),
)

process.o = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string("outfile.root"), outputCommands=cms.untracked.vstring("drop *"))

process.out = cms.EndPath(process.o)

process.p = cms.Path(process.dump)
