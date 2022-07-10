# Album
def make_album(artist_name, title, songs_number=None):
    album = {
        'artist name': artist_name,
        'title': title
    }
    if songs_number:
        album['songs number'] = songs_number

    return album

album_1 = make_album("Linkin Park", "One more light")
album_2 = make_album("Eminem", "Encore")
album_3 = make_album("the Weeknd", "Starboy", 12)
print(album_1)
print(album_2)
print(album_3)

#User album
def make_album_1(artists_name, titles):
    album = {
        'artist name': artists_name,
        'title': titles
    }
    return album

while True:
    artist_name = input("Enter an artist's name: ")
    titles = input("Enter the title of an album: ")
    print("Enter 'q' to quit the program")
    if artist_name == 'q' or titles == 'q':
        break

    input_albums = make_album(artist_name, titles)
    print(input_albums)



