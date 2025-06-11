rule Akira_Ransomware {
  strings:
    $ext = ".akira"
  condition:
    any of them
}