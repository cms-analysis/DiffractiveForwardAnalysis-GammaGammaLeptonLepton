import FWCore.ParameterSet.Config as cms

excltrktrkanalysis = cms.EDFilter("ExclusiveTrackTrack",
    outfilename = cms.untracked.string('tracktrack.pat.root'),
    CaloTowerLabel = cms.InputTag("towerMaker"),
    CastorTowerLabel = cms.InputTag("CastorFastTowerReco"),
    RecoTrackLabel = cms.InputTag("generalTracks"),
    CaloTowerdR = cms.double(0.3),
)


