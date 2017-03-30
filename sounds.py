# import vlc
from pygame import mixer


def play_sound(file):
    # mixer.pre_init(44100, -16, 2, 1024)
    # mixer.init()
    # mixer.music.load(file)
    # mixer.music.play()

    vlc.MediaPlayer(file).play()

    # instance = vlc.Instance()
    # player = instance.media_player_new()

    # # Load the media file
    # media = instance.media_new(file)

    # # Add the media to the player
    # player.set_media(media)

    # player.play()


def intro_sound():
    play_sound("sounds/intro_sound.wav")


def place_ship_sound():
    play_sound("sounds/place_ship.wav")


def wrong_coords_sound():
    play_sound("sounds/wrong_coords.wav")


def shoot_sound():
    play_sound("sounds/shoot.wav")


def hit_sound():
    play_sound("sounds/ship_hit.wav")


def ship_sunk_sound():
    play_sound("sounds/ship_sunk_2.wav")


def computer_wins_sound():
    play_sound("sounds/game_over.wav")


def player_wins_sound():
    play_sound("sounds/player_win")
