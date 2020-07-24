
def test_get_all_heroes(rest):
    is_success, heroes = rest.get_all_heroes()
    print(heroes)

