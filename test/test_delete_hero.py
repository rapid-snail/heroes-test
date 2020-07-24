from model.hero import Hero


def test_delete_hero(rest):
    original_hero = Hero(birth_date="2019-02-01", city="None", full_name="None", gender="M", main_skill="Brain", phone="000222")

    # create
    is_success, just_created_hero = rest.create_hero(original_hero)
    assert(is_success)
    print("created hero with id={}".format(just_created_hero.id))

    # delete
    is_success, _ = rest.delete_hero(just_created_hero.id)
    assert is_success
    print("hero with id={} deleted".format(just_created_hero.id))

    # ensure deleted
    is_success, hero, err_code = rest.get_hero_by_id(just_created_hero.id)
    if is_success:
        raise Exception("unexpected hero found {}".format(hero))
    elif err_code == "NOT_FOUND":
        print("hero with id={} no more exists".format(just_created_hero.id))
    else:
        raise Exception("Unknown result")

