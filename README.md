# NLP Qualification Homework
## Environment
OS：Ubuntu 20.04.3 LTS  
Python版本：3.8.10 

## How to use
### step 1: Installing Packages
```
sudo apt install python3-pip
pip install --user -r ./requirements.txt
```

### step 2: Installing Microsoft Edge and webdriver
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

### step 3: Check Packages Installed
```
pip list | grep -E "tensorflow|ckiptagger|gdown|bs4"
```

### step 4: Download resource file for CKIP
```
python3 CKIP_data_download.py 
```

### step 5: Scraping News
```
python3 NLP_Qualification_Homework.py
```

