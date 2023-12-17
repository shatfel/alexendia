# Генерация html-ки со списком файлов и ссылками на основе YAML-конфига с перегенерацией

## Дерево

```bash
.
├── config.yaml
├── files
│   ├── Carcassonne_v1.10.build.2967.apk
│   ├── index.html
│   ├── Intercepter-NG.2.8.apk
│   ├── MyRecorder v1.01.86.1130 (10140).apk
│   ├── PacketSniffer.apk
│   └── Plus Messenger_v10.2.9.1_v8a_mod_apkdone.com.apk
├── index.html
├── index.html.tmpl
└── update-apk-list.py
```

## Конфиг

Минимальный
```yaml
web:
  apksPath: /files
  index: index.html
  indexTmpl: index.html.tmpl
  path: /usr/local/www/apk

files:
```

## Скрипт

[update-apk-list.py](../../files/gen-files-w-yaml-config/update-apk-list.py)

