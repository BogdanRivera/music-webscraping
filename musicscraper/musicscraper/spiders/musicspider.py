import scrapy
import json
import re

class MusicSpider(scrapy.Spider):
    name = "musicspider"
    allowed_domains = ["genius.com"]
    start_urls = ["https://genius.com"]

    def parse(self, response):
        music_links = response.css('a.PageFooterArtistLinks__Link-sc-1918a364-0::attr(href)').getall()
        music_links.sort(reverse=True)
        for link in music_links:
            link = "https://genius.com" + link #Por cada link de artista, se añade el dominio
            yield scrapy.Request(link, callback=self.parse_artist)

        
        with open('./artist_list.txt', 'r', encoding='utf-8') as f:
            artists = f.read().splitlines()
        for artist in artists:
            artist_link = 'https://genius.com/artists/' + artist.lower().replace(' ', '-') + '/songs' #Cambia espacios por guiones y pone todo en minúscula
            yield scrapy.Request(artist_link, callback=self.parse_artist_songs)

    def parse_artist(self, response):
        # Extraer la lista 
        artist_list = response.css('a[href*="https://genius.com/artists/"]::text').getall()
        # Ordenar 
        artist_list.sort()
        # Leer los artistas ya escritos 
        try:
            with open('artist_list.txt', 'r', encoding='utf-8') as f:
                existing_artists = set(f.read().splitlines())  # Evitar duplicados
        except FileNotFoundError:
            existing_artists = set()
        new_artists = set(artist_list)
        # Determinar los artistas únicos
        unique_artists = new_artists - existing_artists
        # Escribe solo los artistas únicos
        with open('artist_list.txt', 'a', encoding='utf-8') as f:
            for artist in sorted(unique_artists):  # Escribir en orden alfabético
                f.write(artist + '\n')

    def parse_artist_songs(self, response):
        songs_links = response.css('.ListSection-desktop__Content-sc-2bca79e6-7.bmOkxr a::attr(href)').getall()

        for song_link in songs_links:
            yield scrapy.Request(song_link, callback=self.parse_song)

    def parse_song(self, response):
        """Extraer nombre de la canción, albúm, artista, letra, release_date, producers y tags"""

        song_name = response.css('[class*="SongHeader-desktop__HiddenMask-sc"]::text').get() #Nombre de la canción
        artist_name = response.css('.PortalTooltip__Trigger-sc-e6affa6e-1.ceEDGa a::text').get() #Nombre del artista
        album_name = response.css('[href *="primary-album"]::text').get() #Nombre del álbum

        # Extraer el contenido de la letra
        # Extraer todas las partes de texto 
        lyrics = response.css('div[data-lyrics-container="true"] *::text').getall()
        # Unir las partes de texto 
        full_lyrics = '\n'.join([line.strip() for line in lyrics if line.strip()])  # Quitar espacios en blanco

        release_date = response.xpath('//div[div[text()="Released on"]]/div[2]/text()').get() #Fecha de lanzamiento

        producers = response.xpath('//div[div[text()="Producers"]]/div//a[contains(@class, "StyledLink-sc-15c685a-0")]/text()').getall() #Productores
        tags = response.css('a.SongTags__Tag-sc-b55131f0-2::text').getall() #Tags

        # Reemplazar caracteres no válidos en la letra
        full_lyrics = re.sub(r'[{}]', lambda x: '\\' + x.group(0), full_lyrics) 

        song_data ={
            'song_name': song_name,
            'artist_name': artist_name,
            'album_name': album_name,
            'lyrics': full_lyrics,
            'release_date': release_date,
            'producers': producers,
            'tags': tags
        }
        with open('songs.json', 'a', encoding='utf-8') as f:
            json.dump(song_data, f, ensure_ascii=False)
            f.write('\n')
            
        yield song_data


  
