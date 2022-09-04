Se ha testeado este script en Parrot-security-5.0.1.

# Instalación
```sh
  git clone https://github.com/kradtoor/auto-i3-polybar
  cd auto-i3-polybar/
  python3 main.py
```

## Preview
![i3](https://i.ibb.co/1d9tzst/Screenshot-at-2022-09-02-19-50-13.png "auto-i3-polybar by KradToor")

## Target
```sh
  settarget  "HTB's IP"
  cleartarget
```

## Utilidades:
- **i3**: Tiling Window Manager.
- **zsh**: Shell.
- **oh-my-zsh**: Oh-My-Zsh.
- **polybar**: Herramienta  para crear barras de estado.
- **polybar-themes**: Temas para la polybar.
- **rofi**: Lanzador de aplicaciones.
- **feh**: Visor de imágenes.
- **fzf**: Buscador de línea de comandos.
- **scripts**: extractPorts, whichSystem.
- **kitty**:  Terminal.

## Shortcuts
<kbd>Windows</kbd> + <kbd>Enter</kbd> : Abre la consola (kitty).  
<kbd>Ctrl</kbd> + <kbd>1,2,3,4,5,6,7,8,9</kbd> : Cambia entre las tabs de la consola (kitty).  
<kbd>Windows</kbd> + <kbd>W</kbd> : Cierra la ventana actual.  
<kbd>Windows</kbd> + <kbd>Alt</kbd> + <kbd>R</kbd> : Reinicia la configuración del bspwm.  
<kbd>Windows</kbd> + <kbd>Alt</kbd> + <kbd>Q</kbd> : Cierrar la sesión.  
<kbd>Windows</kbd> + <kbd>(⬆⬅⬇➡)</kbd> : Moverse por las ventanas en la workspace actual.  
<kbd>Windows</kbd> + <kbdD</kbd> : Abre el Rofi. <kbd>Esc</kbd> para salir.  
<kbd>Windows</kbd> + <kbd>(1,2,3,4,5,6,7,8,9,0)</kbd> : Cambia entre los workspace.  
<kbd>Windows</kbd> + <kbd>T</kbd> : Cambia la ventana actual a modo "terminal" (normal). Nos sirve cuando la ventana está en modo pantalla completa o flotante.  
<kbd>Windows</kbd> + <kbd>M</kbd> : Cambia la ventana actual a modo "completo" (no ocupa la polybar). Presione la mismas teclas para volver a modo "terminal" (normal).  
<kbd>Windows</kbd> + <kbd>F</kbd> : Cambia la ventana actual a modo pantalla completa (ocupa todo incluyendo la polybar).  
<kbd>Windows</kbd> + <kbd>S</kbd> : Cambia la ventana actual a modo "flotante".  
<kbd>Windows</kbd> + <kbd>Alt</kbd> + <kbd>(1,2,3,4,5,6,7,8,9,0)</kbd> : Mueve la ventana actual a otro workspace.  
<kbd>Windows</kbd> + <kbd>Alt</kbd> + <kbd>(⬆⬅⬇➡)</kbd> : Cambia el tamaño de la ventana actual (solo funciona si está en modo terminal o flotante).  
<kbd>Windows</kbd> + <kbd>Ctrl</kbd> + <kbd>(⬆⬅⬇➡)</kbd> : Cambia la posición de la ventana actual (solo funciona en modo flotante).  
<kbd>Windows</kbd> + <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>(⬆⬅⬇➡)</kbd> : Muestra una preselección para luego abrir una aplicación.  
<kbd>Windows</kbd> + <kbd>Ctrl</kbd> + <kbd>Space</kbd> para deshacer la preselección.  
<kbd>Windows</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> para listar elementos del portapapeles (integrado con rofi).  

## Commands:
- **Abrir imagen en el terminal**:
```sh
  kitty +kitten icat /path/to/image/picture.png
```

## Créditos
- Inspirado en [i3-polybar-config](https://github.com/AriosJentu/i3-polybar-config)
- Tomado como referencia de [auto-bspw-polybar](https://github.com/kradtoor/auto-bspwm-polybar)
- Autor: KradToor
