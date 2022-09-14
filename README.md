# PUE-BE
![GitHub pull requests](https://img.shields.io/github/issues-pr/PUE-AI-ChatBot/PUE-BE)
> ** :two_hearts: AI 심리상담 챗봇 PUE **  
>
> 퓨처로이컴퍼니 <br>
> 프로젝트 기간 : 2022.08 ~ <br> <br>
> 힘든 사람은 누구나 ***위로를 받을 수 있는*** <br>
> ***전국민 위로 프로젝트*** AI 챗봇 서비스 <br> 
>

## Goals
자살예방 상담전화의 평균 응대율 ***36.3%...***   
저희 퓨처로이컴퍼니는 상담사 고용 증가만으로는 해결이 어려운 상황에서 챗봇을 통해 상담 응대율을 높이고, 상담사가 고위험군 환자를 효율적으로 상담하는 것이 목적입니다.

## Developers
<div align="left">
    <table border="1">
        <th><a href="https://github.com/chanbyeongee">이병찬</a></th>
        <tr>
            <td>
                <img src="https://github.com/chanbyeongee.png" width='80' />
            </td>
        </tr>
    </table>
</div>


## Environments
<table>
<tr>
 <td align="center">언어</td>
 <td>
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
 </td>
</tr>
<tr>
 <td align="center">IDE</td>
 <td>
    <img src="https://img.shields.io/badge/VisualStudioCode-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white"/>&nbsp </td>
</tr>
<tr>
 <td align="center">프레임워크</td>
 <td>
     <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>&nbsp
 </td>
</tr>
<tr>
 <td align="center">라이브러리</td>
 <td>
  <img src="https://img.shields.io/badge/Socket.io-black?style=for-the-badge&logo=socket.io&badgeColor=010101"/>&nbsp
</tr>
<tr>
 <td align="center">패키지관리</td>
 <td>
    <img src="https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white"/>&nbsp
  </td>
</tr>
<tr>
 <td align="center">협업툴</td>
 <td>
    <img src="https://img.shields.io/badge/ClickUp-7B68EE.svg?style=for-the-badge&logo=ClickUp&logoColor=white"/>&nbsp
    <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white"/>&nbsp
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"/>&nbsp
 </td>
</tr>
</table>


## Project Settings

#### Install pip  dependencies

```bash
> pip install -r requirements.txt
```

#### Start server

```bash
> python3 app.py
```

#### Start in background

```bash
> nohup python3 -u app.py &

//To take look in logs
> tail -f nohup.out

//To shut down server
> lsof -i :5000
> sudo kill -9 <task-pid>
```

## Bug reporting
[Issues](https://github.com/PUE-AI-ChatBot/PUE-BE/issues)

## REFERENCE
You can also see the [**WIKI**](https://github.com/PUE-AI-ChatBot/PUE-BE/wiki).

## LICENSE
