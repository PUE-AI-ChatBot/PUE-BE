# 💬 PUE-BE
[![Pull Requests](https://img.shields.io/github/issues-pr/PUE-AI-ChatBot/PUE-BE?style=for-the-badge)](https://github.com/PUE-AI-ChatBot/PUE-BE/pulls)
[![GitHub issues](https://img.shields.io/github/issues/PUE-AI-ChatBot/PUE-BE?style=for-the-badge)](https://github.com/PUE-AI-ChatBot/PUE-BE/issues)
![GitHub last commit](https://img.shields.io/github/last-commit/PUE-AI-ChatBot/PUE-BE?style=for-the-badge)
> :two_hearts: **AI 심리상담 챗봇 PUE**  
>
> 퓨처로이컴퍼니 <br>
> 프로젝트 시작 : 2022.08 <br> <br>
> 힘든 사람 누구에게나 ***친구가 되어줄*** <br>
> ***따듯한 위로를 전하는*** AI 챗봇 서비스 <br> 
>

## 🥇 Goals
코로나 블루로 우울감을 호소하는 사람이 많아지자 상담사 고용을 늘렸지만 여전히 응답률이 저조하였습니다. <br>
이를 위해 정보 제공용 챗봇을 뛰어넘어 가벼운 심리 상담이 가능한 챗봇을 만들고자 하였습니다. <br>
상담이 여려운 시간대에도 상담이 가능하며 챗봇 상담의 높은 접근성으로 기존 상담에 대한 인식을 개선하고자 개발하게 되었습니다. <br>

## 🔨 Environments

#### Language 
<img src="https://img.shields.io/badge/python-3.8.1-blue?style=for-the-badge&logo=appveyor">

#### Framework
<img src="https://img.shields.io/badge/flask-2.1.2-black?style=for-the-badge&logo=appveyor">

#### Library
> * Check your socketio version compatibility in [**HERE**](https://flask-socketio.readthedocs.io/en/latest/intro.html#version-compatibility)   
<br>
<img src="https://img.shields.io/badge/flask--restful-0.3.9-red?style=for-the-badge&logo=appveyor"> <img src="https://img.shields.io/badge/flask--socketIO-5.3.0-brightgreen?style=for-the-badge&logo=appveyor"> <img src="https://img.shields.io/badge/flask--SQLAlchemy-2.5.1-orange?style=for-the-badge&logo=appveyor">

### Communication

<img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=white"/>  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>


## File structure
```
│
├─models
│  ├─user         
│  ├─chat        
│  └─statistic
│
├─packages
│  └─pue_AI           //submodule of PUE-AI
│
├─resources
│  ├─chat
│  ├─chatnamespace    //real-time chat resources with SocketIo
│  ├─user
│  ├─statistic
│  └─oauth
│
└──app                //RESTful API server

```

## ⚙️ Project Settings

> **Essential Required dependency's version**
> ```
> python >= 3.8.x
> flask-socketio >= 5.x
> ```

> 

### Install packages dependencies

```bash
> pip install -r requirements.txt
```


### Start server

```bash
python3 app.py
```
  
### Start in background

```bash
nohup python3 -u app.py &

#To take look into logs
tail -f nohup.out

#To shut down server
lsof -i :5000
sudo kill -9 <task-pid>
```
   

## 📜 Auto Setup Feature
> *PUE-AI* is implanted into this project as submodule.   
> It has functions which will setup your environmental variables automatically.   
   
### Environment Variable
**function : setup_environ**
* Initiating with PUE-AI package, it will have set your environment variable first.
```
this_dir, this_filename = os.path.split(__file__)

os.environ['CHATBOT_ROOT'] = this_dir

print("Environment Variable Set Successfully. root: %s" % (os.environ['CHATBOT_ROOT'])) 
```

### Download pretrained weights
**function : download_weights**
* Initiating with PUE-AI package, it will have get weights from this [drive](https://drive.google.com/drive/u/0/folders/1M0t0ngQO-TdjeRYoS69C4ZiAqzbN2fIV).
```
 if not os.path.exists(weight_path+"/Emo_weights") :
        os.makedirs(weight_path+"/Emo_weights")

    if not os.path.isfile(weight_path+"/Emo_weights/Emo_weights.index") or Emo_flag:
        print("Downloading Emo pretrained index...")
        output = weight_path+"/Emo_weights/Emo_weights.index"
        gdown.download(loaded["EMO-index-url"], output, quiet=False)
```

## 📜 Model and Resources description
> **Detailed descripions are in our [WIKI](https://github.com/PUE-AI-ChatBot/PUE-BE/wiki).**

### DB Models
> Managed and Controlled with SQLAchemy    
#### User
* User's personal information table
* Relationships(has 2 child table)
   * Chat table(child) : chatlog
   * Statistic table(child) : number of user's daily emotion   
#### Chat
* User's chatbot logs(encrypted) 
* Relationships(has 1 parent table)
   * User table(parent)    
#### Statistic
* User's number of user's daily emotion logs(encrypted) 
* Relationships(has 1 parent table)
   * User table(parent)     
### Resources
> Apis coming through endpoints are processed by (RESTful)resources
#### Authorization
* User must have JWT to idenify their account.   
#### Find by day range
* Every resources have range method, which can get charts in multiple sqeuntial dates.   
```
#request url example
curl --location --request GET 'http://133.186.215.54:5001//stat/latest/20220910/before/7'
```
```
#response example in statistic resource.
{
    "isSummary": true,
    "summary": {
        "total": 0,
        "emotions": {
            "불만": 0,
            "중립": 1,
            "당혹": 0,
            "기쁨": 0,
            "걱정": 0,
            "질투": 0,
            "슬픔": 1,
            "죄책감": 0,
            "연민": 0
        }
    },
    "statistics": [
        {
            "date": "20220906",
            "chart": {
                "total": 0,
                "emotions": {
                    "불만": 0,
                    "중립": 1,
                    "당혹": 0,
                    "기쁨": 0,
                    "걱정": 0,
                    "질투": 0,
                    "슬픔": 0,
                    "죄책감": 0,
                    "연민": 0
                }
            }
        },
        {
            "date": "20220908",
            "chart": {
                "total": 0,
                "emotions": {
                    "불만": 0,
                    "중립": 0,
                    "당혹": 0,
                    "기쁨": 0,
                    "걱정": 0,
                    "질투": 0,
                    "슬픔": 1,
                    "죄책감": 0,
                    "연민": 0
                }
            }
        }
    ]
}
```
#### Find by number
* Every resources have number method, which can get charts in past sqeuntial dates.   
```
#request url example
curl --location --request GET 'http://133.186.215.54:5001//chats/latest/20220910235700/number/4'
```
```
#response example in statistic resource.
{
  "chats": [
    {
      "day": "20220910",
      "time": "235645",
      "direction": "BOT",
      "utterance": "네, 좋은 밤 되세요."
    },
    {
      "day": "20220910",
      "time": "235640",
      "direction": "USER",
      "utterance": "내일 봐!"
    },
    {
      "day": "20220908",
      "time": "020030",
      "direction": "BOT",
      "utterance": "무슨 일이 있으신가요??"
    },
    {
      "day": "20220908",
      "time": "020022",
      "direction": "USER",
      "utterance": "나 우울해..."
    }
  ]
}
```
   
   
## 📚 Documentations

- [Branch Strategy](https://github.com/PUE-AI-ChatBot/PUE-BE/wiki/Branch-Strategy)

- [Git Convention](https://github.com/PUE-AI-ChatBot/PUE-BE/wiki/Git-Convention)

- [Coding Convention](https://github.com/PUE-AI-ChatBot/PUE-BE/wiki/Coding-Convention)

- [Workflow](https://github.com/PUE-AI-ChatBot/PUE-BE/wiki/Wokflow)


## 🔒 LICENSE

Preparing... 
