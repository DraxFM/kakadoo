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
currently, the dropper only works on users that are in the "Administrators" group. this will be addressed soon.

## :large_blue_circle: - Content
- [:100: - Features](#features)
- [:white_check_mark: - Requirements](#requirements)
- [:hammer: - Installing](#installing)
- [:toolbox:  - Usage](#usage)
- [:question:  - Help](#help)
- [Extended Usage](#extendedusage)
- [To Do](#todo)
- [:wave: - Authors](#authors)
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
4. Configure your kakadoo Dropper.
5. See [extended Usage](#extendedusage) for more help.
6. Let kakadoo do the rest.
7. Your file is ready for usage!

---

### <a id="help"></a> :question: - Help

<details>
<summary>1. Python allegedly "not found", Problems with PATH.</summary>
 A common problem lots of users have with this program is not caused by me or my program, it's caused by Python. Upon installing Python you have to select the option "Add python.exe to PATH". Unfortunately this box is **NOT** ticked by default. If you already have 
 Python installed, there's still a way to avoid a reinstallation. You can look up a tutorial on how to manually extend PATH to include Python.
</details>

<details>
<summary>2. ERROR: File not found!</summary>
 This error indicates that files that kakadoo requires, are missing. Reinstall the program and make sure not to tinker with any names or directories of the different kakadoo-installed files.
</details>

<details>
<summary>3. ERROR: File altering detected!</summary>
 This error usually indicates that the user has tampered with kakadoo. Tampering with the file in small ways introduces bugs, which is why this is detected and blocked.
</details>

<details>
<summary>4. UNKNOWN ERROR</summary>
 As the name suggests, this is an unexpected error that should not occur. Report any unknown errors to me. To establish contact, join the Discord Server, which can be found in the Authors Section.
</details>

<details>
<summary>5. What is an executable Payload?</summary>
 An executable Payload is a file that can be interpreted by Windows to run code. The most common example are files with the **.exe** extension, but there are also other extensions that are executable.
</details>

<details>
<summary>6. Why is there a default icon?</summary>
 Using no icon at all, will lead to the resulting file being wrongfully detected as ransomware and raise detection rate by over 20%. If you insist on using no icon at all, specify that you want to add an icon in the Builder and enter in "NONE" (case sensitive!) as the icon path. This is not recommended!
</details>

<details>
<summary>7. File is not there or not working properly when tested?</summary>
 This can obviously be a bug, if there is an error shown, please contact me so I can improve my software. Otherwise, this won't work because of your antivirus. As my files are not fully undetected, your AV might think that you installed a virus (even though you created 
 it) and break it/parts of it or even delete it. To fix this, simply turn off your Antivirus and then create your file or add the file as extension so it doesn't get locked.
</details>

## <a id="extendedusage"></a>Extended Usage

This will describe every possible config further.

* **Wrap Payload using kakadoo**: Initiates kakadoo main program
  * **Payload File**: Expects an [executable Payload](#help); accepts an absolute path or the file name + extension (if file is in same directory as kakadoo.py)
  * **Dropper File Name**: Expects a name without extension; the final file will be called after the given string
  * **Add icon to file**: Accepts "yes" or "y" as positive, anything else as negative; will continue to sub-option if positive
    * **Icon File**: Expects a **.ico** file; accepts an absolute path, the file name or the file name + .ico ectension (if file is in the same directory as kakadoo.py); also accepts "NONE" for no icon at all (NOT RECOMMENDED)
* **Contact**: Lists contacts
* **Help**: Redirects to Github Help subpage

## <a id="todo"></a>To Do

```
- Support non-admin executions !!! (main)
- Support absolute paths with "" (builder)
- Expand Anti-VM (main)
- Expand Anti Diagnostic Tool System (main)
- Obfuscation? (main)
- Add generated/custom password config (main/builder)
- Add version checking (builder)
- Add full cleanup as config (main/builder)
- Add self destruction as config (main/builder)
- Add elevation to critical process as config (main/builder)
- Add independent Payload launch as config (main/builder)
- Check if SubmitSamplesConsent is 2 and don't assume (builder)
- Add custom Payload extraction path (main/builder)
```

## <a id="authors"></a> :wave: - Authors

* [**Drax**](https://github.com/DraxFM) - *Initial Work*

* [**Nassim Asrir**](https://cxsecurity.com/author/Nassim+Asrir/1/) - *UAC Bypass*

**Discord: [draxfm](https://discord.com/users/654343206275907585)**

Need help? Join the [**Discord**](https://discord.gg/sEXECdC3Et)!

## <a id="license"></a> :exclamation: - License

This project is licensed - see the [LICENSE](LICENSE) file for details.
