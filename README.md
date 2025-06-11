# 🛡️ How to Solve AKIRA Ransomware

> A practical guide and open-source resource for identifying, analyzing, containing, and recovering from AKIRA ransomware attacks.

## 🔍 What is AKIRA Ransomware?

AKIRA is a ransomware variant first identified in 2023 that encrypts files and appends the `.akira` extension. It also leaks stolen data and demands a ransom through Tor-based negotiation.

---

## 📌 Key Features

- 🧬 YARA rules to detect AKIRA patterns.
- 🧪 Python scanner for infected systems.
- 🔐 Documentation for containment and mitigation.
- 📡 Known network indicators and domains.
- 🧯 Recovery and backup strategies.

---

## 📂 Folder Structure

- `tools/`: Scripts and tools (scanner, YARA, etc.)
- `docs/`: Incident response guides and technical notes
- `README.md`: Project overview and instructions
- `LICENSE`: MIT License

---

## ⚠️ Detection

Use our [YARA rules](tools/yara_rules/akira.yar) or the Python [scanner script](tools/scanner/akira_scanner.py) to scan systems for infection indicators.

---

## 🧰 Tools

```bash
# Scan system for AKIRA patterns
python tools/scanner/akira_scanner.py /path/to/scan
```
