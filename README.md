# CHUserChecker
ClubHouse Username Checker

### Installing

Clone it    
  ```sh
  git clone https://github.com/bodresha/CHUserChecker.git
  ```
  
  Install requirements
  ```sh
  pip3 install -r requirements.txt
  ```
  
  ### Usage
  
 ```sh
 python main.py -wordlist users.txt -threading 5 -proxy file.txt
 ```
 
 users.txt = Usernames you need to check if it is taken or not .
 file.txt = Proxies that stored in text file , i do not use this option since never got block from joinclubhouse.com side 
 
 The results of available usernames will be output in file called available.txt
 
 The Red Color Mean Not Available
 The Green Color Mean is Available
 
 ## Contact

Meshal Alenezi aka Bodresha – [@Bodresha](https://twitter.com/Bodresha) – mynamemishal@gmail.com
