from urllib.parse import urljoin

from framework.link_checker import check_link
from framework.report_generator import generate_html_report


BASE_URL = "https://juantorresdev.wordpress.com"


def test_all_links_are_valid(page):

    page.goto(BASE_URL)

    links = page.locator("a")
    count = links.count()

    results = []
    broken_links = []
    seen = set()

    for i in range(count):

        href = links.nth(i).get_attribute("href")

        if not href:
            continue

        # skip non-web links
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
            continue

        full_url = urljoin(BASE_URL, href)

        # avoid duplicates
        if full_url in seen:
            continue
        seen.add(full_url)

        # -------------------------
        # CORE VALIDATION (NOW CLEAN)
        # -------------------------
        result = check_link(full_url)

        print(f"{result['status']} -> {result['url']}")

        results.append(result)

        if not result["ok"]:
            broken_links.append(result)

    # -------------------------
    # REPORTING
    # -------------------------
    generate_html_report(results)
    print("\nHTML report generated: report.html")

    # -------------------------
    # ASSERTION
    # -------------------------
    assert len(broken_links) == 0