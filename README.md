

UnixPasscracker is a simple tool to help you crack unix password .

Author: Mbemekou Fred

Requirements:

Python 2.7.x

Install:

sudo apt-get -y install git python-pip

git clone https://github.com/mbemekou/UnixPasscracker.git        </br>

pip install termcolor threading crypt getopt

cd ./UnixPasscracker

chmod +x UnixPasscracker.py

Use:

./UnixPassCracker.py -w <wordlist_file> -f <shadow_file> -t <number of threads>

arguments:
  -f          Insert the file path of the shadow file
  
  -w          Insert the file path of the dictionnary file
  
  -t          Insert the number of threads           
  
                        
Example:

./UnixPassCracker.py -w /usr/share/wordlist/rockyou.txt -f /etc/shadow -t 4

