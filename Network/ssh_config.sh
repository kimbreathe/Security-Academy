## ssh_config.sh
## argument [username] [password] [ssh port]

echo "[+] START"

apt update

apt install -y openssh-server sudo vim net-tools

useradd -m -d "/home/$1" -s /bin/bash "$1"
cp -r /etc/skel/. "/home/$1"
echo "$1:$2" | chpasswd

usermod -aG sudo $1

if ! grep -q "^AllowGroups" /etc/ssh/sshd_config; then
    echo "AllowGroups sudo" | tee -a /etc/ssh/sshd_config > /dev/null
fi

if ! grep -q "^Port $3" /etc/ssh/sshd_config; then
    echo "Port $3" | tee -a /etc/ssh/sshd_config > /dev/null
fi

service ssh restart