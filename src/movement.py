import random

def movement(player):
    while True:
        print("Chosen move: ", end="")
        move = select_movement(player).upper()
        if move in ["W", "A", "S", "D"]:
            print(move)
            break

    return move

def logic_gate(tile_1, tile_2):
    stench = tile_1[0] and tile_2[0]
    breeze = tile_1[1] and tile_2[1]
    return not (stench or breeze)

def select_movement(player):
    '''
    Keluaran dari fungsi ini adalah arah gerakan player:
        "W" --> player akan berpindah ke atas
        "A" --> player akan berpindah ke kiri
        "S" --> player akan berpindah ke bawah
        "D" --> player akan berpindah ke kanan
    '''

    # delete element current tile di player.tile_need_to_be_checked
    # kemudian append neighbor dari current tile untuk dicek (only yang belum ada di percept_space)
    if (player.x, player.y) in player.tile_need_to_be_checked:
        # check safe nya gasi, kalau iya gaperlu update
        player.tile_need_to_be_checked.remove((player.x, player.y))
        if (player.x-1,player.y) not in player.percept_space and player.x-1 > 0 and (player.x-1,player.y) not in player.tile_need_to_be_checked:
            player.tile_need_to_be_checked.append((player.x-1,player.y))
        if (player.x,player.y-1) not in player.percept_space and player.y-1 > 0 and (player.x,player.y-1) not in player.tile_need_to_be_checked:
            player.tile_need_to_be_checked.append((player.x,player.y-1))
        if (player.x+1,player.y) not in player.percept_space and (player.x+1,player.y) not in player.tile_need_to_be_checked:
            player.tile_need_to_be_checked.append((player.x+1,player.y))
        if (player.x,player.y+1) not in player.percept_space and (player.x,player.y+1) not in player.tile_need_to_be_checked:
            player.tile_need_to_be_checked.append((player.x,player.y+1))
    
    elif (player.x, player.y) == player.prev_coor: # kasus Player tidak bergerak
        try:
            player.tile_need_to_be_checked.pop(-1)
        except: # kasus ingin pop array tapi sudah tidak ada yg dicari (sehingga bergerak random)
            return random.choice(["W", "A", "S", "D"])
    
    else: # kasus player hanya lewat
        pass

    # check apakah belum ada knowledge mengenai tile yang sekarang
    if (player.x,player.y) not in player.percept_space:
        safe = True if not player.percept['stench'] and not player.percept['breeze'] else False
        # update self.safe_or_not
        if (player.x,player.y) not in player.safe_or_not:
            player.safe_or_not[(player.x,player.y)] = safe
        elif not player.safe_or_not[(player.x,player.y)]:
            player.safe_or_not[(player.x,player.y)] = safe
        if (player.x-1,player.y) not in player.safe_or_not:
            player.safe_or_not[(player.x-1,player.y)] = safe
        elif not player.safe_or_not[(player.x-1,player.y)]:
            player.safe_or_not[(player.x-1,player.y)] = safe
        if (player.x+1,player.y) not in player.safe_or_not:
            player.safe_or_not[(player.x+1,player.y)] = safe
        elif not player.safe_or_not[(player.x+1,player.y)]:
            player.safe_or_not[(player.x+1,player.y)] = safe
        if (player.x,player.y-1) not in player.safe_or_not:
            player.safe_or_not[(player.x,player.y-1)] = safe
        elif not player.safe_or_not[(player.x,player.y-1)]:
            player.safe_or_not[(player.x,player.y-1)] = safe
        if (player.x,player.y+1) not in player.safe_or_not:
            player.safe_or_not[(player.x,player.y+1)] = safe
        elif not player.safe_or_not[(player.x,player.y+1)]:
            player.safe_or_not[(player.x,player.y+1)] = safe
        # update percept_space
        player.percept_space[(player.x,player.y)] = [player.percept['stench'], player.percept['breeze']]

        # kasus special: cek diagonalnya untuk membuat another safe tile
        if (player.x-1,player.y-1) in player.percept_space:
            if not player.safe_or_not[(player.x-1,player.y)]:
                player.safe_or_not[(player.x-1,player.y)] = logic_gate(player.percept_space[(player.x,player.y)], player.percept_space[(player.x-1,player.y-1)])
            if not player.safe_or_not[(player.x,player.y-1)]:
                player.safe_or_not[(player.x,player.y-1)] = logic_gate(player.percept_space[(player.x,player.y)], player.percept_space[(player.x-1,player.y-1)])
        if (player.x+1,player.y-1) in player.percept_space:
            if not player.safe_or_not[(player.x+1,player.y)]:
                player.safe_or_not[(player.x+1,player.y)] = logic_gate(player.percept_space[(player.x,player.y)], player.percept_space[(player.x+1,player.y-1)])
            if not player.safe_or_not[(player.x,player.y-1)]:
                player.safe_or_not[(player.x,player.y-1)] = logic_gate(player.percept_space[(player.x,player.y)], player.percept_space[(player.x+1,player.y-1)])
        if (player.x+1,player.y+1) in player.percept_space:
            if not player.safe_or_not[(player.x+1,player.y)]:
                player.safe_or_not[(player.x+1,player.y)] = logic_gate(player.percept_space[(player.x,player.y)], player.percept_space[(player.x+1,player.y+1)])
            if not player.safe_or_not[(player.x,player.y+1)]:
                player.safe_or_not[(player.x,player.y+1)] = logic_gate(player.percept_space[(player.x,player.y)], player.percept_space[(player.x+1,player.y+1)])
        if (player.x-1,player.y+1) in player.percept_space:
            if not player.safe_or_not[(player.x-1,player.y)]:
                player.safe_or_not[(player.x-1,player.y)] = logic_gate(player.percept_space[(player.x,player.y)], player.percept_space[(player.x-1,player.y+1)])
            if not player.safe_or_not[(player.x,player.y+1)]:
                player.safe_or_not[(player.x,player.y+1)] = logic_gate(player.percept_space[(player.x,player.y)], player.percept_space[(player.x-1,player.y+1)])
        
        # add to be checked dari yang sebelumnya sudah di add via special case
        if (player.x-1,player.y) in player.safe_or_not:
            if player.safe_or_not[(player.x-1,player.y)]:
                if (player.x-1,player.y) not in player.tile_need_to_be_checked:
                    player.tile_need_to_be_checked.append((player.x-1,player.y))
                    print(f'add {(player.x-1,player.y)}')
        if (player.x+1,player.y) in player.safe_or_not:
            if player.safe_or_not[(player.x+1,player.y)]:
                if (player.x+1,player.y) not in player.tile_need_to_be_checked:
                    player.tile_need_to_be_checked.append((player.x+1,player.y))
                    print(f'add {(player.x+1,player.y)}')
        if (player.x,player.y-1) in player.safe_or_not:
            if player.safe_or_not[(player.x,player.y-1)]:
                if (player.x,player.y-1) not in player.tile_need_to_be_checked:
                    player.tile_need_to_be_checked.append((player.x,player.y-1))
                    print(f'add {(player.x,player.y-1)}')
        if (player.x,player.y+1) in player.safe_or_not:
            if player.safe_or_not[(player.x,player.y+1)]:
                if (player.x,player.y+1) not in player.tile_need_to_be_checked:
                    player.tile_need_to_be_checked.append((player.x,player.y+1))
                    print(f'add {(player.x,player.y+1)}')
    
    else: # kasus hanya lewat
        pass

    try:
        while not player.safe_or_not[player.tile_need_to_be_checked[-1]]:
            player.tile_need_to_be_checked.pop(-1)
        player.prev_coor = (player.x, player.y)
        if player.x < player.tile_need_to_be_checked[-1][0] and player.safe_or_not[(player.x+1,player.y)]:
            return "S"
        elif player.x > player.tile_need_to_be_checked[-1][0] and player.safe_or_not[(player.x-1,player.y)]:
            return 'W'
        elif player.y < player.tile_need_to_be_checked[-1][1] and player.safe_or_not[(player.x,player.y+1)]:
            return 'D'
        elif player.y > player.tile_need_to_be_checked[-1][1] and player.safe_or_not[(player.x,player.y-1)]:
            return 'A'
        else:
            choices = []
            if player.safe_or_not[(player.x+1,player.y)]:
                choices.append("S")
            if player.safe_or_not[(player.x-1,player.y)]:
                choices.append("W")
            if player.safe_or_not[(player.x,player.y+1)]:
                choices.append("D")
            if player.safe_or_not[(player.x,player.y-1)]:
                choices.append("A")
            # ubah prioritas pencarian karena lokasi tersebut sementara sulit untuk dicapai player
            player.tile_need_to_be_checked = player.tile_need_to_be_checked[-1] + player.tile_need_to_be_checked[:-1]
            return random.choice(choices)

    except: # kondisi yang tidak dapat diselesaikan KBS, yaitu gold dikelilingi wilayah yang not safe, sehingga bot harus melakukan gerakan random
        print(player.tile_need_to_be_checked)
        return random.choice(["W", "A", "S", "D"])
    
    