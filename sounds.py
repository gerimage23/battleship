import subprocess


def play_sound(file):
    subprocess.Popen(['aplay', '-q', file])


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
    play_sound("sounds/player_win.wav")
