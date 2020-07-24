import requests
from model.hero import Hero

class RestHeroesFixture:
    def __init__(self, url):
        self.url = url

    def get_all_heroes(self):
        url = self.url + "/superheroes"
        response = requests.get(url=url)
        res = [Hero().init_from_dict(x) for x in response.json()]
        is_success = response.status_code == 200
        return (is_success, res)

    def get_hero_by_id(self, hero_id):
        url = self.url + "/superheroes/{}".format(hero_id)
        response = requests.get(url=url)

        if response.status_code == 200:
            res = Hero().init_from_dict(response.json())
            return (True, res, "")
        elif response.status_code == 400:
            return (False, None, response.json()["code"])
        else:
            return (False, None, "Unknown error")

    def create_hero(self, hero):
        url = self.url + "/superheroes"
        response = requests.post(url=url, json=hero.to_dict())
        res = Hero().init_from_dict(response.json())
        is_success = response.status_code in (200, 201) # только 201 должно быть ?
        return (is_success, res)

    def delete_hero(self, hero_id):
        url = self.url + "/superheroes/{}".format(hero_id)
        response = requests.delete(url=url)
        is_success = response.status_code == 200
        return (is_success, None)

