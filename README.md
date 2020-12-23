# SystemTTL

[![GitHub top language](https://img.shields.io/github/languages/top/m4lal0/SystemTTL?logo=python&style=flat-square)](#)
[![GitHub repo size](https://img.shields.io/github/repo-size/m4lal0/SystemTTL?logo=webpack&style=flat-square)](#)
[![By](https://img.shields.io/badge/By-m4lal0-green?style=flat-square&logo=github)](#)

<p align="center">
┏━━━┓━━━━━━━━━━┏┓━━━━━━━━━┏━━━━┓┏━━━━┓┏┓━━━
┃┏━┓┃━━━━━━━━━┏┛┗┓━━━━━━━━┃┏┓┏┓┃┃┏┓┏┓┃┃┃━━━
┃┗━━┓┏┓━┏┓┏━━┓┗┓┏┛┏━━┓┏┓┏┓┗┛┃┃┗┛┗┛┃┃┗┛┃┃━━━
┗━━┓┃┃┃━┃┃┃━━┫━┃┃━┃┏┓┃┃┗┛┃━━┃┃━━━━┃┃━━┃┃━┏┓
┃┗━┛┃┃┗━┛┃┣━━┃━┃┗┓┃┃━┫┃┃┃┃━┏┛┗┓━━┏┛┗┓━┃┗━┛┃
┗━━━┛┗━┓┏┛┗━━┛━┗━┛┗━━┛┗┻┻┛━┗━━┛━━┗━━┛━┗━━━┛
━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</p>

Script en Python para saber el Sistema Operativo de acuerdo al valor <abbr title="Time To Live">TTL</abbr> de un equipo pasandole como argumento su dirección IP.

El comando ping se puede utilizar para identificar el sistema operativo a través de valores TTL. Los valores TTL predeterminados varían entre los diferentes sistemas operativos, el script identifica los 3 sistemas operativos más populares:

| OS  | TTL  |
| ------------ | ------------ |
| Linux/Unix  | 64 |
| Windows  | 128 |
| Solaris/AIX  | 254 |

### ¿Cómo funciona?

Al script hay que pasarle como argumento la dirección IP del equipo para identificar el sistema operativo:

```shell
$ python3 systemTTL.py <IP>
```

* `IP` -- Dirección IP del equipo a escanear

------------