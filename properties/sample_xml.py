# this is the basic info
basic_info_sample = """<Result>
<Name>
<Name01 value="Insured or Subscriber"/>
<Name02 value="Person"/>
<Name03 value="DOE"/>
<Name04 value="JANE"/>
<Name05 value="A"/> 
<Name08 value="Member Identification Number"/>
<Name09 value="12345679H"/> 
</Name>
<Address>
<Address01 value="100 MAIN STREET"/> 
</Address>
<Address2>
<Address201 value="ANY CITY"/> 
<Address202 value="FL"/> 
<Address203 value="328255723"/>
</Address2>
<Stats>
<Stats01 value="Date in format CCYYMMDD"/>
<Stats02 value="19220132"/> 
<Stats03 value="Female"/> 
</Stats>
<Date>
<Date01 value="Date of Death"/>
<Date02 value="Date in format CCYYMMDD"/>
<Date03 value="20190131"/>
</Date>
<Section>
<Eligibility>
<Eligibility03 value="Part A"/>
</Eligibility>
<Date>
<Date03 value="19970201-20000101" />
</Date>
</Section>
</Result>
"""

# this is part a deductible, in sf it's Inpatient
inpatient_sample = """
<Result>
<Section>
<Eligibility>
	<Eligibility01 value="Deductible" />
	<Eligibility03 value="Plan Waiting Period" />
	<Eligibility04 value="Medicare Part A" />
	<Eligibility06 value="Remaining" />
	<Eligibility07 value="1364" />
</Eligibility>
<Date>
<Date03 value="20210101-20211231" />
</Date>
</Section>
</Result>
"""

# this is deductible caps - part b deductible
deductible_caps_sample = """
<Result>
<Section>
<Eligibility>
	<Eligibility01 value="Deductible" />
	<Eligibility03 value="Plan Waiting Period" />
	<Eligibility04 value="Medicare Part B" />
	<Eligibility06 value="Remaining" />
	<Eligibility07 value="1364" />
</Eligibility>
<Date>
<Date03 value="20210101-20211231" />
</Date>
</Section>
</Result>
"""

qmb_status_sample = """
<Result>
<Section>
<Eligibility>
	<Eligibility01 value="Other or Additional Payor" />
	<Eligibility04 value="QMB" />
	<Eligibility05 value="CA QMB Plan" />
</Eligibility>
<Date>
<Date03 value="20210101-20211231" />
</Date>
</Section>
</Result>
"""

msp_sample = """
<Result>
<Section>
<Date>
<Date03 value="20120101-20181031"/>
</Date>
<Address>
<Address01 value="100 Main Street"/> 
</Address>
<Address2>
<Address201 value="Miramar"/>
<Address202 value="FL"/>
<Address203 value="33027"/>
</Address2>
</Section>
</Result>

"""

plan_coverage_sample = """<Result>
<Section>
<Eligibility>
<Eligibility01 value="Contact Organization for Eligibility Information"/>
<Eligibility03 value="Plan Waiting Period"/>
<Eligibility04 value="PPO"/>
</Eligibility>
<Info>
<Info01 value="Plan Number"/>
<Info02 value="H1234"/>
</Info>

<Info>
<Info01 value="Plan Network Identification Number"/>
<Info02 value="146"/>
<Info03 value="ACME Gold Plus H1234-123"/>
</Info>

<Date>
<Date01 value="Coordination of Benefits"/>
<Date02 value="Range of Dates in format CCYYMMDD-CCYYMMDD"/>
<Date03 value="20120101-20181031"/>
</Date>

<Note>
<Note01 value="MCO Bill option Code - C"/>
</Note>

<MoreDetails>
<Name>
<Name01 value="Primary Payer"/>
<NameO2 value="Non-Person Entity"/>
<Name03 value="ACME, INC."/>
</Name>

<Address>
<Addresse01 value="100 Main Street"/>
</Address>

<Address2>
<Address201 value="Miramar"/>
<Address202 value="FL"/>
<Address203 value="33027" />
</Address2>

<Contact>
<Contact01 value="Information Contact"/>
<Contact03 value="Telephone"/>
<Contact04 value="8001231234"/>
<Contact05 value="Uniform Resource Locator (URL)"/>
<Contact06 value="www.website.com/page"/>
</Contact>

</MoreDetails>
</Section>

</Result>
"""

part_d_sample = """
<Result>
<Section>
<Eligibility>
<Eligibility01 value="Contact Organization for Eligibility Information"/>
<Eligibility03 value="Plan Waiting Period"/>
<Eligibility04 value="Medicare Part D"/>
</Eligibility>
<Info>
<Info01 value="Plan Number"/>
<Info02 value="H1234"/>
</Info>

<Info>
<Info01 value="Plan Network Identification Number"/>
<Info02 value="146"/>
<Info03 value="ACME Gold Plus H1234-123"/>
</Info>

<Date>
<Date01 value="Coordination of Benefits"/>
<Date02 value="Range of Dates in format CCYYMMDD-CCYYMMDD"/>
<Date03 value="20120101-20181031"/>
</Date>

<Note>
<Note01 value="MCO Bill option Code - C"/>
</Note>

<MoreDetails>
<Name>
<Name01 value="Primary Payer"/>
<NameO2 value="Non-Person Entity"/>
<Name03 value="ACME, INC."/>
</Name>

<Address>
<Addresse01 value="100 Main Street"/>
</Address>

<Address2>
<Address201 value="Miramar"/>
<Address202 value="FL"/>
<Address203 value="33027" />
</Address2>

<Contact>
<Contact01 value="Information Contact"/>
<Contact03 value="Telephone"/>
<Contact04 value="8001231234"/>
<Contact05 value="Uniform Resource Locator (URL)"/>
<Contact06 value="www.website.com/page"/>
</Contact>

</MoreDetails>
</Section>

</Result>
"""

error_sample = "<Result>\r\n  <Name>\r\n    <Name01 value=\"Insured or Subscriber\" />\r\n    <Name02 value=\"Person\" />\r\n    <Name03 value=\"DOE\" />\r\n    <Name04 value=\"JANE\" />\r\n    <Name08 value=\"Member Identification Number\" />\r\n    <Name09 value=\"123456789H\" />\r\n  </Name>\r\n  <Section>\r\n    <Eligibility>\r\n      <Eligibility01 value=\"Cannot Process\" />\r\n    </Eligibility>\r\n    <Date>\r\n      <Date01 value=\"Plan\" />\r\n      <Date02 value=\"Date Expressed in Format CCYYMMDD\" />\r\n      <Date03 value=\"20210304\" />\r\n    </Date>\r\n    <Error>\r\n      <Error01 value=\"No\" />\r\n      <Error03 value=\"Invalid/Missing Subscriber/Insured ID\" />\r\n      <Error04 value=\"Please Correct and Resubmit\" />\r\n    </Error>\r\n    <Note>\r\n      <Note01 value=\"The MBI submitted does not conform to Medicare rules. Please ensure you have a valid MBI. Code : EMCHNL0010A5. (Source : E1.)\" />\r\n    </Note>\r\n  </Section>\r\n</Result>"

aggr_sample = """
<Result>
<Name>
<Name01 value="Insured or Subscriber"/>
<Name02 value="Person"/>
<Name03 value="DOE"/>
<Name04 value="JANE"/>
<Name05 value="A"/> 
<Name08 value="Member Identification Number"/>
<Name09 value="12345679H"/> 
</Name>
<Address>
<Address01 value="100 MAIN STREET"/> 
</Address>
<Address2>
<Address201 value="ANY CITY"/> 
<Address202 value="FL"/> 
<Address203 value="328255723"/>
</Address2>
<Stats>
<Stats01 value="Date in format CCYYMMDD"/>
<Stats02 value="19220132"/> 
<Stats03 value="Female"/> 
</Stats>
<Date>
<Date01 value="Date of Death"/>
<Date02 value="Date in format CCYYMMDD"/>
<Date03 value="20190131"/>
</Date>
<Section>
<Eligibility>
<Eligibility01 value="Other or Additional Payor" />
<Eligibility04 value="QMB" />
<Eligibility05 value="CA QMB Plan" />
<Eligibility03 value="Part A"/>
</Eligibility>
<Date>
<Date03 value="19970201-20000101" />
</Date>
</Section>
</Result>
"""