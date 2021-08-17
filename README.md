# yaml-translater
Google Cloud Translation APIを使ったYamlファイル翻訳するPythonスクリプト
## Setup
サービスアカウントキーの設定(windows)
```
setx GOOGLE_APPLICATION_CREDENTIALS <json_key_path> -m
```
[公式ドキュメント](https://cloud.google.com/translate/docs/setup)
## Requirements
* pyyaml 5.4.1
* google-cloud-translate 2.0.1
## Example
before
```
a: Hello
b:
  a: Good Night
  b: I am Fine
c:
- What are you doing?
- a: Hey Guys!
  b: We have a gift for you
```
after
```
a: こんにちは
b:
  a: おやすみ
  b: 私は元気です
c:
- 何してるの?
- a: やあみんな!
  b: 私たちはあなたへの贈り物を持っています
```
