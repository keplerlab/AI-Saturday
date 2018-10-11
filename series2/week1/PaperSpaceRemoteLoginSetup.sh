printf "Starting setup of Paperspace Remote Login\n"
printf "Enter public IP address of paperdspace machine\n"
read -r ipadd

cd $home
if [ ! -d ".ssh" ]; then
  mkdir .ssh
  printf '.ssh directory deleted\n'
else
  rm -r .ssh
  mkdir .ssh
  printf '.ssh directory deleted and created again\n'
fi
cd .ssh
printf 'Moved to .ssh directory\n\n'

ssh-keygen -f 'id_rsa' -N '' 

ssh-copy-id -i ~/.ssh/id_rsa.pub paperspace@$ipadd

printf "Creating the Config file\n\n"

echo "Host paperspace
     HostName $ipadd
     IdentityFile ~/.ssh/id_rsa
     # StrictHostKeyChecking no  
     User paperspace
     LocalForward 8888 localhost:8888" >> config

printf "All installation completed. Try logging using ssh paperspace"	 