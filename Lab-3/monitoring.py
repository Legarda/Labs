import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    r = requests.get(url)
    data = json.loads(r.content)
    logging.info("Сервер доступний. Час на сервері: %s", data['date'])
    logging.info("Запитувана сторінка: : %s", data['current_page'])
    logging.info("Відповідь сервера місти наступні поля:")
    for key in data.keys():
        logging.info("Ключ: %s, Значення: %s", key, data[key])


if __name__ == '__main__':
    while True:
        try:
            main("http://localhost:8000/health")
        except requests.exceptions.ConnectionError as e:
            logging.warning("Page is unable")
            logging.error(e)
        finally:
            time.sleep(60)
