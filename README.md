# yaml-translater
Google Cloud Translation APIを使ったYamlファイル翻訳するPythonスクリプト
## Example
クォーテーションで囲まれている部分だけ翻訳されます
* before
```
a: false
b:
  a: 'Good Night'
  b: "I am Fine"
c:
- What are you doing?
- a: Hey Guys!
  b: We have a gift for you
```
* after
```
a: false
b:
  a: 'おやすみ'
  b: "私は元気です"
c:
- What are you doing?
- a: Hey Guys!
  b: We have a gift for you
```
## Setup
サービスアカウントキーの設定(windows)
```
setx GOOGLE_APPLICATION_CREDENTIALS <json_key_path> -m
```
[公式ドキュメント](https://cloud.google.com/translate/docs/setup)
## Requirements
* Python 3.9
* pyyaml 5.4.1
* google-cloud-translate 2.0.1
## Usage
```
python main.py <target_file>
```
同じディレクトリに対象ファイル名_translated.ymlが生成されます
