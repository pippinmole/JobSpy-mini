from ..jobspy import scrape_jobs


def test_ziprecruiter():
    result = scrape_jobs(
        site_name="zip_recruiter",
        search_term="software engineer",
    )

    assert (
        isinstance(result, list) and not len(result) == 0
    ), "Result should be a non-empty list"
