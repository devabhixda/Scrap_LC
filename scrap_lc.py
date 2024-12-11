from bs4 import BeautifulSoup
import csv

companies = []

for company in companies:
    with open(f'./input/{company}.html', "r", encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(content, "lxml")  

    que = soup.find('div', class_='absolute left-0 top-0 w-full pb-[80px]')
    data = que.find_all('a')

    que_list = []
    for d in data:
        link = d['href'].split('?')[0]
        question_name = d.find('div', class_='ellipsis line-clamp-1').text.strip()
        difficulty = d.find('p', class_='text-[14px]').text.strip()
        frequency_divs = d.find('div', class_='flex gap-0.5 px-1').find_all('div')
        que_list.append((question_name, link, difficulty))

    csv_file = f'output/{company}_leetcode_3mo.csv'

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Question Name', 'Link', 'Difficulty'])
        writer.writerows(que_list)

    print(f"Data successfully written to {csv_file}")