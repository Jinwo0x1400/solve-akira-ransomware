### Jinwo0x1400 ###

### How to Build .exe Automatically
## 📦 A. Preparation
- Install PyInstaller if you haven't already:
```
pip install pyinstaller
```

### 🚀 B. Run Build
- In the command prompt (CMD), open the folder where the decryptor_gui.py and decryptor_gui.spec files are, then run:
```
pyinstaller decryptor_gui.spec
```

### 📁 C. Output Results
- Once finished, the .exe file will appear in the folder:
```
dist/akira_decryptor_gui/akira_decryptor_gui.exe
```

## 📝 Additional Tips
- To change the .ico icon:
Add this line to the EXE() section:
```
icon='youricon.ico',
```

- To bundle everything into 1 file:
Add onefile=True to EXE():
```
exe = EXE(
    pyz,
    a. scripts,
    [],
    exclude_binaries=True,
    name='akira_decryptor_gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    onefile=True
)
```
