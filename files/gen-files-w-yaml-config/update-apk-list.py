#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import yaml
import os

_wwwPath="/usr/local/www/apk"
_confF="./config.yaml"
_apksPath="/files"
_C = None

def genConfig():
  global _C
  with open(_confF, "r") as _f:
    _C = yaml.safe_load(_f)

  _C["files"].clear()
  print ("/i/ config loaded ..")

  _wwwPath = _C["web"]["path"]
  _apkPath = _C["web"]["apksPath"]

  for _apk in os.listdir(_wwwPath + _apksPath):
    if _apk.endswith(".apk") or _apk.endswith(".xapk"):
      _C["files"].append( { "name": "{}".format(_apk), "link": "/files/" + _apk } )

  with open(_confF, "w") as _f:
    yaml.dump(_C, _f)

  print ("/i/ config saved ..")


def genHtml():
  global _C

  html = ""
  for _apk in _C["files"]:
    html += "<li> <a href='{}' >{}</a> </li>\n  ".format(_apk["link"], _apk["name"])

  with open(_C["web"]["indexTmpl"], "r") as _f:
    _indexTmpl = _f.read()

  _indexTmpl = _indexTmpl.replace("--content-", html)

  with open(_C["web"]["index"], "w") as _f:
    _f.write(_indexTmpl)

if __name__ == "__main__":
  genConfig()
  genHtml()
