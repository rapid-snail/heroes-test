from model.hero import Hero


def test_create_hero(rest):
    original_hero = Hero(birth_date="2019-02-01", city="None", full_name="None", gender="M", main_skill="Brain", phone="+7-905-000-1020")
    is_success, created_hero = rest.create_hero(original_hero)
    print(created_hero)
    assert is_success

    assert original_hero.birth_date == created_hero.birth_date
    assert original_hero.city == created_hero.city
    assert original_hero.full_name == created_hero.full_name
    assert original_hero.gender == created_hero.gender
    assert original_hero.main_skill == created_hero.main_skill
    assert original_hero.phone == created_hero.phone


