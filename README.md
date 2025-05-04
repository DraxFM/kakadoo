> [!CAUTION]
> The only other official source to get kakadoo from is [kakadoo.vercel.app](https://kakadoo.vercel.app)!  
> Do not use this software for malicious purposes! I am not liable for any damages.

> [!NOTE]
> This tool is in early development phase. Bugs and missing features are to be expected.

# kakadoo [BETA]

## Overview

Proof of Concept Python3 non-persistent dropper.  
Only compatible with Windows systems. Tested on Windows 11.

### temporary message
currently, the fact that the exe is compiled with no icon, leads to multiple AVs flagging it down as **ransom.qilra**. using a custom icon lowers the detection from 23 to 11. i will add this feature asap  
adding to that, this only works on users that are in the "Administrators" group. this will also be addressed soon.

## :large_blue_circle: - Content
- [:100: - Features](#features)
- [:white_check_mark: - Requirements](#requirements)
- [:hammer: - Installing](#installing)
- [:toolbox:  - Usage](#usage)
- [:question:  - Help](#help)
- [Extended Usage](#extendedusage)
- [To Do](#todo)
- [:wave: - Authors](#authors)
- [:memo: - Changelog](#changelog)
- [:exclamation: - License](#license)

## <a id="features"></a> :100: - Features

- Builder :sparkles:
- Privilege Escalation :key:
- Anti-VM (BETA) :round_pushpin:
- Anti-Analysis tools (BETA) :round_pushpin:
- Encrypted Payload :syringe:
- No popups during runtime!
- More to be added! :heavy_plus_sign:

---

### <a id="requirements"></a> :white_check_mark: - Requirements

* [Python](https://www.python.org)
* The latest release of [kakadoo](https://github.com/DraxFM/kakadoo/releases/latest/download/draxfm-kakadoo.zip)

---

### <a id="installing"></a> :hammer: - Installing

1. Install the latest release of [kakadoo](https://github.com/DraxFM/kakadoo/releases/latest/download/draxfm-kakadoo.zip)
2. Extract the **.zip** file in the desired directory.
3. Run "**kakadoo.py**"
4. Wait until missing dependencies are installed.
5. kakadoo is ready for use
6. Enjoy!

---

### <a id="usage"></a> :toolbox: - Usage

1. Get an [executable Payload](#help)
2. Run kakadoo
3. Enter in "1" and press Enter.
4. Paste the path of your payload into the entry field.
5. Let kakadoo do the rest.
6. See [extended Usage](#extendedusage) for more help.
7. Your file is ready for usage!

---

### <a id="help"></a> :question: - Help

#### 1. Python allegedly "not found", Problems with PATH.

A common problem lots of users have with this program is not caused by me or my program, it's caused by Python. Upon installing Python you have to select the option "Add python.exe to PATH". Unfortunately this box is **NOT** ticked by default. If you already have Python installed, there's still a way to avoid a reinstallation. You can look up a tutorial on how to manually extend PATH to include Python.

---

#### 2. What is an executable Payload?

An executable Payload is a file that can be interpreted by Windows to run code. The most common example are files with the **.exe** extension, but there are also other extensions that are executable.

---

#### 3. File is not there or not working properly when tested?

This can obviously be a bug, if there is an error shown, please contact me so I can improve my software. Otherwise, this won't work because of your antivirus. As my files are not fully undetected, your AV might think that you installed a virus (even though you created it) and break it/parts of it or even delete it. To fix this, simply turn off your Antivirus and then create your file or add the file as extension so it doesn't get locked.  

## <a id="extendedusage"></a>Extended Usage

This will describe every possible config further.

* **Wrap Payload using kakadoo**: Initiates kakadoo main program
  * **Payload File**: Expects an [executable Payload](#help); accepts an absolute path or the file Name + extension (if file is in same directory as kakadoo.py)
* **Contact**: Lists contacts
* **Help**: Redirects to Github Help subpage

## <a id="todo"></a>To Do

```
- Add custom icon config !!!
- Support non-admin executions !!!
- Add result file name config
- Expand Anti-VM
- Expand Anti Diagnostic Tool System
- Add generated/custom password config
- Add version checking
- Add full cleanup as config
- Add self destruction as config
- Add elevation to critical process as config
- Add independent Payload launch
- Check if SubmitSamplesConsent is 2 and don't assume (in builder)
- Add custom Payload extraction path
```

## <a id="authors"></a> :wave: - Authors

* [**Drax**](https://github.com/DraxFM) - *Initial Work*

* [**Nassim Asrir**](https://cxsecurity.com/author/Nassim+Asrir/1/) - *UAC Bypass*

**Discord: [draxfm](https://discord.com/users/654343206275907585)**

Need help? Join the [**Discord**](https://discord.gg/sEXECdC3Et)!

## <a id="changelog"></a> :memo: - Changelog

```
05/04/2025 v0.0.1: Released kakadoo BETA
```

## <a id="license"></a> :exclamation: - License

This project is licensed - see the [LICENSE](LICENSE) file for details.
