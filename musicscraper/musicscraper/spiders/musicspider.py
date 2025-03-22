import scrapy


class MusicspiderSpider(scrapy.Spider):
    name = "musicspider"
    allowed_domains = ["genius.com"]
    start_urls = ["https://genius.com"]

    def parse(self, response):
        music_links = response.css('a.PageFooterArtistLinks__Link-sc-1918a364-0::attr(href)').getall()
        music_links.sort(reverse=True)
        for link in music_links:
            link = "https://genius.com" + link
            yield scrapy.Request(link, callback=self.parse_artist)

    def parse_artist(self, response):
        artist_list = response.css('a[href*="https://genius.com/artists/"]::text').getall()
        # Guardar en un archivo por orden alfabético
        artist_list.sort()
        with open('artist_list.txt', 'a', encoding='utf-8') as f:
            for artist in artist_list:
                f.write(artist + '\n')


        #artists_links = response.css('a[href*="https://genius.com/artists/"]::attr(href)').getall()
        #for artist_link in artists_links:
            #artist_link = artist_link + "/songs"
            #yield scrapy.Request(artist_link, callback=self.parse_artist_songs)

"""
    def parse_artist_songs(self, response):
        songs_links = response.css('.ListSection-desktop__Content-sc-2bca79e6-7.bmOkxr a::attr(href)').getall()
        for song_link in songs_links:
            yield scrapy.Request(song_link, callback=self.parse_song)

    def parse_song(self, response):
        # Extraer nombre de la canción, albúm, artista, letra, release_date, writters y tags 
        song_name = response.css('span.SongHeader-desktop__HiddenMask-sc-9c2f20c9-11::text').get()
        artist_name = response.css('.PortalTooltip__Trigger-sc-e6affa6e-1.ceEDGa a::text').get()
        album_name = response.css('a.PrimaryAlbum__Title-sc-ed119306-4::text').get()
        yield{
            'song_name': song_name,
            'artist_name': artist_name,
            'album_name': album_name,
        }
"""

  
