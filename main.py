import os
from google.cloud import translate_v2 as translate
import yaml
import sys


# Google Cloud Translation API で翻訳
def transtate(text):
    result = client.translate(text, target_language='ja')
    text = result["translatedText"]
    text = text.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
    print(result["input"] + " ===> " + text)
    return text


# 再起処理で子要素を翻訳していく
def recursive_transtate(yaml_element):

    if isinstance(yaml_element, list):

        return list(map(recursive_transtate, yaml_element))

    elif isinstance(yaml_element, dict):

        for key in yaml_element.keys():

            yaml_element[key] = recursive_transtate(yaml_element[key])

        return yaml_element

    else:
        return transtate(yaml_element)


# client取得
client = translate.Client()

# 引数から、pathを取得
args = sys.argv

if len(args) == 1:
    print("[error]第一引数に対象のファイルのパスを入力してください")
    exit(1)

target_file_path = args[1]

if len(args) == 2:
    dest_path = ""
else:
    dest_path = args[2]

# pathからyamlファイルを読み込む
with open(target_file_path, 'r', encoding="utf-8") as yml:
    loaded_yaml = yaml.safe_load(yml)

# 翻訳
recursive_transtate(loaded_yaml)

target_file_path = os.path.splitext(target_file_path)[0]
output_path = target_file_path + "_translated.yml"

if os.path.exists(output_path):
    os.remove(output_path)

# output_pathにカキコ
with open(output_path, 'w', encoding="utf-8") as file:
    yaml.dump(loaded_yaml, file, allow_unicode=True)
