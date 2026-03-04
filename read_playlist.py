# read_playlist.py
# Reads all items from the DynamoDB Playlist table and prints them.

import boto3

REGION = "us-east-1"
TABLE_NAME = "Playlist"


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_song(song):
    title = song.get("SongTitle", "Unknown Title")
    artist = song.get("Artist", "Unknown Artist")
    genre = song.get("Genre", "Unknown Genre")

    print(f"SongTitle: {title}")
    print(f"Artist   : {artist}")
    print(f"Genre    : {genre}")
    print("-" * 30)


def main():
    print("===== Reading from DynamoDB Playlist =====\n")

    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No songs found. Add items to your Playlist table first.")
        return

    print(f"Found {len(items)} song(s):\n")
    for song in items:
        print_song(song)


if __name__ == "__main__":
    main()