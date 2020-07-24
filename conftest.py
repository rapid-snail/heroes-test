import pytest
from fixture.heroes import RestHeroesFixture
import config

@pytest.fixture(scope="session")
def rest(request):
    rest_fixture = RestHeroesFixture(url=config.HEROES_BASE_URL)
    return rest_fixture
