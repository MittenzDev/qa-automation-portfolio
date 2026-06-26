from report_generator import generate_html_report


def test_portfolio_projects_are_complete(page):

    project_pages = [
        "/2026/04/21/c-rpg-character-system-oop-practice-project/",
        "/2025/05/06/bad-robot-unreal-engine-project/",
        "/2025/05/06/redhood-unreal-engine-project/",
        "/2022/06/17/letter-from-caiatl-to-zavala/",
        "/2022/06/09/branching-quest-line/",
        "/2022/06/09/kinship-eris-and-drifter-short-story/",
        "/2022/06/09/season-of-the-haunted/"
    ]

    results = []

    for project in project_pages:

        url = f"https://juantorresdev.wordpress.com{project}"
        page.goto(url)

        title = page.locator("h1").text_content()
        body = page.locator("body").text_content()

        ok = (
            title is not None
            and len(title.strip()) > 3
            and body is not None
            and len(body.strip()) > 100
        )

        results.append({
            "url": url,
            "title": title,
            "content_length": len(body.strip()) if body else 0,
            "ok": ok
        })

        print(f"{'PASS' if ok else 'FAIL'} -> {url}")

    generate_html_report(results)

    assert all(r["ok"] for r in results)
