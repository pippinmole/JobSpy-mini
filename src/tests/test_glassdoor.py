from ..jobspy import scrape_jobs


def test_indeed():
    result = scrape_jobs(
        site_name="glassdoor", search_term="software engineer", country_indeed="USA"
    )
    assert (
        isinstance(result, list) and not len(result) == 0
    ), "Result should be a non-empty list"
