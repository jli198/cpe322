# Linux Commands

[Explain Shell Commands](https://explainshell.com/)

```sh
$ cd
# Changes directory to /home/pi

$ cd dirname                # Change directory to dirname
$ cd ..                     # Move up to parent directory
$ cp file1 file2            # Copy file1 and call it file2
$ history                   # Print history list
$ history -c                # Clear history list (-c means clear)
$ ls                        # List files and folders
$ mkdir dirname             # Make directory dirname
$ mv filename new_filename  # Rename file
$ nano filename             # Edit file with GNU nano
$ rm filename               # Remove file
$ rm -rf dirname            # Remove directory and its content (nonempty).
# -f forces deletion without confirmation, -r deletes directory recurisvely including its contents (subdirectories + files)

$ rmdir dirname             # Remove empty directory
$ scrot                     # Take screenshot
$ sudo apt install _        # Install software _
$ sudo apt update           # Update package list index
$ sudo apt full-upgrade     # Upgrade software packages
$ sudo apt autoremove       # Remove software packages
$ sudo nano filename        # Edit file in root directory with GNU nano
$ sudo pip install _        # Install Python package _
$ sudo reboot               # Reboot Raspberry Pi
$ sudo shutdown -h now      # Shutdown Raspberry Pi
$ arp -a                    # Show IP addresses of devices
$ cat filename              # Show file contents
$ df -Th                    # Show disk space usage via time/date in human readable form
$ sudo dmesg                # Display kernel ring buffer messages
$ env                       # List environment variables (PATH)
$ find filename             # Find file in current directory
$ hostname -I               # Show IP address of Raspberry Pi
$ ifconfig                  # Show (network) interfce configuration
$ ip addr show wlan0        # Show IP address on Wi-Fi
$ iwconfig                  # Show wireless configuration
$ lsusb                     # List USB devices
$ man program_name          # Show program_name's manual pages
$ more filename             # Show file one page at time
$ netstat -lntp             # Show network statistics (-l listening sockets, -n numerical address, -p PID)
$ ps                        # Show  running processes
$ pwd                       # Print working directory
$ sudo raspi-config         # Configure Raspberry Pi
$ tar -zxvf file.tar.gz     # Extract files
$ uname -a                  # Information about current kernel
$ vncpasswd                 # Change VNC server password
$ vncserver :1              # Run VNC server on display 1
$ wget http://example.com/file.tar.gz # Download file from link     
```
