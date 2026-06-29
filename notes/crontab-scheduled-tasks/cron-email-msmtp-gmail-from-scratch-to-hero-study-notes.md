# Configure Cron Email with Gmail SMTP using msmtp — From Scratch to Hero

## 1. Goal

The goal of this lab is to configure Linux so that **cron jobs can send email notifications**.

By default, cron can send job output to local mail, but on many systems email will not go to Gmail or an external inbox unless SMTP is configured.

Final result:

```text
msmtp direct email test  ✅
mail command test        ✅
cron MAILTO test         ✅
```

---

## 2. What is cron email?

When a cron job produces output, cron can send that output by email.

Example:

```cron
MAILTO="your-email@gmail.com"

* * * * * echo "Hello from cron at $(date)"
```

If the command produces output, cron sends that output to the address in `MAILTO`.

---

## 3. What is msmtp?

`msmtp` is a lightweight SMTP client.

Simple definition:

> `msmtp` sends email from Linux through an SMTP server such as Gmail SMTP.

Flow:

```text
Linux cron/mail command → msmtp → Gmail SMTP → your Gmail inbox
```

---

## 4. Why do we need msmtp?

Cron itself is not a full email service.

Cron can generate email, but the system needs a mail sender to deliver it outside the machine.

Without SMTP configuration, you may see errors like:

```text
mail: cannot send message: Process exited with a non-zero status
```

`msmtp` solves this by sending mail through Gmail SMTP.

---

## 5. Gmail App Password

A Gmail App Password is **not your normal Gmail password**.

It is a special 16-character password generated from your Google Account for apps like `msmtp`.

Use:

```text
Google App Password ✅
```

Do not use:

```text
Normal Gmail password ❌
```

Important:

```text
Never share your Gmail password or App Password.
Use it only inside your Linux configuration file.
```

---

## 6. Enable 2-Step Verification

Before creating an App Password, your Google Account must have **2-Step Verification enabled**.

Steps:

```text
Google Account
Security
2-Step Verification
Turn it ON
```

After enabling 2-Step Verification, search for:

```text
App passwords
```

---

## 7. Create Gmail App Password

Steps:

```text
Google Account
Security
App passwords
App name: Linux msmtp
Create
```

Google will show a 16-character password.

Example format:

```text
abcd efgh ijkl mnop
```

In Linux config, you can usually write it without spaces:

```text
abcdefghijklmnop
```

---

## 8. Install msmtp packages

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install msmtp msmtp-mta mailutils -y
```

### RHEL/CentOS/Fedora

```bash
sudo dnf install msmtp msmtp-mta mailx -y
```

If `msmtp-mta` is not available:

```bash
sudo dnf install msmtp mailx -y
```

---

## 9. AppArmor prompt during installation

During installation, you may see:

```text
Enable AppArmor support?
<Yes> <No>
```

For a simple learning lab, choose:

```text
No
```

Why?

AppArmor is a security layer. It can restrict programs and sometimes cause permission errors if paths are not allowed.

---

## 10. Configure `/etc/msmtprc`

Open:

```bash
sudo vim /etc/msmtprc
```

Example Gmail SMTP configuration:

```conf
defaults
auth           on
tls            on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
logfile        /var/log/msmtp.log

account        gmail
host           smtp.gmail.com
port           587
from           your-email@gmail.com
user           your-email@gmail.com
password       YOUR_16_CHARACTER_APP_PASSWORD

account default : gmail
```

Replace:

```text
your-email@gmail.com
YOUR_16_CHARACTER_APP_PASSWORD
```

Do not share the password.

---

## 11. Secure the msmtp config file

Run:

```bash
sudo chmod 600 /etc/msmtprc
sudo chown root:root /etc/msmtprc
```

Meaning:

| Command | Meaning |
|---|---|
| `chmod 600` | Only owner can read/write |
| `chown root:root` | Owner and group become root |

---

## 12. Create msmtp log file

Run:

```bash
sudo touch /var/log/msmtp.log
sudo chmod 666 /var/log/msmtp.log
```

Meaning:

| Command | Meaning |
|---|---|
| `touch` | Creates the log file if missing |
| `chmod 666` | Allows writing to the log file |

For production, permissions can be tightened later, but this is simple for lab testing.

---

## 13. Error encountered

Command:

```bash
echo "Test email from Linux msmtp" | mail -s "Cron SMTP Test" your-email@gmail.com
```

Error:

```text
mail: cannot send message: Process exited with a non-zero status
```

### Possible causes

```text
msmtp config problem
mail command not connected to msmtp
wrong App Password
permission issue
TLS certificate path issue
sendmail path issue
```

The best troubleshooting method is to test `msmtp` directly.

---

## 14. Test msmtp directly

Direct test command:

```bash
printf "Subject: msmtp direct test\n\nTest email from Linux msmtp\n" | msmtp your-email@gmail.com
```

Example:

```bash
printf "Subject: msmtp direct test\n\nTest email from Linux msmtp\n" | msmtp kkhalid7631@gmail.com
```

Result:

```text
Email received successfully ✅
```

This proves:

```text
Gmail App Password worked
SMTP authentication worked
TLS worked
msmtp config worked
```

---

## 15. Test mail command

After direct `msmtp` test works, test the `mail` command:

```bash
echo "Hello from mail command" | mail -s "Mail Test" your-email@gmail.com
```

Example:

```bash
echo "Hello from mail command" | mail -s "Mail Test" kkhalid7631@gmail.com
```

Result:

```text
Email received successfully ✅
```

This proves:

```text
mail command is connected to msmtp
sendmail compatibility is working
```

---

## 16. Check sendmail link if mail fails

If `mail` fails, check whether `/usr/sbin/sendmail` points to msmtp.

Commands:

```bash
ls -l /usr/sbin/sendmail
readlink -f /usr/sbin/sendmail
```

Expected result should point to something related to `msmtp`, for example:

```text
/usr/bin/msmtp
```

---

## 17. Test cron email with MAILTO

Edit user crontab:

```bash
crontab -e
```

Add:

```cron
MAILTO="your-email@gmail.com"

* * * * * echo "Hello from cron at $(date)"
```

Example:

```cron
MAILTO="kkhalid7631@gmail.com"

* * * * * echo "Hello from cron at $(date)"
```

Wait one minute.

Result:

```text
Cron email received successfully ✅
```

This proves:

```text
cron MAILTO is working
cron can send output by email
mail + msmtp integration works
```

---

## 18. Stop the every-minute test

After confirming it works, stop the test job.

Run:

```bash
crontab -e
```

Remove or comment this line:

```cron
* * * * * echo "Hello from cron at $(date)"
```

Comment it like this:

```cron
# * * * * * echo "Hello from cron at $(date)"
```

Why?

If you leave it running, Gmail will receive an email every minute.

---

## 19. Production style: email output

If you want cron to email output, do not redirect output to a log file.

Example:

```cron
MAILTO="your-email@gmail.com"

0 2 * * * /opt/scripts/backup.sh
```

If `/opt/scripts/backup.sh` prints output, cron emails it.

---

## 20. Production style: log only, no email

If you want output saved to a log file and no email:

```cron
MAILTO=""

0 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1
```

Meaning:

```text
MAILTO="" = disable cron email
>> /var/log/backup.log = append standard output to log
2>&1 = send errors to the same log file
```

---

## 21. Email vs log redirection

### This sends email

```cron
MAILTO="your-email@gmail.com"

* * * * * echo "Hello from cron at $(date)"
```

Why?

The output is not redirected, so cron sends it to email.

### This saves to log file

```cron
MAILTO="your-email@gmail.com"

* * * * * echo "Hello from cron at $(date)" >> /tmp/cron-test.log 2>&1
```

Why?

Output and errors are redirected to the log file. Cron may not email anything because there is no output left for cron to mail.

---

## 22. Best practice decision table

| Goal | Use |
|---|---|
| Get email when cron prints output | `MAILTO="email"` and no redirection |
| Save all output/errors to log | `>> logfile 2>&1` |
| Disable email completely | `MAILTO=""` |
| Both email and log | Use `tee` or custom script logic |
| Production backup logs | Log file is usually better |
| Critical failure alerts | Email only on failure is better |

---

## 23. Send both email and log using tee

If you want output in log and email, use `tee`.

Example:

```cron
MAILTO="your-email@gmail.com"

0 2 * * * /opt/scripts/backup.sh 2>&1 | tee -a /var/log/backup.log
```

Meaning:

```text
2>&1 = combine error and normal output
tee -a = append output to log and also pass it to cron email
```

---

## 24. Email only on failure

A better production style is to email only when a job fails.

Example:

```cron
MAILTO="your-email@gmail.com"

0 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1 || echo "Backup failed on $(hostname) at $(date)"
```

Meaning:

```text
If backup succeeds: output goes to log
If backup fails: cron emails the failure message
```

---

## 25. Troubleshooting commands

### Check msmtp log

```bash
cat /var/log/msmtp.log
```

### Check msmtp command

```bash
which msmtp
```

### Check mail command

```bash
which mail
```

### Check sendmail link

```bash
ls -l /usr/sbin/sendmail
readlink -f /usr/sbin/sendmail
```

### Check cron service

Ubuntu/Debian:

```bash
systemctl status cron
```

RHEL/CentOS/Fedora:

```bash
systemctl status crond
```

### Check cron logs

Ubuntu/Debian:

```bash
grep CRON /var/log/syslog
```

RHEL/CentOS/Fedora:

```bash
sudo grep CRON /var/log/cron
```

---

## 26. Common errors and fixes

### Error 1: `mail: cannot send message`

Error:

```text
mail: cannot send message: Process exited with a non-zero status
```

Possible fixes:

```bash
cat /var/log/msmtp.log
which msmtp
which mail
ls -l /usr/sbin/sendmail
readlink -f /usr/sbin/sendmail
```

Also test msmtp directly:

```bash
printf "Subject: msmtp direct test\n\nTest email from Linux msmtp\n" | msmtp your-email@gmail.com
```

---

### Error 2: Gmail authentication failed

Possible reason:

```text
Normal Gmail password used instead of App Password
Wrong App Password
2-Step Verification not enabled
```

Fix:

```text
Enable 2-Step Verification
Generate App Password
Use the 16-character App Password in /etc/msmtprc
```

---

### Error 3: Permission denied reading config

Possible reason:

```text
/etc/msmtprc is owned by root and not readable by normal user
```

Fix option A: system-wide config:

```bash
sudo chmod 600 /etc/msmtprc
sudo chown root:root /etc/msmtprc
```

Fix option B: user-specific config:

```bash
vim ~/.msmtprc
chmod 600 ~/.msmtprc
```

---

### Error 4: No cron email received

Possible reasons:

```text
Cron job produced no output
MAILTO is empty
Output was redirected to a log file
Cron service is not running
Email went to spam
```

Fix test:

```cron
MAILTO="your-email@gmail.com"

* * * * * echo "Hello from cron at $(date)"
```

---

### Error 5: Too many cron emails

Reason:

```text
Test job runs every minute
```

Fix:

```bash
crontab -e
```

Comment or remove:

```cron
# * * * * * echo "Hello from cron at $(date)"
```

---

### Error 6: AppArmor prompt confusion

Prompt:

```text
Enable AppArmor support?
```

For learning lab:

```text
Choose No
```

Reason:

```text
Avoid extra permission issues while learning SMTP setup.
```

---

## 27. Final working flow

```text
1. Install msmtp and mailutils
2. Enable Gmail 2-Step Verification
3. Create Gmail App Password
4. Configure /etc/msmtprc
5. Secure /etc/msmtprc
6. Create /var/log/msmtp.log
7. Test msmtp directly
8. Test mail command
9. Test cron MAILTO
10. Stop the every-minute test job
```

---

## 28. Final command summary

```bash
# Install packages on Ubuntu/Debian
sudo apt update
sudo apt install msmtp msmtp-mta mailutils -y

# Edit msmtp config
sudo vim /etc/msmtprc

# Secure config
sudo chmod 600 /etc/msmtprc
sudo chown root:root /etc/msmtprc

# Create log file
sudo touch /var/log/msmtp.log
sudo chmod 666 /var/log/msmtp.log

# Direct msmtp test
printf "Subject: msmtp direct test\n\nTest email from Linux msmtp\n" | msmtp your-email@gmail.com

# mail command test
echo "Hello from mail command" | mail -s "Mail Test" your-email@gmail.com

# Edit crontab
crontab -e
```

Cron test:

```cron
MAILTO="your-email@gmail.com"

* * * * * echo "Hello from cron at $(date)"
```

Stop test:

```cron
# * * * * * echo "Hello from cron at $(date)"
```

---

## 29. Final summary

```text
cron = runs scheduled jobs
MAILTO = tells cron where to email output
mail = command used to send email
msmtp = SMTP client that sends email through Gmail SMTP
Gmail App Password = special password for SMTP authentication
```

Golden rule:

```text
If cron output is not redirected, cron can email it.
If output is redirected to a log file, cron usually has nothing to email.
Use MAILTO="" when you want no email.
Use logs for production history.
Use email for alerts.
```

---

## 30. Lab success proof

The lab was successful because these emails arrived:

```text
msmtp direct test
Mail Test
Cron <user@host> echo "Hello from cron..."
```

This confirms:

```text
Gmail SMTP authentication worked
msmtp worked
mail command worked
cron MAILTO worked
```
