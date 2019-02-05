# nuisances
#FIXME: TO BE UPDATED FOR 2017!

# name of samples here must match keys in samples.py 

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

nuisances['lumi']  = {
               'name'  : 'lumi_13TeV',
               'samples'  : {
                   #'DY'       : '1.023',    |
                   #'top'      : '1.023',    | These 3 backgrounds are data driven, no need to include the luminosity uncertainty
                   #'WW'       : '1.023',    |
                   'ggWW'     : '1.023',
                   'Vg'       : '1.023',
                   'VgS'      : '1.023',
                   'WZgS'     : '1.023',
                   'WZgS_L'   : '1.023',
                   'WZgS_H'   : '1.023',
                   'VZ'       : '1.023',
                   'VVV'      : '1.023',
                   'ggH_hww_0j_fid'  : '1.023',
                   'ggH_hww_1j_fid'  : '1.023',
                   'ggH_hww_2j_fid'  : '1.023',
                   'ggH_hww_3j_fid'  : '1.023',
                   'ggH_hww_4j_fid'  : '1.023',
                   'ggH_hww_0j_nonfid'  : '1.023',
                   'ggH_hww_1j_nonfid'  : '1.023',
                   'ggH_hww_2j_nonfid'  : '1.023',
                   'ggH_hww_3j_nonfid'  : '1.023',
                   'ggH_hww_4j_nonfid'  : '1.023',
                   'qqH_hww_0j_fid'  : '1.023',
                   'qqH_hww_1j_fid'  : '1.023',
                   'qqH_hww_2j_fid'  : '1.023',
                   'qqH_hww_3j_fid'  : '1.023',
                   'qqH_hww_4j_fid'  : '1.023',
                   'qqH_hww_0j_nonfid'  : '1.023',
                   'qqH_hww_1j_nonfid'  : '1.023',
                   'qqH_hww_2j_nonfid'  : '1.023',
                   'qqH_hww_3j_nonfid'  : '1.023',
                   'qqH_hww_4j_nonfid'  : '1.023',
                   #
                   'XH_hww_0j_fid'   : '1.023',
                   'XH_hww_1j_fid'   : '1.023',
                   'XH_hww_2j_fid'   : '1.023',
                   'XH_hww_3j_fid'   : '1.023',
                   'XH_hww_4j_fid'   : '1.023',
                   'XH_hww_0j_nonfid'   : '1.023',
                   'XH_hww_1j_nonfid'   : '1.023',
                   'XH_hww_2j_nonfid'   : '1.023',
                   'XH_hww_3j_nonfid'   : '1.023',
                   'XH_hww_4j_nonfid'   : '1.023',
                   #
                   'ZH_hww'   : '1.023',
                   'ggZH_hww' : '1.023',
                   'WH_hww'   : '1.023',
                   'bbH_hww'  : '1.023',
                   'ttH_hww'  : '1.023',
                   'ggH_htt'  : '1.023',
                   'qqH_htt'  : '1.023',
                   'ZH_htt'   : '1.023',
                   'WH_htt'   : '1.023',
                   'H_htt'    : '1.023',
                   },
               'type'  : 'lnN',
              }

#### FAKES

if Nlep == '2' :
  # already divided by central values in formulas !
  fakeW_EleUp       = fakeW+'_EleUp'
  fakeW_EleDown     = fakeW+'_EleDown'
  fakeW_MuUp        = fakeW+'_MuUp'
  fakeW_MuDown      = fakeW+'_MuDown'
  fakeW_statEleUp   = fakeW+'_statEleUp'
  fakeW_statEleDown = fakeW+'_statEleDown'
  fakeW_statMuUp    = fakeW+'_statMuUp'
  fakeW_statMuDown  = fakeW+'_statMuDown'

else:
  fakeW_EleUp       = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_EleDown     = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lElDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_MuUp        = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_MuDown      = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lMuDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statEleUp   = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statEleDown = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatElDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statMuUp    = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'
  fakeW_statMuDown  = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'lstatMuDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l )'

## FIXME: check the 30% lnN
nuisances['fake_syst_em']  = {
               'name'  : 'CMS_hwwem_fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_em' : '1.30',
                             },
               }

nuisances['fake_syst_me']  = {
               'name'  : 'CMS_hwwme_fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_me' : '1.30',
                             },
               }

nuisances['fake_ele']  = {
                'name'  : 'hww_fake_ele',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_EleUp , fakeW_EleDown ],
                              'Fake_me'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'hww_fake_ele_stat',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                              'Fake_me'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'hww_fake_mu',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_MuUp , fakeW_MuDown ],
                              'Fake_me'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
}


nuisances['fake_mu_stat']  = {
                'name'  : 'hww_fake_mu_stat',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                              'Fake_me'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                             },
}

##### B-tagger
nuisances['btag_shape_jes']  = {
                'name'  : 'btag_shape_jes',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'WW'      : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggWW'    : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'VVV'     : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'VZ'      : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'WZgS'    : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'WZgS_L'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'WZgS_H'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'top'     : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'Vg'      : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'VgS'     : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_0j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_1j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_2j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_3j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_4j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_0j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_1j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_2j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_3j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_4j_fid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   #
#                   'XH_hww_0j_fid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
#                   'XH_hww_1j_fid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
#                   'XH_hww_2j_fid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
#                   'XH_hww_3j_fid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
#                   'XH_hww_4j_fid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
#                   'XH_hww_0j_nonfid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
#                   'XH_hww_1j_nonfid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
#                   'XH_hww_2j_nonfid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
#                   'XH_hww_3j_nonfid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
#                   'XH_hww_4j_nonfid'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   #
                   'WH_hww'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ZH_hww'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggZH_hww': ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'H_htt'   : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'bbH_hww' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ttH_hww' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ggH_htt' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],  
                   'qqH_htt' : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'ZH_htt'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                   'WH_htt'  : ['('+btagSF+'_up_jes)/('+btagSF+')', '('+btagSF+'_down_jes)/('+btagSF+')'],
                }
}

nuisances['btag_shape_lf']  = {
                'name'  : 'btag_shape_lf',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'VVV'     : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'VZ'      : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'WZgS'    : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'WZgS_L'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'WZgS_H'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'WW'      : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggWW'    : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'top'     : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'Vg'      : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'VgS'     : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_0j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_1j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_2j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_3j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_4j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_0j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_1j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_2j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_3j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_4j_fid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   #
                   'ZH_hww_0j_fid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww_1j_fid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww_2j_fid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww_3j_fid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww_4j_fid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww_0j_nonfid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww_1j_nonfid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww_2j_nonfid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww_3j_nonfid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww_4j_nonfid'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   #
                   'WH_hww'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_hww'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggZH_hww': ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'bbH_hww' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ttH_hww' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'H_htt'   : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ggH_htt' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'qqH_htt' : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'ZH_htt'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                   'WH_htt'  : ['('+btagSF+'_up_lf)/('+btagSF+')', '('+btagSF+'_down_lf)/('+btagSF+')'],
                }
}

nuisances['btag_shape_hf']  = {
                'name'  : 'btag_shape_hf',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'VVV'     : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'VZ'      : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'WZgS'    : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'WZgS_L'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'WZgS_H'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'WW'      : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggWW'    : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'top'     : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'Vg'      : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'VgS'     : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_0j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_1j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_2j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_3j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_4j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_0j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_1j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_2j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_3j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_4j_fid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   #
#                   'XH_hww_0j_fid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
#                   'XH_hww_1j_fid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
#                   'XH_hww_2j_fid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
#                   'XH_hww_3j_fid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
#                   'XH_hww_4j_fid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
#                   'XH_hww_0j_nonfid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
#                   'XH_hww_1j_nonfid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
#                   'XH_hww_2j_nonfid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
#                   'XH_hww_3j_nonfid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
#                   'XH_hww_4j_nonfid'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   #
                   'WH_hww'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ZH_hww'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggZH_hww': ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'bbH_hww' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ttH_hww' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'H_htt'   : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ggH_htt' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'qqH_htt' : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'ZH_htt'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                   'WH_htt'  : ['('+btagSF+'_up_hf)/('+btagSF+')', '('+btagSF+'_down_hf)/('+btagSF+')'],
                }
}

nuisances['btag_shape_hfstats1']  = {
                'name'  : 'btag_shape_hfstats1',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'VVV'     : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'VZ'      : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'WZgS'    : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'WZgS_L'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'WZgS_H'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'WW'      : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggWW'    : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'top'     : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'Vg'      : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'VgS'     : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_0j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_1j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_2j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_3j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_4j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_0j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_1j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_2j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_3j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_4j_fid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   #
#                   'XH_hww_0j_fid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
#                   'XH_hww_1j_fid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
#                   'XH_hww_2j_fid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
#                   'XH_hww_3j_fid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
#                   'XH_hww_4j_fid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
#                   'XH_hww_0j_nonfid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
#                   'XH_hww_1j_nonfid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
#                   'XH_hww_2j_nonfid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
#                   'XH_hww_3j_nonfid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
#                   'XH_hww_4j_nonfid'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   #
                   'WH_hww'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ZH_hww'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggZH_hww': ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'bbH_hww' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ttH_hww' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'H_htt'   : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ggH_htt' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'qqH_htt' : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'ZH_htt'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                   'WH_htt'  : ['('+btagSF+'_up_hfstats1)/('+btagSF+')', '('+btagSF+'_down_hfstats1)/('+btagSF+')'],
                }
}

nuisances['btag_shape_hfstats2']  = {
                'name'  : 'btag_shape_hfstats2',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'VVV'     : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'VZ'      : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'WZgS'    : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'WZgS_L'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'WZgS_H'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'WW'      : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggWW'    : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'top'     : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'Vg'      : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'VgS'     : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_0j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_1j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_2j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_3j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_4j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_0j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_1j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_2j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_3j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_4j_fid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   #
#                   'XH_hww_0j_fid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
#                   'XH_hww_1j_fid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
#                   'XH_hww_2j_fid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
#                   'XH_hww_3j_fid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
#                   'XH_hww_4j_fid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
#                   'XH_hww_0j_nonfid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
#                   'XH_hww_1j_nonfid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
#                   'XH_hww_2j_nonfid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
#                   'XH_hww_3j_nonfid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
#                   'XH_hww_4j_nonfid'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   #
                   'WH_hww'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ZH_hww'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggZH_hww': ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'bbH_hww' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ttH_hww' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'H_htt'   : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ggH_htt' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'qqH_htt' : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'ZH_htt'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                   'WH_htt'  : ['('+btagSF+'_up_hfstats2)/('+btagSF+')', '('+btagSF+'_down_hfstats2)/('+btagSF+')'],
                }
}

nuisances['btag_shape_lfstats1']  = {
                'name'  : 'btag_shape_lfstats1',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'VVV'     : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'VZ'      : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'WZgS'    : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'WZgS_L'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'WZgS_H'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'WW'      : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggWW'    : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'top'     : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'Vg'      : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'VgS'     : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_0j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_1j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_2j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_3j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_4j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_0j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_1j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_2j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_3j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_4j_fid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   #
#                   'XH_hww_0j_fid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
#                   'XH_hww_1j_fid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
#                   'XH_hww_2j_fid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
#                   'XH_hww_3j_fid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
#                   'XH_hww_4j_fid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
#                   'XH_hww_0j_nonfid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
#                   'XH_hww_1j_nonfid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
#                   'XH_hww_2j_nonfid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
#                   'XH_hww_3j_nonfid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
#                   'XH_hww_4j_nonfid'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   #
                   'WH_hww'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ZH_hww'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggZH_hww': ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'bbH_hww' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ttH_hww' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'H_htt'   : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ggH_htt' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'qqH_htt' : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'ZH_htt'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                   'WH_htt'  : ['('+btagSF+'_up_lfstats1)/('+btagSF+')', '('+btagSF+'_down_lfstats1)/('+btagSF+')'],
                }
}

nuisances['btag_shape_lfstats2']  = {
                'name'  : 'btag_shape_lfstats2',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'VVV'     : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'VZ'      : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'WZgS'    : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'WZgS_L'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'WZgS_H'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'WW'      : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggWW'    : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'top'     : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'Vg'      : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'VgS'     : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_0j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_1j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_2j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_3j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_4j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_0j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_1j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_2j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_3j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_4j_fid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   #
#                   'XH_hww_0j_fid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
#                   'XH_hww_1j_fid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
#                   'XH_hww_2j_fid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
#                   'XH_hww_3j_fid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
#                   'XH_hww_4j_fid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
#                   'XH_hww_0j_nonfid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
#                   'XH_hww_1j_nonfid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
#                   'XH_hww_2j_nonfid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
#                   'XH_hww_3j_nonfid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
#                   'XH_hww_4j_nonfid'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   #
                   'WH_hww'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ZH_hww'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggZH_hww': ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'bbH_hww' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ttH_hww' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'H_htt'   : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ggH_htt' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'qqH_htt' : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'ZH_htt'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                   'WH_htt'  : ['('+btagSF+'_up_lfstats2)/('+btagSF+')', '('+btagSF+'_down_lfstats2)/('+btagSF+')'],
                }
}

nuisances['btag_shape_cferr1']  = {
                'name'  : 'btag_shape_cferr1',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'VVV'     : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'VZ'      : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'WZgS'    : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'WZgS_L'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'WZgS_H'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'WW'      : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggWW'    : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'top'     : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'Vg'      : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'VgS'     : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_0j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_1j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_2j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_3j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_4j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_0j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_1j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_2j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_3j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_4j_fid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   #
#                   'XH_hww_0j_fid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
#                   'XH_hww_1j_fid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
#                   'XH_hww_2j_fid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
#                   'XH_hww_3j_fid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
#                   'XH_hww_4j_fid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
#                   'XH_hww_0j_nonfid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
#                   'XH_hww_1j_nonfid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
#                   'XH_hww_2j_nonfid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
#                   'XH_hww_3j_nonfid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
#                   'XH_hww_4j_nonfid'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   #
                   'WH_hww'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ZH_hww'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggZH_hww': ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'bbH_hww' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ttH_hww' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'H_htt'   : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ggH_htt' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'qqH_htt' : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'ZH_htt'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                   'WH_htt'  : ['('+btagSF+'_up_cferr1)/('+btagSF+')', '('+btagSF+'_down_cferr1)/('+btagSF+')'],
                }
}

nuisances['btag_shape_cferr2']  = {
                'name'  : 'btag_shape_cferr2',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'VVV'     : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'VZ'      : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'WZgS'    : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'WZgS_L'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'WZgS_H'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'WW'      : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggWW'    : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'top'     : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'Vg'      : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'VgS'     : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_0j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_1j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_2j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_3j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_4j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_0j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_1j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_2j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_3j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_hww_4j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_0j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_1j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_2j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_3j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_4j_fid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_0j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_1j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_2j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_3j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_hww_4j_nonfid' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   #
#                   'XH_hww_0j_fid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
#                   'XH_hww_1j_fid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
#                   'XH_hww_2j_fid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
#                   'XH_hww_3j_fid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
#                   'XH_hww_4j_fid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
#                   'XH_hww_0j_nonfid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
#                   'XH_hww_1j_nonfid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
#                   'XH_hww_2j_nonfid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
#                   'XH_hww_3j_nonfid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
#                   'XH_hww_4j_nonfid'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   #
                   'WH_hww'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ZH_hww'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggZH_hww': ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'bbH_hww' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ttH_hww' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'H_htt'   : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ggH_htt' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'qqH_htt' : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'ZH_htt'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                   'WH_htt'  : ['('+btagSF+'_up_cferr2)/('+btagSF+')', '('+btagSF+'_down_cferr2)/('+btagSF+')'],
                }
}

##### Trigger Efficiency

trig_syst = ['(TriggerEffWeight_'+Nlep+'l_u)/(TriggerEffWeight_'+Nlep+'l)', '(TriggerEffWeight_'+Nlep+'l_d)/(TriggerEffWeight_'+Nlep+'l)']

nuisances['trigg']  = {
                'name'  : 'hww_trigger',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : trig_syst ,
                   'VVV'     : trig_syst ,
                   'VZ'      : trig_syst ,
                   'WZgS'    : trig_syst ,
                   'WZgS_L'  : trig_syst ,
                   'WZgS_H'  : trig_syst ,
                   'ggWW'    : trig_syst ,
                   'WW'      : trig_syst ,
                   'top'     : trig_syst ,
                   'Vg'      : trig_syst ,
                   'VgS'     : trig_syst ,
                   'ggH_hww_0j_fid' : trig_syst ,
                   'ggH_hww_1j_fid' : trig_syst ,
                   'ggH_hww_2j_fid' : trig_syst ,
                   'ggH_hww_3j_fid' : trig_syst ,
                   'ggH_hww_4j_fid' : trig_syst ,
                   'ggH_hww_0j_nonfid' : trig_syst ,
                   'ggH_hww_1j_nonfid' : trig_syst ,
                   'ggH_hww_2j_nonfid' : trig_syst ,
                   'ggH_hww_3j_nonfid' : trig_syst ,
                   'ggH_hww_4j_nonfid' : trig_syst ,
                   'qqH_hww_0j_fid' : trig_syst ,
                   'qqH_hww_1j_fid' : trig_syst ,
                   'qqH_hww_2j_fid' : trig_syst ,
                   'qqH_hww_3j_fid' : trig_syst ,
                   'qqH_hww_4j_fid' : trig_syst ,
                   'qqH_hww_0j_nonfid' : trig_syst ,
                   'qqH_hww_1j_nonfid' : trig_syst ,
                   'qqH_hww_2j_nonfid' : trig_syst ,
                   'qqH_hww_3j_nonfid' : trig_syst ,
                   'qqH_hww_4j_nonfid' : trig_syst ,
                   #
#                   'XH_hww_0j_fid'  : trig_syst ,
#                   'XH_hww_1j_fid'  : trig_syst ,
#                   'XH_hww_2j_fid'  : trig_syst ,
#                   'XH_hww_3j_fid'  : trig_syst ,
#                   'XH_hww_4j_fid'  : trig_syst ,
#                   'XH_hww_0j_nonfid'  : trig_syst ,
#                   'XH_hww_1j_nonfid'  : trig_syst ,
#                   'XH_hww_2j_nonfid'  : trig_syst ,
#                   'XH_hww_3j_nonfid'  : trig_syst ,
#                   'XH_hww_4j_nonfid'  : trig_syst ,
                   #
                   'WH_hww'  : trig_syst ,
                   'ZH_hww'  : trig_syst ,
                   'ggZH_hww': trig_syst ,
                   'bbH_hww' : trig_syst ,
                   'ttH_hww' : trig_syst ,
                   'H_htt'   : trig_syst ,
                   'ggH_htt' : trig_syst ,
                   'qqH_htt' : trig_syst ,
                   'ZH_htt'  : trig_syst ,
                   'WH_htt'  : trig_syst ,
                },
}

##### Electron Efficiency and energy scale

id_syst_ele = [ 'LepSF'+Nlep+'l__ele_'+eleWP+'__Up' , 'LepSF'+Nlep+'l__ele_'+eleWP+'__Do' ]

nuisances['eff_e']  = {
                'name'  : 'eff_e',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_ele ,
                   'VVV'     : id_syst_ele ,
                   'VZ'      : id_syst_ele ,
                   'WZgS'    : id_syst_ele ,
                   'WZgS_L'  : id_syst_ele ,
                   'WZgS_H'  : id_syst_ele ,
                   'ggWW'    : id_syst_ele ,
                   'WW'      : id_syst_ele ,
                   'top'     : id_syst_ele ,
                   'Vg'      : id_syst_ele ,
                   'VgS'     : id_syst_ele ,
                   'ggH_hww_0j_fid' : id_syst_ele ,
                   'ggH_hww_1j_fid' : id_syst_ele ,
                   'ggH_hww_2j_fid' : id_syst_ele ,
                   'ggH_hww_3j_fid' : id_syst_ele ,
                   'ggH_hww_4j_fid' : id_syst_ele ,
                   'ggH_hww_0j_nonfid' : id_syst_ele ,
                   'ggH_hww_1j_nonfid' : id_syst_ele ,
                   'ggH_hww_2j_nonfid' : id_syst_ele ,
                   'ggH_hww_3j_nonfid' : id_syst_ele ,
                   'ggH_hww_4j_nonfid' : id_syst_ele ,
                   'qqH_hww_0j_fid' : id_syst_ele ,
                   'qqH_hww_1j_fid' : id_syst_ele ,
                   'qqH_hww_2j_fid' : id_syst_ele ,
                   'qqH_hww_3j_fid' : id_syst_ele ,
                   'qqH_hww_4j_fid' : id_syst_ele ,
                   'qqH_hww_0j_nonfid' : id_syst_ele ,
                   'qqH_hww_1j_nonfid' : id_syst_ele ,
                   'qqH_hww_2j_nonfid' : id_syst_ele ,
                   'qqH_hww_3j_nonfid' : id_syst_ele ,
                   'qqH_hww_4j_nonfid' : id_syst_ele ,
                   #
#                   'XH_hww_0j_fid' : id_syst_ele ,
#                   'XH_hww_1j_fid' : id_syst_ele ,
#                   'XH_hww_2j_fid' : id_syst_ele ,
#                   'XH_hww_3j_fid' : id_syst_ele ,
#                   'XH_hww_4j_fid' : id_syst_ele ,
#                   'XH_hww_0j_nonfid' : id_syst_ele ,
#                   'XH_hww_1j_nonfid' : id_syst_ele ,
#                   'XH_hww_2j_nonfid' : id_syst_ele ,
#                   'XH_hww_3j_nonfid' : id_syst_ele ,
#                   'XH_hww_4j_nonfid' : id_syst_ele ,
                   #
                   'WH_hww'  : id_syst_ele ,
                   'ZH_hww'  : id_syst_ele ,
                   'ggZH_hww': id_syst_ele ,
                   'bbH_hww' : id_syst_ele ,
                   'ttH_hww' : id_syst_ele ,
                   'H_htt'   : id_syst_ele ,
                   'ggH_htt' : id_syst_ele ,
                   'qqH_htt' : id_syst_ele ,
                   'ZH_htt'  : id_syst_ele ,
                   'WH_htt'  : id_syst_ele ,
                },
}
'''
nuisances['electronpt']  = {
                'name'  : 'scale_e',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   #'WZgS'    : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   #'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww'  : ['1', '1'],
                   'ZH_hww'  : ['1', '1'],
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                 },
                'folderUp'   : treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__ElepTup', #xrootdPath+treeBaseDir
                'folderDown' : treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__ElepTdo',
}
'''
#FIXME: The following should not be needed for 2017
#elePtCor_Syst = [ 'electron_ptW_'+Nlep+'l_Up / electron_ptW_'+Nlep+'l', 'electron_ptW_'+Nlep+'l_Down / electron_ptW_'+Nlep+'l']
#nuisances['elePtCor']  = {
#                'name'  : 'hww_elePtCor',
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'DY'         : elePtCor_Syst ,
#                   'ggWW'       : elePtCor_Syst ,
#                   'WW'         : elePtCor_Syst ,
#                   'top'        : elePtCor_Syst ,
#                   'VZ'         : elePtCor_Syst ,
#                   'WZgS_L'     : elePtCor_Syst ,
#                   'WZgS_H'     : elePtCor_Syst ,
#                   'VVV'        : elePtCor_Syst ,
#                   'Vg'         : elePtCor_Syst ,
#                   'VgS'        : elePtCor_Syst ,
#                   'ggH_hww'    : elePtCor_Syst ,
#                   'qqH_hww'    : elePtCor_Syst ,
#                   'WH_hww'     : elePtCor_Syst ,
#                   'ZH_hww'     : elePtCor_Syst ,
#                   'ggZH_hww'   : elePtCor_Syst ,
#                   'bbH_hww'    : elePtCor_Syst ,
#                   'ttH_hww'    : elePtCor_Syst ,
#                   'H_htt'      : elePtCor_Syst ,
#                   'ggH_htt'    : elePtCor_Syst ,
#                   'qqH_htt'    : elePtCor_Syst ,
#                   'ZH_htt'     : elePtCor_Syst ,
#                   'WH_htt'     : elePtCor_Syst ,
#                }
#}
#
#eleEtaCor_Syst = [ 'electron_etaW_'+Nlep+'l_Up / electron_etaW_'+Nlep+'l', 'electron_etaW_'+Nlep+'l_Down / electron_etaW_'+Nlep+'l']
#
#nuisances['eleEtaCor']  = {
#                'name'  : 'hww_eleEtaCor',
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'DY'         : eleEtaCor_Syst ,
#                   'ggWW'       : eleEtaCor_Syst ,
#                   'WW'         : eleEtaCor_Syst ,
#                   'top'        : eleEtaCor_Syst ,
#                   'VZ'         : eleEtaCor_Syst ,
#                   'WZgS_L'     : eleEtaCor_Syst ,
#                   'WZgS_H'     : eleEtaCor_Syst ,
#                   'VVV'        : eleEtaCor_Syst ,
#                   'Vg'         : eleEtaCor_Syst ,
#                   'VgS'        : eleEtaCor_Syst ,
#                   'ggH_hww'    : eleEtaCor_Syst ,
#                   'qqH_hww'    : eleEtaCor_Syst ,
#                   'WH_hww'     : eleEtaCor_Syst ,
#                   'ZH_hww'     : eleEtaCor_Syst ,
#                   'ggZH_hww'   : eleEtaCor_Syst ,
#                   'bbH_hww'    : eleEtaCor_Syst ,
#                   'ttH_hww'    : eleEtaCor_Syst ,
#                   'H_htt'      : eleEtaCor_Syst ,
#                   'ggH_htt'    : eleEtaCor_Syst ,
#                   'qqH_htt'    : eleEtaCor_Syst ,
#                   'ZH_htt'     : eleEtaCor_Syst ,
#                   'WH_htt'     : eleEtaCor_Syst ,
#                }
#}


##### Muon Efficiency and energy scale

id_syst_mu = [ 'LepSF'+Nlep+'l__mu_'+muWP+'__Up' , 'LepSF'+Nlep+'l__mu_'+muWP+'__Do' ]

nuisances['eff_m']  = {
                'name'  : 'eff_m',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : id_syst_mu ,
                   'VVV'     : id_syst_mu ,
                   'VZ'      : id_syst_mu ,
                   'WZgS'    : id_syst_mu ,
                   'WZgS_L'  : id_syst_mu ,
                   'WZgS_H'  : id_syst_mu ,
                   'ggWW'    : id_syst_mu ,
                   'WW'      : id_syst_mu ,
                   'top'     : id_syst_mu ,
                   'Vg'      : id_syst_mu ,
                   'VgS'     : id_syst_mu ,
                   'ggH_hww_0j_fid' : id_syst_mu ,
                   'ggH_hww_1j_fid' : id_syst_mu ,
                   'ggH_hww_2j_fid' : id_syst_mu ,
                   'ggH_hww_3j_fid' : id_syst_mu ,
                   'ggH_hww_4j_fid' : id_syst_mu ,
                   'ggH_hww_0j_nonfid' : id_syst_mu ,
                   'ggH_hww_1j_nonfid' : id_syst_mu ,
                   'ggH_hww_2j_nonfid' : id_syst_mu ,
                   'ggH_hww_3j_nonfid' : id_syst_mu ,
                   'ggH_hww_4j_nonfid' : id_syst_mu ,
                   'qqH_hww_0j_fid' : id_syst_mu ,
                   'qqH_hww_1j_fid' : id_syst_mu ,
                   'qqH_hww_2j_fid' : id_syst_mu ,
                   'qqH_hww_3j_fid' : id_syst_mu ,
                   'qqH_hww_4j_fid' : id_syst_mu ,
                   'qqH_hww_0j_nonfid' : id_syst_mu ,
                   'qqH_hww_1j_nonfid' : id_syst_mu ,
                   'qqH_hww_2j_nonfid' : id_syst_mu ,
                   'qqH_hww_3j_nonfid' : id_syst_mu ,
                   'qqH_hww_4j_nonfid' : id_syst_mu ,
                   #
#                   'XH_hww_0j_fid' : id_syst_mu ,
#                   'XH_hww_1j_fid' : id_syst_mu ,
#                   'XH_hww_2j_fid' : id_syst_mu ,
#                   'XH_hww_3j_fid' : id_syst_mu ,
#                   'XH_hww_4j_fid' : id_syst_mu ,
#                   'XH_hww_0j_nonfid' : id_syst_mu ,
#                   'XH_hww_1j_nonfid' : id_syst_mu ,
#                   'XH_hww_2j_nonfid' : id_syst_mu ,
#                   'XH_hww_3j_nonfid' : id_syst_mu ,
#                   'XH_hww_4j_nonfid' : id_syst_mu ,
                   #
                   'WH_hww'  : id_syst_mu ,
                   'ZH_hww'  : id_syst_mu ,
                   'ggZH_hww': id_syst_mu ,
                   'bbH_hww' : id_syst_mu ,
                   'ttH_hww' : id_syst_mu ,
                   'H_htt'   : id_syst_mu ,
                   'ggH_htt' : id_syst_mu ,
                   'qqH_htt' : id_syst_mu ,
                   'ZH_htt'  : id_syst_mu ,
                   'WH_htt'  : id_syst_mu ,
                },
}
'''
nuisances['muonpt']  = {
                'name'  : 'scale_m',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   #'WZgS'    : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   #'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww'  : ['1', '1'],
                   'ZH_hww'  : ['1', '1'],
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                },
                'folderUp'   : treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__MupTup',
                'folderDown' : treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__MupTdo',
}
'''

##### Jet energy scale
'''
nuisances['jes']  = {
                'name'  : 'scale_j',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   #'WZgS'    : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   #'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww'  : ['1', '1'],
                   'ZH_hww'  : ['1', '1'],
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                },
                'folderUp'   : treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__JESup',
                'folderDown' : treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__JESdo',
}
'''
##### MET energy scale

nuisances['met']  = {
                'name'  : 'scale_met',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['1', '1'],
                   'ggWW'    : ['1', '1'],
                   'WW'      : ['1', '1'],
                   'top'     : ['1', '1'],
                   'VZ'      : ['1', '1'],
                   #'WZgS'    : ['1', '1'],
                   'WZgS_L'  : ['1', '1'],
                   'WZgS_H'  : ['1', '1'],
                   'VVV'     : ['1', '1'],
                   #'Vg'      : ['1', '1'],
                   'VgS'     : ['1', '1'],
                   'ggH_hww_0j_fid' : ['1', '1'],
                   'ggH_hww_1j_fid' : ['1', '1'],
                   'ggH_hww_2j_fid' : ['1', '1'],
                   'ggH_hww_3j_fid' : ['1', '1'],
                   'ggH_hww_4j_fid' : ['1', '1'],
                   'ggH_hww_0j_nonfid' : ['1', '1'],
                   'ggH_hww_1j_nonfid' : ['1', '1'],
                   'ggH_hww_2j_nonfid' : ['1', '1'],
                   'ggH_hww_3j_nonfid' : ['1', '1'],
                   'ggH_hww_4j_nonfid' : ['1', '1'],
                   'qqH_hww_0j_fid' : ['1', '1'],
                   'qqH_hww_1j_fid' : ['1', '1'],
                   'qqH_hww_2j_fid' : ['1', '1'],
                   'qqH_hww_3j_fid' : ['1', '1'],
                   'qqH_hww_4j_fid' : ['1', '1'],
                   'qqH_hww_0j_nonfid' : ['1', '1'],
                   'qqH_hww_1j_nonfid' : ['1', '1'],
                   'qqH_hww_2j_nonfid' : ['1', '1'],
                   'qqH_hww_3j_nonfid' : ['1', '1'],
                   'qqH_hww_4j_nonfid' : ['1', '1'],
                   #
#                   'XH_hww_0j_fid' : ['1', '1'],
#                   'XH_hww_1j_fid' : ['1', '1'],
#                   'XH_hww_2j_fid' : ['1', '1'],
#                   'XH_hww_3j_fid' : ['1', '1'],
#                   'XH_hww_4j_fid' : ['1', '1'],
#                   'XH_hww_0j_nonfid' : ['1', '1'],
#                   'XH_hww_1j_nonfid' : ['1', '1'],
#                   'XH_hww_2j_nonfid' : ['1', '1'],
#                   'XH_hww_3j_nonfid' : ['1', '1'],
#                   'XH_hww_4j_nonfid' : ['1', '1'],
                   #
                   'WH_hww'  : ['1', '1'],
                   'ZH_hww'  : ['1', '1'],
                   'ggZH_hww': ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'ttH_hww' : ['1', '1'],
                   'H_htt'   : ['1', '1'],
                   'ggH_htt' : ['1', '1'] ,
                   'qqH_htt' : ['1', '1'] ,
                   'ZH_htt'  : ['1', '1'] ,
                   'WH_htt'  : ['1', '1'] ,
                },
                'folderUp'   : treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__METup',
                'folderDown' : treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__METdo',
}

#
# PS and UE
#
#FIXME: Add PS uncertainty
#nuisances['PS']  = {
#                'name'  : 'PS',
#                'skipCMS' : 1,
#                'kind'  : 'tree',
#                'type'  : 'shape',
#                'samples'  : {
#                  'WW'      : ['0.92657', '1.'], #
#                  'ggH_hww' : ['0.98554', '1.'], # These numbers are used to normalize the PS variation to the same integral as the nominal after the wwSel skim
#                  'qqH_hww' : ['0.92511', '1.'], #
#                },
#                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__btagSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__PS'+skim,
#                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__btagSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC'+skim,
#                'AsLnN'      : '1',
#                }

#FIXME: Add UE uncertainty
#nuisances['UE']  = {
#                'name'  : 'UE', 
#                'skipCMS' : 1,
#                'kind'  : 'tree',
#                'type'  : 'shape',
#                'samples'  : {
#                  'WW'      : ['1.0226', '0.9897'], #
#                  'ggH_hww' : ['1.0739', '1.0211'], # These numbers are used to normalize the UE up/down variations to the same integral as the nominal after the wwSel skim
#                  'qqH_hww' : ['1.0560', '0.9992'], #
#                },
#                'folderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__btagSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__UEup'+skim,
#                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__btagSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__UEdo'+skim,
#                'AsLnN'      : '1',
#                }


## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)
# [0] is muR=0.50000E+00 muF=0.50000E+00
# [8] is muR=0.20000E+01 muF=0.20000E+01
nuisances['DYQCDscale']  = {
                'name'  : 'QCDscale_V',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'DY'      : ['LHEScaleWeight[8]', 'LHEScaleWeight[0]'],
                }
}


#
#
# Theory uncertainty for ggH
#
#
#   THU_ggH_Mu, THU_ggH_Res, THU_ggH_Mig01, THU_ggH_Mig12, THU_ggH_VBF2j, THU_ggH_VBF3j, THU_ggH_PT60, THU_ggH_PT120, THU_ggH_qmtop
#
#   see https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools
#
# FIXME: Add these uncertainties


#nuisances['ggH_mu']  = {
#                'name'  : 'THU_ggH_Mu',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'ggH_hww'   : ['ggH_mu', '1+(1.-ggH_mu)'],
#                   'ggH_htt'   : ['ggH_mu', '1+(1.-ggH_mu)'],
#                   },
#                }
#
#
#nuisances['ggH_res']  = {
#                'name'  : 'THU_ggH_Res',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'ggH_hww'   : ['ggH_res', '1+(1.-ggH_res)'],
#                   'ggH_htt'   : ['ggH_res', '1+(1.-ggH_res)'],
#                   },
#                }
#
#nuisances['ggH_mig01']  = {
#                'name'  : 'THU_ggH_Mig01',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'ggH_hww'   : ['ggH_mig01', '1+(1.-ggH_mig01)'],
#                   'ggH_htt'   : ['ggH_mig01', '1+(1.-ggH_mig01)'],
#                   },
#                }
#
#nuisances['ggH_mig12']  = {
#                'name'  : 'THU_ggH_Mig12',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'ggH_hww'   : ['ggH_mig12', '1+(1.-ggH_mig12)'],
#                   'ggH_htt'   : ['ggH_mig12', '1+(1.-ggH_mig12)'],
#                   },
#                }
#
#nuisances['ggH_pT60']  = {
#                'name'  : 'THU_ggH_PT60',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'ggH_hww'   : ['ggH_pT60', '1+(1.-ggH_pT60)'],
#                   'ggH_htt'   : ['ggH_pT60', '1+(1.-ggH_pT60)'],
#                   },
#                }
#
#nuisances['ggH_pT120']  = {
#                'name'  : 'THU_ggH_PT120',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'ggH_hww'   : ['ggH_pT120', '1+(1.-ggH_pT120)'],
#                   'ggH_htt'   : ['ggH_pT120', '1+(1.-ggH_pT120)'],
#                   },
#                }
#
#nuisances['ggH_VBF2j']  = {
#                'name'  : 'THU_ggH_VBF2j',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'ggH_hww'   : ['ggH_VBF2j', '1+(1.-ggH_VBF2j)'],
#                   'ggH_htt'   : ['ggH_VBF2j', '1+(1.-ggH_VBF2j)'],
#                   },
#                }
#
#nuisances['ggH_VBF3j']  = {
#                'name'  : 'THU_ggH_VBF3j',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'ggH_hww'   : ['ggH_VBF3j', '1+(1.-ggH_VBF3j)'],
#                   'ggH_htt'   : ['ggH_VBF3j', '1+(1.-ggH_VBF3j)'],
#                   },
#                }
#
#nuisances['ggH_qmtop']  = {
#                'name'  : 'THU_ggH_qmtop',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'ggH_hww'   : ['ggH_qmtop', '1+(1.-ggH_qmtop)'],
#                   'ggH_htt'   : ['ggH_qmtop', '1+(1.-ggH_qmtop)'],
#                   },
#                }

nuisances['QCDscale_CRSR_accept_dytt']  = {
               'name'  : 'CMS_hww_QCDscale_CRSR_accept_dytt', 
               'type'  : 'lnN',
               'samples'  : {
                   'DY' : '1.02',
                   },
               'cuts'  : [
                 'hww2l2v_13TeV_dytt_of0j',
                 'hww2l2v_13TeV_dytt_of2j',
                 'hww2l2v_13TeV_dytt_of3j',
                 'hww2l2v_13TeV_dytt_of4j',
                 'hww2l2v_13TeV_dytt_of2j_vbf',
                 'hww2l2v_13TeV_dytt_of2j_vh2j'
                ]               
              }

nuisances['QCDscale_CRSR_accept_top']  = {
               'name'  : 'CMS_hww_QCDscale_CRSR_accept_top', 
               'type'  : 'lnN',
               'samples'  : {
                   'top' : '1.01',
                   },
               'cuts'  : [
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_top_of3j',
                 'hww2l2v_13TeV_top_of4j',
                 'hww2l2v_13TeV_top_of2j_vbf',
                 'hww2l2v_13TeV_top_of2j_vh2j'
                ]               
              }

#FIXME: check this 3%
nuisances['QCDscale_VZ']  = {
               'name'  : 'QCDscale_VZ', 
               'samples'  : {
                   'VZ' : '1.03',
                   },
               'type'  : 'lnN'
              }



#### QCD scale uncertainties for Higgs signals other than ggH

from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()

nuisances['QCDscale_ggH']  = {
               'name'  : 'QCDscale_ggH', 
               'samples'  : {
                   'H_htt'   : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }


nuisances['QCDscale_qqH']  = {
               'name'  : 'QCDscale_qqH', 
               'samples'  : {
                   'qqH_hww_0j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_hww_1j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_hww_2j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_hww_3j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_hww_4j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_hww_0j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_hww_1j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_hww_2j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_hww_3j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_hww_4j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

#FIXME make it work with XH configuration
nuisances['QCDscale_VH']  = {
               'name'  : 'QCDscale_VH', 
               'samples'  : {
                   'WH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
                   'WH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
                   'ZH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
                   'ZH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_ggZH']  = {
               'name'  : 'QCDscale_ggZH', 
               'samples'  : {
                   'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','scale','sm'),                  
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_bbH']  = {
               'name'  : 'QCDscale_bbH',
               'samples'  : {
                   'bbH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_ttH']  = {
               'name'  : 'QCDscale_ttH',
               'samples'  : {
                   'ttH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

#FIXME: these come from HIG-16-042, maybe should be recomputed?
#FIXME: make it work with XH config
nuisances['QCDscale_qqbar_ACCEPT']  = {
               'name'  : 'QCDscale_qqbar_ACCEPT', 
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww_0j_fid' : '1.007',
                   'qqH_hww_1j_fid' : '1.007',
                   'qqH_hww_2j_fid' : '1.007',
                   'qqH_hww_3j_fid' : '1.007',
                   'qqH_hww_4j_fid' : '1.007',
                   'qqH_hww_0j_nonfid' : '1.007',
                   'qqH_hww_1j_nonfid' : '1.007',
                   'qqH_hww_2j_nonfid' : '1.007',
                   'qqH_hww_3j_nonfid' : '1.007',
                   'qqH_hww_4j_nonfid' : '1.007',
                   'qqH_htt' : '1.007',
                   'WH_hww'  : '1.05',
                   'WH_htt'  : '1.05',
                   'ZH_hww'  : '1.04',
                   'ZH_htt'  : '1.04',
                   'VZ'      : '1.029',
                   },
              }

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['QCDscale_gg_ACCEPT']  = {
               'name'  : 'QCDscale_gg_ACCEPT', 
               'samples'  : {
                   'ggWW'    : '1.027',
                   'ggH_hww_0j_fid' : '1.027',
                   'ggH_hww_1j_fid' : '1.027',
                   'ggH_hww_2j_fid' : '1.027',
                   'ggH_hww_3j_fid' : '1.027',
                   'ggH_hww_4j_fid' : '1.027',
                   'ggH_hww_0j_nonfid' : '1.027',
                   'ggH_hww_1j_nonfid' : '1.027',
                   'ggH_hww_2j_nonfid' : '1.027',
                   'ggH_hww_3j_nonfid' : '1.027',
                   'ggH_hww_4j_nonfid' : '1.027',
                   'ggH_htt' : '1.027',
                   'H_htt'   : '1.027',
                   'ggZH_hww': '1.027',                   
                   },
               'type'  : 'lnN',
              }

###### pdf uncertainty

nuisances['pdf_Higgs_gg']  = {
               'name'  : 'pdf_Higgs_gg', 
               'samples'  : {
                   'ggH_hww_0j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_hww_1j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_hww_2j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_hww_3j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_hww_4j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_hww_0j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_hww_1j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_hww_2j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_hww_3j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_hww_4j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'H_htt'   : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm'), 
                   'bbH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH' ,'125.09','pdf','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_Higgs_ttH']  = {
               'name'  : 'pdf_Higgs_ttH',
               'samples'  : {
                   'ttH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH' ,'125.09','pdf','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_Higgs_qqbar']  = {
               'name'  : 'pdf_Higgs_qqbar', 
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww_0j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_hww_1j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_hww_2j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_hww_3j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_hww_4j_fid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_hww_0j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_hww_1j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_hww_2j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_hww_3j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_hww_4j_nonfid' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'WH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   'WH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   'ZH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   'ZH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   },
              }

#FIXME: check this 4%
nuisances['pdf_qqbar']  = {
               'name'  : 'pdf_qqbar',
               'type'  : 'lnN',
               'samples'  : {
                   'VZ'      : '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
                   },
              }

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_Higgs_gg_ACCEPT']  = {
               'name'  : 'pdf_Higgs_gg_ACCEPT', 
               'samples'  : {
                   'ggH_hww_0j_fid' : '1.005',
                   'ggH_hww_1j_fid' : '1.005',
                   'ggH_hww_2j_fid' : '1.005',
                   'ggH_hww_3j_fid' : '1.005',
                   'ggH_hww_4j_fid' : '1.005',
                   'ggH_hww_0j_nonfid' : '1.005',
                   'ggH_hww_1j_nonfid' : '1.005',
                   'ggH_hww_2j_nonfid' : '1.005',
                   'ggH_hww_3j_nonfid' : '1.005',
                   'ggH_hww_4j_nonfid' : '1.005',
                   'ggH_htt' : '1.005',
                   'H_htt'   : '1.005',
                   'ggZH_hww': '1.005', 
                   },
               'type'  : 'lnN',
              }

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_gg_ACCEPT']  = {
               'name'  : 'pdf_gg_ACCEPT',
               'samples'  : {
                   'ggWW'    : '1.005',
                   },
               'type'  : 'lnN',
              }

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_Higgs_qqbar_ACCEPT']  = {
               'name'  : 'pdf_Higgs_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'qqH_hww_0j_fid' : '1.011',
                   'qqH_hww_1j_fid' : '1.011',
                   'qqH_hww_2j_fid' : '1.011',
                   'qqH_hww_3j_fid' : '1.011',
                   'qqH_hww_4j_fid' : '1.011',
                   'qqH_hww_0j_nonfid' : '1.011',
                   'qqH_hww_1j_nonfid' : '1.011',
                   'qqH_hww_2j_nonfid' : '1.011',
                   'qqH_hww_3j_nonfid' : '1.011',
                   'qqH_hww_4j_nonfid' : '1.011',
                   'qqH_htt' : '1.011',
                   'WH_hww'  : '1.007',
                   'WH_htt'  : '1.007',
                   'ZH_hww'  : '1.012',
                   'ZH_htt'  : '1.012',
                   },
              }

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['pdf_qqbar_ACCEPT']  = {
               'name'  : 'pdf_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'VZ'      : '1.005',
                   },
              }

# ggww and interference

nuisances['QCDscale_ggWW']  = {
               'name'  : 'QCDscale_ggWW',
               'type'  : 'lnN',
               'samples'  : {
                   'ggWW' : '1.15',
                   },
              }

#  - WW shaping
#FIXME: nll weights are not in the trees??
#nuisances['WWresum0j']  = {
#                'name'  : 'WWresum0j',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
#                   },
#               'cuts'  : [
#                 'hww2l2v_13TeV_of0j',
#                 'hww2l2v_13TeV_top_of0j',
#                 'hww2l2v_13TeV_dytt_of0j',
##                 
#                 'hww2l2v_13TeV_me_0j',
#                 'hww2l2v_13TeV_em_0j',
##
#                 'hww2l2v_13TeV_me_mp_0j',
#                 'hww2l2v_13TeV_me_pm_0j',
#                 'hww2l2v_13TeV_em_mp_0j',
#                 'hww2l2v_13TeV_em_pm_0j',
##                
#		 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
#                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
#                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
#                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
##
#                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
#                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
#                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
#                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
##
#                ]               
#                
#                }
#
#
#nuisances['WWresum1j']  = {
#                'name'  : 'WWresum1j',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
#                   },
#               'cuts'  : [
#                 'hww2l2v_13TeV_of1j',
#                 'hww2l2v_13TeV_top_of1j',
#                 'hww2l2v_13TeV_dytt_of1j',
##                 
#                 'hww2l2v_13TeV_me_1j',
#                 'hww2l2v_13TeV_em_1j',
##
#                 'hww2l2v_13TeV_me_mp_1j',
#                 'hww2l2v_13TeV_me_pm_1j',
#                 'hww2l2v_13TeV_em_mp_1j',
#                 'hww2l2v_13TeV_em_pm_1j',
##               
#                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
#                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
#                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
#                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
##
#                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
#                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
#                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
#                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
##
#                ]               
#                }
#
#nuisances['WWqscale0j']  = {
#                'name'  : 'WWqscale0j',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
#                   },
#               'cuts'  : [
#                 'hww2l2v_13TeV_of0j',
#                 'hww2l2v_13TeV_top_of0j',
#                 'hww2l2v_13TeV_dytt_of0j',
##                 
#                 'hww2l2v_13TeV_me_0j',
#                 'hww2l2v_13TeV_em_0j',
##
#                 'hww2l2v_13TeV_me_mp_0j',
#                 'hww2l2v_13TeV_me_pm_0j',
#                 'hww2l2v_13TeV_em_mp_0j',
#                 'hww2l2v_13TeV_em_pm_0j',
##               
#                 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
#                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
#                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
#                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
##                
#                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
#                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
#                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
#                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
##  
#                ] 
#                }
#
#
#nuisances['WWqscale1j']  = {
#                'name'  : 'WWqscale1j',
#                'skipCMS' : 1,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                   'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
#                   },
#               'cuts'  : [
#                 'hww2l2v_13TeV_of1j',
#                 'hww2l2v_13TeV_top_of1j',
#                 'hww2l2v_13TeV_dytt_of1j',
##                 
#                 'hww2l2v_13TeV_me_1j',
#                 'hww2l2v_13TeV_em_1j',
##
#                 'hww2l2v_13TeV_me_mp_1j',
#                 'hww2l2v_13TeV_me_pm_1j',
#                 'hww2l2v_13TeV_em_mp_1j',
#                 'hww2l2v_13TeV_em_pm_1j',
##
#                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
#                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
#                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
#                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
##
#                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
#                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
#                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
#                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
##                 
#                ] 
#                }

nuisances['WgStarScale']  = {
               'name'  : 'CMS_hww_WgStarScale', 
               'type'  : 'lnN',
               'samples'  : {
                   'WgS'    : '1.25',  # 0.5 / 2.0   --> k_factor = 2.0 +/- 0.5
                   'VgS'    : '1.25',  # 0.5 / 2.0   --> k_factor = 2.0 +/- 0.5
                   'WZgS_L' : '1.25',  
                   },
                }
 
nuisances['WZScale'] = {
               'name'  : 'CMS_hww_WZScale',
               'type'  : 'lnN',
               'samples'  : {
                   'WZgS_H' : '1.16', 
                   },
                }

nuisances['DYttnorm0j']  = {
               'name'  : 'CMS_hww_DYttnorm0j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of0j_pt2ge20',
                 'hww2l2v_13TeV_of0j_pt2lt20',
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_dytt_of0j',
#                 
                 'hww2l2v_13TeV_me_0j',
                 'hww2l2v_13TeV_em_0j',
#
                 'hww2l2v_13TeV_me_mp_0j',
                 'hww2l2v_13TeV_me_pm_0j',
                 'hww2l2v_13TeV_em_mp_0j',
                 'hww2l2v_13TeV_em_pm_0j',
#
                 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
#                
                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
#
                ]
              }

nuisances['DYttnorm1j']  = {
               'name'  : 'CMS_hww_DYttnorm1j', 
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of1j_pt2ge20',
                 'hww2l2v_13TeV_of1j_pt2lt20',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_dytt_of1j',
#                 
                 'hww2l2v_13TeV_me_1j',
                 'hww2l2v_13TeV_em_1j',
#
                 'hww2l2v_13TeV_me_mp_1j',
                 'hww2l2v_13TeV_me_pm_1j',
                 'hww2l2v_13TeV_em_mp_1j',
                 'hww2l2v_13TeV_em_pm_1j',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
#                 
                ]
              }

nuisances['DYttnorm2j']  = {
               'name'  : 'CMS_hww_DYttnorm2j',
               'samples'  : {
                   'DY' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of2j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_dytt_of2j',
                ]
              }

nuisances['WWnorm0j']  = {
               'name'  : 'CMS_hww_WWnorm0j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of0j_pt2ge20',
                 'hww2l2v_13TeV_of0j_pt2lt20',
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_dytt_of0j',              
#                 
                 'hww2l2v_13TeV_me_0j',
                 'hww2l2v_13TeV_em_0j',
#
                 'hww2l2v_13TeV_me_mp_0j',
                 'hww2l2v_13TeV_me_pm_0j',
                 'hww2l2v_13TeV_em_mp_0j',
                 'hww2l2v_13TeV_em_pm_0j',
#                
                 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
#                
                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
#
                ]
              }

nuisances['WWnorm1j']  = {
               'name'  : 'CMS_hww_WWnorm1j', 
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of1j_pt2ge20',
                 'hww2l2v_13TeV_of1j_pt2lt20',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_dytt_of1j',              
#                 
                 'hww2l2v_13TeV_me_1j',
                 'hww2l2v_13TeV_em_1j',
#
                 'hww2l2v_13TeV_me_mp_1j',
                 'hww2l2v_13TeV_me_pm_1j',
                 'hww2l2v_13TeV_em_mp_1j',
                 'hww2l2v_13TeV_em_pm_1j',
#               
                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
#  
                ]
              }

nuisances['WWnorm2j']  = {
               'name'  : 'CMS_hww_WWnorm2j',
               'samples'  : {
                   'WW' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of2j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_dytt_of2j',
                ]
              }

nuisances['Topnorm0j']  = {
               'name'  : 'CMS_hww_Topnorm0j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of0j_pt2ge20',
                 'hww2l2v_13TeV_of0j_pt2lt20',
                 'hww2l2v_13TeV_top_of0j',
                 'hww2l2v_13TeV_dytt_of0j',              
#                 
                 'hww2l2v_13TeV_me_0j',
                 'hww2l2v_13TeV_em_0j',
#
                 'hww2l2v_13TeV_me_mp_0j',
                 'hww2l2v_13TeV_me_pm_0j',
                 'hww2l2v_13TeV_em_mp_0j',
                 'hww2l2v_13TeV_em_pm_0j',
#
                 'hww2l2v_13TeV_em_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_0j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_0j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_0j_pt2ge20',
#                
                 'hww2l2v_13TeV_em_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_0j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_0j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_0j_pt2lt20',
#                
                ]
              }

nuisances['Topnorm1j']  = {
               'name'  : 'CMS_hww_Topnorm1j', 
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of1j_pt2ge20',
                 'hww2l2v_13TeV_of1j_pt2lt20',
                 'hww2l2v_13TeV_top_of1j',
                 'hww2l2v_13TeV_dytt_of1j',              
#                 
                 'hww2l2v_13TeV_me_1j',
                 'hww2l2v_13TeV_em_1j',
#
                 'hww2l2v_13TeV_me_mp_1j',
                 'hww2l2v_13TeV_me_pm_1j',
                 'hww2l2v_13TeV_em_mp_1j',
                 'hww2l2v_13TeV_em_pm_1j',
#   
                 'hww2l2v_13TeV_em_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_em_mp_1j_pt2ge20',
                 'hww2l2v_13TeV_me_pm_1j_pt2ge20',
                 'hww2l2v_13TeV_me_mp_1j_pt2ge20',
#
                 'hww2l2v_13TeV_em_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_em_mp_1j_pt2lt20',
                 'hww2l2v_13TeV_me_pm_1j_pt2lt20',
                 'hww2l2v_13TeV_me_mp_1j_pt2lt20',
#              
                ]
              }

nuisances['Topnorm2j']  = {
               'name'  : 'CMS_hww_Topnorm2j',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                 'hww2l2v_13TeV_of2j',
                 'hww2l2v_13TeV_top_of2j',
                 'hww2l2v_13TeV_dytt_of2j',
                ]
              }


nuisances['singleTopToTTbar']  = {
                'name'  : 'singleTopToTTbar',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : { 
                   'top'     : ['(( (topGenPt>0 && antitopGenPt<0) || (topGenPt<0 && antitopGenPt>0)  ) * 1.0816 + ( topGenPt>0 && antitopGenPt>0 ))',
                                '(( (topGenPt>0 && antitopGenPt<0) || (topGenPt<0 && antitopGenPt>0)  ) * 0.9184 + ( topGenPt>0 && antitopGenPt>0 ))'],
                }
                # tt = 17/18/19 depending on the sample/generator
                # tW = 15/16
           }

## Top pT reweighting uncertainty

nuisances['TopPtRew']  = {
                'name'  : 'TopPtRew',   # Theory uncertainty
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : {
                     'top'  : ["1.","((1./"+Top_pTrw+" - 1)*(topGenPt>0 && antitopGenPt>0) + 1)"]
                }
         }


## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }

#### Use the following if you want to apply the MC stat nuisances accoriding to the standard approach
#                         'typeStat' : 'bbb',
#                         },
#                    
#                   'DY': {
#                         'typeStat' : 'bbb',
#                         'keepNormalization' : '1'  # default = 0 -> 0=don't keep normalization
#                         },
#                    
#                   'ggWW': {
#                         'typeStat' : 'bbb',
#                         },
#                    
#                   'ggWW_Int': {
#                         'typeStat' : 'bbb',
#                         },
#                    
#                   'WW': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'VZ': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'WZ': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'VVV': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'H_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ggH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'qqH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'WH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ZH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'H_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ggH_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'qqH_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'WH_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ZH_htt': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'ggZH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#
#                   'bbH_hww': {
#                         'typeStat' : 'bbb',
#                         },
#                   
#                   'Fake': {
#                         'typeStat' : 'bbb',
#                         },
#                   
#                   'Vg': {  
#                         'typeStat' : 'bbb',
#                         },
#
#                   'VgS':{  
#                         'typeStat' : 'bbb',
#                         },
#                 },
#               'type'  : 'shape'
#              }

