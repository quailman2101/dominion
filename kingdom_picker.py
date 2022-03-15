import pandas as pd
import numpy as np
import statistics
import time

def main():
    '''
    Main function controlling the flow of the program.

    '''

    seperator('*-*', 40)
    start = input('Good day Sire.  Would you like to start a game of Dominion? y/n: ').lower()
    if start == 'y':
        time.sleep(1)
        print('Great!  Let\'s start by finding out which sets you have.')
        time.sleep(1)
        seperator()
        owned_sets = get_sets()
        df = create_df(owned_sets)
        kingdom = make_kingdom(df)
        game(kingdom)
        elpw(df)
        print('\nHave a great game!!!')
    else:
        print('Okay, goodbye.')

def seperator(x = '-', y = 80):
    '''
    Seperator function used for aesthetic purposes.
    Args:
    (string) x - The character used for the seperator, defaults to '-'.
    (integer) y - The number of times to repeat the seperator, defaults to 80.
    '''
    print(x * y)

def get_sets():
    '''
    Function creates a list of all Dominion set that the user owns.  If they own
    all cards, it is a quick one question funcion.  If not, we need to go through
    the sets one by one.  Returns the completed list.

    '''

    # List used to hold sets the user indicates they have
    owned_sets = []

    # If they have every Dominion card, populate list with all cards except Base
    all = input('Do you own ALL Dominion cards? y/n: ').lower()
    if all == 'y':
        owned_sets = ['Dominion 1st Edition', 'Dominion 2nd Edition',
        'Intrigue 1st Edition', 'Intrigue 2nd Edition', 'Seaside', 'Prosperity',
        'Alchemy', 'Hinterlands', 'Cornucopia', 'Dark Ages', 'Guilds',
        'Adventures', 'Empires', 'Nocturne', 'Renaissance', 'Menagerie',
        'Promo']

        return owned_sets

    # If they don't have all cards, go through the sets one by one
    dom1 = input('Do you have Dominion 1st Edition? y/n: ').lower()
    if dom1 == 'y':
        owned_sets.append('Dominion 1st Edition')

    dom2 = input('Do you have Dominion 2nd Edition? y/n: ').lower()
    if dom2 == 'y':
        owned_sets.append('Dominion 2nd Edition')

    intr1 = input('Do you have Intrigue 1st Edition? y/n: ').lower()
    if intr1 == 'y':
        owned_sets.append('Intrigue 1st Edition')

    intr2 = input('Do you have Intrigue 2nd Edition? y/n: ').lower()
    if intr2 == 'y':
        owned_sets.append('Intrigue 2nd Edition')

    sea = input('Do you have Seaside? y/n: ').lower()
    if sea == 'y':
        owned_sets.append('Seaside')

    pros = input('Do you have Prosperity? y/n: ').lower()
    if pros == 'y':
        owned_sets.append('Prosperity')

    alc = input('Do you have Alchemy? y/n: ').lower()
    if alc == 'y':
        owned_sets.append('Alchemy')

    hint = input('Do you have Hinterlands? y/n: ').lower()
    if hint == 'y':
        owned_sets.append('Hinterlands')

    corn = input('Do you have Cornucopia? y/n: ').lower()
    if corn == 'y':
        owned_sets.append('Cornucopia')

    dark = input('Do you have Dark Ages? y/n: ').lower()
    if dark == 'y':
        owned_sets.append('Dark Ages')

    guild = input('Do you have Guilds? y/n: ').lower()
    if guild == 'y':
        owned_sets.append('Guilds')

    adv = input('Do you have Adventures? y/n: ').lower()
    if adv == 'y':
        owned_sets.append('Adventures')

    emp = input('Do you have Empires? y/n: ').lower()
    if emp == 'y':
        owned_sets.append('Empires')

    noct = input('Do you have Nocturne? y/n: ').lower()
    if noct == 'y':
        owned_sets.append('Nocturne')

    ren = input('Do you have Renaissance? y/n: ').lower()
    if ren == 'y':
        owned_sets.append('Renaissance')

    mena = input('Do you have Menagerie? y/n: ').lower()
    if mena == 'y':
        owned_sets.append('Menagerie')

    promo = input('Do you have ALL of the Promo cards? y/n: ').lower()
    if promo == 'y':
        owned_sets.append('Promo')


    return(owned_sets)

def create_df(owned_sets):
    '''
    Takes the list of owned sets created earlier and adds specific promo cards
    if needed.  Reads the excel file into a dataframe and filters it so that
    only owned cards are included.
    Args:
    (list) owned_sets - a list of owned Dominion sets created in last function

    '''

    # Read excel file into dataframe and include only owned cards
    cards = pd.read_excel('dominion_cards.xlsx')
    boolean_series = cards.set.isin(owned_sets)
    df = cards[boolean_series]

    # If user indicated they don't have all promos, ask if they have some of them
    if 'Promo' not in owned_sets:
        promos = []
        some = input('Do you have any Promo cards? y/n: ').lower()
        time.sleep(1)
        if some == 'y':
            bm = input('Do you have Black Market? y/n: ').lower()
            if bm == 'y':
                promos.append('Black Market')

            capt = input('Do you have Captain? y/n: ').lower()
            if capt == 'y':
                promos.append('Captain')

            chur = input('Do you have Church? y/n: ').lower()
            if chur == 'y':
                promos.append('Church')

            dism = input('Do you have Dismantle? y/n: ').lower()
            if dism == 'y':
                promos.append('Dismantle')

            env = input('Do you have Envoy? y/n: ').lower()
            if env == 'y':
                promos.append('Envoy')

            gov = input('Do you have Governor? y/n: ').lower()
            if gov == 'y':
                promos.append('Governor')

            prin = input('Do you have Prince? y/n: ').lower()
            if prin == 'y':
                promos.append('Prince')

            saun = input('Do you have Sauna/Avanto? y/n: ').lower()
            if saun == 'y':
                promos.append('Sauna')
                promos.append('Avanto')

            stash = input('Do you have Stash? y/n: ').lower()
            if stash == 'y':
                promos.append('Stash')

            sum = input('Do you have Summon? y/n: ').lower()
            if sum == 'y':
                promos.append('Summon')

            wal = input('Do you have Walled Village? y/n: ').lower()
            if wal == 'y':
                promos.append('Walled Village')

            boolean_series_2 = cards.name.isin(promos)
            df2 = cards[boolean_series_2]

            frames = [df, df2]
            df = pd.concat(frames)

    # Return the dataframe if it isn't empty or quit if it is
    if not df.empty:
        return df
    else:
        print('You\'ll need to buy some cards first and try again.')
        quit()

def make_kingdom(df):
    '''
    Takes the raw dataframe create earlier and removes several cards so that 10
    random kingdom cards can be chosen.
    Args:
    (dataframe) df - raw dataframe created in previous function

    '''
    # Convert cost column to integer
    df = df.convert_dtypes()

    # Remove cards that are not in the supply
    supply = df.in_supply == True
    df_supply = df[supply]

    # Remove Colony, Potion, and Platinum
    cpp = df[(df.name.isin(['Colony', 'Potion', 'Platinum']))]
    cpp_indexes = list(cpp.index.values)

    df_supply = df_supply.drop(labels = cpp_indexes, axis = 0)

    # Remove all buy one Knight, all but one Castle and the second part of split piles if present
    extras = df[(df["type_2"] == 'Castle') | (df["type_3"] == 'Castle') |
                (df["type_3"] == 'Knight') | (df['type_4'] == 'Castle')]
    extras = extras[(extras['name'] != 'Humble Castle') &
                (extras['name'] != 'Dame Anna')]
    extra_indexes = list(extras.index.values)

    splits = df[(df.name.isin(['Avanto', 'Rocks', 'Plunder', 'Fortune',
                'Emporium', 'Bustling Village']))]
    splits_indexes = list(splits.index.values)

    df_supply = df_supply.drop(labels = extra_indexes, axis = 0)
    df_supply = df_supply.drop(labels = splits_indexes, axis = 0)

    # Rename the last Knight and Castle if present
    castle_index = df_supply[df_supply['name']== 'Humble Castle'].index.values
    knight_index = df_supply[df_supply['name']== 'Dame Anna'].index.values

    df_supply.at[castle_index, 'name'] = 'Castles'
    df_supply.at[knight_index, 'name'] = 'Knights'

    # Rename split piles if present
    sauna_index = df_supply[df_supply['name']== 'Sauna'].index.values
    glad_index = df_supply[df_supply['name']== 'Gladiator'].index.values
    cata_index = df_supply[df_supply['name']== 'Catapult'].index.values
    encam_index = df_supply[df_supply['name']== 'Encampment'].index.values
    patr_index = df_supply[df_supply['name']== 'Patrician'].index.values
    sett_index = df_supply[df_supply['name']== 'Settlers'].index.values

    df_supply.at[sauna_index, 'name'] = 'Sauna/Avanto'
    df_supply.at[glad_index, 'name'] = 'Gladiator/Fortune'
    df_supply.at[cata_index, 'name'] = 'Catapult/Rocks'
    df_supply.at[encam_index, 'name'] = 'Encampment/Plunder'
    df_supply.at[patr_index, 'name'] = 'Patrician/Emporium'
    df_supply.at[sett_index, 'name'] = 'Settlers/Bustling Village'

    # At last our dataframe is ready to work with.  Pick 10 random cards
    kingdom = df_supply.sample(n = 10)
    return kingdom

def game(kingdom):
    '''
    Takes the completed Kingdom dataframe and gives the player the cards names
    and other info.
    Args:
    (dataframe) kingdom - the 10 card dataframe created previously

    '''

    # Sort the kingdom dataframe and print out the cards and their sets
    print('\n\n')
    seperator()
    print('Excellent Sire.  Your victory awaits!  These are the Kingdom cards.')
    seperator('~')
    seperator('~')

    kingdom.sort_values(by=['set','name'], inplace=True)
    print(kingdom[['name', 'set', 'cost']].to_string(index=False))
    print(f'\nThe average card cost is {statistics.fmean(kingdom.cost)}.')
    seperator()
    time.sleep(1)

    # Check if Colony, Platinum and Shelters should be added
    counts = kingdom['set'].value_counts()

    if 'Prosperity' in counts:
        if counts['Prosperity'] >= 5:
            print('\nYou are looking pretty Prosperous.  Lets add Colonies and Platinum this game.\n')
            time.sleep(1)
    if 'Dark Ages' in counts:
        if counts['Dark Ages'] == 10:
            print('\nThings are looking pretty Dark.  You should replace starting Estates with Shelters.\n')
            time.sleep(1)

    # Identify any cards that must be added to the game
    called_card_list = kingdom['called_cards'].unique().dropna()
    called_card_string = ', '.join(called_card_list)
    called_card_set = set(called_card_string.split(', '))

    if len(called_card_set) > 1:
        print('Some additional cards are needed for this game:')
        for card in called_card_set:
            print(card)
        seperator()
        time.sleep(1)

    # Identify any tokens or mats needed for the game
    token_list = kingdom['associated_token'].unique().dropna()
    mat_list = kingdom['associated_mat'].unique().dropna()

    if token_list:
        print('You need the following tokens too: ')
        for token in token_list:
            print(token)
        seperator()
        time.sleep(1)

    if mat_list:
        print('Don\'t forget the mats you need: ')
        for mat in mat_list:
            print(mat)
        seperator()
        time.sleep(1)

def elpw(df):
    '''
    Takes the original dataframe from all owned cards and adds up to two Events,
    Landmarks, Projects, or Ways to the game, if any are owned.
    Args:
    (datafram) df - the raw dataframe created in a previous function
    '''
    elpw = df[(df.type.isin(['Event', 'Landmark', 'Project', 'Way']))]
    if not elpw.empty:
        type_list = elpw['type'].unique()
        seperator()
        print('\nIt looks like you have the following card types we can add too: ')
        for type in type_list:
            print(type)

        num_to_add = input('\nWould you like to add 0, 1, or 2?  0/1/2: ')
        if num_to_add == '1' or num_to_add == '2':
            print('\nOkay, lets add the following card(s):\n')
            added_elpw = elpw.sample(n = int(num_to_add))
            print(added_elpw[['name', 'type']].to_string(index = False))



if __name__ == '__main__':
    main()
