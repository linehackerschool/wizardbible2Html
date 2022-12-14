import requests
import re
import chardet
from pprint import pprint
import json
class compile:
    def __init__(self):
        pass
    
    #読み込み
    def fromUrl(self,URL:str):
        #URLから読み込み
        self.text=requests.get(URL).text
    def fromPath(self,path:str):
        #GithubのwizardbibleのPathから読み取り
        jsDelivr="https://cdn.jsdelivr.net/gh/linehackerschool/wizardbible@master/"
        self.text=requests.get(jsDelivr+path).text
    def fromText(self,text:str):
        #テキストを指定
        self.text=text
    
    def parse(self):
        #テキストを読み込み、かつ整形
        text=self.text.replace("\u3000"," ").replace("：",":")+"\r\n  ----"
        brs=text.split("\r\n")
        tmp=[]
        obj={}
        for br in brs:
            if br==brs[0]:
                #1回目ならなら
                arg=br[5:-4]
            if br[0:3]==" --" or br[0:6]=="  ----":
                tmp2=[]
                tmpobj={}
                for tm in tmp:
                    if tm[0:3]=="■0x":
                        tmpobj[tm]=tmp2
                    else:
                        tmp2.append(tm)

                obj[arg]=tmpobj
                tmp=[]
                arg=br[5:-4]
            else:
                tmp.append(br)
        print(obj)
        self.obj=obj
    def html(self):
        obj=self.obj
        html=""
        for i in range(len(obj.keys())):
            key=list(obj.keys())[i]
            v=obj[key]
            html+="<h2>"+key+"</h2>"
            for i2 in range(len(v.keys())):
                key2=list(v.keys())[i2]
                v2=v[key2]
                txt="<br/>".join(v2).replace("x0xXx0xx0xXx0xx0xXx0xx0xXx0xx0xXx0xx0xXx0xx0xXx0xx0xXx0xx0xXx0xx0xXx0xx0xXx0x","</hr>")
                html+=f"<h3>{key2}</h3><p>{txt}</p>"
        return html

