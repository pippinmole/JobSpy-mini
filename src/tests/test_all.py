from ..jobspy import scrape_jobs


def test_all():
    result = scrape_jobs(
        site_name=["linkedin", "indeed", "zip_recruiter", "glassdoor"],
        search_term="software engineer",
        results_wanted=5,
    )

    assert (
            isinstance(result, list) and not len(result) == 0
    ), "Result should be a non-empty list"
