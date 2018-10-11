# SSH client on your laptop/machine
## Windows

Install Git for windows with git bash ( git bash includes ssh client as well as other usefull unix tools) from here 
https://git-scm.com/download/win
Make sure to also install git bash 

## Mac
* Mac OS X already has built in SSH client called terminal

# Paperspace for GPU machine - On cloud

## About
* Paperspace is a **GPU** accelerated cloud platform
* Paperspace login:  https://www.paperspace.com
  * create account
  * :key: save user name and password somewhere where you can find it
  * click on confirmation email to activate account
* Paperspace runs on their own machines (unlike Crestle, which runs on top of AWS)

## Summary of Charges
- STORAGE:   `50 GB ($5/month)` 
- USAGE:  `$0.51/hr` (GPU+)
- PUBLIC IP ADDRESS:  `$3/month` (single static IP address)


## Paperspace Support
- Technical support, email support@paperspace.com


---
## Part I:  Creating a Machine
### Step 1:  Where to start
- click on this link:  https://www.paperspace.com/console/machines

### Step 2:  Create a new machine
- select green button `New Machine`

### Step 3:  Choose region
- pick a data center
- Regions:  there are 3 regions available
   - West Coast (California)
   - East Coast (New York)
   - Europe
- pick the one closest to you; (for me it is East Coast (NYC));  if a region is unavailable, try another region.  (West Coast may be unavailable for some machines).  

### Step 4:  Choose template
- Select `Public Templates`
- Select icon for `fast.ai`


### Step 5:  Choose machine
- there are various machines with charges noted by the hour
- Paperspace is cheaper than Crestle, with fast machines
- if you choose the `$0.65/hr` machine, it may ask you to contact Paperspace asking why (anti-fraud step); let them know it is for **fast.ai** and they will get you up and running
- Machines to choose
  - the **GPU+** `$0.51/hr`

### Step 6:  Choose storage
- note that you pay for storage as soon as you start the machine up
- select `50 GB ($5/month)`
- storage costs are pro-rated (like compute (or "usage") costs) 

### Step 7:  Options
- turn ON `Public IP` (cost is `$3/month`)
- turn OFF `Auto Snapshot` (to save money on doing back-ups)

### Step 8:  Payment
- add in promo code
- add in credit card information (required, even if you have a promo code)

### Step 9:  Create machine
- select `Create your Paperspace` box
- you'll see the new machine "provisioning"
- It will take several hours (4-5 hrs) to receive the confirmation email from Paperspace due to high demand
- you'll receive an email with subject *"Your new Paperspace Linux machine is ready"*
  - a temporary password will be included in that email

Your temporary sign-in password for machine New Machine 1 is: *************

You can ssh into your new machine with the following command:ssh paperspace@184.105.2.222

## DON”T FORGET TO CLOSE THE NOTEBOOKS AND SHUTDOWN THE INSTANCE

# SSH client on your laptop/machine for easy Paperspace access MACOS/UNIX/UBUNTU 
 
### Step 1: Install ssh-copy-id
- If you don't have it already, here's how to install it:
```
apt-get install ssh-copy-id (Unix)

brew install ssh-copy-id (mac) ( Assuming you already have homebrew installed on your Mac) 

```

### Step 2: Ensure public keys are available
- cd into ``~/.ssh`` directory  (~ is home your directory) 
- if you don't have an .ssh directory in your home folder, create it (mkdir .ssh)
- if you don't have an id_rsa.pub file in your .ssh folder, create it (ssh-keygen and hit Enter  3 times)

### Step 3: Copy public key to Paperspace
- replace IP address in syntax below with your own, and run command
```
ssh-copy-id -i ~/.ssh/id_rsa.pub paperspace@184.105.2.222
```

### Step 4: Add Paperspace info to config file
- make sure you are in the right directory
```
cd ~/.ssh
```
- if you don't have a config file, create one. This example creates file using nano editor.
``` If you do not have Nano installed just create an new file config using any text editor 
nano config
```
- add these contents to your config file (replace IP address here with your Paperspace IP address)
### PLEASE NOTE SOME NETWORKS DO NOT ALLOW 8888 PORT ACCESS FROM THEIR INTRANET THIS CONFIG FILE ACTUALLY FORWORDS 8888 PORT FROM PAPERSPACE MACHINE TO YOUR LOCAL MACHINE
```

Host paperspace
     HostName <Your public IP>
     IdentityFile ~/.ssh/id_rsa
     # StrictHostKeyChecking no  
     User paperspace
     LocalForward 8888 localhost:8888
```
- here's the nano command for saving file
   
   ```
   ctrl o
   Enter
   ```

- here's the nano command for exiting a file
  ```
  ctrl x
  ```

- my example of config file
```
% pwd
/Users/<youruserid>/.ssh
% cat config
Host paperspace
     HostName 184.105.2.222
     IdentityFile ~/.ssh/id_rsa
     # StrictHostKeyChecking no  
     User paperspace
     LocalForward 8888 localhost:8888
```

### Step 5: ssh into Paperspace from local computer
```
ssh paperspace
```
- my example

```
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-104-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

Last login: Mon Jan 29 20:53:40 2018 from 10.64.48.1
(fastai) paperspace@psgyqmt1m:~$

```




# SSH client on your laptop/machine for easy Paperspace access WINDOWS Users

STEP 1: 
Install Git for windows with git bash ( git bash includes ssh client as well as other usefull unix tools) from here 
https://git-scm.com/download/win
Make sure to also install git bash 

STEP 2: 
open git bash from right click context menu
- go to your Users home directory using cd ~ 
- create .ssh directory if not there 
- cd into ``~/.ssh directory``  (~ is home your directory) 
- if you don't have an .ssh directory in your home folder, create it (mkdir .ssh)
- if you don't have an id_rsa.pub file in your .ssh folder, create it (ssh-keygen and hit Enter  3 times)

STEP-3: 
### Step 3: Copy public key to Paperspace
- replace IP address in syntax below with your own, and run command
```
ssh-copy-id -i ~/.ssh/id_rsa.pub paperspace@184.105.2.222
```

### Step 4: Add Paperspace info to config file
- make sure you are in the right directory
```
cd ~/.ssh
```
- if you don't have a config file, create one. This example creates file using nano editor.
``` If you do not have Nano installed just create an new file config using any text editor 
nano config
```

### PLEASE NOTE SOME NETWORKS DO NOT ALLOW 8888 PORT ACCESS FROM THEIR INTRANET THIS CONFIG FILE ACTUALLY FORWORDS 8888 PORT FROM PAPERSPACE MACHINE TO YOUR LOCAL MACHINE
```

- add these contents to your config file (replace <Your public IP here> with your Paperspace IP address)

Host paperspace
     HostName <Your public IP>
     IdentityFile ~/.ssh/id_rsa
     # StrictHostKeyChecking no  
     User paperspace
     LocalForward 8888 localhost:8888
```
- here's the nano command for saving file
   
   ```
   ctrl o
   Enter
   ```

- here's the nano command for exiting a file
  ```
  ctrl x
  ```

### Step 5: ssh into Paperspace from local computer using this command 
```
ssh paperspace
```

### STEP 6: Open jupyter notebook : Make sure jupyter notebook is using port 8888 as this is the port we have actually forwarded/tunneled on our local machine 
```
jupyter notebook 
```
copy paste URL ( keep localhost if inside corporate network or behind any firewall, can use public ip if no firewalled home network ) on browser 

### STEP 7 :  CHECK IF any existing session of jupyter notebook is running using : do not open new session if any existing session is running 
```
jupyter notebook list 
```



