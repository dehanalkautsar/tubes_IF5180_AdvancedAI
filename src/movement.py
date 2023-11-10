import random

def movement(myPlayer):
    while True:
        print("Chosen move: ", end="")
        move = select_movement(myPlayer).upper()
        if move in ["W", "A", "S", "D"]:
            print(move)
            break

    return move

def select_movement(myPlayer):
    '''
    Ubahlah algoritma perpindahan yang dipilih player dengan mengubah fungsi ini.
    Untuk saat ini fungsi masih mengembalikan random
    Keluaran dari fungsi ini adalah arah gerakan player:
        "W" --> player akan berpindah ke atas
        "A" --> player akan berpindah ke kiri
        "S" --> player akan berpindah ke bawah
        "D" --> player akan berpindah ke kanan
    Silahkan tambahkan atribut/ method di kelas Player jika dibutuhkan, tapi jangan menghapus/ mengganti atribut/ kelas yang sudah ada.
    # return random.choice(["W", "A", "S", "D"])
    '''

    # delete element current tile di myPlayer.tile_need_to_be_checked
    # kemudian append neighbor dari current tile untuk dicek (only yang belum ada di percept_space)
    if (myPlayer.x, myPlayer.y) in myPlayer.tile_need_to_be_checked:
        # check safe nya gasi, kalau iya gaperlu update
        myPlayer.tile_need_to_be_checked.remove((myPlayer.x, myPlayer.y))
        if (myPlayer.x-1,myPlayer.y) not in myPlayer.percept_space and myPlayer.x-1 > 0 and (myPlayer.x-1,myPlayer.y) not in myPlayer.tile_need_to_be_checked:
            myPlayer.tile_need_to_be_checked.append((myPlayer.x-1,myPlayer.y))
        if (myPlayer.x,myPlayer.y-1) not in myPlayer.percept_space and myPlayer.y-1 > 0 and (myPlayer.x,myPlayer.y-1) not in myPlayer.tile_need_to_be_checked:
            myPlayer.tile_need_to_be_checked.append((myPlayer.x,myPlayer.y-1))
        if (myPlayer.x+1,myPlayer.y) not in myPlayer.percept_space and (myPlayer.x+1,myPlayer.y) not in myPlayer.tile_need_to_be_checked:
            myPlayer.tile_need_to_be_checked.append((myPlayer.x+1,myPlayer.y))
        if (myPlayer.x,myPlayer.y+1) not in myPlayer.percept_space and (myPlayer.x,myPlayer.y+1) not in myPlayer.tile_need_to_be_checked:
            myPlayer.tile_need_to_be_checked.append((myPlayer.x,myPlayer.y+1))
    
    elif (myPlayer.x, myPlayer.y) == myPlayer.prev_coor: # kasus Player tidak bergerak
        try:
            myPlayer.tile_need_to_be_checked.pop(-1)
        except: # kasus ingin pop array tapi sudah tidak ada yg dicari (sehingga bergerak random)
            return random.choice(["W", "A", "S", "D"])
    
    else: # kasus player hanya lewat
        pass

    # check apakah belum ada knowledge mengenai tile yang sekarang
    if (myPlayer.x,myPlayer.y) not in myPlayer.percept_space:
        safe = True if not myPlayer.percept['stench'] and not myPlayer.percept['breeze'] else False
        # update self.safe_or_not
        myPlayer.safe_or_not[(myPlayer.x,myPlayer.y)] = safe
        if (myPlayer.x-1,myPlayer.y) not in myPlayer.safe_or_not:
            myPlayer.safe_or_not[(myPlayer.x-1,myPlayer.y)] = safe
        if (myPlayer.x+1,myPlayer.y) not in myPlayer.safe_or_not:
            myPlayer.safe_or_not[(myPlayer.x+1,myPlayer.y)] = safe
        if (myPlayer.x,myPlayer.y-1) not in myPlayer.safe_or_not:
            myPlayer.safe_or_not[(myPlayer.x,myPlayer.y-1)] = safe
        if (myPlayer.x,myPlayer.y+1) not in myPlayer.safe_or_not:
            myPlayer.safe_or_not[(myPlayer.x,myPlayer.y+1)] = safe
        # update percept_space
        myPlayer.percept_space[(myPlayer.x,myPlayer.y)] = [myPlayer.percept['stench'], myPlayer.percept['breeze']]
    
    else: # kasus hanya lewat
        pass

    # print(myPlayer.x)
    # print(myPlayer.y)
    # print(myPlayer.tile_need_to_be_checked)
    # pergi ke safe tile yang harus dicek
    # print(myPlayer.safe_or_not[(myPlayer.x+1,myPlayer.y)])
    # print(myPlayer.safe_or_not[(myPlayer.x-1,myPlayer.y)])
    # print(myPlayer.safe_or_not[(myPlayer.x,myPlayer.y+1)])
    # print(myPlayer.safe_or_not[(myPlayer.x,myPlayer.y-1)])
    try:
        while not myPlayer.safe_or_not[myPlayer.tile_need_to_be_checked[-1]]:
            myPlayer.tile_need_to_be_checked.pop(-1)
        myPlayer.prev_coor = (myPlayer.x, myPlayer.y)
        if myPlayer.x < myPlayer.tile_need_to_be_checked[-1][0] and myPlayer.safe_or_not[(myPlayer.x+1,myPlayer.y)]:
            return "S"
        elif myPlayer.x > myPlayer.tile_need_to_be_checked[-1][0] and myPlayer.safe_or_not[(myPlayer.x-1,myPlayer.y)]:
            return 'W'
        elif myPlayer.y < myPlayer.tile_need_to_be_checked[-1][1] and myPlayer.safe_or_not[(myPlayer.x,myPlayer.y+1)]:
            return 'D'
        elif myPlayer.y > myPlayer.tile_need_to_be_checked[-1][1] and myPlayer.safe_or_not[(myPlayer.x,myPlayer.y-1)]:
            return 'A'
    except:
        return random.choice(["W", "A", "S", "D"])
    
    