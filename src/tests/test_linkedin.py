from ..jobspy import scrape_jobs


def test_linkedin():
    result = scrape_jobs(
        site_name="linkedin",
        search_term="software engineer",
    )
    assert (
        isinstance(result, list) and not len(result) == 0
    ), "Result should be a non-empty list"
