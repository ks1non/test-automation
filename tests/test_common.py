import pytest
from pytest import mark

url_list = ['https://toghrulmirzayev.github.io/ui-simulator/drag-and-drop.html',
            'https://toghrulmirzayev.github.io/ui-simulator/input-and-click.html',
            'https://toghrulmirzayev.github.io/ui-simulator/checkbox-and-scroll.html',
            'https://toghrulmirzayev.github.io/ui-simulator/check_and_validate.html',
            'https://toghrulmirzayev.github.io/ui-simulator/sorting.html']

page_1 = [1, 'https://toghrulmirzayev.github.io/ui-simulator/drag-and-drop.html']
page_2 = [2, 'https://toghrulmirzayev.github.io/ui-simulator/input-and-click.html']
page_3 = [3, 'https://toghrulmirzayev.github.io/ui-simulator/checkbox-and-scroll.html']
page_4 = [4, 'https://toghrulmirzayev.github.io/ui-simulator/check_and_validate.html']
page_5 = [5, 'https://toghrulmirzayev.github.io/ui-simulator/sorting.html']


@mark.common
def test_back_per_pages(common_instance):
    common_instance.navigate_pages(5, url_list)


@mark.common
@pytest.mark.parametrize('index, url', (page_1, page_2, page_3, page_4, page_5))
def test_back_per_pages_parametrize(common_instance, index, url):
    common_instance.navigate_pages_parametrize(index, url)
