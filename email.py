#Jacob Amrine 5/16/22
#I started writing this script for the email SMTP migration to 365 because the mailboxes had the illegal
#character "/" in a couple of the folders. This uses SMTP though, so ironically it cant even list said folders.
#It does trigger the Exchange warning though, which will generate a list of the illegal folders and send it to the users inbox.
#From there, you can re-name the folders.

import email
import imaplib

hostname = "hostname.net"
username = "username@hostname.net"
password = "Password1" #Reset this after use - I promise it wasnt actually Password1

root_folders = []
svr = imaplib.IMAP4_SSL(hostname)
svr.login(username, password)
svr.select('inbox')
response, folders = svr.list('""', '*')

rv, data = svr.search(None, "ALL")
test, folders = svr.list('""', '*')
print(folders)
