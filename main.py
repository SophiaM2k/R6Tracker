import requests
from bs4 import BeautifulSoup
from tkinter import *

root = Tk()
root.iconbitmap('img/r6.ico')
root.title('R6 Stat Tracker')

def runApp():
    stats()
    searchButton['state'] = DISABLED

def destroyLabel():
    labels = [label1, label2, label3, label4, label5, label6, label7, label8 ,label9, label10, label11, label12, label13, label14, label15, label16, label17, label_name, label_plat, label_cas, label_rank]
    for x in labels:
        x.destroy()
    searchButton['state'] = NORMAL

player = Entry(root, width=30)
player.grid(row=0, column=0)

options = ['xbox', 'psn', 'pc']
clicked = StringVar()
clicked.set(options[0])

platform = OptionMenu(root, clicked, *options)
platform.grid(row=0, column=1)

searchButton = Button(root, text= 'Search', command =runApp)
searchButton.grid(row=0, column=3)

clearButton = Button(root, text='Clear', command=destroyLabel)
clearButton.grid(row=0, column=4)

def stats():
    global label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, label16, label17, label_name, label_plat, label_cas, label_rank
    data = requests.get(f'https://r6.tracker.network/profile/{clicked.get()}/{player.get()}')
    soup = BeautifulSoup(data.text, 'html.parser')
    name = soup.find('h1', {'class': 'trn-profile-header__name'})
    player_name = name.find('span').text
    label_name = Label(root, width=30, text='Player: ' + player_name + '\n')
    label_name.grid(row=1, column=0)
    label_plat = Label(root, width=30, text='Platform: ' + clicked.get() + '\n')
    label_plat.grid(row=1, column=1)

    label_cas = Label(root, width=30, text='Casual Stats' + '\n')
    label_cas.grid(row=2, column=0)

    for div in soup.find_all('div', {'data-stat': 'CasualTimePlayed'}):
        label1 = Label(root, width=30,padx = 0, pady=0, text='Time Played: ' + div.text)
        label1.grid(row=3, column=0)
    for div in soup.find_all('div', {'data-stat': 'CasualWins'}):
        label2 = Label(root, width=30, padx=0, pady=0, text='Wins: ' + div.text)
        label2.grid(row=4, column=0)
    for div in soup.find_all('div', {'data-stat': 'CasualLosses'}):
        label3 = Label(root, width=30, padx=0, pady=0, text='Losses: ' + div.text)
        label3.grid(row=5, column=0)
    for div in soup.find_all('div', {'data-stat': 'CasualKills'}):
        label4 = Label(root, width=30, padx=0, pady=0, text='Kills: ' + div.text)
        label4.grid(row=6, column=0)
    for div in soup.find_all('div', {'data-stat': 'CasualDeaths'}):
        label5 = Label(root, width=30, padx=0, pady=0, text='Deaths: ' + div.text)
        label5.grid(row=7, column=0)
    for div in soup.find_all('div', {'data-stat': 'CasualWLRatio'}):
        label6 = Label(root, width=30, padx=0, pady=0, text='Win Loss: ' + div.text)
        label6.grid(row=8, column=0)
    for div in soup.find_all('div', {'data-stat': 'CasualKDRatio'}):
        label7 = Label(root, width=30, padx=0, pady=0, text='KD: ' + div.text)
        label7.grid(row=9, column=0)

    label_rank = Label(root, width=30, padx=0, pady=0, text='Ranked Stats' + '\n')
    label_rank.grid(row=2, column=1)

    for div in soup.find_all('div', {'data-stat': 'RankedTimePlayed'}):
        label8 = Label(root, width=30, padx=0, pady=0, text='Time Played: ' + div.text)
        label8.grid(row=3, column=1)
    for div in soup.find_all('div', {'data-stat': 'RankedWins'}):
        label9 = Label(root, width=30, padx=0, pady=0, text='Wins: ' + div.text)
        label9.grid(row=4, column=1)
    for div in soup.find_all('div', {'data-stat': 'RankedLosses'}):
        label10 = Label(root, width=30, padx=0, pady=0, text='Losses: ' + div.text)
        label10.grid(row=5, column=1)
    for div in soup.find_all('div', {'data-stat': 'RankedKills'}):
        label11 = Label(root, width=30, padx=0, pady=0, text='Kills: ' + div.text)
        label11.grid(row=6, column=1)
    for div in soup.find_all('div', {'data-stat': 'RankedDeaths'}):
        label12 = Label(root, width=30, padx=0, pady=0, text='Deaths: ' + div.text)
        label12.grid(row=7, column=1)
    for div in soup.find_all('div', {'data-stat': 'RankedWLRatio'}):
        label13 = Label(root, width=30, padx=0, pady=0, text='Win Loss: ' + div.text)
        label13.grid(row=8, column=1)
    for div in soup.find_all('div', {'data-stat': 'RankedKDRatio'}):
        label14 = Label(root, width=30, padx=0, pady=0, text='KD: ' + div.text)
        label14.grid(row=9, column=1)
    for div in soup.find_all('div', {'class': 'r6-season__region'}):
        label15 = Label(root, width=30, padx=0, pady=0, text='Region: ' + div.text)
        label15.grid(row=10, column=1)
    for div in soup.find_all('div', {'class': 'trn-text--dimmed trn-text--center'}):
        label16 = Label(root, width=30, padx=0, pady=0, text='Rank: ' + div.text + '\n')
        label16.grid(row=11, column=1)
    for div in soup.find_all('div', {'class': 'r6-season-rank__progress-fill'}):
        label17 = Label(root, width=30, padx=0, pady=0, text='MMR: ' + div.text)
        label17.grid(row=12, column=1)

root.mainloop()

