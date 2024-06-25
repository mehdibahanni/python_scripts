import os
import requests
from bs4 import BeautifulSoup
import csv

# movie_name = input('Enter movie name...').replace(' ', '-')
movie_name = 'serie-mehmed-fetihler-sultani-8my'
html_content = requests.get(f'https://3isk.biz/watch/episodes/{movie_name}-season-1-episode-1/')
soup = BeautifulSoup(html_content.content, 'html.parser')



def fetch_episodes(items_list_season_eps):
    links_set = set()
    episodes = items_list_season_eps.find_all('a', class_='ep-num')

    if os.path.exists(movie_name+'_links.txt'):
        answor = input('file exists. Do you want to continue?...(N/Y)')
        if answor in ['no','NO','No','nO','n','N']:
            exit
        else:
            with open(movie_name+'_links.txt','r') as file:
                for line in file:
                    links_set.add(line.strip())
    
            for episode in episodes:
                href = episode.get('href')
                if href:
                    links_set.add(href)

            with open(movie_name+'_links.txt', 'w') as file:
                for href in links_set:
                    file.write(href + '\n')
                    print(href + '\n')
                    
# Find the link container
main_wrapper = soup.find('div', class_='main-wrapper')
if main_wrapper:
    single_pre_container = main_wrapper.find('div', class_='single-pre-container')
    if single_pre_container:

        single_main_content = single_pre_container.find('div', class_='single_main_content')
        if single_main_content:
    
            main_container = single_main_content.find('div', class_='main-container')
            if main_container:
        
                home_items_sec = main_container.find('section', class_='home-items-sec episodes-items-sec')
                if home_items_sec:
            
                    episodes_container = home_items_sec.find('div', class_='episodes-container')                    
                    if episodes_container:
                
                        episodes_list = episodes_container.find('div', class_='episodes-list')
                        if episodes_list:
                            
                            items_list_season_eps = episodes_list.find('div', class_='items_list season-eps')
                            if items_list_season_eps:           
                                fetch_episodes(items_list_season_eps)
                            else:
                                print('items_list_season_eps')
                        else:
                            print("episodes-list not found.")
                    else:
                        print("episodes-container not found.")
                else:
                    print("home-items-sec episodes-items-sec not found.")
            else:
                print("main-container not found.")
        else:
            print("single_main_content not found.")
    else:
        print("single-pre-container not found.")
else:
    print("main-wrapper not found.")
