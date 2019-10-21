Python API:{
{
  "_class" : "hudson.model.FreeStyleBuild",
  "actions" : [
    {
      "_class" : "hudson.model.CauseAction",
      "causes" : [
        {
          "_class" : "hudson.model.Cause$UpstreamCause",
          "shortDescription" : "Started by upstream project \"Gerrit-verifier-pipeline/46%2F241546%2F4\" build number 1",
          "upstreamBuild" : 1,
          "upstreamProject" : "Gerrit-verifier-pipeline/46%2F241546%2F4",
          "upstreamUrl" : "job/Gerrit-verifier-pipeline/job/46%252F241546%252F4/"
        }
      ]
    },
    {
      
    },
    {
      "_class" : "hudson.model.ParametersAction",
      "parameters" : [
        {
          "_class" : "hudson.model.StringParameterValue",
          "name" : "REFSPEC",
          "value" : "refs/changes/46/241546/4"
        },
        {
          "_class" : "hudson.model.StringParameterValue",
          "name" : "BRANCH",
          "value" : "607c3f853f4cb489811fa77bfcad7a638fff898e"
        },
        {
          "_class" : "hudson.model.StringParameterValue",
          "name" : "MODE",
          "value" : "reviewdb"
        },
        {
          "_class" : "hudson.model.StringParameterValue",
          "name" : "CHANGE_URL",
          "value" : "https://gerrit-review.googlesource.com/#/c/241546/4"
        },
        {
          "_class" : "hudson.model.StringParameterValue",
          "name" : "TARGET_BRANCH",
          "value" : "stable-2.14"
        }
      ]
    },
    {
      
    },
    {
      "_class" : "hudson.plugins.git.util.BuildData",
      "buildsByBranchName" : {
        "detached" : {
          "_class" : "hudson.plugins.git.util.Build",
          "buildNumber" : 46047,
          "buildResult" : None,
          "marked" : {
            "SHA1" : "607c3f853f4cb489811fa77bfcad7a638fff898e",
            "branch" : [
              {
                "SHA1" : "607c3f853f4cb489811fa77bfcad7a638fff898e",
                "name" : "detached"
              }
            ]
          },
          "revision" : {
            "SHA1" : "607c3f853f4cb489811fa77bfcad7a638fff898e",
            "branch" : [
              {
                "SHA1" : "607c3f853f4cb489811fa77bfcad7a638fff898e",
                "name" : "detached"
              }
            ]
          }
        }
      },
      "lastBuiltRevision" : {
        "SHA1" : "607c3f853f4cb489811fa77bfcad7a638fff898e",
        "branch" : [
          {
            "SHA1" : "607c3f853f4cb489811fa77bfcad7a638fff898e",
            "name" : "detached"
          }
        ]
      },
      "remoteUrls" : [
        "https://gerrit.googlesource.com/gerrit"
      ],
      "scmName" : ""
    },
    {
      "_class" : "hudson.plugins.git.GitTagAction"
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "com.nirima.jenkins.plugins.docker.action.DockerBuildAction"
    },
    {
      
    },
    {
      
    }
  ],
  "artifacts" : [
    
  ],
  "building" : False,
  "description" : None,
  "displayName" : "#46047",
  "duration" : 141763,
  "estimatedDuration" : 174977,
  "executor" : None,
  "fullDisplayName" : "Gerrit-codestyle #46047",
  "id" : "46047",
  "keepLog" : False,
  "number" : 46047,
  "queueId" : 10303,
  "result" : "FAILURE",
  "timestamp" : 1571320100749,
  "url" : "https://gerrit-ci.gerritforge.com/job/Gerrit-codestyle/46047/",
  "builtOn" : "gcloud64-a4e664f44158",
  "changeSet" : {
    "_class" : "hudson.plugins.git.GitChangeSetList",
    "items" : [
      {
        "_class" : "hudson.plugins.git.GitChangeSet",
        "affectedPaths" : [
          "Jenkinsfile"
        ],
        "commitId" : "bdff807f0733ef12975ec1183e09c5527738bd0b",
        "timestamp" : 1571319051000,
        "author" : {
          "absoluteUrl" : "https://gerrit-ci.gerritforge.com/user/thomas.draebing",
          "fullName" : "thomas.draebing"
        },
        "authorEmail" : "thomas.draebing@sap.com",
        "comment" : "Don't sort messages returned by Jenkins\nThe sorting of messages Jenkins would send back after verifying a change\ndid not work anymore as it was implemented in the workflow script.\nThis change removes the sorting of the messages.\nChange-Id: I9cb14308ed354c31fae08e3c7190a7f886f242bf\n",
        "date" : "2019-10-17 15:30:51 +0200",
        "id" : "bdff807f0733ef12975ec1183e09c5527738bd0b",
        "msg" : "Don't sort messages returned by Jenkins",
        "paths" : [
          {
            "editType" : "edit",
            "file" : "Jenkinsfile"
          }
        ]
      },
      {
        "_class" : "hudson.plugins.git.GitChangeSet",
        "affectedPaths" : [
          "gerrit-main/src/main/java/Main.java",
          "polygerrit-ui/app/behaviors/gr-change-table-behavior/gr-change-table-behavior_test.html"
        ],
        "commitId" : "607c3f853f4cb489811fa77bfcad7a638fff898e",
        "timestamp" : 1571319729000,
        "author" : {
          "absoluteUrl" : "https://gerrit-ci.gerritforge.com/user/tdraebing",
          "fullName" : "Thomas Dräbing"
        },
        "authorEmail" : "thomas.draebing@sap.com",
        "comment" : "[DO NOT MERGE] testing the build pipeline\nBump to trigger CI again\nChange-Id: Iea19da3f107f1189ef664e306ed5b3d021628086\n",
        "date" : "2019-10-17 13:42:09 +0000",
        "id" : "607c3f853f4cb489811fa77bfcad7a638fff898e",
        "msg" : "[DO NOT MERGE] testing the build pipeline",
        "paths" : [
          {
            "editType" : "edit",
            "file" : "gerrit-main/src/main/java/Main.java"
          },
          {
            "editType" : "edit",
            "file" : "polygerrit-ui/app/behaviors/gr-change-table-behavior/gr-change-table-behavior_test.html"
          }
        ]
      }
    ],
    "kind" : "git"
  }
}
api.json:{
{
  "_class": "hudson.model.FreeStyleBuild",
  "การกระทำ": [
    {
      "_class": "hudson.model.CauseAction",
      "สาเหตุ": [
        {
          "_class": "hudson.model.Cause $ UpstreamCause",
          "shortDescription": "เริ่มโดยโครงการอัปสตรีม \" Gerrit-verifier-pipeline / 46% 2F241546% 2F4 \ "บิลด์หมายเลข 1",
          "upstreamBuild": 1,
          "upstreamProject": "Gerrit-verifier-pipeline / 46% 2F241546% 2F4"
          "upstreamUrl": "job / Gerrit-verifier-pip / งาน / 46% 252F241546% 252F4 /"
        }
      ]
    }
    {
      
    }
    {
      "_class": "hudson.model.ParametersAction",
      "พารามิเตอร์": [
        {
          "_class": "hudson.model.StringParameterValue",
          "name": "REFSPEC",
          "ค่า": "อ้างอิง / เปลี่ยนแปลง / 46/241546/4"
        }
        {
          "_class": "hudson.model.StringParameterValue",
          "ชื่อ": "สาขา",
          "ค่า": "607c3f853f4cb489811fa77bfcad7a638fff898e"
        }
        {
          "_class": "hudson.model.StringParameterValue",
          "name": "MODE",
          "value": "reviewdb"
        }
        {
          "_class": "hudson.model.StringParameterValue",
          "name": "CHANGE_URL",
          "value": "https://gerrit-review.googlesource.com/#/c/241546/4"
        }
        {
          "_class": "hudson.model.StringParameterValue",
          "name": "TARGET_BRANCH",
          "value": "stable-2.14"
        }
      ]
    }
    {
      
    }
    {
      "_class": "hudson.plugins.git.util.BuildData",
      "buildsByBranchName": {
        "แฝด": {
          "_class": "hudson.plugins.git.util.Build",
          "buildNumber": 46047,
          "buildResult": null,
          "ทำเครื่องหมาย": {
            "SHA1": "607c3f853f4cb489811fa77bfcad7a638fff898e",
            "สาขา": [
              {
                "SHA1": "607c3f853f4cb489811fa77bfcad7a638fff898e",
                "name": "แฝด"
              }
            ]
          }
          "การแก้ไข": {
            "SHA1": "607c3f853f4cb489811fa77bfcad7a638fff898e",
            "สาขา": [
              {
                "SHA1": "607c3f853f4cb489811fa77bfcad7a638fff898e",
                "name": "แฝด"
              }
            ]
          }
        }
      }
      "lastBuiltRevision": {
        "SHA1": "607c3f853f4cb489811fa77bfcad7a638fff898e",
        "สาขา": [
          {
            "SHA1": "607c3f853f4cb489811fa77bfcad7a638fff898e",
            "name": "แฝด"
          }
        ]
      }
      "remoteUrls": [
        "https://gerrit.googlesource.com/gerrit"
      ]
      "scmName": ""
    }
    {
      "_class": "hudson.plugins.git.GitTagAction"
    }
    {
      
    }
    {
      
    }
    {
      
    }
    {
      "_class": "com.nirima.jenkins.plugins.docker.action.DockerBuildAction"
    }
    {
      
    }
    {
      
    }
  ]
  "สิ่งประดิษฐ์": [
    
  ]
  "อาคาร": เท็จ
  "description": null,
  "displayName": "# 46047",
  "ระยะเวลา": 141763,
  "โดยประมาณระยะเวลา": 174977,
  "ผู้ปฏิบัติการ": null,
  "fullDisplayName": "Gerrit-codestyle # 46047",
  "id": "46047",
  "keepLog": false
  "หมายเลข": 46047,
  "queId": 10303,
  "result": "FAILURE",
  "การประทับเวลา": 1571320100749,
  "url": "https://gerrit-ci.gerritforge.com/job/Gerrit-codestyle/46047/"
  "builtOn": "gcloud64-a4e664f44158",
  "changeSet": {
    "_class": "hudson.plugins.git.GitChangeSetList",
    "รายการ": [
      {
        "_class": "hudson.plugins.git.GitChangeSet",
        "impactPaths": [
          "Jenkinsfile"
        ]
        "commitId": "bdff807f0733ef12975ec1183e09c5527738bd0b",
        "การประทับเวลา": 1571319051000,
        "ผู้แต่ง": {
          "absoluteUrl": "https://gerrit-ci.gerritforge.com/user/thomas.draebing",
          "fullName": "thomas.draebing"
        }
        "authorEmail": "thomas.draebing@sap.com",
        "ความคิดเห็น": "อย่าจัดเรียงข้อความที่ส่งคืนโดยเจนกินส์ \ n การเรียงลำดับข้อความเจนกินส์จะส่งกลับหลังจากตรวจสอบการเปลี่ยนแปลง \ nd ไม่ทำงานอีกต่อไปเนื่องจากถูกนำไปใช้ในสคริปต์เวิร์กโฟลว์ \ n การเปลี่ยนแปลงนี้จะลบการเรียงลำดับข้อความ \ n เปลี่ยนรหัส: I9cb14308ed354c31fae08e3c7190a7f886f242bf \ n ",
        "วันที่": "2019-10-17 15:30:51 +0200",
        "id": "bdff807f0733ef12975ec1183e09c5527738bd0b",
        "msg": "อย่าจัดเรียงข้อความที่ส่งคืนโดย Jenkins",
        "เส้นทาง": [
          {
            "editType": "แก้ไข",
            "file": "Jenkinsfile"
          }
        ]
      }
      {
        "_class": "hudson.plugins.git.GitChangeSet",
        "impactPaths": [
          "Gerrit หลัก / src / main / java / Main.java"
          "polygerrit-UI / app / พฤติกรรม / GR-เปลี่ยนแปลงตารางพฤติกรรม / GR-เปลี่ยนแปลงตาราง behavior_test.html"
        ]
        "commitId": "607c3f853f4cb489811fa77bfcad7a638fff898e",
        "การประทับเวลา": 1571319729000,
        "ผู้แต่ง": {
          "absoluteUrl": "https://gerrit-ci.gerritforge.com/user/tdraebing",
          "fullName": "Thomas Dräbing"
        }
        "authorEmail": "thomas.draebing@sap.com",
        "ความคิดเห็น": "[อย่ารวม] ทดสอบการวางท่อ \ n กดเพื่อเรียก CI อีกครั้ง \ n เปลี่ยนรหัส: Iea19da3f107f1189ef664e306ed5b3d021628086 \ n",
        "วันที่": "2019-10-17 13:42:09 +0000",
        "id": "607c3f853f4cb489811fa77bfcad7a638fff898e",
        "msg": "[ไม่ต้องรวม] ทดสอบขั้นตอนการสร้าง",
        "เส้นทาง": [
          {
            "editType": "แก้ไข",
            "file": "polygerrit-ui / app / behaviours / gr-change-table-behavior / gr-change-table-behavior_test.html"
          }
          {
            "editType": "แก้ไข",
            "ไฟล์": "gerrit-main / src / main / java / Main.java"
          }
        ]
      }
    ]
    "kind": "git"
  }
}
