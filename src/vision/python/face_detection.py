# -*- coding: utf-8 -*-
#こちらの記事より
#http://qiita.com/bluemooninc/items/075a658f0d2c7ac62efc

import requests
import json
import base64
import os

GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='
API_KEY = os.environ.get('GOOGLE_API')
print(API_KEY)

def goog_cloud_vison (image_content):
    api_url = GOOGLE_CLOUD_VISION_API_URL + API_KEY
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': image_content
            },
            'features': [{
                'type': 'FACE_DETECTION',
                'maxResults': 1
            }]
        }]
    })

    res = requests.post(api_url, data=req_body)
    return res.json()

def img_to_base64(filepath):
    with open(filepath, 'rb') as img:
        img_byte = img.read()
    base64.b64encode(img_byte)
    base64_bytes = base64.b64encode(img_byte)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string


def get_descs_from_return(res_json):
    labels = res_json['responses'][0]['faceAnnotations']
    descs = []
    for value in labels:
        descs.append(value)

    return json.dumps(descs)

def update_json_file(json_desc):
    fname = './face_detection.json'
    if os.path.isfile(fname)==True:
        with open('./face_detection', 'r') as f:
            f_desc = json.load(f)
    else:
        f_desc = ''

    if json_desc != f_desc:
        with open('./face_detection', 'w') as f:
            json.dump(json_desc, f, sort_keys=True, indent=4)
        return True
    else:
        return False

##
## main
##
dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dir, '../../../img/faces/2008_001322.jpg')
print(filename)
img = img_to_base64(filename)
res_json = goog_cloud_vison(img)
json_desc = get_descs_from_return(res_json)
print(json_desc)
update_json_file(json_desc)



