# SystemTTL
Script en Python para saber el Sistema Operativo de acuerdo al valor TTL de una dirección IP

El comando ping se puede utilizar para identificar el sistema operativo a través de valores TTL. Los valores TTL predeterminados varían entre los diferentes sistemas operativos, el script identifica los 3 sistemas operativos más populares:

| OS  | TTL  |
| ------------ | ------------ |
| Linux/Unix  | 64 |
| Windows  | 128 |
| Solaris/AIX  | 254 |

#### ¿Cómo funciona?

Al script hay que pasarle como argumento la dirección IP del equipo que requerimos saber con que sistema operativo cuenta:

`SystemTTL.py <ip>`