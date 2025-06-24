def brasileirao(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')

if __name__ == '__main__':
    times = {
        'primeiro':'Corinthians',
        'segundo': 'Santos',
        'terceiro': 'Fortaleza'
    }
    brasileirao(**times)