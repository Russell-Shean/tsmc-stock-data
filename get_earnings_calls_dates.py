from playwright.sync_api import sync_playwright
import pandas as pd
from bs4 import BeautifulSoup


from playwright.sync_api import sync_playwright
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import os


def fetch_mops_conference_calls(stock_id="2330"):
    url = f"https://investor.tsmc.com/english/financial-calendar"

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)

        # Let the page load fully
        page.wait_for_load_state("networkidle")

        html = page.content()
        with open('data/tsmc/earnings_announcements.html', "w", encoding="utf-8") as f:
                f.write(html)

        browser.close()

    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for tr in soup.select("tr"):
        cols = [c.get_text(strip=True) for c in tr.find_all("td")]
        if cols:
            rows.append(cols)

    df = pd.DataFrame(rows)
    df = df[df.apply(lambda row: row.astype(str).str.contains("法說會").any(), axis=1)]
    return df

if __name__ == "__main__":
    df = fetch_mops_conference_calls()
    print(df.head())
    df.to_csv('data/tsmc/meetings_announcements.csv')
