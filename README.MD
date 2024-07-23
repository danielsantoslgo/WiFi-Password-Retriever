```markdown
# 🔐 WiFi Password Retriever

Este script en Python te permite recuperar la contraseña de una red WiFi en un sistema Linux utilizando `nmcli`.

## 🚀 Comenzando

Sigue estos pasos para configurar y ejecutar el script en tu sistema.

### 📋 Prerrequisitos

Asegúrate de tener `nmcli` instalado en tu sistema. Puedes instalarlo en distribuciones basadas en Debian (como Ubuntu) con el siguiente comando:

```sh
sudo apt install network-manager
```

### 📂 Instalación

1. Clona este repositorio en tu máquina local o descarga el archivo ZIP y extráelo.
   
   ```sh
   git clone https://github.com/tuusuario/wifi-password-retriever.git
   ```

2. Navega al directorio del proyecto.
   
   ```sh
   cd wifi-password-retriever
   ```

### 🛠️ Uso

1. Da permisos de ejecución al archivo:

   ```sh
   chmod +x wifi_password.py
   ```

2. Ejecuta el script con privilegios de superusuario:

   ```sh
   sudo python3 wifi_password.py
   ```

3. Introduce el SSID de la red WiFi cuando se te solicite:

   ```sh
   $ sudo python3 wifi_password.py
   Enter the SSID of the WiFi network: MyWiFiNetwork
   The password for MyWiFiNetwork is: MySecretPassword
   ```

### 📦 Estructura del Proyecto

```
wifi-password-retriever/
├── wifi_password.py
└── README.md
```

### 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

¡Gracias por usar este script! 🌟
```

Este `README.md` incluye todos los pasos necesarios para configurar y ejecutar el script, y está diseñado para ser claro y atractivo utilizando emojis.