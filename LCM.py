import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.





draw = {}

round = 1
# game loop
while True:
    my_hand = {}
    my_board = {}
    enemy_board = {}
    summon_list = []
    attack_list = []
    min_mana = 100
    best_card = 0
    for i in range(2):
        player_health, player_mana, player_deck, player_rune = [int(j) for j in input().split()]
    opponent_hand = int(input())
    card_count = int(input())
    for i in range(card_count):
        card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw = input().split()
        card_number = int(card_number)
        instance_id = int(instance_id)
        location = int(location)
        card_type = int(card_type)
        cost = int(cost)
        attack = int(attack)
        defense = int(defense)
        my_health_change = int(my_health_change)
        opponent_health_change = int(opponent_health_change)
        card_draw = int(card_draw)
        

        if round <= 30 and cost < min_mana:
            best_card = i
            min_mana = cost
        else:
            if location == 0:
                my_hand[i] = card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw
            elif location == 1:
                my_board[i] = card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw
            else:
                if 'G' in abilities:
                    enemy_board[i] = card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw

    # Write an action using print
    
    if round <= 30:
        print("PICK " + str(best_card));
        round += 1
    else:
        round += 1
        

        nothing_to_do = False
        while not(nothing_to_do):
            nothing_to_do = True
            best_card = -1
            best_card_mana = 100
            can_attack = False
            for i in list(my_hand):

                card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw = my_hand[i]

                if cost < best_card_mana and cost <= player_mana:
                    best_card = instance_id
                    if 'C' in abilities:
                        can_attack = True
                    best_card_mana = cost
                    nothing_to_do = False
                    my_hand.pop(i)
            if(best_card > -1):
                summon_list += [best_card]
                if can_attack:
                    print("here",file=sys.stderr)
                    print(attack_list,file=sys.stderr)
                    attack_list += [(best_card,attack)]
                player_mana -= best_card_mana
        
        for j in list(my_board):
            card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw = my_board[j]
            attack_list += [(instance_id,attack)]
        
        
        result = ""
        for k in range(len(summon_list)):
            result += "SUMMON " + str(summon_list[k]) +";"
            
        for i in list(enemy_board):
            l = 0
            card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw = enemy_board[i]
            while defense > 0 and l < len(attack_list):
                print(attack_list,file=sys.stderr)
                result += "ATTACK " + str(attack_list[l][0]) + " " + str(instance_id) + ";"
                defense -= attack_list[l][1]
                attack_list.pop(l)
    
            enemy_board.pop(i)
            
        for k in range(len(attack_list)):
            result += "ATTACK " + str(attack_list[k][0]) + " -1;"
        
        if result == "":
            print("PASS")
        else:
            print(result)

        
        
        
        
        
