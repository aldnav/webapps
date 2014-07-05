import re
import requests
import multiprocessing as mp
from bs4 import BeautifulSoup

# class Scraper(mp.Process):

#     def __init__(self, fm_url, mma_url):
#         mp.Process.__init__(self)
#         self.data = None
#         self.fm_url = fm_url
#         self.mma_url = mma_url

#     def run(self):
#         while True:
#             self.data = self.scrape_details(self.fm_url, self.mma_url)
#             break
#     def scrape_details(self, fm_url, mma_url):
#         data = None
#         r = requests.get(fm_url)
#         if r.status_code == 200:
#             soup = BeautifulSoup(r.text)
#             data = {
#                 'name': None,
#                 'age':  None,
#                 'height': None,
#                 'weight': None,
#                 'division': None,
#                 'wins': None,
#                 'loses': None,
#                 'draws': None,
#                 'octagon_time': None,
#                 'f_540_metric': None,
#                 'rating_points': None,
#                 'quality_performance': None,
#                 'win_finish': None,
#                 'last_opponent': None,
#                 'fight_status': None,
#             }
#             table = soup.find_all('table', {'class':'tblRank'})[0]
#             tbody_rows = table.find_all('tr')
#             try:
#                 data['name'] = tbody_rows[0].select('a[href^="http://www.sherdog.com/fightfinder/fightfinder.asp?"]')[0].get_text(strip=True).encode('utf-8')
#             except: pass
#             try:
#                 data['age'] = soup.find_all('td', text=re.compile('Age'))[
#                           0].parent.contents[-1].string.encode('utf-8')
#             except: pass
#             try:
#                 pro_record = soup.find_all('td', text=re.compile('Pro Record:'))[
#                     0].next_sibling.next_sibling.get_text().encode('utf-8').strip().replace(' *May include TUF fights', '').split('-')
#                 data['wins'], data['loses'], data['draws'] = int(pro_record[0]), int(
#                     pro_record[1]), int(pro_record[2])
#             except: pass
#             try:
#                 octagon_time = soup.find_all('a', text=re.compile('Octagon Time:'))[
#                     0].next_sibling.next_sibling.get_text().encode('utf-8').split(':')
#                 octagon_time = int(octagon_time[0]) * 60 + int(octagon_time[1])
#                 data['octagon_time'] = octagon_time
#             except: pass
#             try:
#                 data['f_540_metric'] = int(soup.find_all('td', text=re.compile('540 Metric:'))[
#                                   0].next_sibling.next_sibling.get_text().encode('utf-8').replace('.', ''))
#             except: pass
#             try:
#                 data['rating_points'] = int(soup.find_all('td', text=re.compile('Rating Points:'))[
#                                     0].next_sibling.next_sibling.get_text().encode('utf-8'))
#             except: pass
#             try:
#                 data['win_finish'] = int(soup.find_all('td', text=re.compile('Win Finish %:'))[
#                                  0].next_sibling.next_sibling.get_text().encode('utf-8').replace('%', '').replace('.', ''))
#             except: pass
#             try:
#                 data['quality_performance'] = int(soup.find_all('td', text=re.compile('Quality Perf. %:'))[
#                                    0].next_sibling.next_sibling.get_text().encode('utf-8').replace('%', '').replace('.', ''))
#             except: pass
#             try:
#                 opponent_fm_url = self.domain_fm + soup.find_all(text=re.compile('Last Opponent: '))[0].parent.a['href']
#                 data['last_opponent'] = ' '.join(opponent_fm_url.split('/')[-3].split('+'))
#             except: pass
#             try:
#                 # wins_in_last_5 = len(soup_fm.find_all('td', {'class': 'tdRankHead'})[
#                 #                      1].div.find_all('span', text=re.compile('W')))
#                 data['fight_status'] = soup_fm.find_all('td', {'class': 'tdRankHead'})[
#                                      1].div.find_all('span')[0].upper()
#             except: pass

#             r = requests.get(mma_url)
#             soup = BeautifulSoup(r.text)
#             if r.status_code == 200:
#                 try:
#                     height = soup.find_all('td', text=re.compile('Height:'))[0].next_sibling.next_sibling.get_text().encode('utf-8').split()
#                     height = int(height[0]) * 12 + int(height[2])
#                     if height > 0:
#                         data['height'] = height
#                 except: pass
#                 try:
#                     weight = int(soup.find_all('td', text=re.compile('Weight:'))[0].next_sibling.next_sibling.get_text().replace(' lbs.', ''))
#                     if weight > 0:
#                         data['weight'] = weight
#                         weight = data['weight']
#                         if weight >= 155 and weight < 170: div = 'lightweight'
#                         elif weight >= 170 and weight < 185: div = 'welterweight'
#                         elif weight >= 185 and weight < 205: div = 'middleweight'
#                         data['division'] = div
#                 except: pass
        
#         return data

def scrape_details(fm_url, mma_url):
        data = None
        r = requests.get(fm_url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text)
            data = {
                'name': None,
                'age':  None,
                'height': None,
                'weight': None,
                'division': None,
                'wins': None,
                'loses': None,
                'draws': None,
                'octagon_time': None,
                'f_540_metric': None,
                'rating_points': None,
                'quality_performance': None,
                'win_finish': None,
                'last_opponent': None,
                'fight_status': None,
            }
            table = soup.find_all('table', {'class':'tblRank'})[0]
            tbody_rows = table.find_all('tr')
            try:
                data['name'] = tbody_rows[0].select('a[href^="http://www.sherdog.com/fightfinder/fightfinder.asp?"]')[0].get_text(strip=True).encode('utf-8')
            except: pass
            try:
                data['age'] = soup.find_all('td', text=re.compile('Age'))[
                          0].parent.contents[-1].string.encode('utf-8')
            except: pass
            try:
                pro_record = soup.find_all('td', text=re.compile('Pro Record:'))[
                    0].next_sibling.next_sibling.get_text().encode('utf-8').strip().replace(' *May include TUF fights', '').split('-')
                data['wins'], data['loses'], data['draws'] = int(pro_record[0]), int(
                    pro_record[1]), int(pro_record[2])
            except: pass
            try:
                octagon_time = soup.find_all('a', text=re.compile('Octagon Time:'))[
                    0].next_sibling.next_sibling.get_text().encode('utf-8').split(':')
                octagon_time = int(octagon_time[0]) * 60 + int(octagon_time[1])
                data['octagon_time'] = octagon_time
            except: pass
            try:
                data['f_540_metric'] = int(soup.find_all('td', text=re.compile('540 Metric:'))[
                                  0].next_sibling.next_sibling.get_text().encode('utf-8').replace('.', ''))
            except: pass
            try:
                data['rating_points'] = int(soup.find_all('td', text=re.compile('Rating Points:'))[
                                    0].next_sibling.next_sibling.get_text().encode('utf-8'))
            except: pass
            try:
                data['win_finish'] = int(soup.find_all('td', text=re.compile('Win Finish %:'))[
                                 0].next_sibling.next_sibling.get_text().encode('utf-8').replace('%', '').replace('.', ''))
            except: pass
            try:
                data['quality_performance'] = int(soup.find_all('td', text=re.compile('Quality Perf. %:'))[
                                   0].next_sibling.next_sibling.get_text().encode('utf-8').replace('%', '').replace('.', ''))
            except: pass
            try:
                opponent_fm_url = self.domain_fm + soup.find_all(text=re.compile('Last Opponent: '))[0].parent.a['href']
                data['last_opponent'] = ' '.join(opponent_fm_url.split('/')[-3].split('+'))
            except: pass
            try:
                # wins_in_last_5 = len(soup_fm.find_all('td', {'class': 'tdRankHead'})[
                #                      1].div.find_all('span', text=re.compile('W')))
                data['fight_status'] = soup_fm.find_all('td', {'class': 'tdRankHead'})[
                                     1].div.find_all('span')[0].upper()
            except: pass

            r = requests.get(mma_url)
            soup = BeautifulSoup(r.text)
            if r.status_code == 200:
                try:
                    height = soup.find_all('td', text=re.compile('Height:'))[0].next_sibling.next_sibling.get_text().encode('utf-8').split()
                    height = int(height[0]) * 12 + int(height[2])
                    if height > 0:
                        data['height'] = height
                except: pass
                try:
                    weight = int(soup.find_all('td', text=re.compile('Weight:'))[0].next_sibling.next_sibling.get_text().replace(' lbs.', ''))
                    if weight > 0:
                        data['weight'] = weight
                        weight = data['weight']
                        if weight >= 155 and weight < 170: div = 'lightweight'
                        elif weight >= 170 and weight < 185: div = 'welterweight'
                        elif weight >= 185 and weight < 205: div = 'middleweight'
                        data['division'] = div
                except: pass
        
        return data

if __name__ == '__main__':
    
    fm = 'http://www.fightmatrix.com/fighter-profile/Johny+Hendricks/4741/'
    mma = 'http://www.mixedmartialarts.com/f/698E678D3D567AE4/Johny-Hendricks/'
    print scrape_details(fm, mma)
