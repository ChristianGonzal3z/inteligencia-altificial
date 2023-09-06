# **Practica #1**

## **Nombre:** Christian Zorrilla Gonzalez

## **Matrícula:** 21-SISN-2-070

## **Fecha de entrega:** N/A

1. Cree una tabla Markdown que contenga las columnas nombre, fecha y las columnas con los aportes que necesite (mínimo 2 de cada uno), las entradas deben ser de Warren McCulloch, Walter Pitts, Donald Hebb, Alan Turing, John McCarthy, Marvin Minsky y Artur Samuel. (3 puntos)

| Nombre           | Fecha       | Aporte 1                          | Aporte 2                          |
|------------------|-------------|-----------------------------------|-----------------------------------|
| Warren McCulloch | 1898-1969   | Investigación en neurociencia     | Desarrollo de las redes neuronales |
| Walter Pitts     | 1923-1969   | Contribuciones a la lógica formal | Teoría de las redes neuronales     |
| Donald Hebb      | 1904-1985   | Teoría del aprendizaje hebbiano    | Investigación en psicología       |
| Alan Turing      | 1912-1954   | Fundamentos de la computación      | Descifrado de códigos en la WWII   |
| John McCarthy    | 1927-2011   | Desarrollo de la inteligencia artificial | Lenguajes de programación       |
| Marvin Minsky    | 1927-2016   | Contribuciones a la inteligencia artificial | Robótica                      |
| Artur Samuel     | 1901-1990   | Aprendizaje automático             | Juegos de mesa                     |


---
2. Utilizando Markdown haga una lista con los 3 aportes más relevantes de la tabla anterior y justifique por qué usted considera que son importantes.(2 puntos)

- Investigación en neurociencia por Warren McCulloch: Este aporte es importante porque sentó las bases para comprender el funcionamiento de las redes neuronales en el cerebro, lo cual ha sido fundamental para el desarrollo de la inteligencia artificial y el aprendizaje automático.

- Fundamentos de la computación por Alan Turing: Este aporte es crucial ya que sentó las bases teóricas de la computación moderna. Su trabajo en la máquina de Turing y la noción de algoritmo ha sido fundamental para el desarrollo de la informática y la resolución de problemas computacionales.

- Desarrollo de la inteligencia artificial por John McCarthy: Este aporte es relevante porque McCarthy fue pionero en el desarrollo de la inteligencia artificial como campo de estudio. Sus contribuciones sentaron las bases para el desarrollo de algoritmos y técnicas que permiten a las máquinas realizar tareas que requieren inteligencia humana, lo cual ha tenido un impacto significativo en áreas como la robótica, el procesamiento del lenguaje natural y la visión por computadora.

---
3. Utilizando una celda python haga un codigo que al ejecutarse cree un archivo de texto que tenga la definicion de Inteligencia Artificial que usted considere más acertada y justifique por qué, ademas incluya algunos sucesos recientes en la historia de la inteligencia artificial y su impacto en la sociedad. (3 puntos)

```python
definicion = '''Inteligencia Artificial (IA) es el campo de estudio que se enfoca en la creación de sistemas y programas capaces de realizar tareas que requieren de inteligencia humana. Estos sistemas son capaces de aprender, razonar, planificar, reconocer voz y texto, y tomar decisiones basadas en datos y patrones. La IA busca simular la inteligencia humana en máquinas, permitiendo que estas realicen tareas de manera autónoma y eficiente.'''

sucesos_recientes = '''- Avances en el aprendizaje profundo (deep learning) han permitido grandes avances en áreas como el reconocimiento de imágenes y voz, la traducción automática y los chatbots.
- El desarrollo de sistemas de IA en el campo de la medicina ha permitido diagnósticos más precisos y rápidos, así como el descubrimiento de nuevos tratamientos.
- La IA ha revolucionado la industria automotriz con el desarrollo de vehículos autónomos, que prometen mejorar la seguridad vial y transformar la forma en que nos desplazamos.
- En el ámbito de la atención al cliente, los chatbots y asistentes virtuales han mejorado la experiencia del usuario al brindar respuestas rápidas y personalizadas.
- La IA ha tenido un impacto significativo en el campo financiero, permitiendo el análisis de grandes volúmenes de datos para la toma de decisiones de inversión y la detección de fraudes.
- El desarrollo de robots inteligentes ha transformado la industria manufacturera, permitiendo la automatización de tareas repetitivas y peligrosas.'''

# Crear archivo de texto
with open('definicion_ia.txt', 'w') as archivo:
    archivo.write("Definición de Inteligencia Artificial:\n\n")
    archivo.write(definicion)
    archivo.write("\n\nSucesos recientes en la historia de la Inteligencia Artificial:\n\n")
    archivo.write(sucesos_recientes)

print("Archivo 'definicion_ia.txt' creado exitosamente.")


```
---
4. Utilizando una celda python que lea el archivo creado en la celda anterior, muestre el contenido del archivo en pantalla. (2 puntos)
```python
# Leer archivo de texto
with open('definicion_ia.txt', 'r') as archivo:
    contenido = archivo.read()

# Mostrar contenido en pantalla
print(contenido)

```
---