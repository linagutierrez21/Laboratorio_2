# Piano con Arduino

---

## Nota Importante

Debido a la falta de disponibilidad del programador **Pickit** y su alto costo, no fue posible implementar el sistema directamente en el microcontrolador **PIC16F887**.

Como alternativa, se utilizó **Arduino UNO**, logrando cumplir con todos los requerimientos funcionales del laboratorio.

---

## Descripción

Este proyecto consiste en el diseño e implementación de un instrumento musical electrónico tipo piano, integrando sensores y actuadores para generar una respuesta interactiva tanto sonora como visual.

Inicialmente, el desarrollo estaba planteado con el microcontrolador **PIC16F887**. Sin embargo, debido a limitaciones en el acceso al programador **Pickit**, se optó por implementar la solución utilizando **Arduino**, permitiendo cumplir los objetivos del laboratorio de manera eficiente.

---

## Componentes Utilizados

- Arduino UNO  
- Buzzer (Piezoeléctrico)  
- LED  
- Fotocelda (LDR)  
- Resistencias (220Ω y 10kΩ)  
- Botones pulsadores  
- Protoboard y cables  

---

## Conexiones

- **Buzzer** → Pin 11  
- **LED (PWM)** → Pin 10  
- **Botones** → Pines 2 a 9 (con `INPUT_PULLUP`)  
- **Fotocelda (LDR)** → A0 (con divisor de voltaje)  

<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/c9ec1ecb-a622-45d6-9cfd-65607d006ba7" />

### Botones (Teclas del piano)

Los botones representan las notas musicales y están conectados de la siguiente forma:

- Botón Do → Pin 2
- Botón Re → Pin 3
- Botón Mi → Pin 4
- Botón Fa → Pin 5
- Botón Sol → Pin 6
- Botón La → Pin 7
- Botón Si → Pin 8
- Botón Do agudo → Pin 9

Todos los botones están configurados en modo INPUT_PULLUP, por lo tanto:

- Un extremo del botón va al pin digital
- El otro extremo va a GND
- Buzzer (Salida de sonido)
- Terminal positivo del buzzer → Pin 11 del Arduino
- Terminal negativo → GND

Este componente es el encargado de generar las notas musicales.

- LED (Indicador visual)
- Ánodo → Pin 10 (PWM)
- Cátodo → Resistencia (220Ω) → GND

El LED cambia su intensidad dependiendo de la luz ambiental.

### Sensor de luz (LDR)

El LDR funciona como divisor de voltaje:

- Un extremo del LDR → 5V
- Otro extremo → Pin A0
- Resistencia de 10kΩ → entre A0 y GND

<img width="1280" height="755" alt="image" src="https://github.com/user-attachments/assets/d9515fb2-01f2-4c7e-9ef2-d4f6b4528780" />

<img width="1280" height="1030" alt="image" src="https://github.com/user-attachments/assets/95ba5980-d311-4f15-a6d4-ce466a6fc4d4" />

---

## Funcionamiento

El sistema opera de la siguiente manera:

- Cada botón representa una nota musical (Do, Re, Mi, etc.).
- Al presionar un botón, se genera un tono en el buzzer.
- La fotocelda (LDR) mide la intensidad de luz del entorno.
- Este valor es procesado mediante el **ADC** del Arduino.
- La señal se utiliza para:
  - Modular la frecuencia del sonido.
  - Controlar la intensidad del LED mediante **PWM**.

### El video del funcionamiento esta  montado en la Raiz
---

## Conceptos Aplicados

- Conversión Analógico-Digital (ADC)  
- Modulación por Ancho de Pulso (PWM)  
- Lectura de entradas digitales  
- Generación de señales (tone)  
- Modulación de señal  

---

## Resultados

- Generación de notas musicales mediante botones  
- Control de intensidad del LED según luz ambiental  
- Modulación del sonido en tiempo real  
- Integración de sensores y actuadores  

