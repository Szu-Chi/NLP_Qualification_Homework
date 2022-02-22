# NLP Qualification Homework
## Environment
OS：Ubuntu 20.04.3 LTS  
Python版本：3.8.10 

## How to use
### step 1: Check OS and Python Version
```
lsb_release -a
python3 --version
```
### step 2: Installing Packages
```
sudo apt install python3-pip
pip install --user -r ./requirements.txt
```

### step 3: Installing Microsoft Edge and webdriver
```
sudo apt update
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main"
sudo apt install microsoft-edge-stable
wget https://msedgedriver.azureedge.net/98.0.1108.56/edgedriver_linux64.zip
unzip edgedriver_linux64.zip
sudo cp ./msedgedriver /usr/bin/
```

### step 4: Check Packages Installed
```
pip list | grep -E "tensorflow|ckiptagger|gdown|bs4"
```

### step 5: Download resource file for CKIP
```
python3 CKIP_data_download.py 
```

### step 6: Scraping News
```
python3 NLP_Qualification_Homework.py
```
