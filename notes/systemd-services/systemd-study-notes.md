# systemd in Linux 

## 1. One-Line Definition

**systemd** is the main **init system** and **service manager** in most modern Linux distributions. It starts, stops, manages, monitors, and controls Linux services and system processes.

---

## 2. What is systemd?

When a Linux system boots, the Linux kernel starts the first main user-space process. On most modern Linux systems, that process is **systemd**.

systemd usually runs as **PID 1**.

Check PID 1:

```bash
ps -p 1
```

Example output:

```text
PID TTY          TIME CMD
1   ?        00:00:02 systemd
```

That means systemd is the first major process started by the kernel and becomes responsible for starting the rest of the system.

---

## 3. Linux Boot Flow

Simple boot flow:

```text
Power On
  ↓
BIOS / UEFI
  ↓
Bootloader, for example GRUB
  ↓
Linux Kernel
  ↓
systemd
  ↓
Services, login prompt, GUI, networking, applications
```

systemd brings the system from “kernel started” to “ready to use.”

---

## 4. Why Do We Need systemd?

A Linux server has many services that need to start, stop, restart, and run in the background.

Examples:

```text
sshd
nginx
httpd
docker
cron
NetworkManager
firewalld
mariadb
postgresql
```

Without a service manager, the administrator would need to manually start every service.

systemd helps us:

```text
Start services
Stop services
Restart services
Enable services at boot
Disable services from boot
Check service status
View service logs
Handle service dependencies
Restart failed services automatically
Manage system targets
Schedule tasks with timers
```

---

## 5. What is a Service?

A **service** is a background program managed by systemd.

Examples:

```text
nginx.service
sshd.service
docker.service
NetworkManager.service
firewalld.service
httpd.service
```

Usually, we manage services with the `systemctl` command.

---

## 6. What is systemctl?

**systemctl** is the main command-line tool used to control systemd.

Basic syntax:

```bash
systemctl action service-name
```

Example:

```bash
sudo systemctl restart nginx
```

Meaning:

```text
Use systemctl to restart the nginx service.
```

---

## 7. Common systemctl Commands

### Check Service Status

```bash
sudo systemctl status nginx
```

This shows whether the service is running, stopped, failed, enabled, or disabled.

### Start a Service Now

```bash
sudo systemctl start nginx
```

### Stop a Service Now

```bash
sudo systemctl stop nginx
```

### Restart a Service

```bash
sudo systemctl restart nginx
```

Restart is useful after configuration changes.

### Reload a Service

```bash
sudo systemctl reload nginx
```

Reload means the service reloads its configuration without fully stopping. Not every service supports reload.

### Enable a Service at Boot

```bash
sudo systemctl enable nginx
```

This means nginx will start automatically when the system boots.

Important:

```text
enable does not start the service immediately.
```

### Disable a Service from Boot

```bash
sudo systemctl disable nginx
```

Important:

```text
disable does not stop the service immediately.
```

### Enable and Start Together

```bash
sudo systemctl enable --now nginx
```

Meaning:

```text
Start nginx now and also start it automatically at boot.
```

### Disable and Stop Together

```bash
sudo systemctl disable --now nginx
```

Meaning:

```text
Stop nginx now and prevent it from starting automatically at boot.
```

---

## 8. Start vs Enable

| Command | Meaning |
|---|---|
| `start` | Start the service now |
| `stop` | Stop the service now |
| `restart` | Stop and start the service again |
| `reload` | Reload service configuration without full restart |
| `enable` | Start the service automatically at boot |
| `disable` | Do not start the service automatically at boot |

Example:

```bash
sudo systemctl start nginx
```

This starts nginx now, but after reboot it may not start automatically.

```bash
sudo systemctl enable nginx
```

This makes nginx start during future boots, but it may not start right now.

Best combined command:

```bash
sudo systemctl enable --now nginx
```

---

## 9. What is a Unit in systemd?

systemd manages things using **units**.

A **unit** is an object that systemd knows how to manage.

Common unit types:

| Unit Type | Purpose | Example |
|---|---|---|
| `.service` | Manage services | `nginx.service` |
| `.target` | Group of units/system state | `multi-user.target` |
| `.timer` | Schedule tasks | `backup.timer` |
| `.socket` | Socket activation | `docker.socket` |
| `.mount` | Mount filesystem | `home.mount` |
| `.path` | Watch file or directory changes | `example.path` |

Most beginners and Linux admins commonly use:

```text
.service
.target
.timer
```

---

## 10. Where Are systemd Unit Files Stored?

Common locations:

```bash
/etc/systemd/system/
```

Used for custom unit files created by system administrators.

```bash
/usr/lib/systemd/system/
```

Common on RHEL, CentOS, Fedora, and Rocky Linux.

```bash
/lib/systemd/system/
```

Common on Ubuntu and Debian.

| Path | Meaning |
|---|---|
| `/etc/systemd/system/` | Admin-created or custom unit files |
| `/usr/lib/systemd/system/` | Package-installed unit files on RHEL-based systems |
| `/lib/systemd/system/` | Package-installed unit files on Debian/Ubuntu-based systems |

---

## 11. View a Service Unit File

Use:

```bash
systemctl cat nginx
```

For Apache on RHEL:

```bash
systemctl cat httpd
```

This shows the actual unit file used by systemd.

---

## 12. Basic systemd Service File Structure

A service file usually has three main sections:

```ini
[Unit]
[Service]
[Install]
```

### `[Unit]` Section

This section describes the service and its dependencies.

Example:

```ini
[Unit]
Description=My App Service
After=network.target
```

Meaning:

| Directive | Meaning |
|---|---|
| `Description=` | Human-readable service description |
| `After=` | Start this service after the mentioned unit |

### `[Service]` Section

This section tells systemd how to run the service.

Example:

```ini
[Service]
ExecStart=/usr/bin/python3 /opt/app/app.py
Restart=always
```

Meaning:

| Directive | Meaning |
|---|---|
| `ExecStart=` | Command used to start the service |
| `Restart=always` | Restart the service if it stops/fails |

### `[Install]` Section

This section tells systemd when the service should start during boot when enabled.

Example:

```ini
[Install]
WantedBy=multi-user.target
```

Meaning:

```text
Start this service when the system reaches multi-user mode, if the service is enabled.
```

---

## 13. Create Your Own systemd Service

### Step 1: Create a Script

```bash
sudo mkdir -p /opt/myapp
sudo nano /opt/myapp/hello.sh
```

Add this script:

```bash
#!/bin/bash
while true
do
  echo "Hello from systemd at $(date)" >> /var/log/hello-systemd.log
  sleep 10
done
```

Make it executable:

```bash
sudo chmod +x /opt/myapp/hello.sh
```

---

### Step 2: Create the Service File

```bash
sudo nano /etc/systemd/system/hello.service
```

Add:

```ini
[Unit]
Description=Hello systemd demo service
After=network.target

[Service]
ExecStart=/opt/myapp/hello.sh
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

---

### Step 3: Reload systemd

Whenever you create or edit a unit file, run:

```bash
sudo systemctl daemon-reload
```

Meaning:

```text
systemd, reload your unit file definitions.
```

---

### Step 4: Start the Service

```bash
sudo systemctl start hello
```

---

### Step 5: Check Status

```bash
sudo systemctl status hello
```

---

### Step 6: Check the Log File

```bash
sudo tail -f /var/log/hello-systemd.log
```

---

### Step 7: Enable at Boot

```bash
sudo systemctl enable hello
```

Or start and enable together:

```bash
sudo systemctl enable --now hello
```

---

## 14. What is daemon-reload?

`daemon-reload` tells systemd to reload unit file definitions.

Use it after creating or editing files in:

```text
/etc/systemd/system/
```

Example:

```bash
sudo nano /etc/systemd/system/myapp.service
sudo systemctl daemon-reload
sudo systemctl restart myapp
```

Important:

```text
If you edit a unit file but forget daemon-reload, systemd may still use the old version.
```

---

## 15. Logs with journalctl

systemd stores logs using **systemd-journald**.

The command to read those logs is:

```bash
journalctl
```

### View Logs for a Service

```bash
sudo journalctl -u nginx
```

### Follow Logs Live

```bash
sudo journalctl -u nginx -f
```

### Show Recent Logs

```bash
sudo journalctl -u nginx -n 50
```

### Show Logs Since Today

```bash
sudo journalctl -u nginx --since today
```

### Show Logs from Current Boot

```bash
journalctl -b
```

---

## 16. systemctl status Output Explained

Command:

```bash
sudo systemctl status nginx
```

Example output:

```text
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled)
     Active: active (running)
   Main PID: 1234 (nginx)
      Tasks: 3
     Memory: 12.5M
        CPU: 100ms
```

Meaning:

| Line | Meaning |
|---|---|
| `Loaded` | Unit file was found |
| `enabled` | Service starts automatically at boot |
| `disabled` | Service does not start automatically at boot |
| `Active: active (running)` | Service is running |
| `Active: inactive` | Service is stopped |
| `Active: failed` | Service failed |
| `Main PID` | Main process ID of the service |
| `Tasks` | Number of processes/threads |
| `Memory` | RAM used by the service |
| `CPU` | CPU time used |

---

## 17. Common Service States

| State | Meaning |
|---|---|
| `active` | Service is running |
| `inactive` | Service is stopped |
| `failed` | Service tried to start but failed |
| `enabled` | Service starts automatically at boot |
| `disabled` | Service does not start automatically at boot |
| `masked` | Service is completely blocked from starting |

Check if service is active:

```bash
systemctl is-active nginx
```

Check if service is enabled:

```bash
systemctl is-enabled nginx
```

Mask a service:

```bash
sudo systemctl mask nginx
```

Unmask a service:

```bash
sudo systemctl unmask nginx
```

---

## 18. What is a Target?

A **target** is a group of systemd units.

It represents a system state.

Common targets:

| Target | Meaning |
|---|---|
| `poweroff.target` | Shut down the system |
| `rescue.target` | Single-user rescue mode |
| `multi-user.target` | Multi-user command-line mode |
| `graphical.target` | GUI mode |
| `reboot.target` | Reboot the system |

Check default target:

```bash
systemctl get-default
```

Set CLI mode as default:

```bash
sudo systemctl set-default multi-user.target
```

Set GUI mode as default:

```bash
sudo systemctl set-default graphical.target
```

Switch target immediately:

```bash
sudo systemctl isolate multi-user.target
```

---

## 19. systemd Timers

A **timer** is systemd’s way to schedule tasks.

It can be used like cron.

A timer usually has two files:

```text
backup.service
backup.timer
```

### Example Service File

```bash
sudo nano /etc/systemd/system/backup.service
```

```ini
[Unit]
Description=Run backup script

[Service]
Type=oneshot
ExecStart=/opt/scripts/backup.sh
```

### Example Timer File

```bash
sudo nano /etc/systemd/system/backup.timer
```

```ini
[Unit]
Description=Run backup daily

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable the timer:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now backup.timer
```

Check timers:

```bash
systemctl list-timers
```

---

## 20. Troubleshooting systemd Services

When a service fails, follow this flow:

```text
1. Check service status
2. Read service logs
3. Check configuration file
4. Check file permissions
5. Check port conflicts
6. Run daemon-reload if unit file changed
7. Restart service
```

Useful commands:

```bash
sudo systemctl status nginx
sudo journalctl -u nginx -n 50
sudo nginx -t
sudo ss -tulnp
sudo systemctl daemon-reload
sudo systemctl restart nginx
```

For Apache on RHEL:

```bash
sudo systemctl status httpd
sudo journalctl -u httpd -n 50
sudo apachectl configtest
sudo ss -tulnp
sudo systemctl restart httpd
```

---

## 21. Real Admin Examples

### Restart SSH Service

Ubuntu/Debian:

```bash
sudo systemctl restart ssh
```

RHEL/Rocky/AlmaLinux:

```bash
sudo systemctl restart sshd
```

### Enable Docker at Boot

```bash
sudo systemctl enable --now docker
```

### Check Firewall Service

RHEL/Rocky/AlmaLinux:

```bash
sudo systemctl status firewalld
```

### Check NetworkManager

```bash
sudo systemctl status NetworkManager
```

---

## 22. Important Interview Questions

### Q1. What is systemd?

systemd is the init system and service manager used by modern Linux systems to start, stop, monitor, and manage services.

### Q2. What is PID 1?

PID 1 is the first user-space process started by the Linux kernel. On most modern Linux systems, PID 1 is systemd.

### Q3. What is the difference between `start` and `enable`?

`start` runs the service now.

`enable` makes the service start automatically at boot.

### Q4. What is `daemon-reload`?

It reloads systemd unit files after you create or modify them.

### Q5. What is `journalctl`?

`journalctl` is used to view logs collected by systemd-journald.

### Q6. What is a target?

A target is a group of units used to define a system state, such as multi-user mode or graphical mode.

### Q7. What does `systemctl enable --now nginx` do?

It starts nginx immediately and also enables it to start automatically at boot.

### Q8. What does masked mean?

A masked service is completely blocked from starting until it is unmasked.

---

## 23. Quick Command Cheat Sheet

```bash
# Check PID 1
ps -p 1

# Service management
systemctl status nginx
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx

# Boot behavior
sudo systemctl enable nginx
sudo systemctl disable nginx
sudo systemctl enable --now nginx
sudo systemctl disable --now nginx

# Check state
systemctl is-active nginx
systemctl is-enabled nginx

# List units
systemctl list-units
systemctl list-unit-files

# Targets
systemctl get-default
sudo systemctl set-default multi-user.target
sudo systemctl set-default graphical.target

# Logs
sudo journalctl -u nginx
sudo journalctl -u nginx -f
sudo journalctl -u nginx -n 50
journalctl -b

# Unit file changes
sudo systemctl daemon-reload
```

---

## 24. Final Summary

```text
systemd = Linux init system and service manager
systemctl = command used to control systemd
journalctl = command used to read systemd logs
.service = unit file for a service
.target = group of services/system state
.timer = scheduled job
enable = start at boot
start = start now
daemon-reload = reload changed unit files
```

From a Linux Admin and DevOps point of view, systemd is very important because almost every production service is managed by it, including NGINX, Apache, Docker, SSH, databases, monitoring agents, and custom applications.

