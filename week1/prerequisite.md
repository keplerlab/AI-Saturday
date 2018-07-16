# SSH client on your laptop/machine
## Windows
* https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands/
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
- USAGE:  `$0.65/hr` (P5000)
- PUBLIC IP ADDRESS:  `$3/month` (single static IP address)

Note:  There is a **$15 credit code you can use: `FASTAI6GKZ`**.  **This code is only for fastai students.**  

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
  - the **P5000** `$0.65/hr`

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
```text
Your temporary sign-in password for machine New Machine 1 is: *************

You can ssh into your new machine with the following command:ssh paperspace@184.105.2.222

## DON”T FORGET TO CLOSE THE NOTEBOOKS AND SHUTDOWN THE INSTANCE