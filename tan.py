from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ChatRoomAnnouncementContents, OpType, MediaType, ContentType, ApplicationType, TalkException, ErrorCode
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#==============================================================================#
# Login line
nn1 = LINE('')
waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#==============================================================================#
nn1MID = nn1.profile.mid
nn1Profile = nn1.getProfile()
nn1Settings = nn1.getSettings()
#==============================================================================#
nn1Poll = OEPoll(nn1)
nn1MID = nn1.getProfile().mid
admin = [nn1MID]
RfuBot=[nn1MID]
Bot = RfuBot
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','IOSIPAD']
mc = {"wr":{}}
sai = {'wc':{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
msg_dict = {}
temp_flood = {}
DDATE = {}
protectcancel =[]
protectJoin = []
protectInvite = []
protectKick = []
protectQr = []
protectkick = []
protectqr = []
protectjoin = []
protectinvite = []
autocancel = {}
#================================================#
autorejit = {
    "autoJoin":False,
    'autoCancel':{"on":True,"members":3},
}    
spamc = {
    "spamcall": False, 
}
commant = {
     "com":False,
}     
set = {"spamcall": False,"wc":{}}
autobl = {
    "autoblock":True,
    "autoaddf":True, 
}    
welcomes = {
    "Welcome":True, 
    "Wc":False, 
    "lv":False,
    "Leave":True, 
    "wcsti2":False, 
}    
sets = {
    "pictsa":False, 
    "sendpict": {},
    "gpict": False,
    "gilstpict": {},
    "pict": False,
    "ilstpict": {},
    "inv":{},
    "wc":{},
    "leave":{},
    "spamGroup":True, 
    "tagsticker": False,
    "Sticker": False,
    "autoJoinTicket": False,
    "tagkick":False,
    "Api": False,
    "autoLeave":True,
    "changeGroupPicture": [],
    "changePictureProfile": False,
    "autoRead": False,
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "readerSticker": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
}
autolike = {
  "autolike":True
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "วิธีตั้งแทค \n ตั้งแทค ข้อความที่ต้องการ",
    "comment": "ออโต้ไลค์  by   ™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯ ",
    "add": "ยินดีที่ได้รู้จักนะครับ 😃\nรับแอดละน้า. >_<",
    "wctext": "ยินดีต้อนรับเข้ากลุ่มนะครับ 😃",
    "lv": "บ๊ายบาย >< ขอให้เธอโชคดีงับ >_<",
    "b": "🐱 บัญชีนี้ถูกป้องกันด้วย ™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯ ระบบได้บล็อคบัญชีคุณอัตโนมัติ 🐱",
    "m": "🐱 สวัสดี เรามุดลิ้งมานะ 🐱",
}
apalo = {
    "bc":{},
    "bc1":{},
    "bc2":{},
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#66FFFF","t": "#000000"}
sets1 = {'autoCancel':{"on":True,"members":10}}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hnn2o = {
    "savefile": False,
    "namefile": "",
}

user1 = nn1MID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = nn1.getProfile() 
backup = nn1.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = nn1Profile.displayName
settings["myProfile"]["statusMessage"] = nn1Profile.statusMessage
settings["myProfile"]["pictureStatus"] = nn1Profile.pictureStatus
cont = nn1.getContact(nn1MID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = nn1.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = nn1Profile.statusMessage
ProfileMe["pictureStatus"] = nn1Profile.pictureStatus
coverId = nn1.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("max.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Max2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        nn1.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    nn1.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    nn1.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = nn1.getContact(mid)
    if contact.videoProfile == None:
        nn1.cloneContactProfile(mid)
    else:
        profile = nn1.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        nn1.updateProfile(profile)
        pict = nn1.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = nn1.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = nn1.getProfileDetail(mid)['result']['objectId']
    nn1.updateProfileCoverById(coverId)
def backupProfile():
    profile = nn1.getContact(nn1MID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = nn1.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = nn1.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        nn1.updateProfileAttribute(8, profile.pictureStatus)
        nn1.updateProfile(profile)
    else:
        nn1.updateProfile(profile)
        pict = nn1.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = nn1.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    nn1.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        nn1.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = nn1.getGroup(msg.to).name
    sd = nn1.waktunjir()
    nn1.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = nn1.getContact(to)
        profile = nn1.profile
        profileName = nn1.profile
        profileStatus = nn1.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        nn1.updateProfile(profileName)
        nn1.updateProfile(profileStatus)
        profile.pictureStatus = nn1.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if nn1.getProfileCoverId(to) is not None:
            nn1.updateProfileCoverById(nn1.getProfileCoverId(to))
        nn1.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return nn1.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        nn1.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
#----------------------------------------------------------------------------#  
