# SystemTTL

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

#### ¿Cómo funciona?

Al script hay que pasarle como argumento la dirección IP del equipo para identificar su sistema operativo:

```shell
$ python3 SystemTTL.py <IP>
```

* `IP` -- IP del equipo a escanear

------------