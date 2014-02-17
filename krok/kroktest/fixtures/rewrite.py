i = 1
with open('/home/antisocial/dev/krok/krok/kroktest/fixtures/initial_data.json') as f:
    for line in f:
        if 'pk":' in line:
            print '  "pk":', i
            i += 1
        else:
            print(line)
