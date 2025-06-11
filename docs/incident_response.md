# 🚨 Incident Response: AKIRA Ransomware

## 1. Immediate Containment

- Disconnect infected machines from the network.
- Block Tor-related outbound connections.
- Isolate backups if not yet affected.

## 2. Identification

- Look for `.akira` file extensions.
- Check for ransom notes usually named `akira_readme.txt`.

## 3. Forensics

- Collect memory dumps.
- Retrieve logs (Sysmon, Event Viewer).
- Identify C2 communications.
