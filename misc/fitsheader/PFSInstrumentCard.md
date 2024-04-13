## ``ccdActor`` FITS cards, generated from ``ics_actorkeys`` 1.5.7-dirty

Name | Longname | Type | Format | pFormat | Units | Actor | Keyword | Comment | Enum
---- | -------- | ---- | ------ | ----- | ----- | ------- | ------- | ------- | ----
``W_AGDEC`` | ``W_AGDEC`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``arcsec`` | ``gen2`` | ``telGuide[1]`` | Cumulative Dec guide offset | 
``W_AGINR`` | ``W_AGINR`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``arcsec`` | ``gen2`` | ``telGuide[2]`` | Cumulative rotator guide offset | 
``W_AGRA`` | ``W_AGRA`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``arcsec`` | ``gen2`` | ``telGuide[0]`` | Cumulative RA guide offset | 
``W_AITARG`` | ``W_ARGON_LAMP_STATE`` | ``bool`` |  |  | ``-`` | ``pfilamps`` | ``lampRequestMask[1]`` | Argon lamp was on | 
``W_AITHGC`` | ``W_HGCD_LAMP_STATE`` | ``bool`` |  |  | ``-`` | ``pfilamps`` | ``lampRequestMask[4]`` | HgCd lamp was on | 
``W_AITKRY`` | ``W_KRYPTON_LAMP_STATE`` | ``bool`` |  |  | ``-`` | ``pfilamps`` | ``lampRequestMask[2]`` | Krypton lamp was on | 
``W_AITLWH`` | ``W_AIT_DCB_LINEWHEEL`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``linewheel[1]`` | line wheel hole size | 
``W_AITNEO`` | ``W_NEON_LAMP_STATE`` | ``bool`` |  |  | ``-`` | ``pfilamps`` | ``lampRequestMask[0]`` | Neon lamp was on | 
``W_AITQTH`` | ``W_HALOGEN_LAMP_STATE`` | ``bool`` |  |  | ``-`` | ``pfilamps`` | ``lampRequestMask[5]`` | Halogen lamp was on | 
``W_AITQWH`` | ``W_AIT_DCB_QTHWHEEL`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``qthwheel[1]`` | qth wheel hole size | 
``W_AITWAV`` | ``W_AIT_MONO_WAVELENGTH`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``-`` | ``dcb`` | ``monochromator[2]`` | wavelength (nm) | 
``W_AITXEN`` | ``W_XENON_LAMP_STATE`` | ``bool`` |  |  | ``-`` | ``pfilamps`` | ``lampRequestMask[3]`` | Xenon lamp was on | 
``W_BIADTY`` | ``W_SPS_BIA_STROBE_DUTY`` | ``int`` | ``%d`` | ``%d`` | ``percent`` | ``sps`` | ``biaStatus[2]`` | bia strobe duty cycle | 
``W_BIAOFF`` | ``W_SPS_BIA_PULSE_OFF`` | ``int`` | ``%d`` | ``%d`` | ``ms`` | ``sps`` | ``biaStatus[4]`` | bia pulse low duration | 
``W_BIAON`` | ``W_SPS_BIA_PULSE_ON`` | ``int`` | ``%d`` | ``%d`` | ``ms`` | ``sps`` | ``biaStatus[3]`` | bia pulse high duration | 
``W_BIAPER`` | ``W_SPS_BIA_STROBE_PERIOD`` | ``int`` | ``%d`` | ``%d`` | ``ms`` | ``sps`` | ``biaStatus[1]`` | bia strobe period | 
``W_BIAPOW`` | ``W_SPS_BIA_POWER`` | ``int`` | ``%d`` | ``%d`` | ``percent`` | ``sps`` | ``biaStatus[0]`` | bia power(%) | 
``W_CAMPRW`` | ``W_CCD_AMP_ROWS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``ccd_r3`` | ``geometry[2]`` | total number of columns in amp | 
``W_CCD0T`` | ``W_CCD0_TEMP`` | ``float`` | ``%-15G`` | ``%0.2f`` | ``K`` | ``ccd_r3`` | ``ccdTemps[1]`` | CCD0 temperature | 
``W_CCD1T`` | ``W_CCD1_TEMP`` | ``float`` | ``%-15G`` | ``%0.2f`` | ``K`` | ``ccd_r3`` | ``ccdTemps[2]`` | CCD1 temperature | 
``W_CCLACT`` | ``W_CCD_ACTIVE_COLS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``ccd_r3`` | ``geometry[7]`` | active cols | 
``W_CCLLDN`` | ``W_CCD_LEADIN_COLS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``ccd_r3`` | ``geometry[6]`` | (dropped) leadin columns | 
``W_CCLOVR`` | ``W_CCD_OVERSCAN_COLS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``ccd_r3`` | ``geometry[8]`` | overscan cols | 
``W_CIMROW`` | ``W_CCD_ROWS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``ccd_r3`` | ``geometry[1]`` | total number of rows in image | 
``W_CLARGT`` | ``W_PFILAMPS_ARGON_TIME`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``pfilamps`` | ``lampRequestTimes[1]`` | Argon lamp request time | 
``W_CLHGCT`` | ``W_PFILAMPS_HGCD_TIME`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``pfilamps`` | ``lampRequestTimes[4]`` | HgCd lamp request time | 
``W_CLKRYT`` | ``W_PFILAMPS_KRYPTON_TIME`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``pfilamps`` | ``lampRequestTimes[2]`` | Krypton lamp request time | 
``W_CLNEOT`` | ``W_PFILAMPS_NEON_TIME`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``pfilamps`` | ``lampRequestTimes[0]`` | Neon lamp request time | 
``W_CLQTHT`` | ``W_PFILAMPS_HALOGEN_TIME`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``pfilamps`` | ``lampRequestTimes[5]`` | Halogen lamp request time | 
``W_CLXENT`` | ``W_PFILAMPS_XENON_TIME`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``pfilamps`` | ``lampRequestTimes[3]`` | Xenon lamp request time | 
``W_CNAMPS`` | ``W_CCD_NAMPS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``ccd_r3`` | ``geometry[0]`` | number of CCD amps | 
``W_COFM00`` | ``W_ADC_MASTER_OFFSET_AMP00`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_master[0]`` | CCD0 amp0 master offset | 
``W_COFM01`` | ``W_ADC_MASTER_OFFSET_AMP01`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_master[1]`` | CCD0 amp1 master offset | 
``W_COFM02`` | ``W_ADC_MASTER_OFFSET_AMP02`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_master[2]`` | CCD0 amp2 master offset | 
``W_COFM03`` | ``W_ADC_MASTER_OFFSET_AMP03`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_master[3]`` | CCD0 amp3 master offset | 
``W_COFM10`` | ``W_ADC_MASTER_OFFSET_AMP10`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_master[4]`` | CCD1 amp0 master offset | 
``W_COFM11`` | ``W_ADC_MASTER_OFFSET_AMP11`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_master[5]`` | CCD1 amp1 master offset | 
``W_COFM12`` | ``W_ADC_MASTER_OFFSET_AMP12`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_master[6]`` | CCD1 amp2 master offset | 
``W_COFM13`` | ``W_ADC_MASTER_OFFSET_AMP13`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_master[7]`` | CCD1 amp3 master offset | 
``W_COFR00`` | ``W_ADC_REFERENCE_OFFSET_AMP00`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_reference[0]`` | CCD0 amp0 reference offset | 
``W_COFR01`` | ``W_ADC_REFERENCE_OFFSET_AMP01`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_reference[1]`` | CCD0 amp1 reference offset | 
``W_COFR02`` | ``W_ADC_REFERENCE_OFFSET_AMP02`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_reference[2]`` | CCD0 amp2 reference offset | 
``W_COFR03`` | ``W_ADC_REFERENCE_OFFSET_AMP03`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_reference[3]`` | CCD0 amp3 reference offset | 
``W_COFR10`` | ``W_ADC_REFERENCE_OFFSET_AMP10`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_reference[4]`` | CCD1 amp0 reference offset | 
``W_COFR11`` | ``W_ADC_REFERENCE_OFFSET_AMP11`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_reference[5]`` | CCD1 amp1 reference offset | 
``W_COFR12`` | ``W_ADC_REFERENCE_OFFSET_AMP12`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_reference[6]`` | CCD1 amp2 reference offset | 
``W_COFR13`` | ``W_ADC_REFERENCE_OFFSET_AMP13`` | ``float`` | ``%-15G`` |  | ``mV`` | ``ccd_r3`` | ``offsets_reference[7]`` | CCD1 amp3 reference offset | 
``W_CPAMPT`` | ``W_CCD_PREAMP_TEMP`` | ``float`` | ``%-15G`` | ``%0.2f`` | ``K`` | ``ccd_r3`` | ``ccdTemps[0]`` | preamp temperature | 
``W_CRLGHT`` | ``W_SCR_ROOMLIGHTS`` | ``str`` |  | ``%s`` | ``-`` | ``scr`` | ``scrLights[0]`` | State of ceiling lights | ``{'off', 'unknown', 'on'}``
``W_CRLOOP`` | ``W_SCR_CONTROL_LOOP_STATE`` | ``str`` |  | ``%s`` | ``-`` | ``scr`` | ``scrLoop[2]`` | Clean room operational state | ``{'off', 'unknown', 'on'}``
``W_CRRHUM`` | ``W_SCR_RELATIVE_HUMIDITY`` | ``float`` | ``%-15G`` |  | ``%`` | ``scr`` | ``scrHumidity[1]`` | Relative humidity inside clean room | 
``W_CRSETP`` | ``W_SCR_CONTROL_SETPOINT`` | ``float`` | ``%-15G`` |  | ``degC`` | ``scr`` | ``scrLoop[1]`` | Clean room setpoint temperature | 
``W_CRTEMP`` | ``W_SCR_CONTROL_TEMP`` | ``float`` | ``%-15G`` |  | ``degC`` | ``scr`` | ``scrLoop[0]`` | Clean room air temperature | 
``W_CRWACT`` | ``W_CCD_ACTIVE_ROWS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``ccd_r3`` | ``geometry[4]`` | active rows | 
``W_CRWLDN`` | ``W_CCD_LEADIN_ROWS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``ccd_r3`` | ``geometry[3]`` | (dropped) leadin rows | 
``W_CRWOVR`` | ``W_CCD_OVERSCAN_ROWS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``ccd_r3`` | ``geometry[5]`` | overscan rows | 
``W_DBNL01`` | ``W_DCB_BUNDLE01`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[0]`` | - | 
``W_DBNL02`` | ``W_DCB_BUNDLE02`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[1]`` | - | 
``W_DBNL03`` | ``W_DCB_BUNDLE03`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[2]`` | - | 
``W_DBNL04`` | ``W_DCB_BUNDLE04`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[3]`` | - | 
``W_DBNL05`` | ``W_DCB_BUNDLE05`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[4]`` | - | 
``W_DBNL06`` | ``W_DCB_BUNDLE06`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[5]`` | - | 
``W_DBNL07`` | ``W_DCB_BUNDLE07`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[6]`` | - | 
``W_DBNL08`` | ``W_DCB_BUNDLE08`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[7]`` | - | 
``W_DBNL09`` | ``W_DCB_BUNDLE09`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[8]`` | - | 
``W_DBNL10`` | ``W_DCB_BUNDLE10`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[9]`` | - | 
``W_DBNL11`` | ``W_DCB_BUNDLE11`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbBundles[10]`` | - | 
``W_DBNL12`` | ``W_DCB_BUNDLE12`` | ``str`` |  | ``%s`` |``-`` | ``dcb`` | ``dcbBundles[11]`` | - | 
``W_DECOFF`` | ``W_DECOFF`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``arcsec`` | ``gen2`` | ``offsets[1]`` | Dec offset | 
``W_DMSK01`` | ``W_DCB_MASK01`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[0]`` | - | 
``W_DMSK02`` | ``W_DCB_MASK02`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[1]`` | - | 
``W_DMSK03`` | ``W_DCB_MASK03`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[2]`` | - | 
``W_DMSK04`` | ``W_DCB_MASK04`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[3]`` | - | 
``W_DMSK05`` | ``W_DCB_MASK05`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[4]`` | - | 
``W_DMSK06`` | ``W_DCB_MASK06`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[5]`` | - | 
``W_DMSK07`` | ``W_DCB_MASK07`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[6]`` | - | 
``W_DMSK08`` | ``W_DCB_MASK08`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[7]`` | - | 
``W_DMSK09`` | ``W_DCB_MASK09`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[8]`` | - | 
``W_DMSK10`` | ``W_DCB_MASK10`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[9]`` | - | 
``W_DMSK11`` | ``W_DCB_MASK11`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[10]`` | - | 
``W_DMSK12`` | ``W_DCB_MASK12`` | ``str`` |  | ``%s`` | ``-`` | ``dcb`` | ``dcbMasks[11]`` | - | 
``W_DTHDEC`` | ``W_DTHDEC`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``arcsec`` | ``gen2`` | ``telDither[1]`` | Cumulative Dec dither offset | 
``W_DTHPA`` | ``W_DTHPA`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``arcsec`` | ``gen2`` | ``telDither[2]`` | Cumulative posAngle dither offset | 
``W_DTHRA`` | ``W_DTHRA`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``arcsec`` | ``gen2`` | ``telDither[0]`` | Cumulative RA dither offset | 
``W_ENBIAS`` | ``W_ENU_BIA_STATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``bia[0]`` | bia current state | ``{'off', 'on', 'undef'}``
``W_ENBSHM`` | ``W_ENU_BIASHA_MODE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``biashaMode[0]`` | biasha operation mode | ``{'operation', 'simulation'}``
``W_ENBSHS`` | ``W_ENU_BIASHA_STATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``biashaFSM[0]`` | biasha operational state-machine | ``{'ONLINE', 'none', 'LOADED', 'OFF'}``
``W_ENBSHT`` | ``W_ENU_BIASHA_SUBSTATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``biashaFSM[1]`` | biasha action state-machine | ``{'BIA', 'IDLE', 'none', 'FAILED', 'OPENBLUE', 'LOADING', 'OPENRED', 'INITIALISING', 'BUSY', 'EXPOSING'}``
``W_ENFCAM`` | ``W_ENU_FCA_MODE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``slitMode[0]`` | fca operation mode | ``{'operation', 'simulation'}``
``W_ENFCAP`` | ``W_ENU_FCA_POSITION`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``slitPosition[0]`` | FCA position | 
``W_ENFCAS`` | ``W_ENU_FCA_STATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``slitFSM[0]`` | slit-hexapod operational state-machine | ``{'ONLINE', 'none', 'LOADED', 'OFF'}``
``W_ENFCAT`` | ``W_ENU_FCA_SUBSTATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``slitFSM[1]`` | slit-hexapod action state-machine | ``{'IDLE', 'none', 'FAILED', 'LOADING', 'INITIALISING', 'MOVING', 'SHUTDOWN'}``
``W_ENFCAU`` | ``W_ENU_FCA_ROLL`` | ``float`` | ``%-15G`` | ``%.5f`` | ``deg`` | ``enu_sm3`` | ``slit[3]`` | - | 
``W_ENFCAV`` | ``W_ENU_FCA_PITCH`` | ``float`` | ``%-15G`` | ``%.5f`` | ``deg`` | ``enu_sm3`` | ``slit[4]`` | - | 
``W_ENFCAW`` | ``W_ENU_FCA_YAW`` | ``float`` | ``%-15G`` | ``%.5f`` | ``deg`` | ``enu_sm3`` | ``slit[5]`` | - | 
``W_ENFCAX`` | ``W_ENU_FCA_FOCUS, wrt optical axis (+ towards collimator)`` | ``float`` | ``%-15G`` | ``%.5f`` | ``mm`` | ``enu_sm3`` | ``slit[0]`` | - | 
``W_ENFCAY`` | ``W_ENU_FCA_WAVELENGTH, wrt wavelength axis (+ towards red wl)`` | ``float`` | ``%-15G`` | ``%.5f`` | ``mm`` | ``enu_sm3`` | ``slit[1]`` | - | 
``W_ENFCAZ`` | ``W_ENU_FCA_FIBERS, wrt fibers axis (+ towards low fiber id)`` | ``float`` | ``%-15G`` | ``%.5f`` | ``mm`` | ``enu_sm3`` | ``slit[2]`` | - | 
``W_ENIISA`` | ``W_ENU_IIS_ARGON`` | ``bool`` |  |  | ``-`` | ``enu_sm3`` | ``argon[0]`` | argon lamp state | 
``W_ENIISC`` | ``W_ENU_IIS_HALOGEN`` | ``bool`` |  |  | ``-`` | ``enu_sm3`` | ``halogen[0]`` | halogen lamp state | 
``W_ENIISH`` | ``W_ENU_IIS_HGAR`` | ``bool`` |  |  | ``-`` | ``enu_sm3`` | ``hgar[0]`` | Mercury-argon lamp state | 
``W_ENIISK`` | ``W_ENU_IIS_KRYPTON`` | ``bool`` |  |  | ``-`` | ``enu_sm3`` | ``krypton[0]`` | krypton lamp state | 
``W_ENIISM`` | ``W_ENU_IIS_MODE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``iisMode[0]`` | iis operation mode | ``{'operation', 'simulation'}``
``W_ENIISN`` | ``W_ENU_IIS_NEON`` | ``bool`` |  |  | ``-`` | ``enu_sm3`` | ``neon[0]`` | Neon lamp state | 
``W_ENIISS`` | ``W_ENU_IIS_STATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``iisFSM[0]`` | iis operational state-machine | ``{'ONLINE', 'none', 'LOADED', 'OFF'}``
``W_ENIIST`` | ``W_ENU_IIS_SUBSTATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``iisFSM[1]`` | iis action state-machine | ``{'IDLE', 'none', 'FAILED', 'WARMING', 'LOADING', 'INITIALISING'}``
``W_ENPDUM`` | ``W_ENU_PDU_MODE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``pduMode[0]`` | pdu operation mode | ``{'operation', 'simulation'}``
``W_ENPDUS`` | ``W_ENU_PDU_STATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``pduFSM[0]`` | pdu operational state-machine | ``{'ONLINE', 'none', 'LOADED', 'OFF'}``
``W_ENPDUT`` | ``W_ENU_PDU_SUBSTATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``pduFSM[1]`` | pdu action state-machine | ``{'IDLE', 'none', 'FAILED', 'LOADING', 'INITIALISING', 'SWITCHING'}``
``W_ENRDAM`` | ``W_ENU_RDA_MODE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``rexmMode[0]`` | rda operation mode | ``{'operation', 'simulation'}``
``W_ENRDAP`` | ``W_ENU_RDA_POSITION`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``rexm[0]`` | rexm current position | ``{'undef', 'low', 'med', 'error'}``
``W_ENRDAS`` | ``W_ENU_RDA_STATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``rexmFSM[0]`` | rexm operational state-machine | ``{'ONLINE', 'none', 'LOADED', 'OFF'}``
``W_ENRDAT`` | ``W_ENU_RDA_SUBSTATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``rexmFSM[1]`` | rexm action state-machine | ``{'IDLE', 'none', 'FAILED', 'LOADING', 'INITIALISING', 'SAFESTOP', 'MOVING'}``
``W_ENSHUT`` | ``W_ENU_SHUTTERS_POSITION`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``shutters[0]`` | shutters current position | ``{'openblue', 'close', 'open', 'undef', 'openred'}``
``W_ENTMPM`` | ``W_ENU_TEMP_MODE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``tempsMode[0]`` | temps operation mode | ``{'operation', 'simulation'}``
``W_ENTMPS`` | ``W_ENU_TEMP_STATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``tempsFSM[0]`` | temps controller operational state-machine | ``{'ONLINE', 'none', 'LOADED', 'OFF'}``
``W_ENTMPT`` | ``W_ENU_TEMP_SUBSTATE`` | ``str`` |  | ``%s`` | ``-`` | ``enu_sm3`` | ``tempsFSM[1]`` | temps controller action state-machine | ``{'IDLE', 'none', 'FAILED', 'LOADING', 'INITIALISING'}``
``W_ETMP1`` | ``W_MOTOR_RDA`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[0]`` | MOTOR_RDA | 
``W_ETMP10`` | ``W_COLLIMATOR_FRAME_TOP`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[9]`` | COLLIMATOR_FRAME_TOP | 
``W_ETMP11`` | ``W_BENCH_LEFT_TOP`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[0]`` | BENCH_LEFT_TOP | 
``W_ETMP12`` | ``W_BENCH_LEFT_BOTTOM`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[1]`` | BENCH_LEFT_BOTTOM | 
``W_ETMP13`` | ``W_BENCH_RIGHT_TOP`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[2]`` | BENCH_RIGHT_TOP | 
``W_ETMP14`` | ``W_BENCH_RIGHT_BOTTOM`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[3]`` | BENCH_RIGHT_BOTTOM | 
``W_ETMP15`` | ``W_BENCH_FAR_TOP`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[4]`` | BENCH_FAR_TOP | 
``W_ETMP16`` | ``W_BENCH_FAR_BOTTOM`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[5]`` | BENCH_FAR_BOTTOM | 
``W_ETMP17`` | ``W_BENCH_NEAR_TOP`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[6]`` | BENCH_NEAR_TOP | 
``W_ETMP18`` | ``W_BENCH_NEAR_BOTTOM`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[7]`` | BENCH_NEAR_BOTTOM | 
``W_ETMP19`` | ``W_BENCH_CENTRAL_TOP`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[8]`` | BENCH_CENTRAL_TOP | 
``W_ETMP2`` | ``W_MOTOR_SHUTTER_B`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[1]`` | MOTOR_SHUTTER_B | 
``W_ETMP20`` | ``W_ENU_TEMP_20`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps2[9]`` | ENU_TEMP_20 | 
``W_ETMP3`` | ``W_MOTOR_SHUTTER_R`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[2]`` | MOTOR_SHUTTER_R | 
``W_ETMP4`` | ``W_BIA_BOX_TOP`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[3]`` | BIA_BOX_TOP | 
``W_ETMP5`` | ``W_BIA_BOX_BOTTOM`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[4]`` | BIA_BOX_BOTTOM | 
``W_ETMP6`` | ``W_FIBER_UNIT_HEXAPOD_BOTTOM`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[5]`` | FIBER_UNIT_HEXAPOD_BOTTOM | 
``W_ETMP7`` | ``W_FIBER_UNIT_HEXAPOD_TOP`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[6]`` | FIBER_UNIT_HEXAPOD_TOP | 
``W_ETMP8`` | ``W_FIBER_UNIT_FIBER_FRAME_TOP`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[7]`` | FIBER_UNIT_FIBER_FRAME_TOP | 
``W_ETMP9`` | ``W_COLLIMATOR_FRAME_BOTTOM`` | ``float`` | ``%-15G`` | ``%.3f`` | ``degC`` | ``enu_sm3`` | ``temps1[8]`` | COLLIMATOR_FRAME_BOTTOM | 
``W_F12VM`` | ``W_FEE_-12V`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[7]`` | -12V at FEE | 
``W_F12VP`` | ``W_FEE_+12V`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[6]`` | +12V at FEE | 
``W_F24VP`` | ``W_FEE_+24V`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[8]`` | +24V at FEE | 
``W_F3V3`` | ``W_FEE_3.3V`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[1]`` | 3.3V at FEE | 
``W_F3V3M`` | ``W_FEE_3.3VM`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[0]`` | 3.3V at FEE | 
``W_F54VP`` | ``W_FEE_+54V`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[9]`` | +54V at FEE | 
``W_F5VM`` | ``W_FEE_-5V`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[3]`` | -5V at FEE | 
``W_F5VMPA`` | ``W_FEE_-5V_PREAMP`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[5]`` | -5V for preamp at FEE | 
``W_F5VP`` | ``W_FEE_+5V`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[2]`` | +5V at FEE | 
``W_F5VPPA`` | ``W_FEE_+5V_PREAMP`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``feeVoltages[4]`` | +5V for preamp at FEE | 
``W_FI0BB`` | ``W_FEE_CCD_0BB`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``integrationVoltages0[3]`` | ccd0 integration BB voltage, measured | 
``W_FI0OD`` | ``W_FEE_CCD0_INTEGRATION_OD`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``integrationVoltages0[2]`` | ccd0 integration OD voltage, measured | 
``W_FI0OG`` | ``W_FEE_CCD0_INTEGRATION_OG`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``integrationVoltages0[0]`` | ccd0 integration OG voltage, measured | 
``W_FI0RD`` | ``W_FEE_CCD0_INTEGRATION_RD`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``integrationVoltages0[1]`` | ccd0 integration RD voltage, measured | 
``W_FI1BB`` | ``W_FEE_CCD_1BB`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``integrationVoltages1[3]`` | ccd1 integration BB voltage, measured | 
``W_FI1OD`` | ``W_FEE_CCD1_INTEGRATION_OD`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``integrationVoltages1[2]`` | ccd1 integration OD voltage, measured | 
``W_FI1OG`` | ``W_FEE_CCD1_INTEGRATION_OG`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``integrationVoltages1[0]`` | ccd1 integration OG voltage, measured | 
``W_FI1RD`` | ``W_FEE_CCD1_INTEGRATION_RD`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``integrationVoltages1[1]`` | ccd1 integration RD voltage, measured | 
``W_FR0BB`` | ``W_FEE_CCD0_READ_BB`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[13]`` | ccd0 readout BB voltage, measured | 
``W_FR0DGF`` | ``W_FEE_CCD0_READ_DG_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[3]`` | ccd0 Drain Gate clock off, measured | 
``W_FR0DGN`` | ``W_FEE_CCD0_READ_DG_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[2]`` | ccd0 Drain Gate clock on, measured | 
``W_FR0OD`` | ``W_FEE_CCD0_READ_OD`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[12]`` | ccd0 readout OD voltage, measured | 
``W_FR0OG`` | ``W_FEE_CCD0_READ_OG`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[10]`` | ccd0 readout OG voltage, measured | 
``W_FR0POF`` | ``W_FEE_CCD0_READ_P_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[1]`` | ccd0 Parallel clock off, measured | 
``W_FR0PON`` | ``W_FEE_CCD0_READ_P_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[0]`` | ccd0 Parallel clock on, measured | 
``W_FR0RD`` | ``W_FEE_CCD0_READ_RD`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[11]`` | ccd0 readout RD voltage, measured | 
``W_FR0RGF`` | ``W_FEE_CCD0_READ_RESET_GATE_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[9]`` | ccd0 Reset Gate clock off, measured | 
``W_FR0RGN`` | ``W_FEE_CCD0_READ_RESET_GATE_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[8]`` | ccd0 Reset Gate clock on, measured | 
``W_FR0SOF`` | ``W_FEE_CCD0_READ_SERIAL_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[5]`` | ccd0 Serial clock off, measured | 
``W_FR0SON`` | ``W_FEE_CCD0_READ_SERIAL_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[4]`` | ccd0 Serial clock on, measured | 
``W_FR0SWF`` | ``W_FEE_CCD0_READ_SUMMING_WELL_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[7]`` | ccd0 Summing Well clock off, measured | 
``W_FR0SWN`` | ``W_FEE_CCD0_READ_SUMMING_WELL_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages0[6]`` | ccd0 Summing Well clock on, measured | 
``W_FR1BB`` | ``W_FEE_CCD1_READ_BB`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[13]`` | ccd1 readout BB voltage, measured | 
``W_FR1DGF`` | ``W_FEE_CCD1_READ_DG_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[3]`` | ccd1 Drain Gate clock off, measured | 
``W_FR1DGN`` | ``W_FEE_CCD1_READ_DG_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[2]`` | ccd1 Drain Gate clock on, measured | 
``W_FR1OD`` | ``W_FEE_CCD1_READ_OD`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[12]`` | ccd1 readout OD voltage, measured | 
``W_FR1OG`` | ``W_FEE_CCD1_READ_OG`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[10]`` | ccd1 readout OG voltage, measured | 
``W_FR1POF`` | ``W_FEE_CCD1_READ_P_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[1]`` | ccd1 Parallel clock off, measured | 
``W_FR1PON`` | ``W_FEE_CCD1_READ_P_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[0]`` | ccd1 Parallel clock on, measured | 
``W_FR1RD`` | ``W_FEE_CCD1_READ_RD`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[11]`` | ccd1 readout RD voltage, measured | 
``W_FR1RGF`` | ``W_FEE_CCD1_READ_RESET_GATE_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[9]`` | ccd1 Reset Gate clock off, measured | 
``W_FR1RGN`` | ``W_FEE_CCD1_READ_RESET_GATE_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[8]`` | ccd1 Reset Gate clock on, measured | 
``W_FR1SOF`` | ``W_FEE_CCD1_READ_SERIAL_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[5]`` | ccd1 Serial clock off, measured | 
``W_FR1SON`` | ``W_FEE_CCD1_READ_SERIAL_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[4]`` | ccd1 Serial clock on, measured | 
``W_FR1SWF`` | ``W_FEE_CCD1_READ_SUMMING_WELL_OFF`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[7]`` | ccd1 Summing Well clock off, measured | 
``W_FR1SWN`` | ``W_FEE_CCD1_READ_SUMMING_WELL_ON`` | ``float`` | ``%-15G`` |  | ``V`` | ``ccd_r3`` | ``readoutVoltages1[6]`` | ccd1 Summing Well clock on, measured | 
``W_G2SERV`` | ``W_GEN2_SERVER_NAME`` | ``str`` |  |  ``%s`` | ``-`` | ``gen2`` | ``gen2server[0]`` | Internal name of Gen2 server used by PFS | 
``W_G2SVIP`` | ``W_GEN2_SERVER_IP`` | ``str`` |  |  ``%s`` | ``-`` | ``gen2`` | ``gen2server[1]`` | IP address of Gen2 server used by PFS | 
``W_M2OFF1`` | ``W_GEN2_M2_XOFFSET`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``mm`` | ``gen2`` | ``pfuOffset[0]`` | M2 X offset | 
``W_M2OFF2`` | ``W_GEN2_M2_YOFFSET`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``mm`` | ``gen2`` | ``pfuOffset[1]`` | M2 Y offset | 
``W_M2OFF3`` | ``W_GEN2_M2_ZOFFSET`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``mm`` | ``gen2`` | ``pfuOffset[2]`` | M2 Z offset | 
``W_RAOFF`` | ``W_RAOFF`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``arcsec`` | ``gen2`` | ``offsets[0]`` | RA offset | 
``W_RVACOR`` | ``W_ACTORCORE_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``version_tron_actorcore[0]`` | tron_actorcore version | 
``W_RVAKEY`` | ``W_ACTORKEYS_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``version_ics_actorkeys[0]`` | ics_actorkeys version | 
``W_RVCCD`` | ``W_CCDACTOR_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``version[0]`` | CCD actor version | 
``W_RVDCB`` | ``W_DCBACTOR_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``dcb`` | ``version[0]`` | DCB actor version | 
``W_RVENU`` | ``W_ENUACTOR_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``enu_sm3`` | ``version[0]`` | ENU actor version | 
``W_RVFEE`` | ``W_FEE_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``version_fee[0]`` | FEE firmware version | 
``W_RVFPGA`` | ``W_FPGA_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``version_fpga[0]`` | FPGA firmware version | 
``W_RVG2LB`` | ``W_GEN2_LIBRARY_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``gen2`` | ``version_gen2[0]`` | Gen2 library version | 
``W_RVGEN2`` | ``W_GEN2ACTOR_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``gen2`` | ``version[0]`` | Gen2 actor version | 
``W_RVIIC`` | ``W_IICACTOR_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``iic`` | ``version[0]`` | IIC actor version | 
``W_RVPFIL`` | ``W_PFILAMPSACTOR_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``pfilamps`` | ``version[0]`` | pfilamps actor version | 
``W_RVSCR`` | ``W_SCRACTOR_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``scr`` | ``version[0]`` | SCR Actor version | 
``W_RVSPS`` | ``W_SPSACTOR_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``sps`` | ``version[0]`` | SPS actor version | 
``W_RVXCU`` | ``W_XCUACTOR_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``xcu_r3`` | ``version[0]`` | XCU actor version | 
``W_RVXFPG`` | ``W_XCU_FPGA_VERSION`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``version_ics_xcu_fpga[0]`` | ics_xcu_fpga version | 
``W_SRADC`` | ``W_CCD_ADC_SERIAL`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``serials[1]`` | ADC serial ID | 
``W_SRCCD0`` | ``W_CCD0_SERIAL`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``serials[3]`` | CCD0 serial ID | 
``W_SRCCD1`` | ``W_CCD1_SERIAL`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``serials[4]`` | CCD1 serial ID | 
``W_SRFCA`` | ``W_ENU_FCA_SERIAL_NUMBER`` | ``str`` |  |  ``%s`` | ``-`` | ``enu_sm3`` | ``serials[0]`` | FCA ID/Number | 
``W_SRFEE`` | ``W_CCD_FEE_SERIAL`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``serials[0]`` | FEE serial ID | 
``W_SRPAMP`` | ``W_CCD_PREAMP_SERIAL`` | ``str`` |  |  ``%s`` | ``-`` | ``ccd_r3`` | ``serials[2]`` | Preamp serial ID | 
``W_TDLGHT`` | ``W_GEN2_DOME_LIGHT_MASK`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``gen2`` | ``domeLights[0]`` | which dome lamps are on | 
``W_TFF1ST`` | ``W_GEN2_RING_LAMP1_STATUS`` | ``int`` | ``%d`` | ``%d`` |  ``-`` | ``gen2`` | ``ringLampsStatus[0]`` | status of ring lamp #1 | 
``W_TFF1VC`` | ``W_GEN2_RING_LAMP1_CMD_V`` | ``float`` | ``%-15G`` | ``%0.1f`` | ``V`` | ``gen2`` | ``ringLampsCmd[0]`` | Command to ring lamp #1 | 
``W_TFF1VV`` | ``W_GEN2_RING_LAMP1_MEAS_V`` | ``float`` | ``%-15G`` | ``%0.1f`` | ``V`` | ``gen2`` | ``ringLamps[0]`` | Measured ring lamp #1 | 
``W_TFF2ST`` | ``W_GEN2_RING_LAMP2_STATUS`` | ``int`` | ``%d`` | ``%d`` |  ``-`` | ``gen2`` | ``ringLampsStatus[1]`` | status of ring lamp #2 | 
``W_TFF2VC`` | ``W_GEN2_RING_LAMP2_CMD_V`` | ``float`` | ``%-15G`` | `%0.1f` | ``V`` | ``gen2`` | ``ringLampsCmd[1]`` | Command to ring lamp #2 | 
``W_TFF2VV`` | ``W_GEN2_RING_LAMP2_MEAS_V`` | ``float`` | ``%-15G`` | `%0.1f` | ``V`` | ``gen2`` | ``ringLamps[1]`` | Measured ring lamp #2 | 
``W_TFF3ST`` | ``W_GEN2_RING_LAMP3_STATUS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``gen2`` | ``ringLampsStatus[2]`` | status of ring lamp #3 | 
``W_TFF3VC`` | ``W_GEN2_RING_LAMP3_CMD_V`` | ``float`` | ``%-15G`` | `%0.1f` | ``V`` | ``gen2`` | ``ringLampsCmd[2]`` | Command to ring lamp #3 | 
``W_TFF3VV`` | ``W_GEN2_RING_LAMP3_MEAS_V`` | ``float`` | ``%-15G`` | `%0.1f` | ``V`` | ``gen2`` | ``ringLamps[2]`` | Measured ring lamp #3 | 
``W_TFF4ST`` | ``W_GEN2_RING_LAMP4_STATUS`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``gen2`` | ``ringLampsStatus[3]`` | status of ring lamp #4 | 
``W_TFF4VC`` | ``W_GEN2_RING_LAMP4_CMD_V`` | ``float`` | ``%-15G`` | ``%0.1f`` | ``V`` | ``gen2`` | ``ringLampsCmd[3]`` | Command to ring lamp #4 | 
``W_TFF4VV`` | ``W_GEN2_RING_LAMP4_MEAS_V`` | ``float`` | ``%-15G`` | ``%0.1f`` | ``V`` | ``gen2`` | ``ringLamps[3]`` | Measured ring lamp #4 | 
``W_TFFPOS`` | ``W_GEN2_FLATFIELD_SCREEN_POSITION`` | ``str`` |  | ``%s`` | ``-`` | ``gen2`` | ``topScreenPos[2]`` | name of known position | 
``W_TFFSFP`` | ``W_GEN2_FLATFIELD_SCREEN_FRONT`` | ``float`` | ``%-15G`` | ``%0.2f`` | ``m`` | ``gen2`` | ``topScreenPos[0]`` | front edge of FF screen | 
``W_TFFSRP`` | ``W_GEN2_FLATFIELD_SCREEN_REAR`` | ``float`` | ``%-15G`` | ``%0.2f`` | ``m`` | ``gen2`` | ``topScreenPos[1]`` | rear edge of FF screen | 
``W_XCL1PW`` | ``W_XCU_COOLER1_POWER`` | ``float`` | ``%-15G`` | ``%g`` | ``W`` | ``xcu_r3`` | ``coolerTemps[3]`` | Cooler1 power | 
``W_XCL1RJ`` | ``W_XCU_COOLER1_REJECT_TEMP`` | ``float`` | ``%-15G`` | ``%g`` | ``degC`` | ``xcu_r3`` | ``coolerTemps[1]`` | Cooler1 reject temperature | 
``W_XCL1ST`` | ``W_XCU_COOLER1_SETPOINT`` | ``float`` | ``%-15G`` | ``%g`` | ``K`` | ``xcu_r3`` | ``coolerTemps[0]`` | Cooler1 setpoint | 
``W_XCL1TP`` | ``W_XCU_COOLER1_TIP_TEMP`` | ``float`` | ``%-15G`` | ``%g`` | ``K`` | ``xcu_r3`` | ``coolerTemps[2]`` | Cooler1 tip temperature | 
``W_XCL2PW`` | ``W_XCU_COOLER2_POWER`` | ``float`` | ``%-15G`` | ``%g`` | ``W`` | ``xcu_r3`` | ``cooler2Temps[3]`` | Cooler2 power | 
``W_XCL2RJ`` | ``W_XCU_COOLER2_REJECT_TEMP`` | ``float`` | ``%-15G`` | ``%g`` | ``degC`` | ``xcu_r3`` | ``cooler2Temps[1]`` | Cooler2 reject temperature | 
``W_XCL2ST`` | ``W_XCU_COOLER2_SETPOINT`` | ``float`` | ``%-15G`` | ``%g`` | ``K`` | ``xcu_r3`` | ``cooler2Temps[0]`` | Cooler2 setpoint | 
``W_XCL2TP`` | ``W_XCU_COOLER2_TIP_TEMP`` | ``float`` | ``%-15G`` | ``%g`` | ``K`` | ``xcu_r3`` | ``cooler2Temps[2]`` | Cooler2 tip temperature | 
``W_XCOOL1`` | ``W_XCU_COOLER1_STATE`` | ``str`` | ``%s`` | ``%s`` | ``-`` | ``xcu_r3`` | ``coolerLoop[0]`` | Cooler1 control loop state | ``{'ON', 'POWER', 'OFF'}``
``W_XCOOL2`` | ``W_XCU_COOLER2_STATE`` | ``str`` | ``%s`` | ``%s`` | ``-`` | ``xcu_r3`` | ``cooler2Loop[0]`` | Cooler2 control loop state | ``{'ON', 'POWER', 'OFF'}``
``W_XGATPS`` | ``W_XCU_GATEVALVE_POSITION`` | ``str`` | ``%s`` | ``%s`` | ``-`` | ``xcu_r3`` | ``gatevalve[1]`` | actual gatevalve position | ``{'Closed', 'Unknown', 'Open', 'Invalid'}``
``W_XGATRQ`` | ``W_XCU_GATEVALVE_REQUESTED_POS`` | ``str`` | ``%s`` | ``%s`` | ``-`` | ``xcu_r3`` | ``gatevalve[2]`` | gatevalve request status | ``{'Invalid', 'Blocked', 'TimedOut', 'Closed', 'Open'}``
``W_XH1ENA`` | ``W_XCU_ASIC_HEATER_ENABLED`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``xcu_r3`` | ``heaters[0]`` | asic heater enabled | 
``W_XH1FRA`` | ``W_XCU_ASIC_HEATER_FRACTION`` | ``float`` | ``%-15G`` | ``%.3f`` | ``-`` | ``xcu_r3`` | ``heaters[2]`` | frac power to asic heater: 0..1 | 
``W_XH2ENA`` | ``W_XCU_CCD_HEATER_ENABLED`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``xcu_r3`` | ``heaters[4]`` | ccd heater enabled | 
``W_XH2FRA`` | ``W_XCU_CCD_HEATER_FRACTION`` | ``float`` | ``%-15G`` | ``%.3f`` | ``-`` | ``xcu_r3`` | ``heaters[6]`` | frac power to ccd heater: 0..1 | 
``W_XHP1EN`` | ``W_XCU_SHIELD_HEATER_ENABLED`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``xcu_r3`` | ``heaters[1]`` | shield heater enabled | 
``W_XHP1FR`` | ``W_XCU_SHIELD_HEATER_FRACTION`` | ``float`` | ``%-15G`` | ``%.3f`` | ``-`` | ``xcu_r3`` | ``heaters[3]`` | Shield heater power: 0 or 1 | 
``W_XHP2EN`` | ``W_XCU_SPREADER_HEATER_ENABLED`` | ``int`` | ``%d`` | ``%d`` | ``-`` | ``xcu_r3`` | ``heaters[5]`` | spreader heater enabled | 
``W_XHP2FR`` | ``W_XCU_SPREADER_HEATER_FRACTION`` | ``float`` | ``%-15G`` | ``%.3f`` | ``-`` | ``xcu_r3`` | ``heaters[7]`` | Spreader heater power: 0 or 1 | 
``W_XIP1EN`` | ``W_XCU_IONPUMP1_ENABLED`` | ``bool`` |  |  | ``-`` | ``xcu_r3`` | ``ionpump1[0]`` | ionpump1 enabled | 
``W_XIP1PR`` | ``W_XCU_IONPUMP1_PRESSURE`` | ``float`` | ``%-15G`` | ``%g`` | ``Torr`` | ``xcu_r3`` | ``ionpump1[4]`` | ionpump1 pressure | 
``W_XIP2EN`` | ``W_XCU_IONPUMP2_ENABLED`` | ``bool`` |  |  | ``-`` | ``xcu_r3`` | ``ionpump2[0]`` | ionpump2 enabled | 
``W_XIP2PR`` | ``W_XCU_IONPUMP2_PRESSURE`` | ``float`` | ``%-15G`` | ``%g`` | ``Torr`` | ``xcu_r3`` | ``ionpump2[4]`` | ionpump2 pressure | 
``W_XM1POS`` | ``W_XCU_FPA_ARM1_POSITION`` | ``float`` | ``%-15G`` | ``%0.2f`` | ``um`` | ``xcu_r3`` | ``ccdMotor1[4]`` | arm 1 vertex offset from home | 
``W_XM1STP`` | ``W_XCU_FPA_MOT1_STEPS`` | ``int`` | ``%d`` | ``%d`` | ``steps`` | ``xcu_r3`` | ``ccdMotor1[3]`` | ccd motor1 steps | 
``W_XM2POS`` | ``W_XCU_FPA_ARM2_POSITION`` | ``float`` | ``%-15G`` | ``%0.2f`` | ``um`` | ``xcu_r3`` | ``ccdMotor2[4]`` | arm 2 vertex offset from home | 
``W_XM2STP`` | ``W_XCU_FPA_MOT2_STEPS`` | ``int`` | ``%d`` | ``%d`` | ``steps`` | ``xcu_r3`` | ``ccdMotor2[3]`` | ccd motor2 steps | 
``W_XM3POS`` | ``W_XCU_FPA_ARM3_POSITION`` | ``float`` | ``%-15G`` | ``%0.2f`` | ``um`` | ``xcu_r3`` | ``ccdMotor3[4]`` | arm 3 vertex offset from home | 
``W_XM3STP`` | ``W_XCU_FPA_MOT3_STEPS`` | ``int`` | ``%d`` | ``%d`` | ``steps`` | ``xcu_r3`` | ``ccdMotor3[3]`` | ccd motor3 steps | 
``W_XPRESS`` | ``W_XCU_PRESSURE`` | ``float`` | ``%-15G`` | ``%g`` | ``Torr`` | ``xcu_r3`` | ``pressure[0]`` | Cryostat gauge pressure | 
``W_XSUP1V`` | ``W_XCU_PCM_POWER_SUPPLY1`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``V`` | ``xcu_r3`` | ``pcmPower1[2]`` | PCM bus 1 input voltage | 
``W_XSUP2V`` | ``W_XCU_PCM_POWER_SUPPLY2`` | ``float`` | ``%-15G`` | ``%0.3f`` | ``V`` | ``xcu_r3`` | ``pcmPower2[2]`` | PCM bus 2 input voltage | 
``W_XTASIC`` | ``W_XCU_TEMP_ASIC`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[8]`` | ASIC temp | 
``W_XTBOSP`` | ``W_XCU_TURBO_SPEED`` | ``int`` | ``%d`` | ``%d`` | ``rpm`` | ``xcu_r3`` | ``turboSpeed[0]`` | turbo pump speed | 
``W_XTDBOX`` | ``W_XCU_TEMP_DETBOX`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``visTemps[0]`` | Detector Box temp | 
``W_XTDET1`` | ``W_XCU_TEMP_DETECTOR_1`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[9]`` | Detector temp #1 | 
``W_XTDET2`` | ``W_XCU_TEMP_DETECTOR_2`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[10]`` | Detector temp #2 | 
``W_XTFBAR`` | ``W_XCU_TEMP_FRONT_BARREL`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[4]`` | Front Barrel ring temp | 
``W_XTMANG`` | ``W_XCU_TEMP_MANGIN`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[0]`` | Mangin mirror temp | 
``W_XTMCL1`` | ``W_XCU_TEMP_MIRRORCELL_1`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[1]`` | Mirror cell temp #1 | 
``W_XTMCL2`` | ``W_XCU_TEMP_MIRRORCELL_2`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[2]`` | Mirror cell temp #2 | 
``W_XTMP1`` | ``W_XCU_TEMP_1`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[0]`` | temp probe #1 | 
``W_XTMP10`` | ``W_XCU_TEMP_10`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[9]`` | temp probe #10 | 
``W_XTMP11`` | ``W_XCU_TEMP_11`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[10]`` | temp probe #11 | 
``W_XTMP12`` | ``W_XCU_TEMP_12`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[11]`` | temp probe #12 | 
``W_XTMP2`` | ``W_XCU_TEMP_2`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[1]`` | temp probe #2 | 
``W_XTMP3`` | ``W_XCU_TEMP_3`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[2]`` | temp probe #3 | 
``W_XTMP4`` | ``W_XCU_TEMP_4`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[3]`` | temp probe #4 | 
``W_XTMP5`` | ``W_XCU_TEMP_5`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[4]`` | temp probe #5 | 
``W_XTMP6`` | ``W_XCU_TEMP_6`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[5]`` | temp probe #6 | 
``W_XTMP7`` | ``W_XCU_TEMP_7`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[6]`` | temp probe #7 | 
``W_XTMP8`` | ``W_XCU_TEMP_8`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[7]`` | temp probe #8 | 
``W_XTMP9`` | ``W_XCU_TEMP_9`` | ``float`` | ``%-15G`` | ``%0.4f`` |  ``K`` | ``xcu_r3`` | ``temps[8]`` | temp probe #9 | 
``W_XTSHD1`` | ``W_XCU_TEMP_RADSHIELD_1`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[6]`` | Radiation shield temp #1 | 
``W_XTSHD2`` | ``W_XCU_TEMP_RADSHIELD_2`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[7]`` | Radiation shield temp #2 | 
``W_XTSICS`` | ``W_XCU_TEMP_SIC_SPREADER`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[3]`` | SiC spreader temp | 
``W_XTSPAN`` | ``W_XCU_TEMP_SPREADER`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``nirTemps[5]`` | Spreader pan temp | 
``W_XTSPID`` | ``W_XCU_TEMP_SPIDER`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``visTemps[2]`` | Spider temp | 
``W_XTSPRD`` | ``W_XCU_TEMP_SPREADER`` | ``float`` | ``%-15G`` | ``%0.4f`` | ``K`` | ``xcu_r3`` | ``visTemps[3]`` | Thermal spreader temp | 