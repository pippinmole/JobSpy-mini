from ..jobspy import scrape_jobs


def test_indeed():
    result = scrape_jobs(
        site_name="indeed", search_term="software engineer", country_indeed="usa"
    )
    assert (
        isinstance(result, list) and not len(result) == 0
    ), "Result should be a non-empty list"
