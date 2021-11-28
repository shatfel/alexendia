# ps2exe

- [ps2exe](#ps2exe)
  - [Установка](#установка)
  - [Запуск](#запуск)
  - [Примечания](#примечания)

## Установка

```powershell
Install-Module ps2exe -Repository PSGallery
```

## Запуск

```powershell
[invoke-ps2exe|win-ps2exe|ps2exe]
  -inputFile <inFile>.ps1
  -outputFile <outFile>.exe
  [-version <version>]
  [-title <title>]
  [-description <description>]
  [-copyright <copyright>]
  [-x86]
  [-x64]
  [-noConsole]
  [-noError]
  [-noOutput]
```

## Примечания

1. Если не рабоатет из консоли, то только win-ps2exe (GUI) может помочь (тестил на Win10)
2. При установленном PowerShell 7+ отказался работать в последнем. Видимо, хардкодинг под старую версию или пути в Windows
3. noConsole, noError, noOutput - сильно упростят, если есть консольный (не нужный вывод). Или перенаправляйте в файлы.
