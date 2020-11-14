
def display_inventory(inventory):               #print any given Dictionary displaying each key, followed by a colon
    for supply, amount in inventory.items():    #then a space, then the corresponding value, then a newline
        print(supply, ': ', amount)             #Calling the function with an empty dictionary results in displaying nothing


def add_to_inventory(inventory, added_items):   #add the contents of the added_items list to the inventory dictionary
    for supply in added_items:                  #calling with dictionary and items list results in adding items into dictionary
        inventory[supply] = inventory.get(supply, 0) + 1    #as keys and values are set to 1 , or +1 if existed in inventory before
                                                #if same occures more, then dictionary values are incremented those amounts o time


def remove_from_inventory(inventory, removed_items):        #remove the contents of the removed_items list from the inventory dictionary
    for supply in removed_items:
        inventory[supply] = inventory.get(supply, 0) - 1    #decrease by one at every mention -> leaves supplies with 0 volume
    [inventory.pop(supply) for supply in [amount for amount in inventory if inventory[amount] < 1]]  #Remove less-than-one supplies by key
                                                            #as nothing < 1 stays, will not display deducted items, not in original dict


def print_table(inventory, order):
    pass


def import_inventory(inventory, filename):
    pass


def export_inventory(inventory, filename):
    pass

# git commit
# use f: strings where possible


game_inventory = {'Star Wars':5, 'ToyStory':7, 'WowG':10, 'Office':8}
non_inventory = {}
added_items = ['Star Wars', 'ToyStory', 'HubalaBaba', 'Seventh', 'Star Wars']
no_exist = ['rubber', 'boy', 'leToy']

print('Game Inventory: ')
display_inventory(game_inventory)
print('\nNon Inventory: ')
display_inventory(non_inventory)

print("\nAdd these items: ", added_items, " to the inventory, so ")
add_to_inventory(game_inventory, added_items)
print("Inventory is now ", )
display_inventory(game_inventory)

print("\nRemove these items: ", added_items, " from the inventory, so ")
remove_from_inventory(game_inventory, added_items)
print("Inventory is now ", )
display_inventory(game_inventory)

print("\nRemove these items: ", no_exist, " from the inventory, so ")
remove_from_inventory(game_inventory, no_exist)
print("Inventory is now ", )
display_inventory(game_inventory)