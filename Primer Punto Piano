# Piano Electrónico con Arduino

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

---

## Ejecución

1. Conectar los componentes según el esquema.
2. Cargar el código en Arduino IDE.
3. Presionar los botones para generar sonido.
4. Cubrir la fotocelda para observar cambios en el sistema.
