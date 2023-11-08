import random

def movement():
    while True:
        print("masukkan gerakan: ")
        move = select_movement().upper()
        if move in ["W", "A", "S", "D"]:
            break

    return move

def select_movement():
    '''
    Ubahlah algoritma perpindahan yang dipilih player dengan mengubah fungsi ini.
    Untuk saat ini fungsi masih mengembalikan random
    Keluaran dari fungsi ini adalah arah gerakan player:
        "W" --> player akan berpindah ke atas
        "A" --> player akan berpindah ke kiri
        "S" --> player akan berpindah ke bawah
        "D" --> player akan berpindah ke kanan
    '''
    return random.choice(["W", "A", "S", "D"])