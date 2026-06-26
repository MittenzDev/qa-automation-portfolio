def generate_html_report(results, output_file="report.html"):

    passed = sum(1 for r in results if r["ok"])
    total = len(results)
    failed = total - passed

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("""
<html>
<head>
    <title>QA Report</title>
    <meta charset="utf-8">
</head>
<body>
""")

        f.write("<h1>QA Link Report</h1>")
        f.write(f"<p><b>Total:</b> {total} | <b>Passed:</b> {passed} | <b>Failed:</b> {failed}</p>")

        f.write("<table border='1' cellpadding='5'>")
        f.write("<tr><th>URL</th><th>Status</th><th>Result</th></tr>")

        for r in results:
            color = "green" if r["ok"] else "red"
            result = "PASS" if r["ok"] else "FAIL"
            style = "background-color:#ffcccc" if not r["ok"] else ""

            f.write(
                f"<tr style='{style}'>"
                f"<td>{r['url']}</td>"
                f"<td>{r['status']}</td>"
                f"<td style='color:{color}'>{result}</td>"
                f"</tr>"
            )

        f.write("</table></body></html>\n")