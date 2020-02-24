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
def nn4(to, text):
    s = temp["te"]
    a = temp["t"]
    cover = nn1.getProfileCoverURL(nn1MID)
    warna1 = ("#000000")
    warna2 = ("#FF6600")
    warnanya1 = warna1
    warnanya2 = warna2
    data = {
    "type": "flex",
    "altText": "™TANBOTNEVERDIE✯",
    "contents": {
    "type": "bubble",
    "styles": {
    "body": {
    "backgroundColor":warnanya1
    }
    },    
    "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
    {
    "type": "box",
    "layout": "horizontal",
    "contents": [
    {
    "type": "image",
    "url":  "https://www.img.live/images/2019/09/12/images13.jpg",
    "size":"full",
    "aspectRatio":"20:13",
    "aspectMode":"cover"
    },
    ]
    },
    {
    "type": "separator",
    "color": "#CC0000"
    },
    {
    "type": "text",
    "text": text,
    "color":"#66FFFF",
    "gravity": "center",
    "align":"center",
    "wrap": True,
    "size": "xl"
    },
    {
    "type": "separator",
    "color": "#FF6600"
    },
    {
    "type":"button",
    "style": "primary",
    "height": "sm",
    "color": "#FF6600",
    "action": {
    "type": "uri",
    "label": "สนใจบอทติดต่อ",
    "uri": "line://ti/p/~"+nn1.getProfile().userid,
    }
    },
    ]
    }
    }
    }
    sendTemplate(to,data)        
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(nn1.getContact(nn1MID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus)
        ticket = "https://line.me/ti/p/~steveneverdie002"
        nn1.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nn1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def messageTime():
    global DDATE
    while True:
        date = subprocess.getoutput('date +"%H:%M:%S"')
        for x in DDATE:
            if x == date:
                groups = nn1.getGroupIdsJoined()
                for group in groups:
                    nn1.sendMessage(group, DDATE[x])
       
threads = threading.Thread(target=messageTime)
threads.daemon = True
threads.start()
def nn2(to, text):
    s = temp["te"]
    a = temp["t"]
    cover = nn1.getProfileCoverURL(nn1MID)
    data = {
    "type": "flex",
    "altText": "™TANBOTMEVERDIE✯͜͡❂➣",
    "contents": {
    "type": "bubble",
    "styles": {
    "body": {
    "backgroundColor":a
    }
    },    
    "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
    {
    "type": "box",
    "layout": "horizontal",
    "contents": [
    {
    "type": "image",
    "url":  "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
    "size": "sm",
    },
    {
    "type": "separator",
    "color": "#66FFFF"
    },
    {
    "type": "image",
    "url":  "https://www.img.live/images/2019/09/12/images13.jpg",
    "size": "sm",
    },
    ]
    },
    {
    "type": "separator",
    "color": "#66FFFF"
    },
    {
    "type": "text",
    "text": "™TANBOTNEVERDIE✯͜͡❂➣",
    "color": s,
    "weight": "bold",
    "align":"center",
    "size": "xl"
    },
    {
    "type": "separator",
    "color": "#66FFFF"
    },
    {
    "type":"text",
    "text": " ",
    },
    {
    "type": "text",
    "text": text,
    "color":s,
    "gravity": "center",
    "align":"center",
    "wrap": True,
    "size": "lg"
    },
    {
    "type":"text",
    "text": " ",
    },
    {
    "type":"button",
    "style": "primary",
    "height": "sm",
    "color": "#FF6600",
    "action": {
    "type": "uri",
    "label": "™TANBOTNEVERDIE✯",
    "uri": "line://ti/p/~"+nn1.getProfile().userid,
    }
    },
    ]
    }
    }
    }
    sendTemplate(to,data)        
def nn5(to, text):
    s = temp["te"]
    a = temp["t"]
    warna1 = ("#00FFcc","#FF9999","#009999","#666666","#FF1493","#FFFF00","#50B1493","#66600CC","#00FF00","FF0033")
    warna2 = ("#FF0033","#00FF00","#6600CC","#50B4F5","#FFFF00","#FF1493","#666666","#009999","#FF9999","#00FFcc")
    warnanya1 = random.choice(warna1)
    warnanya2 = random.choice(warna2)
    data = {
    "type": "flex",
    "altText": text,
    "contents": {
    "type": "bubble",
    "styles": {
    "body": {
    "backgroundColor":a
    }
    },
    "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
    {
    "type": "text",
    "text": text,
    "color":s,
    "gravity": "center",
    "wrap": True,
    "size": "sm"
    }
    ]
    }
    }
    }
    sendTemplate(to,data)
def nn3(to, nn3):
    data={
"type": "flex",
"altText": nn3,
"contents": {
"type": "bubble",
"styles": {
"footer": {"backgroundColor": "#000000"},
},
"footer": {
"type": "box",
"layout": "vertical",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
"size": "md"
},
{
"type": "text",
"text": nn3,
"color":"#66FFFF",
"gravity": "center",
"align":"center",
"wrap": True,
"size": "md"
},
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
"size": "md"
},
]
}
]
}
}
}
    sendTemplate(to, data)
#----------------------------------------------------------------------------#    
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "「{}」\nต่ะเอ๋ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(nn1.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        nn1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        nn1.sendMessage(to, "[ INFO ] Error :\n" + str(error))		
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@nn1  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    nn1.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(nn1.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + nn1.getContact("u8b4c22de6d4a1e18190ae14f76465d66").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = nn1.genOBSParams({'oid': nn1MID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = nn1.server.postContent('{}/talk/vp/upload.nhn'.format(str(nn1.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        nn1.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = nn1.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = nn1.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    nn1.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nn1.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nn1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = nn1.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        nn1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nn1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d สัปดาห์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
