# google_cloud_api_tools

## goal
google apiを簡単に動かせるスクリプト複数言語で提供
<br>
<br>


## 環境
python,bash
<br>

- 個人でログインする    

```
gcloud auth login
gcloud config set project [PROJECT_ID]
```



```
gcloud config list
gcloud config configurations list
gcloud config configurations create config2
gcloud config set compute/region asia-northeast1
gcloud config set core/project [PROJECT_ID]
```

[リソース管理](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ja&visit_id=636832537130276261-1692010590&rd=1)

    

設定を切り替える場合    

```
gcloud config configurations activate config2
```


このままだとwarningが出るので認証する。

[サービスアカウントキー](https://cloud.google.com/vision/docs/libraries)    
役割なしで作成してください。    


```
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

[例]
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
```

<br>

## 使い方
.bashrcなど環境変数にapi keyを設定。
スクリプトを実行するとjsonが返ってくる。

## サンプル

    export GOOGLE_API="XXXXXXXXXXXXXX"
    python face_detection.py


## テキスト検出サンプル


```
python text_detection.py ../../../img/text/receipt.jpg
```

- 検出結果    


<img src="https://github.com/miyamotok0105/google_cloud_api_tools/blob/master/img/text/receipt_result.jpg" height="500">


## 連絡先
miyamotok0105@gmail.com
<br>

## LICENSE

The MIT License (MIT)
<br>


<br>

