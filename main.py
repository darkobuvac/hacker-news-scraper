import time
from scrape import read_news
from argparse import ArgumentParser

parser = ArgumentParser(description='Custom hacker news')

parser.add_argument('-s', '--sites', type=int, help='Number of Hacker news pages to scrape')
parser.add_argument('-v', '--votes', type=int, help='Minimal score number')
parser.add_argument('-f', '--folder', type=str, help='Folder path to store news')

args = parser.parse_args()

time_string = time.strftime("%d_%m_%Y")

file_path = f'HackerNews_{time_string}.txt'
folder = args.folder
if folder:
    file_path = f'{folder}/{file_path}'

if __name__ == '__main__':
    pages = int(args.sites)
    score = int(args.votes)
    news = read_news(pages, score)
    with open(file_path, 'w', encoding='utf-8') as f:
        for hn in news:
            for key, value in hn.items():
                f.write('%s: %s\n' % (key, value))

            line = '_' * 100
            f.write(f'{line} \n')
            f.write('\n')

    print('DONE!')
