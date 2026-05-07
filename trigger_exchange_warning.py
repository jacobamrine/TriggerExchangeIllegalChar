"""Trigger Exchange Online's illegal folder character warning.

During some Exchange Online migrations, mailboxes can contain folder names with
characters that Exchange cannot migrate cleanly. This script connects to a
mailbox over IMAP and lists the available folders, which can prompt Exchange to
send the affected user a warning email that identifies folders needing cleanup.
"""

import imaplib
import os

HOSTNAME = os.environ["IMAP_HOSTNAME"]
USERNAME = os.environ["IMAP_USERNAME"]
PASSWORD = os.environ["IMAP_PASSWORD"]

svr = imaplib.IMAP4_SSL(HOSTNAME)
svr.login(USERNAME, PASSWORD)
svr.select('inbox')
response, folders = svr.list('""', '*')

rv, data = svr.search(None, "ALL")
test, folders = svr.list('""', '*')
print(folders)

svr.logout()