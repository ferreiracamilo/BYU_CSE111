bad_guys = {
    'daredvil' : 'kingping',
    'x-men' : 'apocalypse',
    'batman' : 'bane'
}

print(f"Print batman a specific value > batman key val: {bad_guys['batman']}")
print(bad_guys)

# print(f"Print non existing value: {bad_guys['non_existing_hero']}")

print("\nAdd x-men key and its value")
bad_guys['x-men'] = 'juggernut'

print(bad_guys)

print("\ndelete x-men value")
del bad_guys['x-men']

print(bad_guys)