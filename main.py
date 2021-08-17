import os

from google.cloud import translate_v2 as translate
from ruamel import yaml
from ruamel.yaml.comments import CommentedMap, CommentedSeq
from ruamel.yaml.scalarstring import DoubleQuotedScalarString, SingleQuotedScalarString
import sys


# Google Cloud Translation API で翻訳
def transtate(text):

    if (not isinstance(text, DoubleQuotedScalarString)) and (not isinstance(text, SingleQuotedScalarString)):
        return text

    result = client.translate(text, target_language='ja')
    text = result["translatedText"]
    text = text.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
    print(result["input"] + " ===> " + text)
    return text


# 再起処理で子要素を翻訳していく
def recursive_transtate(yaml_element):

    if isinstance(yaml_element, CommentedSeq):

        return list(map(recursive_transtate, yaml_element))

    elif isinstance(yaml_element, CommentedMap):

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
    loaded_yaml = yaml.round_trip_load(yml, preserve_quotes=True)

# 翻訳
recursive_transtate(loaded_yaml)

target_file_path = os.path.splitext(target_file_path)[0]
target_file_name = os.path.split(target_file_path)[1]

if dest_path == "":
    output_path = target_file_path + "_translated.yml"
else:
    output_path = os.path.dirname(dest_path) + "/" + target_file_name + "_translated.yml"

if os.path.exists(output_path):
    os.remove(output_path)

# output_pathにカキコ
with open(output_path, 'w', encoding="utf-8") as file:
    yaml.round_trip_dump(loaded_yaml, stream=file, allow_unicode=True)
