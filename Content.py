
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<xsd:element name="freeStyleBuild" type="hudson.model.FreeStyleBuild"/>
<xsd:complexType name="hudson.model.FreeStyleBuild">
<xsd:complexContent>
<xsd:extension base="hudson.model.Build">
<xsd:sequence/>
</xsd:extension>
</xsd:complexContent>
</xsd:complexType>
<xsd:complexType name="hudson.model.Build">
<xsd:complexContent>
<xsd:extension base="hudson.model.AbstractBuild">
<xsd:sequence/>
</xsd:extension>
</xsd:complexContent>
</xsd:complexType>
<xsd:complexType name="hudson.model.AbstractBuild">
<xsd:complexContent>
<xsd:extension base="hudson.model.Run">
<xsd:sequence>
<xsd:element name="builtOn" type="xsd:string" minOccurs="0"/>
<xsd:element name="changeSet" type="hudson.scm.ChangeLogSet" minOccurs="0"/>
<xsd:element name="fingerprint" type="hudson.model.Fingerprint" minOccurs="0" maxOccurs="unbounded"/>
</xsd:sequence>
</xsd:extension>
</xsd:complexContent>
</xsd:complexType>
<xsd:complexType name="hudson.model.Fingerprint">
<xsd:sequence>
<xsd:element name="fileName" type="xsd:string" minOccurs="0"/>
<xsd:element name="hash" type="xsd:string" minOccurs="0"/>
<xsd:element name="original" type="hudson.model.Fingerprint-BuildPtr" minOccurs="0"/>
<xsd:element name="timestamp" type="xsd:anyType" minOccurs="0"/>
<xsd:element name="usage" type="hudson.model.Fingerprint-RangeItem" minOccurs="0" maxOccurs="unbounded"/>
</xsd:sequence>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
<xsd:complexType name="hudson.model.Fingerprint-RangeItem">
<xsd:sequence>
<xsd:element name="name" type="xsd:string" minOccurs="0"/>
<xsd:element name="ranges" type="hudson.model.Fingerprint-RangeSet" minOccurs="0"/>
</xsd:sequence>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
<xsd:complexType name="hudson.model.Fingerprint-RangeSet">
<xsd:sequence>
<xsd:element name="range" type="hudson.model.Fingerprint-Range" minOccurs="0" maxOccurs="unbounded"/>
</xsd:sequence>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
<xsd:complexType name="hudson.model.Fingerprint-Range">
<xsd:sequence>
<xsd:element name="end" type="xsd:int"/>
<xsd:element name="start" type="xsd:int"/>
</xsd:sequence>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
<xsd:complexType name="hudson.model.Fingerprint-BuildPtr">
<xsd:sequence>
<xsd:element name="name" type="xsd:string" minOccurs="0"/>
<xsd:element name="number" type="xsd:int"/>
</xsd:sequence>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
<xsd:complexType name="hudson.scm.ChangeLogSet">
<xsd:sequence>
<xsd:element name="item" type="xsd:anyType" minOccurs="0" maxOccurs="unbounded"/>
<xsd:element name="kind" type="xsd:string" minOccurs="0"/>
</xsd:sequence>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
<xsd:complexType name="hudson.model.Run">
<xsd:complexContent>
<xsd:extension base="hudson.model.Actionable">
<xsd:sequence>
<xsd:element name="artifact" type="hudson.model.Run-Artifact" minOccurs="0" maxOccurs="unbounded"/>
<xsd:element name="building" type="xsd:boolean"/>
<xsd:element name="description" type="xsd:string" minOccurs="0"/>
<xsd:element name="displayName" type="xsd:string" minOccurs="0"/>
<xsd:element name="duration" type="xsd:long"/>
<xsd:element name="estimatedDuration" type="xsd:long"/>
<xsd:element name="executor" type="hudson.model.Executor" minOccurs="0"/>
<xsd:element name="fullDisplayName" type="xsd:string" minOccurs="0"/>
<xsd:element name="id" type="xsd:string" minOccurs="0"/>
<xsd:element name="keepLog" type="xsd:boolean"/>
<xsd:element name="number" type="xsd:int"/>
<xsd:element name="queueId" type="xsd:long"/>
<xsd:element name="result" type="xsd:anyType" minOccurs="0"/>
<xsd:element name="timestamp" type="xsd:long" minOccurs="0"/>
<xsd:element name="url" type="xsd:string" minOccurs="0"/>
</xsd:sequence>
</xsd:extension>
</xsd:complexContent>
</xsd:complexType>
<xsd:complexType name="hudson.model.Executor">
<xsd:sequence>
<xsd:element name="currentExecutable" type="xsd:anyType" minOccurs="0"/>
<xsd:element name="currentWorkUnit" type="hudson.model.queue.WorkUnit" minOccurs="0"/>
<xsd:element name="idle" type="xsd:boolean"/>
<xsd:element name="likelyStuck" type="xsd:boolean"/>
<xsd:element name="number" type="xsd:int"/>
<xsd:element name="progress" type="xsd:int"/>
</xsd:sequence>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
<xsd:complexType name="hudson.model.queue.WorkUnit">
<xsd:sequence/>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
<xsd:complexType name="hudson.model.Run-Artifact">
<xsd:sequence>
<xsd:element name="displayPath" type="xsd:string" minOccurs="0"/>
<xsd:element name="fileName" type="xsd:string" minOccurs="0"/>
<xsd:element name="relativePath" type="xsd:string" minOccurs="0">
<xsd:annotation>
<xsd:documentation> Relative path name from artifacts root. </xsd:documentation>
</xsd:annotation>
</xsd:element>
</xsd:sequence>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
<xsd:complexType name="hudson.model.Actionable">
<xsd:sequence>
<xsd:element name="action" type="xsd:anyType" minOccurs="0" maxOccurs="unbounded"/>
</xsd:sequence>
<xsd:attribute name="_class" type="xsd:string" use="optional"/>
</xsd:complexType>
</xsd:schema>
