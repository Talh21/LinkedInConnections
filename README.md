# LinkedInConnections :robot:
This tool will help you to grow your network and mange your invitations!

If you just created your LinkedIn account, or you does not have enough connections(as you should) this tool is just for you.
Making connections is a core fundamental of LinkedIn(500+ is recommended). With more first-degree connections, the more second-degree and third-degree connections you have, 
and more connections means more people Will be exposed to your posts, and you will be more often comes up in the search results.

## Features
1. **Auto pilot :airplane:** - add as much connections as you want(according to Linkedin policy) through the "network page" - it will add connections based on the LinkedIn      suggestions algoritm.

2. **Search by keyword :mag_right:** - add connections based on keywords given by the user.

3. **Withdraw invitations**  

## Instructions & Requirements

1. Make sure you install [WebDriver](https://chromedriver.chromium.org/downloads)
 >Note: Set ChromeDriver path. Change the path according to your ChromeDrive.exe installation path.
 
 
 In settings.py:
 
  ``` 
CHROME_PATH = ''
  ```

2. Also in settings.py edit according to your login credentials
>Note: Please fill in your credentials between the quotation mark

```
    email = ""
    password = ""
```

3. - [selenium](https://pypi.org/project/selenium/)
   - [urllib3](https://pypi.org/project/urllib3/)

## Installation

1. Clone or dowload the repository:
 
     `git clone https://github.com/Talh21/LinkedInConnections.git`
     
 2. Change directory to the folder of the dowloaded program:

     `cd <path>`
     
 3. Install all the requirements:

     `pip install -r requirements.txt`

      **or**

     `pip3 install -r requirements.txt`
     
 4. Run main.py
    
    `python main.py`
