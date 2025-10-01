"""
TSMC data fetcher (TW: 2330, US ADR: TSM)
- Monthly revenue announcement date & figures (FinMind: TaiwanStockMonthRevenue)
- Foreign institutional investors buy/sell volume & amount (FinMind: InstitutionalInvestorsBuySell)
- Quarterly gross margin (computed from FinMind FinancialStatements)
- Earnings conference call dates (TSMC IR Financial Calendar - scraping hook)
- Advanced-node process mix (%) (TSMC transcript PDFs - scraping hook)

Sources:
- FinMind docs & datasets: 
  - Data list + dataset names: https://finmind.github.io/v3/tutor/TaiwanMarket/DataList/
  - Chip/籌碼面 overview: https://finmind.github.io/v3/tutor/TaiwanMarket/Chip/
  - FinancialStatements doc: https://finmind.github.io/v3/tutor/TaiwanMarket/FinancialStatements/
- TSMC IR:
  - Financial Calendar (earnings dates, monthly sales posts): https://investor.tsmc.com/english/financial-calendar
  - Q2'25 transcript (node mix example): https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2025-07/1f4f86c935f1de837672a6973154e64b26bdae57/TSMC%202Q25%20Transcript.pdf
"""

from dataclasses import dataclass
from typing import Optional, Tuple
import os
import pandas as pd
from datetime import date

# --------- FinMind setup ----------
try:
    # pip install FinMind
    from FinMind.data import DataLoader
except ImportError as e:
    raise SystemExit("Please `pip install FinMind` first") from e

@dataclass
class Config:
    start_date: str = "2016-01-01"
    end_date: Optional[str] = None  # None = today
    tw_stock_id: str = "2330"
    us_adr_ticker: str = "TSM"  # used for labeling only
    finmind_token: Optional[str] = os.getenv("FINMIND_TOKEN")  # or login via email/password

def get_loader(cfg: Config) -> DataLoader:
    dl = DataLoader()
    if cfg.finmind_token:
        # If you already have a token (recommended)
        dl.login_by_token(api_token=cfg.finmind_token)
    #else:
     #   # Fallback: login with FinMind account creds in env (FINMIND_EMAIL/FINMIND_PASSWORD)
     #   email = os.getenv("FINMIND_EMAIL")
      #  password = os.getenv("FINMIND_PASSWORD")
     #   if not (email and password):
     #       raise SystemExit(
     #           "Set FINMIND_TOKEN or FINMIND_EMAIL + FINMIND_PASSWORD in your environment."
     #       )
    #    dl.login(email, password)
    return dl

# --------- 1) Monthly revenue (announcement date & figures) ----------
def fetch_monthly_revenue(dl: DataLoader, cfg: Config) -> pd.DataFrame:
    # FinMind helper is taiwan_stock_month_revenue(); underlying dataset: TaiwanStockMonthRevenue
    # Columns include: stock_id, date (announcement date), revenue (TWD), revenue_month, revenue_year, ...
    df = dl.taiwan_stock_month_revenue(
        stock_id=cfg.tw_stock_id, start_date=cfg.start_date, end_date=cfg.end_date
    )
    # Add helpful labels + ADR twin
    df = df.rename(
        columns={
            "date": "announcement_date",
            "revenue": "revenue_twd",
        }
    )
    df["market_instrument"] = "TW-2330"  # company-level; same for ADR logically
    df["adr_twin"] = "US-TSM"
    # Keep core fields
    cols = [
        "announcement_date",
        "revenue_year",
        "revenue_month",
        "revenue_twd",
        "stock_id",
        "market_instrument",
        "adr_twin",
    ]
    return df[cols].sort_values("announcement_date")

# --------- 2) Institutional investors buy/sell (volume & amount) ----------
def fetch_institutional_investors(dl: DataLoader, cfg: Config) -> pd.DataFrame:
    """
    FinMind dataset: InstitutionalInvestorsBuySell (個股三大法人買賣表)
    Helper function in some docs: dl.taiwan_stock_institutional_investors_buy_sell
    Typical columns: date, stock_id, investor (=Foreign, InvestmentTrust, Dealer, etc),
                     buy, sell, buy_value, sell_value, net_buy_sell, net_value
    We’ll filter to Foreign only.
    """
    # API naming differs slightly across FinMind versions; try v3 name first:
    if hasattr(dl, "taiwan_stock_institutional_investors_buy_sell"):
        raw = dl.taiwan_stock_institutional_investors_buy_sell(
            stock_id=cfg.tw_stock_id, start_date=cfg.start_date, end_date=cfg.end_date
        )
    else:
        # fallback to generic fetch (older library): dl.dataset()
        raw = dl.dataset(
            dataset="InstitutionalInvestorsBuySell",
            data_id=cfg.tw_stock_id,
            start_date=cfg.start_date,
            end_date=cfg.end_date,
        )

    df = raw.copy()
    # Normalize column names if needed
    df.columns = [c.strip() for c in df.columns]
    # Keep foreign investors only
    mask = df["Investor"].str.lower().str.contains("foreign") if "Investor" in df.columns else df["investor"].str.lower().str.contains("foreign")
    df = df[mask].copy()
    # Standardize names
    rename_map = {
        "date": "date",
        "Date": "date",
        "stock_id": "stock_id",
        "StockID": "stock_id",
        "Investor": "investor",
        "Buy": "buy_volume",
        "Sell": "sell_volume",
        "buy": "buy_volume",
        "sell": "sell_volume",
        "buy_value": "buy_amount_twd",
        "sell_value": "sell_amount_twd",
        "BuyValue": "buy_amount_twd",
        "SellValue": "sell_amount_twd",
        "NetBuySell": "net_volume",
        "net_buy_sell": "net_volume",
        "NetValue": "net_amount_twd",
        "net_value": "net_amount_twd",
    }
    for k, v in rename_map.items():
        if k in df.columns:
            df.rename(columns={k: v}, inplace=True)

    df["market_instrument"] = "TW-2330"
    df["adr_twin"] = "US-TSM"
    keep = [
        "date",
        "stock_id",
        "investor",
        "buy_volume",
        "sell_volume",
        "net_volume",
        "buy_amount_twd",
        "sell_amount_twd",
        "net_amount_twd",
        "market_instrument",
        "adr_twin",
    ]
    return df[keep].sort_values("date")

# --------- 3) Quarterly gross margin (%), computed from FinancialStatements ----------
def fetch_quarterly_gross_margin(dl: DataLoader, cfg: Config) -> pd.DataFrame:
    """
    FinMind dataset: FinancialStatements (綜合損益表/三大表)
    We’ll pivot out OperatingRevenue and GrossProfit and compute GrossMargin = GrossProfit / OperatingRevenue.
    FinMind returns consolidated values by quarter when you pass 'frequency="quarter"'.
    """
    # Try the v3 helper name first:
    if hasattr(dl, "financial_statements"):
        fs = dl.financial_statements(
            stock_id=cfg.tw_stock_id,
            start_date=cfg.start_date,
            end_date=cfg.end_date,
            frequency="quarter",
        )
    else:
        fs = dl.dataset(
            dataset="FinancialStatements",
            data_id=cfg.tw_stock_id,
            start_date=cfg.start_date,
            end_date=cfg.end_date,
        )

    # Expect columns like: stock_id, date, type, value (type includes OperatingRevenue, GrossProfit, etc.)
    fs.columns = [c.strip() for c in fs.columns]
    # Normalize column names
    if "type" not in fs.columns:
        # Some older versions use 'item' or 'account'
        for alt in ("item", "account"):
            if alt in fs.columns:
                fs.rename(columns={alt: "type"}, inplace=True)
                break
    if "value" not in fs.columns:
        # Some versions use 'amount'
        if "amount" in fs.columns:
            fs.rename(columns={"amount": "value"}, inplace=True)

    need = fs[fs["type"].isin(["OperatingRevenue", "GrossProfit"])].copy()
    wide = need.pivot_table(
        index=["date", "stock_id"], columns="type", values="value", aggfunc="last"
    ).reset_index()
    # Compute gross margin
    wide["gross_margin"] = (wide["GrossProfit"] / wide["OperatingRevenue"]).replace([float("inf")], pd.NA)
    # Nice columns
    wide["market_instrument"] = "TW-2330"
    wide["adr_twin"] = "US-TSM"
    out = wide.rename(
        columns={
            "date": "quarter_end_date",
            "OperatingRevenue": "operating_revenue_twd",
            "GrossProfit": "gross_profit_twd",
            "gross_margin": "gross_margin_ratio",
        }
    )
    # Optional: percentage column
    out["gross_margin_pct"] = (out["gross_margin_ratio"] * 100).round(2)
    cols = [
        "quarter_end_date",
        "stock_id",
        "operating_revenue_twd",
        "gross_profit_twd",
        "gross_margin_ratio",
        "gross_margin_pct",
        "market_instrument",
        "adr_twin",
    ]
    return out[cols].sort_values("quarter_end_date")

# --------- 4) IR scraping hooks (earnings call dates; advanced-node %) ----------
TSMC_FIN_CALENDAR_URL = "https://investor.tsmc.com/english/financial-calendar"
# Example transcript with node mix lines:
# https://investor.tsmc.com/chinese/encrypt/files/encrypt_file/reports/2025-07/1f4f86c935f1de837672a6973154e64b26bdae57/TSMC%202Q25%20Transcript.pdf

def explain_ir_scraping():
    """
    There is no official JSON API for earnings call release dates or node mix.
    If you allow scraping:
      - Use requests + BeautifulSoup to read TSMC_FIN_CALENDAR_URL and extract rows where
        the event contains 'Results - Earnings Conference'.
      - For node mix, download each quarter's Transcript PDF and text-extract the
        'Advanced technologies ... accounted for XX% of wafer revenue' line.
    Keep this separate to respect rate limits, robots, and retry/backoff.
    """
    pass

# --------- Runner ----------
def fetch_all(config: Config) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if config.end_date is None:
        config.end_date = str(date.today())
    dl = get_loader(config)
    rev = fetch_monthly_revenue(dl, config)
    inst = fetch_institutional_investors(dl, config)
    gm = fetch_quarterly_gross_margin(dl, config)
    return rev, inst, gm

if __name__ == "__main__":
    cfg = Config(
        start_date="2016-01-01",
        end_date=None,       # up to today
        tw_stock_id="2330",
        us_adr_ticker="TSM",
        finmind_token=os.getenv("FINMIND_TOKEN"),
    )
    monthly_revenue, inst_investors, quarterly_gross_margin = fetch_all(cfg)

    # Save locally
    monthly_revenue.to_csv("tsmc_monthly_revenue_2330.csv", index=False)
    inst_investors.to_csv("tsmc_foreign_inst_buy_sell_2330.csv", index=False)
    quarterly_gross_margin.to_csv("tsmc_quarterly_gross_margin_2330.csv", index=False)

    # Heads-up prints
    print("Monthly revenue sample:")
    print(monthly_revenue.head())
    print("\nForeign institutional investors (Foreign) sample:")
    print(inst_investors.head())
    print("\nQuarterly gross margin sample:")
    print(quarterly_gross_margin.head())

    print("\nFor earnings call dates & advanced-node %:")
    print(f"- Financial Calendar (scrape): {TSMC_FIN_CALENDAR_URL}")
    print("- For each quarter, parse the transcript PDF to extract node-mix %. See comments in code.")
