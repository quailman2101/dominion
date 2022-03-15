# dominion
This dataset contains information about every Dominion card so far released, including promo cards (Dominion Allies is not yet included). I wanted to make the set pretty comprehensive so there is a lot of data about each card.  I've also included a basic kingdom picker script.

Here is a list of what each column in the dataset represents:

name - The name of the card.																				

set - The Dominion set the card appears in.																				

type 1, 2, 3, 4 - This is the type of card. The common types being Action, Treasure and Victory. Some cards have up to four types. Many of the lesser used types only show up in the one expansion.																				

cost - The cost in coin.  All cards that can end up in your deck have a cost, even if they can't be directly purchased (this is so they can interact with various other card effects).  There are several types of cards that cannot be purchased or added to your deck and so they get an N/A for this column. 	

additional_cost	- Two expansions include cards that have an additional cost.  Alchemy has cards that have a cost in Potions.  Empires has cards that have a cost in debt tokens.  These are in addition to any cost in coin.	

number_of_cards - Simply put, the number of each specific card.			

modify_cost	- Does the card itself allow it's cost to be modified?  Guilds has several cards that allow the player to overpay for an effect.  Peddler from Prosperity also can have it's cost modified.

in_supply	- Is the card part of the supply?  The base cards (and Colony/Platinum/Potion if used), along with the 10 kingdom cards being used for the game are in the supply.  Any other cards are not part of the supply and either cannot be purchased (i.e. Travelers) or cannot be added to a deck (i.e. Events).  Therefore they do not count against the game end condition of empty supply piles.

on_trash_effect	- Does the card text itself cause something to happen when the card is trashed?  Many Dark Ages cards use this mechanic.

on_gain_effect - Does the card text itself cause something to happen when the card is gained?  Note that cards with abilities that trigger only when bought, are not included.																				

trasher	- Does the card text allow you to trash another one of your own cards?  This can be optional or mandatory.  It can trash a card(s) that is in your hand, your deck, or in play.  Cards that trash only themselves or ones that only trash other player's cards are not included.	

special_setup	- Does the card text specify a special setup condition for the game?  Many Landmarks from Empires do.  Or do the directions specify special setup directions (i.e. Shelters from Dark Ages or Heirlooms from Nocturne)?		

curse	- Does the card explicitly have the ability to dispurse curses, typically to the other players?  Swindler is not included even though he could possibly give a curse.																				

cost_reducer - This refers to the few cards that have the ability to reduce the cost of other cards in the supply, such as Bridge from Intrigue.																				

associated_token 1, 2 - Each column names a token that the card adds to the game such as the point or coin tokens, or the many cardboard tokens from Adventures.  There is only one card that refers to more than 2 tokens and that is Teacher from Adventures.  It wasn't worth adding two more columns just for it. 

associated_mat - This names any mat that the card makes use of such as the Tavern or Exile mat.

called_cards -	This is a list of any other cards that will need to be added to the game when this card is included.  																				
