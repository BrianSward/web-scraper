import pytest
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


# @pytest.mark.skip("TODO")
def test_exists_count():
    assert get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')


# @pytest.mark.skip("TODO")
def test_exists_report():
    assert get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')


# @pytest.mark.skip("TODO")
def test_count():
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_count(url)
    expected = 12
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_report():
    url = 'https://en.wikipedia.org/wiki/Milford,_Connecticut'
    actual = get_citations_needed_report(url)
    expected = 'The Milford Oyster Festival has drawn large musical acts over the years including Joan Jett, ' \
               'The Marshall Tucker Band, John Cafferty & The Beaver Brown Band, and Soul Asylum.[citation needed]'
    assert actual == expected
