# **Practica #1**

## **Nombre:** Christian Zorrilla Gonzalez

## **Matricula:** 21-SISN-2-070

## **Fecha de entrega:** N/A

1. Cree una tabla Markdown que contenga las columnas nombre, fecha y las columnas con los aportes que necesite (minimo 2 de cada uno), las entradas deben ser de Warren McCulloch, Walter Pitts, Donald Hebb, Alan Turing, John McCarthy, Marvin Minsky y Artur Samuel. (3 puntos)

| Nombre           | Fecha       | Aporte 1                          | Aporte 2                          |
|------------------|-------------|-----------------------------------|-----------------------------------|
| Warren McCulloch | 1898-1969   | Investigacion en neurociencia     | Desarrollo de las redes neuronales |
| Walter Pitts     | 1923-1969   | Contribuciones a la logica formal | Teoria de las redes neuronales     |
| Donald Hebb      | 1904-1985   | Teoria del aprendizaje hebbiano    | Investigacion en psicologia       |
| Alan Turing      | 1912-1954   | Fundamentos de la computacion      | Descifrado de codigos en la WWII   |
| John McCarthy    | 1927-2011   | Desarrollo de la inteligencia artificial | Lenguajes de programacion       |
| Marvin Minsky    | 1927-2016   | Contribuciones a la inteligencia artificial | Robotica                      |
| Artur Samuel     | 1901-1990   | Aprendizaje automatico             | Juegos de mesa                     |


---
2. Utilizando Markdown haga una lista con los 3 aportes mas relevantes de la tabla anterior y justifique por que usted considera que son importantes.(2 puntos)

- Investigacion en neurociencia por Warren McCulloch: Este aporte es importante porque sento las bases para comprender el funcionamiento de las redes neuronales en el cerebro, lo cual ha sido fundamental para el desarrollo de la inteligencia artificial y el aprendizaje automatico.

- Fundamentos de la computacion por Alan Turing: Este aporte es crucial ya que sento las bases teoricas de la computacion moderna. Su trabajo en la maquina de Turing y la nocion de algoritmo ha sido fundamental para el desarrollo de la informatica y la resolucion de problemas computacionales.

- Desarrollo de la inteligencia artificial por John McCarthy: Este aporte es relevante porque McCarthy fue pionero en el desarrollo de la inteligencia artificial como campo de estudio. Sus contribuciones sentaron las bases para el desarrollo de algoritmos y tecnicas que permiten a las maquinas realizar tareas que requieren inteligencia humana, lo cual ha tenido un impacto significativo en areas como la robotica, el procesamiento del lenguaje natural y la vision por computadora.

---
3. Utilizando una celda python haga un codigo que al ejecutarse cree un archivo de texto que tenga la definicion de Inteligencia Artificial que usted considere mas acertada y justifique por que, ademas incluya algunos sucesos recientes en la historia de la inteligencia artificial y su impacto en la sociedad. (3 puntos)

```python
definicion = '''La Inteligencia Artificial es un campo que crea programas para que las maquinas hagan cosas inteligentes, como aprender, pensar y tomar decisiones.'''

sucesos_recientes = '''
- La IA ha revolucionado la industria automotriz con el desarrollo de vehiculos autonomos, que prometen mejorar la seguridad vial y transformar la forma en que nos desplazamos.
- En el ambito de la atencion al cliente, los chatbots y asistentes virtuales han mejorado la experiencia del usuario al brindar respuestas rapidas y personalizadas.
- El desarrollo de robots inteligentes ha transformado la industria manufacturera, permitiendo la automatizacion de tareas repetitivas y peligrosas.'''

with open('definicion_ia.txt', 'w') as archivo:
    archivo.write("Definicion de Inteligencia Artificial:\n\n")
    archivo.write(definicion)
    archivo.write("\n\nSucesos recientes en la historia de la Inteligencia Artificial:\n\n")
    archivo.write(sucesos_recientes)

print("Archivo 'definicion_ia.txt' creado")

```
---
4. Utilizando una celda python que lea el archivo creado en la celda anterior, muestre el contenido del archivo en pantalla. (2 puntos)
```python

with open('definicion_ia.txt', 'r') as archivo:
    contenido_archivo = archivo.read()

print(contenido_archivo)

```
---