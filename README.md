# Music Scraper - Genius.com

Este proyecto es un scraper de datos musicales que extrae información relevante de la página web Genius.com.

## Descripción

El proyecto utiliza la librería Scrapy de Python para realizar web scraping y obtener datos como:

* Nombre de la canción
* Nombre del artista
* Nombre del álbum
* Letra completa de la canción
* Fecha de lanzamiento
* Productores
* Géneros musicales (tags)

Los datos extraídos se guardan en un archivo `songs.json` para su posterior análisis.

## Tecnologías Utilizadas

* **Python:** Lenguaje de programación principal.
* **Scrapy:** Framework de web scraping.
* **Anaconda:** Para la gestión del entorno virtual.

## Requisitos

* Python 3.6+
* Anaconda (opcional, pero recomendado para la gestión del entorno virtual)
* Librerías listadas en `requirements.txt`

## Instalación

1.  Clona el repositorio:

    ```bash
    git clone https://github.com/BogdanRivera/music-webscraping
    ```

2.  Crea un entorno virtual:

    ```bash
    conda create -n music-scraper python=3.8
    conda activate music-scraper
    ```


3. Navega hasta el directorio `musicscraper`:

    ```bash
    cd ./musicscraper
    ```

3.  Instala las dependencias:

    ```bash
    conda install requirements.txt
    ```

## Ejecución

1.  Ejecuta el spider:

    ```bash
    scrapy crawl musicspider
    ```

    Esto iniciará el proceso de web scraping y guardará los datos en `songs.json`.

    En dado caso de que no inicie se deberá ejecutar este comando y posteriormente volver a probar el código anterior:
   ```bash
    conda install scrapy parsel lxml
   ```

## Estructura del Proyecto

* `musicscraper/`: Contiene el código fuente del spider de Scrapy.
    * `musicspider.py`: El spider principal que extrae los datos.
* `requirements.txt`: Lista de dependencias del proyecto.
* `songs.json`: Archivo JSON que almacena los datos extraídos.

## Autor

* Bogdan Rivera



