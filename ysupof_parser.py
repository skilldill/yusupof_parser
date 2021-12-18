from bs4 import BeautifulSoup
import requests

YUSUPOF_SITE = 'https://www.yusupov-palace.ru/'


class YusupofParser:
    event_page = None
    programs_page = None

    def __init__(self):
        self.__upload_site()

    def __upload_site(self):
        result_events_page = requests.get(YUSUPOF_SITE + 'ru/events')
        result_programs_page = requests.get(YUSUPOF_SITE + 'programs')

        self.event_page = BeautifulSoup(result_events_page.text, 'html.parser')
        self.programs_page = BeautifulSoup(result_programs_page.text, 'html.parser')

    def get_events(self):
        events = []

        if self.event_page is not None:
            html_events = self.event_page.find_all('div', {'class': 'theatre-item'})

            for html_event in html_events:
                event = {
                    'name': html_event.find('a', {'class': 'theatre-title'}).text,
                    'date': html_event.find('div', {'class': 'theatre-date'}).text,
                    'place': html_event.find('div', {'class': 'theatre-place'}).text,
                    'poster': html_event.find('img')['src']
                }

                events.append(event)

        return events

    def get_programs(self):
        programs = []

        if self.programs_page is not None:
            html_programs = self.programs_page.find_all('div', {'class': 'program-item'})

            for html_program in html_programs:
                program = {
                    'name': html_program.find('div', {'class': 'program-name'}).text,
                    'description': html_program.find('div', {'class': 'program-place'}).text,
                    'poster': html_program.find('img')['src']
                }

                programs.append(program)

        return programs


parser = YusupofParser()
