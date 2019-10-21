This XML file does not appear to have any style information associated with it. The document tree is shown below.
<freeStyleBuild _class="hudson.model.FreeStyleBuild">
<action _class="hudson.model.CauseAction">
<cause _class="hudson.model.Cause$UpstreamCause">
<shortDescription>
Started by upstream project "Gerrit-verifier-pipeline/46%2F241546%2F4" build number 1
</shortDescription>
<upstreamBuild>1</upstreamBuild>
<upstreamProject>Gerrit-verifier-pipeline/46%2F241546%2F4</upstreamProject>
<upstreamUrl>
job/Gerrit-verifier-pipeline/job/46%252F241546%252F4/
</upstreamUrl>
</cause>
</action>
<action/>
<action _class="hudson.model.ParametersAction">
<parameter _class="hudson.model.StringParameterValue">
<name>REFSPEC</name>
<value>refs/changes/46/241546/4</value>
</parameter>
<parameter _class="hudson.model.StringParameterValue">
<name>BRANCH</name>
<value>607c3f853f4cb489811fa77bfcad7a638fff898e</value>
</parameter>
<parameter _class="hudson.model.StringParameterValue">
<name>MODE</name>
<value>reviewdb</value>
</parameter>
<parameter _class="hudson.model.StringParameterValue">
<name>CHANGE_URL</name>
<value>
https://gerrit-review.googlesource.com/#/c/241546/4
</value>
</parameter>
<parameter _class="hudson.model.StringParameterValue">
<name>TARGET_BRANCH</name>
<value>stable-2.14</value>
</parameter>
</action>
<action/>
<action _class="hudson.plugins.git.util.BuildData">
<buildsByBranchName>
<detached _class="hudson.plugins.git.util.Build">
<buildNumber>46047</buildNumber>
<marked>
<SHA1>607c3f853f4cb489811fa77bfcad7a638fff898e</SHA1>
<branch>
<SHA1>607c3f853f4cb489811fa77bfcad7a638fff898e</SHA1>
<name>detached</name>
</branch>
</marked>
<revision>
<SHA1>607c3f853f4cb489811fa77bfcad7a638fff898e</SHA1>
<branch>
<SHA1>607c3f853f4cb489811fa77bfcad7a638fff898e</SHA1>
<name>detached</name>
</branch>
</revision>
</detached>
</buildsByBranchName>
<lastBuiltRevision>
<SHA1>607c3f853f4cb489811fa77bfcad7a638fff898e</SHA1>
<branch>
<SHA1>607c3f853f4cb489811fa77bfcad7a638fff898e</SHA1>
<name>detached</name>
</branch>
</lastBuiltRevision>
<remoteUrl>https://gerrit.googlesource.com/gerrit</remoteUrl>
<scmName/>
</action>
<action _class="hudson.plugins.git.GitTagAction"/>
<action/>
<action/>
<action/>
<action _class="com.nirima.jenkins.plugins.docker.action.DockerBuildAction"/>
<action/>
<action/>
<building>false</building>
<displayName>#46047</displayName>
<duration>141763</duration>
<estimatedDuration>174977</estimatedDuration>
<fullDisplayName>Gerrit-codestyle #46047</fullDisplayName>
<id>46047</id>
<keepLog>false</keepLog>
<number>46047</number>
<queueId>10303</queueId>
<result>FAILURE</result>
<timestamp>1571320100749</timestamp>
<url>
https://gerrit-ci.gerritforge.com/job/Gerrit-codestyle/46047/
</url>
<builtOn>gcloud64-a4e664f44158</builtOn>
<changeSet _class="hudson.plugins.git.GitChangeSetList">
<item _class="hudson.plugins.git.GitChangeSet">
<affectedPath>Jenkinsfile</affectedPath>
<commitId>bdff807f0733ef12975ec1183e09c5527738bd0b</commitId>
<timestamp>1571319051000</timestamp>
<author>
<absoluteUrl>
https://gerrit-ci.gerritforge.com/user/thomas.draebing
</absoluteUrl>
<fullName>thomas.draebing</fullName>
</author>
<authorEmail>thomas.draebing@sap.com</authorEmail>
<comment>
Don't sort messages returned by Jenkins The sorting of messages Jenkins would send back after verifying a change did not work anymore as it was implemented in the workflow script. This change removes the sorting of the messages. Change-Id: I9cb14308ed354c31fae08e3c7190a7f886f242bf
</comment>
<date>2019-10-17 15:30:51 +0200</date>
<id>bdff807f0733ef12975ec1183e09c5527738bd0b</id>
<msg>Don't sort messages returned by Jenkins</msg>
<path>
<editType>edit</editType>
<file>Jenkinsfile</file>
</path>
</item>
<item _class="hudson.plugins.git.GitChangeSet">
<affectedPath>gerrit-main/src/main/java/Main.java</affectedPath>
<affectedPath>
polygerrit-ui/app/behaviors/gr-change-table-behavior/gr-change-table-behavior_test.html
</affectedPath>
<commitId>607c3f853f4cb489811fa77bfcad7a638fff898e</commitId>
<timestamp>1571319729000</timestamp>
<author>
<absoluteUrl>https://gerrit-ci.gerritforge.com/user/tdraebing</absoluteUrl>
<fullName>Thomas Dräbing</fullName>
</author>
<authorEmail>thomas.draebing@sap.com</authorEmail>
<comment>
[DO NOT MERGE] testing the build pipeline Bump to trigger CI again Change-Id: Iea19da3f107f1189ef664e306ed5b3d021628086
</comment>
<date>2019-10-17 13:42:09 +0000</date>
<id>607c3f853f4cb489811fa77bfcad7a638fff898e</id>
<msg>[DO NOT MERGE] testing the build pipeline</msg>
<path>
<editType>edit</editType>
<file>gerrit-main/src/main/java/Main.java</file>
</path>
<path>
<editType>edit</editType>
<file>
polygerrit-ui/app/behaviors/gr-change-table-behavior/gr-change-table-behavior_test.html
</file>
</path>
</item>
<kind>git</kind>
</changeSet>
</freeStyleBuild>
