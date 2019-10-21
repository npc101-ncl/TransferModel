<COPASI xmlns="http://www.copasi.org/static/schema" versionMajor="4" versionMinor="25" versionDevel="207" copasiSourcesModified="0">
  <ListOfFunctions>
    <Function key="Function_13" name="Mass action (irreversible)" type="MassAction" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:CopasiMT="http://www.copasi.org/RDF/MiriamTerms#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_13">
            <CopasiMT:is rdf:resource="urn:miriam:obo.sbo:SBO:0000163"/>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Comment>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <b>Mass action rate law for irreversible reactions</b>
          <p>
Reaction scheme where the products are created from the reactants and the change of a product quantity is proportional to the product of reactant activities. The reaction scheme does not include any reverse process that creates the reactants from the products. The change of a product quantity is proportional to the quantity of one reactant.
</p>
        </body>
      </Comment>
      <Expression>
        k1*PRODUCT&lt;substrate_i&gt;
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_80" name="k1" order="0" role="constant"/>
        <ParameterDescription key="FunctionParameter_81" name="substrate" order="1" role="substrate"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_51" name="Function for R1f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_51">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kIRS1Act*IRS1*Insulin
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_319" name="IRS1" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_320" name="Insulin" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_321" name="kIRS1Act" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_52" name="Function for R2f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_52">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kIRS1Phos*IRS1a*S6KpT389
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_325" name="IRS1a" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_326" name="S6KpT389" order="1" role="modifier"/>
        <ParameterDescription key="FunctionParameter_327" name="kIRS1Phos" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_53" name="Function for R3f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_53">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kPI3KPhos*PI3K*IRS1a
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_333" name="IRS1a" order="0" role="modifier"/>
        <ParameterDescription key="FunctionParameter_334" name="PI3K" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_335" name="kPI3KPhos" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_54" name="Function for R4f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_54">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kAktPhos*Akt*pPI3K
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_341" name="Akt" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_342" name="kAktPhos" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_343" name="pPI3K" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_55" name="Function for R4b" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_55">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kAktDephos*pPI3K*AktpT308
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_347" name="AktpT308" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_348" name="kAktDephos" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_349" name="pPI3K" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_56" name="Function for R5f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_56">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kTSC2Phos*TSC2*AktpT308
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_353" name="AktpT308" order="0" role="modifier"/>
        <ParameterDescription key="FunctionParameter_354" name="TSC2" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_355" name="kTSC2Phos" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_57" name="Function for R6f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_57">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kmTORC1cytToLys*mTORC1cyt*AA
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_361" name="AA" order="0" role="constant"/>
        <ParameterDescription key="FunctionParameter_362" name="kmTORC1cytToLys" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_363" name="mTORC1cyt" order="2" role="substrate"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_58" name="Function for R7f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_58">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kmTORC1Phos*mTORC1lys*TSC2
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_369" name="TSC2" order="0" role="modifier"/>
        <ParameterDescription key="FunctionParameter_370" name="kmTORC1Phos" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_371" name="mTORC1lys" order="2" role="substrate"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_59" name="Function for R8f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_59">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kPras40Phos*PRAS40*AktpT308
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_377" name="AktpT308" order="0" role="modifier"/>
        <ParameterDescription key="FunctionParameter_378" name="PRAS40" order="1" role="substrate"/>
        <ParameterDescription key="FunctionParameter_379" name="kPras40Phos" order="2" role="constant"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_60" name="Function for R9f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_60">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kFourEBP1Phos*FourEBP1*pmTORC1
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_385" name="FourEBP1" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_386" name="kFourEBP1Phos" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_387" name="pmTORC1" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
    <Function key="Function_61" name="Function for R10f" type="UserDefined" reversible="false">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Function_61">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        kS6KPhos*S6K*pmTORC1
      </Expression>
      <ListOfParameterDescriptions>
        <ParameterDescription key="FunctionParameter_393" name="S6K" order="0" role="substrate"/>
        <ParameterDescription key="FunctionParameter_394" name="kS6KPhos" order="1" role="constant"/>
        <ParameterDescription key="FunctionParameter_395" name="pmTORC1" order="2" role="modifier"/>
      </ListOfParameterDescriptions>
    </Function>
  </ListOfFunctions>
  <Model key="Model_1" name="SimpleAktModel" simulationType="time" timeUnit="s" volumeUnit="l" areaUnit="m&#178;" lengthUnit="m" quantityUnit="mol" type="deterministic" avogadroConstant="6.0221417899999999e+23">
    <MiriamAnnotation>
      <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="#Model_1">
          <dcterms:created>
            <rdf:Description>
              <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
            </rdf:Description>
          </dcterms:created>
        </rdf:Description>
      </rdf:RDF>
    </MiriamAnnotation>
    <ListOfCompartments>
      <Compartment key="Compartment_0" name="Cell" simulationType="fixed" dimensionality="3" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Compartment_0">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Compartment>
    </ListOfCompartments>
    <ListOfMetabolites>
      <Metabolite key="Metabolite_0" name="IRS1" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+24">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_0">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_1" name="IRS1a" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_1">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_2" name="IRS1pS636_639" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_2">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_3" name="Akt" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+24">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_3">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_4" name="AktpT308" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_4">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_5" name="TSC2" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_5">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_6" name="TSC2pT1462" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+24">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_6">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_7" name="PRAS40" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+24">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_7">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_8" name="PRAS40pT246" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_8">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_9" name="S6K" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+24">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_9">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_10" name="S6KpT389" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_10">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_11" name="FourEBP1" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+24">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_11">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_12" name="FourEBP1pT37_46" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_12">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_13" name="PI3K" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+24">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_13">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_14" name="pPI3K" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_14">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_15" name="pmTORC1" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_15">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_16" name="mTORC1cyt" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="6.02214179e+24">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_16">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
      <Metabolite key="Metabolite_17" name="mTORC1lys" simulationType="reactions" compartment="Compartment_0" addNoise="false" particle_numbers="0.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Metabolite_17">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </Metabolite>
    </ListOfMetabolites>
    <ListOfModelValues>
      <ModelValue key="ModelValue_0" name="Insulin" simulationType="fixed" addNoise="false" initial_value="1.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_0">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_1" name="AA" simulationType="fixed" addNoise="false" initial_value="1.0">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_1">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_2" name="kIRS1Act" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_2">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_3" name="kIRS1Inact" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_3">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_4" name="kIRS1Phos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_4">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_5" name="kPI3KPhos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_5">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_6" name="kPI3KDephos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_6">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_7" name="kAktPhos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_7">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_8" name="kAktDephos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_8">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_9" name="kTSC2Phos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_9">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_10" name="kTSC2Dephos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_10">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_11" name="kmTORC1cytToLys" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_11">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_12" name="kmTORC1LysToCyt" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_12">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_13" name="kmTORC1Phos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_13">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_14" name="kmTORC1Dephos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_14">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_15" name="kPras40Phos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_15">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_16" name="kPras40Dephos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_16">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_17" name="kFourEBP1Phos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_17">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_18" name="kFourEBP1Dephos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_18">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_19" name="kS6KPhos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_19">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
      <ModelValue key="ModelValue_20" name="kS6KDephos" simulationType="fixed" addNoise="false" initial_value="0.5">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelValue_20">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
      </ModelValue>
    </ListOfModelValues>
    <ListOfReactions>
      <Reaction key="Reaction_0" name="R1f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_0">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_0" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5013" name="Insulin" value="1"/>
          <Constant key="Parameter_5012" name="kIRS1Act" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_51" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_319">
              <SourceParameter reference="Metabolite_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_320">
              <SourceParameter reference="ModelValue_0"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_321">
              <SourceParameter reference="ModelValue_2"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_1" name="R2f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_1">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_2" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_10" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_5011" name="kIRS1Phos" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_52" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_325">
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_326">
              <SourceParameter reference="Metabolite_10"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_327">
              <SourceParameter reference="ModelValue_4"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_2" name="R2b" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_2">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_2" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_0" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5010" name="k1" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_2"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_3" name="R3f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_3">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_13" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_14" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_1" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_5009" name="kPI3KPhos" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_53" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_333">
              <SourceParameter reference="Metabolite_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_334">
              <SourceParameter reference="Metabolite_13"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_335">
              <SourceParameter reference="ModelValue_5"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_4" name="R3b" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_4">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_14" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_13" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5008" name="k1" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_6"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_14"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_5" name="R4f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_5">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_4" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_14" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_5007" name="kAktPhos" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_54" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_341">
              <SourceParameter reference="Metabolite_3"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_342">
              <SourceParameter reference="ModelValue_7"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_343">
              <SourceParameter reference="Metabolite_14"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_6" name="R4b" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_6">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_4" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_3" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_14" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_5006" name="kAktDephos" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_55" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_347">
              <SourceParameter reference="Metabolite_4"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_348">
              <SourceParameter reference="ModelValue_8"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_349">
              <SourceParameter reference="Metabolite_14"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_7" name="R5f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_7">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_6" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_4" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_5005" name="kTSC2Phos" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_56" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_353">
              <SourceParameter reference="Metabolite_4"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_354">
              <SourceParameter reference="Metabolite_5"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_355">
              <SourceParameter reference="ModelValue_9"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_8" name="R5b" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_8">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_6" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5004" name="k1" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_10"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_6"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_9" name="R6f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_9">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_16" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_17" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5003" name="AA" value="1"/>
          <Constant key="Parameter_5002" name="kmTORC1cytToLys" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_57" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_361">
              <SourceParameter reference="ModelValue_1"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_362">
              <SourceParameter reference="ModelValue_11"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_363">
              <SourceParameter reference="Metabolite_16"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_10" name="R6b" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_10">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_17" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_16" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_5001" name="k1" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_12"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_17"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_11" name="R7f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_11">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_17" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_15" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_5" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_5000" name="kmTORC1Phos" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_58" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_369">
              <SourceParameter reference="Metabolite_5"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_370">
              <SourceParameter reference="ModelValue_13"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_371">
              <SourceParameter reference="Metabolite_17"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_12" name="R7b" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_12">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_15" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_17" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4999" name="k1" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_14"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_15"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_13" name="R8f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_13">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_8" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_4" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_4998" name="kPras40Phos" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_59" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_377">
              <SourceParameter reference="Metabolite_4"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_378">
              <SourceParameter reference="Metabolite_7"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_379">
              <SourceParameter reference="ModelValue_15"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_14" name="R8b" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_14">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_8" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_7" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4997" name="k1" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_16"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_8"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_15" name="R9f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_15">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_15" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_4996" name="kFourEBP1Phos" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_60" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_385">
              <SourceParameter reference="Metabolite_11"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_386">
              <SourceParameter reference="ModelValue_17"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_387">
              <SourceParameter reference="Metabolite_15"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_16" name="R9b" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_16">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_12" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_11" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4995" name="k1" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_18"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_12"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_17" name="R10f" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_17">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_9" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_10" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfModifiers>
          <Modifier metabolite="Metabolite_15" stoichiometry="1"/>
        </ListOfModifiers>
        <ListOfConstants>
          <Constant key="Parameter_4994" name="kS6KPhos" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_61" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_393">
              <SourceParameter reference="Metabolite_9"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_394">
              <SourceParameter reference="ModelValue_19"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_395">
              <SourceParameter reference="Metabolite_15"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
      <Reaction key="Reaction_18" name="R10b" reversible="false" fast="false" addNoise="false">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#Reaction_18">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ListOfSubstrates>
          <Substrate metabolite="Metabolite_10" stoichiometry="1"/>
        </ListOfSubstrates>
        <ListOfProducts>
          <Product metabolite="Metabolite_9" stoichiometry="1"/>
        </ListOfProducts>
        <ListOfConstants>
          <Constant key="Parameter_4993" name="k1" value="0.5"/>
        </ListOfConstants>
        <KineticLaw function="Function_13" unitType="Default" scalingCompartment="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]">
          <ListOfCallParameters>
            <CallParameter functionParameter="FunctionParameter_80">
              <SourceParameter reference="ModelValue_20"/>
            </CallParameter>
            <CallParameter functionParameter="FunctionParameter_81">
              <SourceParameter reference="Metabolite_10"/>
            </CallParameter>
          </ListOfCallParameters>
        </KineticLaw>
      </Reaction>
    </ListOfReactions>
    <ListOfModelParameterSets activeSet="ModelParameterSet_1">
      <ModelParameterSet key="ModelParameterSet_1" name="Initial State">
        <MiriamAnnotation>
          <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <rdf:Description rdf:about="#ModelParameterSet_1">
              <dcterms:created>
                <rdf:Description>
                  <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
                </rdf:Description>
              </dcterms:created>
            </rdf:Description>
          </rdf:RDF>
        </MiriamAnnotation>
        <ModelParameterGroup cn="String=Initial Time" type="Group">
          <ModelParameter cn="CN=Root,Model=SimpleAktModel" value="0" type="Model" simulationType="time"/>
        </ModelParameterGroup>
        <ModelParameterGroup cn="String=Initial Compartment Sizes" type="Group">
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell]" value="1" type="Compartment" simulationType="fixed"/>
        </ModelParameterGroup>
        <ModelParameterGroup cn="String=Initial Species Values" type="Group">
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1]" value="6.0221417899999996e+24" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1a]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1pS636_639]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[Akt]" value="6.0221417899999996e+24" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[AktpT308]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2pT1462]" value="6.0221417899999996e+24" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40]" value="6.0221417899999996e+24" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40pT246]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6K]" value="6.0221417899999996e+24" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6KpT389]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1]" value="6.0221417899999996e+24" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1pT37_46]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PI3K]" value="6.0221417899999996e+24" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[pPI3K]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[pmTORC1]" value="0" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[mTORC1cyt]" value="6.0221417899999996e+24" type="Species" simulationType="reactions"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[mTORC1lys]" value="0" type="Species" simulationType="reactions"/>
        </ModelParameterGroup>
        <ModelParameterGroup cn="String=Initial Global Quantities" type="Group">
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[Insulin]" value="1" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[AA]" value="1" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kIRS1Act]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kIRS1Inact]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kIRS1Phos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kPI3KPhos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kPI3KDephos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kAktPhos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kAktDephos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kTSC2Phos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kTSC2Dephos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1cytToLys]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1LysToCyt]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1Phos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1Dephos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kPras40Phos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kPras40Dephos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kFourEBP1Phos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kFourEBP1Dephos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kS6KPhos]" value="0.5" type="ModelValue" simulationType="fixed"/>
          <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Values[kS6KDephos]" value="0.5" type="ModelValue" simulationType="fixed"/>
        </ModelParameterGroup>
        <ModelParameterGroup cn="String=Kinetic Parameters" type="Group">
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R1f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R1f],ParameterGroup=Parameters,Parameter=Insulin" value="1" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[Insulin],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R1f],ParameterGroup=Parameters,Parameter=kIRS1Act" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kIRS1Act],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R2f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R2f],ParameterGroup=Parameters,Parameter=kIRS1Phos" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kIRS1Phos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R2b]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R2b],ParameterGroup=Parameters,Parameter=k1" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kIRS1Inact],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R3f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R3f],ParameterGroup=Parameters,Parameter=kPI3KPhos" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kPI3KPhos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R3b]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R3b],ParameterGroup=Parameters,Parameter=k1" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kPI3KDephos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R4f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R4f],ParameterGroup=Parameters,Parameter=kAktPhos" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kAktPhos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R4b]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R4b],ParameterGroup=Parameters,Parameter=kAktDephos" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kAktDephos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R5f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R5f],ParameterGroup=Parameters,Parameter=kTSC2Phos" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kTSC2Phos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R5b]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R5b],ParameterGroup=Parameters,Parameter=k1" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kTSC2Dephos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R6f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R6f],ParameterGroup=Parameters,Parameter=AA" value="1" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[AA],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R6f],ParameterGroup=Parameters,Parameter=kmTORC1cytToLys" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1cytToLys],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R6b]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R6b],ParameterGroup=Parameters,Parameter=k1" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1LysToCyt],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R7f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R7f],ParameterGroup=Parameters,Parameter=kmTORC1Phos" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1Phos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R7b]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R7b],ParameterGroup=Parameters,Parameter=k1" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1Dephos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R8f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R8f],ParameterGroup=Parameters,Parameter=kPras40Phos" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kPras40Phos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R8b]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R8b],ParameterGroup=Parameters,Parameter=k1" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kPras40Dephos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R9f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R9f],ParameterGroup=Parameters,Parameter=kFourEBP1Phos" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kFourEBP1Phos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R9b]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R9b],ParameterGroup=Parameters,Parameter=k1" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kFourEBP1Dephos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R10f]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R10f],ParameterGroup=Parameters,Parameter=kS6KPhos" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kS6KPhos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
          <ModelParameterGroup cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R10b]" type="Reaction">
            <ModelParameter cn="CN=Root,Model=SimpleAktModel,Vector=Reactions[R10b],ParameterGroup=Parameters,Parameter=k1" value="0.5" type="ReactionParameter" simulationType="assignment">
              <InitialExpression>
                &lt;CN=Root,Model=SimpleAktModel,Vector=Values[kS6KDephos],Reference=InitialValue&gt;
              </InitialExpression>
            </ModelParameter>
          </ModelParameterGroup>
        </ModelParameterGroup>
      </ModelParameterSet>
    </ListOfModelParameterSets>
    <StateTemplate>
      <StateTemplateVariable objectReference="Model_1"/>
      <StateTemplateVariable objectReference="Metabolite_17"/>
      <StateTemplateVariable objectReference="Metabolite_1"/>
      <StateTemplateVariable objectReference="Metabolite_3"/>
      <StateTemplateVariable objectReference="Metabolite_5"/>
      <StateTemplateVariable objectReference="Metabolite_7"/>
      <StateTemplateVariable objectReference="Metabolite_9"/>
      <StateTemplateVariable objectReference="Metabolite_11"/>
      <StateTemplateVariable objectReference="Metabolite_13"/>
      <StateTemplateVariable objectReference="Metabolite_2"/>
      <StateTemplateVariable objectReference="Metabolite_15"/>
      <StateTemplateVariable objectReference="Metabolite_0"/>
      <StateTemplateVariable objectReference="Metabolite_12"/>
      <StateTemplateVariable objectReference="Metabolite_10"/>
      <StateTemplateVariable objectReference="Metabolite_6"/>
      <StateTemplateVariable objectReference="Metabolite_16"/>
      <StateTemplateVariable objectReference="Metabolite_4"/>
      <StateTemplateVariable objectReference="Metabolite_8"/>
      <StateTemplateVariable objectReference="Metabolite_14"/>
      <StateTemplateVariable objectReference="Compartment_0"/>
      <StateTemplateVariable objectReference="ModelValue_0"/>
      <StateTemplateVariable objectReference="ModelValue_1"/>
      <StateTemplateVariable objectReference="ModelValue_2"/>
      <StateTemplateVariable objectReference="ModelValue_3"/>
      <StateTemplateVariable objectReference="ModelValue_4"/>
      <StateTemplateVariable objectReference="ModelValue_5"/>
      <StateTemplateVariable objectReference="ModelValue_6"/>
      <StateTemplateVariable objectReference="ModelValue_7"/>
      <StateTemplateVariable objectReference="ModelValue_8"/>
      <StateTemplateVariable objectReference="ModelValue_9"/>
      <StateTemplateVariable objectReference="ModelValue_10"/>
      <StateTemplateVariable objectReference="ModelValue_11"/>
      <StateTemplateVariable objectReference="ModelValue_12"/>
      <StateTemplateVariable objectReference="ModelValue_13"/>
      <StateTemplateVariable objectReference="ModelValue_14"/>
      <StateTemplateVariable objectReference="ModelValue_15"/>
      <StateTemplateVariable objectReference="ModelValue_16"/>
      <StateTemplateVariable objectReference="ModelValue_17"/>
      <StateTemplateVariable objectReference="ModelValue_18"/>
      <StateTemplateVariable objectReference="ModelValue_19"/>
      <StateTemplateVariable objectReference="ModelValue_20"/>
    </StateTemplate>
    <InitialState type="initialState">
      0 0 0 6.0221417899999996e+24 0 6.0221417899999996e+24 6.0221417899999996e+24 6.0221417899999996e+24 6.0221417899999996e+24 0 0 6.0221417899999996e+24 0 0 6.0221417899999996e+24 6.0221417899999996e+24 0 0 0 1 1 1 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 
    </InitialState>
  </Model>
  <ListOfTasks>
    <Task key="Task_14" name="Steady-State" type="steadyState" scheduled="false" updateModel="false">
      <Report reference="Report_10" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="JacobianRequested" type="bool" value="1"/>
        <Parameter name="StabilityAnalysisRequested" type="bool" value="1"/>
      </Problem>
      <Method name="Enhanced Newton" type="EnhancedNewton">
        <Parameter name="Resolution" type="unsignedFloat" value="1.0000000000000001e-09"/>
        <Parameter name="Derivation Factor" type="unsignedFloat" value="0.001"/>
        <Parameter name="Use Newton" type="bool" value="1"/>
        <Parameter name="Use Integration" type="bool" value="1"/>
        <Parameter name="Use Back Integration" type="bool" value="0"/>
        <Parameter name="Accept Negative Concentrations" type="bool" value="0"/>
        <Parameter name="Iteration Limit" type="unsignedInteger" value="50"/>
        <Parameter name="Maximum duration for forward integration" type="unsignedFloat" value="1000000000"/>
        <Parameter name="Maximum duration for backward integration" type="unsignedFloat" value="1000000"/>
      </Method>
    </Task>
    <Task key="Task_100" name="Time-Course" scheduled="false" type="timeCourse" update_model="false">
      <Report append="0" confirmOverwrite="0" reference="Report_30" target="/home/ncw135/Documents/MesiSTRAT2/TransferModel/transfer_model/models/TimeCourseData.txt"/>
      <Problem>
        <Parameter name="AutomaticStepSize" type="bool" value="0"/>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="150"/>
        <Parameter name="TimeSeriesRequested" type="float" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
        <Parameter name="Output Event" type="bool" value="0"/>
        <Parameter name="Start in Steady State" type="bool" value="0"/>
      </Problem>
      <Method name="Deterministic (LSODA)" type="Deterministic(LSODA)">
        <Parameter name="Integrate Reduced Model" type="bool" value="0"/>
        <Parameter name="Relative Tolerance" type="unsignedFloat" value="1e-06"/>
        <Parameter name="Absolute Tolerance" type="unsignedFloat" value="1e-12"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="10000"/>
        <Parameter name="Max Internal Step Size" type="unsignedFloat" value="0"/>
      </Method>
    </Task>
    <Task key="Task_16" name="Scan" type="scan" scheduled="true" updateModel="0">
      <Report append="0" confirmOverwrite="0" reference="Report_34" target="/home/ncw135/Documents/MesiSTRAT2/TransferModel/transfer_model/models/Problem1/Fit1/simple_akt_model/ParameterEstimationData/PEData0.txt"/>
      <Problem>
        <Parameter name="Subtask" type="unsignedInteger" value="5"/>
        <ParameterGroup name="ScanItems">
        <ParameterGroup name="ScanItem"><Parameter name="Number of steps" type="unsignedInteger" value="1"/><Parameter name="Type" type="unsignedInteger" value="0"/><Parameter name="Object" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1],Reference=InitialConcentration"/></ParameterGroup></ParameterGroup>
        <Parameter name="Output in subtask" type="bool" value="0"/>
        <Parameter name="Adjust initial conditions" type="bool" value="0"/>
      </Problem>
      <Method name="Scan Framework" type="ScanFramework">
      </Method>
    </Task>
    <Task key="Task_17" name="Elementary Flux Modes" type="fluxMode" scheduled="false" updateModel="false">
      <Report reference="Report_11" target="" append="1" confirmOverwrite="1"/>
      <Problem>
      </Problem>
      <Method name="EFM Algorithm" type="EFMAlgorithm">
      </Method>
    </Task>
    <Task key="Task_18" name="Optimization" type="optimization" scheduled="false" updateModel="false">
      <Report reference="Report_12" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="Subtask" type="cn" value="CN=Root,Vector=TaskList[Steady-State]"/>
        <ParameterText name="ObjectiveExpression" type="expression">
          
        </ParameterText>
        <Parameter name="Maximize" type="bool" value="0"/>
        <Parameter name="Randomize Start Values" type="bool" value="0"/>
        <Parameter name="Calculate Statistics" type="bool" value="1"/>
        <ParameterGroup name="OptimizationItemList">
        </ParameterGroup>
        <ParameterGroup name="OptimizationConstraintList">
        </ParameterGroup>
      </Problem>
      <Method name="Random Search" type="RandomSearch">
        <Parameter name="Log Verbosity" type="unsignedInteger" value="0"/>
        <Parameter name="Number of Iterations" type="unsignedInteger" value="100000"/>
        <Parameter name="Random Number Generator" type="unsignedInteger" value="1"/>
        <Parameter name="Seed" type="unsignedInteger" value="0"/>
      </Method>
    </Task>
    <Task key="Task_19" name="Parameter Estimation" type="parameterFitting" scheduled="false" updateModel="0">
      <Report reference="Report_32" target="PEData.txt" append="False" confirmOverwrite="False"/>
      <Problem>
        <Parameter name="Maximize" type="bool" value="0"/>
        <Parameter name="Randomize Start Values" type="bool" value="0"/>
        <Parameter name="Calculate Statistics" type="bool" value="0"/>
        <ParameterGroup name="OptimizationItemList">
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[Akt],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[AktpT308],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1pT37_46],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1a],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1pS636_639],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PI3K],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40pT246],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6K],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6KpT389],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2pT1462],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[mTORC1cyt],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[mTORC1lys],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[pPI3K],Reference=InitialConcentration"/>
          </ParameterGroup>
          <ParameterGroup name="FitItem">
            <ParameterGroup name="Affected Experiments"/>
            <ParameterGroup name="Affected Cross Validation Experiments"/>
            <Parameter name="LowerBound" type="cn" value="0.1"/>
            <Parameter name="UpperBound" type="cn" value="10"/>
            <Parameter name="StartValue" type="float" value="0.1"/>
            <Parameter name="ObjectCN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[pmTORC1],Reference=InitialConcentration"/>
          </ParameterGroup>
        </ParameterGroup>
        <ParameterGroup name="OptimizationConstraintList">
        </ParameterGroup>
        <Parameter name="Steady-State" type="cn" value="CN=Root,Vector=TaskList[Steady-State]"/>
        <Parameter name="Time-Course" type="cn" value="CN=Root,Vector=TaskList[Time-Course]"/>
        <Parameter name="Create Parameter Sets" type="bool" value="0"/>
        <ParameterGroup name="Experiment Set">
          <ParameterGroup name="not_interpolated_MCF7">
            <Parameter name="Key" type="key" value="Experiment_not_interpolated_MCF7"/>
            <Parameter name="File Name" type="file" value="/home/ncw135/Documents/MesiSTRAT2/TransferModel/transfer_model/data/CopasiFormattedData/T47DSheet/not_interpolated_MCF7.csv"/>
            <Parameter name="Data is Row Oriented" type="bool" value="1"/>
            <Parameter name="First Row" type="unsignedInteger" value="1"/>
            <Parameter name="Last Row" type="unsignedInteger" value="7"/>
            <Parameter name="Experiment Type" type="unsignedInteger" value="1"/>
            <Parameter name="Normalize Weights per Experiment" type="bool" value="1"/>
            <Parameter name="Separator" type="string" value=","/>
            <Parameter name="Weight Method" type="unsignedInteger" value="1"/>
            <Parameter name="Row containing Names" type="unsignedInteger" value="1"/>
            <Parameter name="Number of Columns" type="unsignedInteger" value="31"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0">
                <Parameter name="Role" type="unsignedInteger" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="1"/>
              <ParameterGroup name="2">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[AktpT308],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3"/>
              <ParameterGroup name="4"/>
              <ParameterGroup name="5"/>
              <ParameterGroup name="6">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1pT37_46],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="7"/>
              <ParameterGroup name="8">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1pS636_639],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="9"/>
              <ParameterGroup name="10">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40pT246],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="11"/>
              <ParameterGroup name="12">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6KpT389],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="13">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2pT1462],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="14"/>
              <ParameterGroup name="15"/>
              <ParameterGroup name="16">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[AktpT308],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="17"/>
              <ParameterGroup name="18"/>
              <ParameterGroup name="19"/>
              <ParameterGroup name="20">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1pT37_46],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="21"/>
              <ParameterGroup name="22">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1pS636_639],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="23"/>
              <ParameterGroup name="24">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40pT246],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="25"/>
              <ParameterGroup name="26">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6KpT389],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="27">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2pT1462],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="28"/>
              <ParameterGroup name="29">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Values[Insulin],Reference=InitialValue"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="30">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Values[AA],Reference=InitialValue"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
          <ParameterGroup name="not_interpolated_T47D">
            <Parameter name="Key" type="key" value="Experiment_not_interpolated_T47D"/>
            <Parameter name="File Name" type="file" value="/home/ncw135/Documents/MesiSTRAT2/TransferModel/transfer_model/data/CopasiFormattedData/T47DSheet/not_interpolated_T47D.csv"/>
            <Parameter name="Data is Row Oriented" type="bool" value="1"/>
            <Parameter name="First Row" type="unsignedInteger" value="1"/>
            <Parameter name="Last Row" type="unsignedInteger" value="7"/>
            <Parameter name="Experiment Type" type="unsignedInteger" value="1"/>
            <Parameter name="Normalize Weights per Experiment" type="bool" value="1"/>
            <Parameter name="Separator" type="string" value=","/>
            <Parameter name="Weight Method" type="unsignedInteger" value="1"/>
            <Parameter name="Row containing Names" type="unsignedInteger" value="1"/>
            <Parameter name="Number of Columns" type="unsignedInteger" value="31"/>
            <ParameterGroup name="Object Map">
              <ParameterGroup name="0">
                <Parameter name="Role" type="unsignedInteger" value="3"/>
              </ParameterGroup>
              <ParameterGroup name="1"/>
              <ParameterGroup name="2">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[AktpT308],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="3"/>
              <ParameterGroup name="4"/>
              <ParameterGroup name="5"/>
              <ParameterGroup name="6">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1pT37_46],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="7"/>
              <ParameterGroup name="8">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1pS636_639],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="9"/>
              <ParameterGroup name="10">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40pT246],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="11"/>
              <ParameterGroup name="12">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6KpT389],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="13">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2pT1462],Reference=Concentration"/>
                <Parameter name="Role" type="unsignedInteger" value="2"/>
              </ParameterGroup>
              <ParameterGroup name="14"/>
              <ParameterGroup name="15"/>
              <ParameterGroup name="16">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[AktpT308],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="17"/>
              <ParameterGroup name="18"/>
              <ParameterGroup name="19"/>
              <ParameterGroup name="20">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1pT37_46],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="21"/>
              <ParameterGroup name="22">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1pS636_639],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="23"/>
              <ParameterGroup name="24">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40pT246],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="25"/>
              <ParameterGroup name="26">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6KpT389],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="27">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2pT1462],Reference=InitialConcentration"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="28"/>
              <ParameterGroup name="29">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Values[Insulin],Reference=InitialValue"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
              <ParameterGroup name="30">
                <Parameter name="Object CN" type="cn" value="CN=Root,Model=SimpleAktModel,Vector=Values[AA],Reference=InitialValue"/>
                <Parameter name="Role" type="unsignedInteger" value="1"/>
              </ParameterGroup>
            </ParameterGroup>
          </ParameterGroup>
        </ParameterGroup>
        <ParameterGroup name="Validation Set">
          <Parameter name="Weight" type="unsignedFloat" value="1"/>
          <Parameter name="Threshold" type="unsignedInteger" value="5"/>
        </ParameterGroup>
      </Problem>
      <Method name="Genetic Algorithm" type="GeneticAlgorithm">
        <Parameter name="Number of Generations" type="unsignedInteger" value="200"/>
        <Parameter name="Population Size" type="unsignedInteger" value="50"/>
        <Parameter name="Random Number Generator" type="unsignedInteger" value="1"/>
        <Parameter name="Seed" type="unsignedInteger" value="0"/>
      </Method>
    </Task>
    <Task key="Task_20" name="Metabolic Control Analysis" type="metabolicControlAnalysis" scheduled="false" updateModel="false">
      <Report reference="Report_14" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="Steady-State" type="key" value="Task_14"/>
      </Problem>
      <Method name="MCA Method (Reder)" type="MCAMethod(Reder)">
        <Parameter name="Modulation Factor" type="unsignedFloat" value="1.0000000000000001e-09"/>
        <Parameter name="Use Reder" type="bool" value="1"/>
        <Parameter name="Use Smallbone" type="bool" value="1"/>
      </Method>
    </Task>
    <Task key="Task_21" name="Lyapunov Exponents" type="lyapunovExponents" scheduled="false" updateModel="false">
      <Report reference="Report_15" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="ExponentNumber" type="unsignedInteger" value="3"/>
        <Parameter name="DivergenceRequested" type="bool" value="1"/>
        <Parameter name="TransientTime" type="float" value="0"/>
      </Problem>
      <Method name="Wolf Method" type="WolfMethod">
        <Parameter name="Orthonormalization Interval" type="unsignedFloat" value="1"/>
        <Parameter name="Overall time" type="unsignedFloat" value="1000"/>
        <Parameter name="Relative Tolerance" type="unsignedFloat" value="9.9999999999999995e-07"/>
        <Parameter name="Absolute Tolerance" type="unsignedFloat" value="9.9999999999999998e-13"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="10000"/>
      </Method>
    </Task>
    <Task key="Task_22" name="Time Scale Separation Analysis" type="timeScaleSeparationAnalysis" scheduled="false" updateModel="false">
      <Report reference="Report_16" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
      </Problem>
      <Method name="ILDM (LSODA,Deuflhard)" type="TimeScaleSeparation(ILDM,Deuflhard)">
        <Parameter name="Deuflhard Tolerance" type="unsignedFloat" value="0.0001"/>
      </Method>
    </Task>
    <Task key="Task_23" name="Sensitivities" type="sensitivities" scheduled="false" updateModel="false">
      <Report reference="Report_17" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="SubtaskType" type="unsignedInteger" value="1"/>
        <ParameterGroup name="TargetFunctions">
          <Parameter name="SingleObject" type="cn" value=""/>
          <Parameter name="ObjectListType" type="unsignedInteger" value="7"/>
        </ParameterGroup>
        <ParameterGroup name="ListOfVariables">
          <ParameterGroup name="Variables">
            <Parameter name="SingleObject" type="cn" value=""/>
            <Parameter name="ObjectListType" type="unsignedInteger" value="41"/>
          </ParameterGroup>
          <ParameterGroup name="Variables">
            <Parameter name="SingleObject" type="cn" value=""/>
            <Parameter name="ObjectListType" type="unsignedInteger" value="0"/>
          </ParameterGroup>
        </ParameterGroup>
      </Problem>
      <Method name="Sensitivities Method" type="SensitivitiesMethod">
        <Parameter name="Delta factor" type="unsignedFloat" value="0.001"/>
        <Parameter name="Delta minimum" type="unsignedFloat" value="9.9999999999999998e-13"/>
      </Method>
    </Task>
    <Task key="Task_24" name="Moieties" type="moieties" scheduled="false" updateModel="false">
      <Report reference="Report_18" target="" append="1" confirmOverwrite="1"/>
      <Problem>
      </Problem>
      <Method name="Householder Reduction" type="Householder">
      </Method>
    </Task>
    <Task key="Task_25" name="Cross Section" type="crosssection" scheduled="false" updateModel="false">
      <Problem>
        <Parameter name="AutomaticStepSize" type="bool" value="0"/>
        <Parameter name="StepNumber" type="unsignedInteger" value="100"/>
        <Parameter name="StepSize" type="float" value="0.01"/>
        <Parameter name="Duration" type="float" value="1"/>
        <Parameter name="TimeSeriesRequested" type="bool" value="1"/>
        <Parameter name="OutputStartTime" type="float" value="0"/>
        <Parameter name="Output Event" type="bool" value="0"/>
        <Parameter name="Start in Steady State" type="bool" value="0"/>
        <Parameter name="LimitCrossings" type="bool" value="0"/>
        <Parameter name="NumCrossingsLimit" type="unsignedInteger" value="0"/>
        <Parameter name="LimitOutTime" type="bool" value="0"/>
        <Parameter name="LimitOutCrossings" type="bool" value="0"/>
        <Parameter name="PositiveDirection" type="bool" value="1"/>
        <Parameter name="NumOutCrossingsLimit" type="unsignedInteger" value="0"/>
        <Parameter name="LimitUntilConvergence" type="bool" value="0"/>
        <Parameter name="ConvergenceTolerance" type="float" value="9.9999999999999995e-07"/>
        <Parameter name="Threshold" type="float" value="0"/>
        <Parameter name="DelayOutputUntilConvergence" type="bool" value="0"/>
        <Parameter name="OutputConvergenceTolerance" type="float" value="9.9999999999999995e-07"/>
        <ParameterText name="TriggerExpression" type="expression">
          
        </ParameterText>
        <Parameter name="SingleVariable" type="cn" value=""/>
      </Problem>
      <Method name="Deterministic (LSODA)" type="Deterministic(LSODA)">
        <Parameter name="Integrate Reduced Model" type="bool" value="0"/>
        <Parameter name="Relative Tolerance" type="unsignedFloat" value="9.9999999999999995e-07"/>
        <Parameter name="Absolute Tolerance" type="unsignedFloat" value="9.9999999999999998e-13"/>
        <Parameter name="Max Internal Steps" type="unsignedInteger" value="100000"/>
        <Parameter name="Max Internal Step Size" type="unsignedFloat" value="0"/>
      </Method>
    </Task>
    <Task key="Task_26" name="Linear Noise Approximation" type="linearNoiseApproximation" scheduled="false" updateModel="false">
      <Report reference="Report_19" target="" append="1" confirmOverwrite="1"/>
      <Problem>
        <Parameter name="Steady-State" type="key" value="Task_14"/>
      </Problem>
      <Method name="Linear Noise Approximation" type="LinearNoiseApproximation">
      </Method>
    </Task>
  </ListOfTasks>
  <ListOfReports>
    <Report key="Report_10" name="Steady-State" taskType="steadyState" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Steady-State]"/>
      </Footer>
    </Report>
    <Report key="Report_11" name="Elementary Flux Modes" taskType="fluxMode" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Footer>
        <Object cn="CN=Root,Vector=TaskList[Elementary Flux Modes],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_12" name="Optimization" taskType="optimization" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Object=Description"/>
        <Object cn="String=\[Function Evaluations\]"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="String=\[Best Value\]"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="String=\[Best Parameters\]"/>
      </Header>
      <Body>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Function Evaluations"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Best Value"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Problem=Optimization,Reference=Best Parameters"/>
      </Body>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Optimization],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_13" name="Parameter Estimation" taskType="parameterFitting" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Object=Description"/>
        <Object cn="String=\[Function Evaluations\]"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="String=\[Best Value\]"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="String=\[Best Parameters\]"/>
      </Header>
      <Body>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Function Evaluations"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Value"/>
        <Object cn="Separator=&#9;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Parameters"/>
      </Body>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_14" name="Metabolic Control Analysis" taskType="metabolicControlAnalysis" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Metabolic Control Analysis],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Metabolic Control Analysis],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_15" name="Lyapunov Exponents" taskType="lyapunovExponents" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Lyapunov Exponents],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Lyapunov Exponents],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_16" name="Time Scale Separation Analysis" taskType="timeScaleSeparationAnalysis" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Time Scale Separation Analysis],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Time Scale Separation Analysis],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_17" name="Sensitivities" taskType="sensitivities" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Sensitivities],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Sensitivities],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_18" name="Moieties" taskType="moieties" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Moieties],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Moieties],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_19" name="Linear Noise Approximation" taskType="linearNoiseApproximation" separator="&#9;" precision="6">
      <Comment>
        Automatically generated report.
      </Comment>
      <Header>
        <Object cn="CN=Root,Vector=TaskList[Linear Noise Approximation],Object=Description"/>
      </Header>
      <Footer>
        <Object cn="String=&#10;"/>
        <Object cn="CN=Root,Vector=TaskList[Linear Noise Approximation],Object=Result"/>
      </Footer>
    </Report>
    <Report key="Report_30" name="Time-Course" precision="6" separator="&#9;" taskType="Time-Course">
      <Comment/>
      <Table printTitle="1">
        <Object cn="CN=Root,Model=SimpleAktModel,Reference=Time"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1a],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[IRS1pS636_639],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[Akt],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[AktpT308],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[TSC2pT1462],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PRAS40pT246],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6K],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[S6KpT389],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[FourEBP1pT37_46],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[PI3K],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[pPI3K],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[pmTORC1],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[mTORC1cyt],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Compartments[Cell],Vector=Metabolites[mTORC1lys],Reference=Concentration"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[Insulin],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[AA],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kIRS1Act],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kIRS1Inact],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kIRS1Phos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kPI3KPhos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kPI3KDephos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kAktPhos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kAktDephos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kTSC2Phos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kTSC2Dephos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1cytToLys],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1LysToCyt],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1Phos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kmTORC1Dephos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kPras40Phos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kPras40Dephos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kFourEBP1Phos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kFourEBP1Dephos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kS6KPhos],Reference=Value"/>
        <Object cn="CN=Root,Model=SimpleAktModel,Vector=Values[kS6KDephos],Reference=Value"/>
      </Table>
    </Report>
    <Report precision="6" separator="&#9;" name="multi_parameter_estimation" key="Report_34" taskType="parameterFitting">
      <Comment/>
      <Table printTitle="1">
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Parameters"/>
        <Object cn="CN=Root,Vector=TaskList[Parameter Estimation],Problem=Parameter Estimation,Reference=Best Value"/>
      </Table>
    </Report>
  </ListOfReports>
  <SBMLReference file="simple_akt_model.sbml">
    <SBMLMap SBMLid="AA" COPASIkey="ModelValue_1"/>
    <SBMLMap SBMLid="Akt" COPASIkey="Metabolite_3"/>
    <SBMLMap SBMLid="AktpT308" COPASIkey="Metabolite_4"/>
    <SBMLMap SBMLid="Cell" COPASIkey="Compartment_0"/>
    <SBMLMap SBMLid="FourEBP1" COPASIkey="Metabolite_11"/>
    <SBMLMap SBMLid="FourEBP1pT37_46" COPASIkey="Metabolite_12"/>
    <SBMLMap SBMLid="IRS1" COPASIkey="Metabolite_0"/>
    <SBMLMap SBMLid="IRS1a" COPASIkey="Metabolite_1"/>
    <SBMLMap SBMLid="IRS1pS636_639" COPASIkey="Metabolite_2"/>
    <SBMLMap SBMLid="Insulin" COPASIkey="ModelValue_0"/>
    <SBMLMap SBMLid="PI3K" COPASIkey="Metabolite_13"/>
    <SBMLMap SBMLid="PRAS40" COPASIkey="Metabolite_7"/>
    <SBMLMap SBMLid="PRAS40pT246" COPASIkey="Metabolite_8"/>
    <SBMLMap SBMLid="R10b" COPASIkey="Reaction_18"/>
    <SBMLMap SBMLid="R10f" COPASIkey="Reaction_17"/>
    <SBMLMap SBMLid="R1f" COPASIkey="Reaction_0"/>
    <SBMLMap SBMLid="R2b" COPASIkey="Reaction_2"/>
    <SBMLMap SBMLid="R2f" COPASIkey="Reaction_1"/>
    <SBMLMap SBMLid="R3b" COPASIkey="Reaction_4"/>
    <SBMLMap SBMLid="R3f" COPASIkey="Reaction_3"/>
    <SBMLMap SBMLid="R4b" COPASIkey="Reaction_6"/>
    <SBMLMap SBMLid="R4f" COPASIkey="Reaction_5"/>
    <SBMLMap SBMLid="R5b" COPASIkey="Reaction_8"/>
    <SBMLMap SBMLid="R5f" COPASIkey="Reaction_7"/>
    <SBMLMap SBMLid="R6b" COPASIkey="Reaction_10"/>
    <SBMLMap SBMLid="R6f" COPASIkey="Reaction_9"/>
    <SBMLMap SBMLid="R7b" COPASIkey="Reaction_12"/>
    <SBMLMap SBMLid="R7f" COPASIkey="Reaction_11"/>
    <SBMLMap SBMLid="R8b" COPASIkey="Reaction_14"/>
    <SBMLMap SBMLid="R8f" COPASIkey="Reaction_13"/>
    <SBMLMap SBMLid="R9b" COPASIkey="Reaction_16"/>
    <SBMLMap SBMLid="R9f" COPASIkey="Reaction_15"/>
    <SBMLMap SBMLid="S6K" COPASIkey="Metabolite_9"/>
    <SBMLMap SBMLid="S6KpT389" COPASIkey="Metabolite_10"/>
    <SBMLMap SBMLid="TSC2" COPASIkey="Metabolite_5"/>
    <SBMLMap SBMLid="TSC2pT1462" COPASIkey="Metabolite_6"/>
    <SBMLMap SBMLid="kAktDephos" COPASIkey="ModelValue_8"/>
    <SBMLMap SBMLid="kAktPhos" COPASIkey="ModelValue_7"/>
    <SBMLMap SBMLid="kFourEBP1Dephos" COPASIkey="ModelValue_18"/>
    <SBMLMap SBMLid="kFourEBP1Phos" COPASIkey="ModelValue_17"/>
    <SBMLMap SBMLid="kIRS1Act" COPASIkey="ModelValue_2"/>
    <SBMLMap SBMLid="kIRS1Inact" COPASIkey="ModelValue_3"/>
    <SBMLMap SBMLid="kIRS1Phos" COPASIkey="ModelValue_4"/>
    <SBMLMap SBMLid="kPI3KDephos" COPASIkey="ModelValue_6"/>
    <SBMLMap SBMLid="kPI3KPhos" COPASIkey="ModelValue_5"/>
    <SBMLMap SBMLid="kPras40Dephos" COPASIkey="ModelValue_16"/>
    <SBMLMap SBMLid="kPras40Phos" COPASIkey="ModelValue_15"/>
    <SBMLMap SBMLid="kS6KDephos" COPASIkey="ModelValue_20"/>
    <SBMLMap SBMLid="kS6KPhos" COPASIkey="ModelValue_19"/>
    <SBMLMap SBMLid="kTSC2Dephos" COPASIkey="ModelValue_10"/>
    <SBMLMap SBMLid="kTSC2Phos" COPASIkey="ModelValue_9"/>
    <SBMLMap SBMLid="kmTORC1Dephos" COPASIkey="ModelValue_14"/>
    <SBMLMap SBMLid="kmTORC1LysToCyt" COPASIkey="ModelValue_12"/>
    <SBMLMap SBMLid="kmTORC1Phos" COPASIkey="ModelValue_13"/>
    <SBMLMap SBMLid="kmTORC1cytToLys" COPASIkey="ModelValue_11"/>
    <SBMLMap SBMLid="mTORC1cyt" COPASIkey="Metabolite_16"/>
    <SBMLMap SBMLid="mTORC1lys" COPASIkey="Metabolite_17"/>
    <SBMLMap SBMLid="pPI3K" COPASIkey="Metabolite_14"/>
    <SBMLMap SBMLid="pmTORC1" COPASIkey="Metabolite_15"/>
  </SBMLReference>
  <ListOfUnitDefinitions>
    <UnitDefinition key="Unit_1" name="meter" symbol="m">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_0">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        m
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_5" name="second" symbol="s">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_4">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        s
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_13" name="Avogadro" symbol="Avogadro">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_12">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        Avogadro
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_17" name="item" symbol="#">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_16">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        #
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_35" name="liter" symbol="l">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_34">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        0.001*m^3
      </Expression>
    </UnitDefinition>
    <UnitDefinition key="Unit_41" name="mole" symbol="mol">
      <MiriamAnnotation>
        <rdf:RDF xmlns:dcterms="http://purl.org/dc/terms/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          <rdf:Description rdf:about="#Unit_40">
            <dcterms:created>
              <rdf:Description>
                <dcterms:W3CDTF>2019-10-21T08:50:42Z</dcterms:W3CDTF>
              </rdf:Description>
            </dcterms:created>
          </rdf:Description>
        </rdf:RDF>
      </MiriamAnnotation>
      <Expression>
        Avogadro*#
      </Expression>
    </UnitDefinition>
  </ListOfUnitDefinitions>
</COPASI>
