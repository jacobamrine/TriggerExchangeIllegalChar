# Trigger Exchange Illegal Character Warning

A small Python utility for Exchange Online migration cleanup. The script connects
to a mailbox over IMAP and lists mailbox folders, which can trigger Exchange to
send the user a warning email that identifies folders with unsupported
characters in their names.

## Why this exists

During Exchange Online migrations, folders with unsupported characters can block
mailbox moves. In the original migration scenario, some folders
contained `/`, but the migration tooling did not provide a convenient folder
list. Listing the mailbox folders over IMAP prompted Exchange to generate the
warning message needed to identify and rename the affected folders.

## Requirements

- Python 3
- IMAP access enabled for the target mailbox
- Mailbox credentials or an app password, depending on the tenant's
  authentication policy

## Setup

Set the IMAP connection values as environment variables before running the
script.

PowerShell:

```powershell
$env:IMAP_HOSTNAME = "outlook.office365.com"
$env:IMAP_USERNAME = "user@example.com"
$env:IMAP_PASSWORD = "password"
```

## Usage

```powershell
python .\trigger_exchange_warning.py
```

The script prints the folders returned by IMAP. If Exchange detects unsupported
folder characters, the mailbox user should receive a warning email with the
folders that need to be renamed.

## Security Notes

- Prefer temporary credentials or app passwords when possible.
- Rotate or remove any credential used for migration troubleshooting after the
  work is complete.