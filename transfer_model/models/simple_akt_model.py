from pathlib import Path
import os, glob
import pandas, numpy
from collections import OrderedDict
import tellurium as te
import site
from sys import platform
import matplotlib.pyplot as plt
import seaborn
import matplotlib

# from data.data_analysis import
from transfer_model import WORKING_DIRECTORY, MODELS_DIRECTORY, SIMULATION_DIRECTORY, \
    EXPERIMENTAL_DATA_FILE, COPASI_FILE, DATA_DIRECTORY, OFFSET_PARAMETER, \
    COPASI_FORMATTED_DATA_DIRECTORY

import site
site.addsitedir('/home/ncw135/Documents/pycotools3')
from pycotools3 import tasks, viz, model

matplotlib.use('Qt5Agg')
seaborn.set_context('talk')

model_string = f"""

function MM(km, Vmax, S)
    Vmax * S / (km + S)
end

function MMWithKcat(km, kcat, S, E)
    kcat * E * S / (km + S)
end

function NonCompetitiveInhibition(km, ki, Vmax, n, I, S)
    Vmax * S / ( (km + S) * (1 + (I / ki)^n ) )
end

function NonCompetitiveInhibitionWithKcat(km, ki, kcat, E, n, I, S)
    kcat * E * S / ( (km + S) * (1 + (I / ki)^n ) )
end

function NonCompetitiveInhibitionWithKcatAndExtraActivator(km, ki, kcat, E1, E2, n, I, S)
    kcat * E1 * E2 * S / ( (km + S) * (1 + (I / ki)^n ) )
end


function MA1(k, S)
    k * S
end

function MA2(k, S1, S2)
    k * S1 * S2
end

function MA1Mod(k, S, M)
    k * S * M
end

function MA2Mod(k, S1, S2, M)
    k * S1 * S2 * M
end

function CompetitiveInhibitionWithKcat(km, ki, kcat, E, I, S)
    kcat * E * S / (km + S + ((km * I )/ ki)  )
end

function CompetitiveInhibition(Vmax, km, ki, I, S)
    Vmax * S / (km + S + ((km * I )/ ki)  )
end

function Hill(km, kcat, L, S, h)
    kcat * L * (S / km)^h  /   1 + (S / km)^h
end

model SimpleAktModel()
    compartment             Cell = 1;
    var IRS1                in Cell;
    var IRS1a               in Cell;
    var IRS1pS636_639       in Cell;
    var Akt                 in Cell;
    var AktpT308            in Cell;
    var TSC2                in Cell;
    var TSC2pT1462          in Cell;
    var PRAS40              in Cell;
    var PRAS40pT246         in Cell;
    var S6K                 in Cell;
    var S6KpT389            in Cell;
    var FourEBP1            in Cell;
    var FourEBP1pT37_46     in Cell;
    var PI3K                in Cell;
    var pPI3K               in Cell;
    var pmTORC1            in Cell;
    var mTORC1cyt          in Cell;
    var mTORC1lys          in Cell;
    const Insulin          in Cell;
    const AA               in Cell;

    // global variables
    Insulin = 1;

    // Offset is added onto total proteins in order to prevent phospho being present in
    //  greater quantity than total
    // offset_amount                  = {OFFSET_PARAMETER}

    // FourEBP1_tot                  := 1.593687 + offset_amount;
    // Akt_tot                       := 0.736138 + offset_amount;
    // IRS1_tot                      := 0.458843 + offset_amount;
    // TSC2_tot                      := 0.816176 + offset_amount;
    // PRAS40_tot                    := 0.954775 + offset_amount;
    // S6K_tot                       := 0.487419 + offset_amount;
    // PI3K_tot                      := 1          + offset_amount;

    // we do not need to fit total proteins
    // IRS1_obs                   := IRS1_tot;
    // Akt_obs                    := Akt_tot;
    // TSC2_obs                   := TSC2_tot;
    // PRAS40_obs                 := PRAS40_tot;
    // S6K_obs                    := S6K_tot ;

    // IRS1pS636_639_obs             := IRS1pS636_639;
    // AktpT308_obs                  := AktpT308;
    // TSC2pT1462_obs                := TSC2pT1462;
    // PRAS40pT246_obs               := PRAS40pT246;
    // S6KpT389_obs                  := S6KpT389;
    // S6KpT229_obs                  := S6KpT229;
    // FourEBP1pT37_46_obs           := FourEBP1pT37_46;

    //initial conditions
    // FourEBP1pT37_46    = 0.644677;
    // AktpT308           = 0.585251;
    // IRS1pS636_639      = 0.458843;
    // PRAS40pT246        = 0.537742;
    // S6KpT229           = 0.241475;
    // S6KpT389           = 0.177316;
    // TSC2pT1462         = 0.654499;
    // pPI3K              = 0.1;

    IRS1            = 10;
    IRS1a           = 0;
    IRS1pS636_639   = 0;
    PI3K            = 10;
    pPI3K           = 0;
    AktpT308        = 0;
    Akt             = 10;
    TSC2pT1462      = 10;
    TSC2            = 0;
    pmTORC1         = 0;
    mTORC1cyt       = 10;
    mTORC1lys       = 0;
    PRAS40          = 10;
    PRAS40pT246     = 0;
    FourEBP1pT37_46 = 0;
    FourEBP1        = 10;
    S6KpT389        = 0;
    S6K             = 10;


    // IRS1               := IRS1_tot       -     IRS1pS636_639             ;
    // Akt                := Akt_tot        -     AktpT308                  ;
    // TSC2               := TSC2_tot       -     TSC2pT1462                ;
    // PRAS40             := PRAS40_tot     -     PRAS40pT246               ;
    // FourEBP1           := FourEBP1_tot   -     FourEBP1pT37_46           ;
    // S6K                := S6K_tot        -     S6KpT389   - S6KpT229     ;
    // PI3K               := PI3K_tot       -     pPI3K                    ;

    // kinetic parameters
    kIRS1Act                =0.1;
    kIRS1Inact              =0.1;
    kIRS1Phos               =0.1;
    kIRS1Dephos             =0.1;
    kPI3KPhos               =0.1;
    kPI3KDephos             =0.1;
    kAktPhos                =0.1;
    kAktDephos              =0.1;
    kTSC2Phos               =0.1;
    kTSC2Dephos             =0.1;
    kmTORC1cytToLys         =0.1;
    kmTORC1LysToCyt         =0.1;
    kmTORC1Phos             =0.1;
    kmTORC1Dephos           =0.1;
    kPras40Phos             =0.1;
    kPras40Dephos           =0.1;
    kFourEBP1Phos           =0.1;
    kFourEBP1Dephos         =0.1;
    kS6KPhos                =0.1;
    kS6KDephos              =0.1;
    kmTORC1cytToLys         =0.1;
    kmTORC1LysToCyt         =0.1;



    // reactions // MMWithKcat(km, kcat, S, E)
    // function CompetitiveInhibitionWithKcat(km, ki, kcat, E, I, S)
    // function MM(km, Vmax, S)
    // function NonCompetitiveInhibitionWithKcat(km, ki, kcat, E, n, I, S)
    // R1In    : => IRS1                               ; Cell * kIRS1In
    R1f     : IRS1 => IRS1a                         ; Cell * kIRS1Act*IRS1*Insulin;
    //R1b     : IRS1a => IRS1                         ; Cell * kIRS1Inact*IRS1a;
    R2f     : IRS1a => IRS1pS636_639                ; Cell * kIRS1Phos*IRS1a*S6KpT389
    R2b     : IRS1pS636_639 => IRS1                 ; Cell * kIRS1Inact*IRS1pS636_639
    //R2b     : IRS1pS636_639 => IRS1                 ; Cell * kIRS1Dephos*IRS1pS636_639
    R3f     : PI3K => pPI3K                         ; Cell * kPI3KPhos*PI3K*IRS1a
    R3b     : pPI3K => PI3K                         ; Cell * kPI3KDephos*pPI3K
    R4f     : Akt => AktpT308                       ; Cell * kAktPhos*Akt*pPI3K
    R4b     : AktpT308 => Akt                       ; Cell * kAktDephos*pPI3K*AktpT308
    R5f     : TSC2 => TSC2pT1462                    ; Cell * kTSC2Phos*TSC2*AktpT308
    R5b     : TSC2pT1462 => TSC2                    ; Cell * kTSC2Dephos*TSC2pT1462
    R6f     : mTORC1cyt => mTORC1lys                ; Cell * kmTORC1cytToLys*mTORC1cyt*AA
    R6b     : mTORC1lys => mTORC1cyt                ; Cell * kmTORC1LysToCyt*mTORC1lys
    R7f     : mTORC1lys => pmTORC1                  ; Cell * kmTORC1Phos*mTORC1lys*TSC2
    R7b     : pmTORC1 => mTORC1lys                  ; Cell * kmTORC1Dephos*pmTORC1
    R8f     : PRAS40 => PRAS40pT246                 ; Cell * kPras40Phos*PRAS40*AktpT308
    R8b     : PRAS40pT246 => PRAS40                 ; Cell * kPras40Dephos*PRAS40pT246
    R9f     : FourEBP1 => FourEBP1pT37_46           ; Cell * kFourEBP1Phos*FourEBP1*pmTORC1
    R9b     : FourEBP1pT37_46 => FourEBP1           ; Cell * kFourEBP1Dephos*FourEBP1pT37_46
    R10f    : S6K => S6KpT389                       ; Cell * kS6KPhos*S6K*pmTORC1
    R10b    : S6KpT389 => S6K                       ; Cell * kS6KDephos*S6KpT389

    //R1f : IRS1 => IRS1pS636_639           ; Cell*   MMWithKcat(_kIRS1Phos_km, _kIRS1Phos_kcat, IRS1, S6KpT389);
    //R1b : IRS1pS636_639 => IRS1           ; Cell*   MMWithKcat(_kIRS1Dephos_km, _kIRS1Dephos_kcat, IRS1pS636_639, Insulin );
    //R2f : PI3K => pPI3K                   ; Cell*   MMWithKcat(_kPI3KPhos_km, _kPI3KPhos_kcat, PI3K, IRS1);
    //R2b : pPI3K => PI3K                   ; Cell*   _kPI3KDephos*pPI3K;
    //R3f : S6K => S6KpT229                 ; Cell*   MMWithKcat(_kS6KPhosS229_km, _kS6KPhosS229_kcat, S6K, pPI3K);
    //R3b : S6KpT229 => S6K                 ; Cell*   kS6KDephosS229*S6KpT229;
    //R4f : Akt => AktpT308                 ; Cell*   MMWithKcat(_kAktPhos_km, _kAktPhos_kcat, Akt, pPI3K);
    //R4b : AktpT308 => Akt                 ; Cell*   _kAktDephos*AktpT308;
    //R5f : TSC2 => TSC2pT1462              ; Cell*   MMWithKcat(_kTSC2Phos_km, _kTSC2Phos_kcat, TSC2, AktpT308);
    //R5b : TSC2pT1462 => TSC2              ; Cell*   _kTSC2Dephos*TSC2pT1462;
    //R6f : PRAS40 => PRAS40pT246           ; Cell*   MMWithKcat(_kPras40PhosByAkt_km, _kPras40PhosByAkt_kcat, PRAS40, AktpT308);
    //R6b : PRAS40pT246 => PRAS40           ; Cell*   kPras40Dephos*PRAS40pT246;
    //R7f : FourEBP1 => FourEBP1pT37_46     ; Cell*   MMWithKcat(_kFourEBP1Phos_km, _kFourEBP1Phos_kcat, FourEBP1, TSC2pT1462);
    //R7b : FourEBP1pT37_46 => FourEBP1     ; Cell*   kFourEBP1Dephos*FourEBP1pT37_46;
    //R8f : S6K => S6KpT389                 ; Cell*   MMWithKcat(_kS6KT389Phos_km, _kS6KT389Phos_kcat, S6K, TSC2pT1462);
    //R8b : S6KpT389 => S6K                 ; Cell*   _kS6KT389Dephos*S6KpT389;
end

"""









if __name__ == '__main__':

    OPEN_WITH_COPASI = False

    CONFIGURE_PARAMETER_ESTIMATION = True


    mod = model.loada(model_string, copasi_file=COPASI_FILE)
    mod = tasks.TimeCourse(mod, start=0, end=150).model

    if OPEN_WITH_COPASI:
        mod.open()

    if CONFIGURE_PARAMETER_ESTIMATION:
        params = ['IRS1', 'Akt', 'PRAS40', 'TSC2', 'FourEBP1', 'S6K']
        exp_files = glob.glob(os.path.join(COPASI_FORMATTED_DATA_DIRECTORY, '*.csv'))
        with tasks.ParameterEstimation.Context(mod, exp_files, parameters='g', context='s') as context:
            context.set('run_mode', False)
            context.set('separator', ',')
            config = context.get_config()

        pe = tasks.ParameterEstimation(config)
        mod = pe.models['simple_akt_model'].model
        mod.open()







