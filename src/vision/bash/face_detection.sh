#!/bin/bash
set -ue

BODY=$(cat <<JSON
{
  "requests": {
    "image":{
      "content": "$(base64 ../../../img/faces/2008_001322.jpg)"
    },
    "features": [
      {
        "type": "FACE_DETECTION",
        "maxResults": 1
      }
    ]
  }
}
JSON
)

api_key=$GOOGLE_API

echo $BODY | curl \
  -H "Accept: application/json" \
  -H "Content-type: application/json" \
  -X POST \
  -d @- \
  "https://vision.googleapis.com/v1/images:annotate?key="$api_key
