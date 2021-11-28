# Ffmpeg запись видео с экрана в Windows

- [Ffmpeg запись видео с экрана в Windows](#ffmpeg-запись-видео-с-экрана-в-windows)
  - [Запуск](#запуск)

## Запуск

```powershell
ffmpeg `
  -f gdigrab `
  -framerate 30 `
  -i desktop `
  -c:v libx264 `
  -vf "scale=1920:1080,setsar=1" `
  output.mkv
```
