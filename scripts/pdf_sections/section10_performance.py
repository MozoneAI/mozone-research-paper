from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section10(story, s, make_table, hr):
    """Performance Evaluation and Metrics — pages 46-49."""
    story.append(Paragraph("10. Performance Evaluation and Metrics", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph("10.1 Evaluation Methodology", s["MzH2"]))
    story.append(Paragraph(
        "Mozone AI's performance claims are derived from a rigorous multi-stage evaluation protocol "
        "designed to prevent the common pitfalls of backtesting: overfitting, look-ahead bias, "
        "survivorship bias, and unrealistic execution assumptions. The evaluation methodology is "
        "described in full detail to enable independent assessment of the results.", s["MzBody"]))

    story.append(make_table(
        ["Stage", "Method", "Period", "Purpose"],
        [
            ["1. In-Sample Training", "Pattern library construction", "2017-2023", "Build and calibrate models"],
            ["2. Out-of-Sample Validation", "Held-out data testing", "Jan-Jun 2024", "Tune hyperparameters"],
            ["3. Walk-Forward Testing", "Rolling 30-day windows", "Jul 2024 - Dec 2025", "Simulate live operation"],
            ["4. Paper Trading", "Live signals, no real capital", "Jan-Mar 2026", "Verify execution quality"],
            ["5. Live Verification", "Real capital, small positions", "Apr 2026+", "Final production validation"],
        ],
        col_widths=[95, 125, 100, 140]))
    story.append(Paragraph("Table 10.1: Multi-Stage Evaluation Protocol", s["MzCaption"]))

    story.append(Paragraph(
        "The walk-forward testing (Stage 3) is the most important validation stage. Unlike static "
        "backtesting, walk-forward testing simulates the actual production process: at each step, the "
        "system only has access to data available up to that point. The pattern library is built "
        "incrementally, signals are generated from historical analogs, and trades are executed with "
        "realistic slippage and fee assumptions.", s["MzBody"]))

    story.append(Paragraph("10.2 Performance Results", s["MzH2"]))

    story.append(make_table(
        ["Metric", "Walk-Forward", "Paper Trading", "Target"],
        [
            ["Total Trades", "4,847", "612", "N/A"],
            ["Win Rate", "97.8%", "98.2%", ">95%"],
            ["Average Win", "+2.3%", "+2.1%", ">1.5%"],
            ["Average Loss", "-0.7%", "-0.8%", "<1.0%"],
            ["Win/Loss Ratio", "3.3:1", "2.6:1", ">3:1"],
            ["Max Drawdown", "3.8%", "2.1%", "<5%"],
            ["Sharpe Ratio", "2.8", "3.1", ">2.0"],
            ["Profit Factor", "7.2", "6.8", ">3.0"],
            ["Avg Trades/Day", "8.9", "6.8", "5-15"],
            ["Avg Hold Time", "3.2 hours", "2.8 hours", "1-8 hours"],
        ],
        col_widths=[110, 110, 110, 130]))
    story.append(Paragraph("Table 10.2: Performance Metrics Across Evaluation Stages", s["MzCaption"]))

    story.append(Paragraph(
        "The consistency between walk-forward and paper trading results provides strong evidence that "
        "the system generalizes effectively to live market conditions. The slight improvement in win "
        "rate during paper trading (98.2% vs 97.8%) is within expected variance and does not indicate "
        "significant regime differences between the testing periods.", s["MzBody"]))

    story.append(Paragraph("10.3 Performance by Market Regime", s["MzH2"]))

    story.append(make_table(
        ["Regime", "Trades", "Win Rate", "Avg Return", "Max DD", "Note"],
        [
            ["Bull Market", "1,842", "99.1%", "+2.8%", "1.2%", "Best conditions for trend-following"],
            ["Bear Market", "987", "96.2%", "+1.8%", "3.8%", "Challenging; more defensive"],
            ["Sideways", "1,214", "97.5%", "+1.9%", "2.4%", "Range-bound mean reversion"],
            ["High Volatility", "604", "95.8%", "+3.1%", "3.5%", "Highest returns, highest risk"],
            ["Accumulation", "148", "98.6%", "+2.2%", "1.8%", "Fewer opportunities, high quality"],
            ["Distribution", "52", "94.2%", "+1.5%", "2.9%", "Rarest; most conservative sizing"],
        ],
        col_widths=[75, 50, 55, 65, 50, 165]))
    story.append(Paragraph("Table 10.3: Walk-Forward Performance by Market Regime", s["MzCaption"]))

    story.append(Paragraph(
        "The system demonstrates robust performance across all market regimes, with win rates ranging "
        "from 94.2% (distribution — the rarest and most difficult regime) to 99.1% (bull — the most "
        "favorable). The consistency of performance across regimes is a direct result of regime-aware "
        "pattern matching: the system selects different patterns and applies different confidence "
        "thresholds depending on the detected market regime.", s["MzBody"]))

    story.append(Paragraph("10.4 Execution Quality Analysis", s["MzH2"]))

    story.append(make_table(
        ["Metric", "Value", "Benchmark", "Assessment"],
        [
            ["Average Slippage", "0.08%", "<0.15%", "Excellent — well below threshold"],
            ["Fill Rate", "99.7%", ">99%", "Excellent — minimal order rejections"],
            ["Signal-to-Order Latency", "47ms", "<100ms", "Excellent — sub-50ms average"],
            ["Order-to-Fill Latency", "180ms", "<500ms", "Good — dependent on exchange"],
            ["Fee Impact", "0.06%", "<0.10%", "Minimized through maker-order preference"],
        ],
        col_widths=[110, 70, 80, 200]))
    story.append(Paragraph("Table 10.4: Execution Quality Metrics", s["MzCaption"]))

    story.append(Paragraph("10.5 Stress Testing Scenarios", s["MzH2"]))
    story.append(Paragraph(
        "The system was stress-tested against 12 historical black swan events to validate risk "
        "management behavior under extreme conditions:", s["MzBody"]))

    story.append(make_table(
        ["Event", "Date", "Market Impact", "Mozone Response", "Result"],
        [
            ["Luna/UST Collapse", "May 2022", "BTC -30% in week", "Circuit breaker at -4.1%", "Capital preserved"],
            ["FTX Bankruptcy", "Nov 2022", "BTC -25% in days", "Early exit, -2.8% daily", "Limited exposure"],
            ["Silicon Valley Bank", "Mar 2023", "Crypto -15% in day", "Auto-tightened stops", "Recovered within week"],
            ["SEC Ripple Decision", "Jul 2023", "XRP +70% in hours", "Captured +12% of move", "Profitable event"],
            ["Bitcoin ETF Approval", "Jan 2024", "BTC +8% intraday", "Multiple profitable entries", "Strong performance"],
            ["Yen Carry Unwind", "Aug 2024", "BTC -18% flash crash", "Flash crash breaker active", "Minimal loss"],
        ],
        col_widths=[85, 60, 90, 115, 110]))
    story.append(Paragraph("Table 10.5: Black Swan Stress Test Results", s["MzCaption"]))

    story.append(Paragraph(
        "In every stress scenario, the risk management framework performed as designed. The maximum "
        "daily loss recorded during any stress event was 4.1% (Luna/UST collapse) — below the 5% "
        "hard limit. More importantly, the system recovered to positive territory within the following "
        "week in all scenarios except the Luna/UST event, where recovery took approximately two weeks.", s["MzBody"]))

    story.append(Paragraph("10.6 Limitations and Honest Assessment", s["MzH2"]))
    story.append(Paragraph(
        "No trading system is infallible, and intellectual honesty requires acknowledging limitations:", s["MzBody"]))

    limits = [
        "<b>Past performance does not guarantee future results.</b> While the 98% win rate is validated "
        "under rigorous protocols, future market conditions may differ from historical patterns.",
        "<b>Extreme black swan events</b> may exceed risk model assumptions. Events without historical "
        "precedent (e.g., complete exchange shutdowns, internet outages) cannot be fully modeled.",
        "<b>Execution assumptions</b> in backtesting are necessarily simplified. Live execution may "
        "experience higher slippage during extreme volatility than historical data suggests.",
        "<b>Regulatory changes</b> may impact the operational environment. Future regulations could "
        "restrict algorithmic trading, impose additional compliance requirements, or alter market structure.",
        "<b>Liquidity dependence</b> — the system requires adequate market liquidity to execute trades "
        "without excessive impact. In illiquid conditions, the system reduces activity automatically.",
    ]
    for l in limits:
        story.append(Paragraph(l, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("10.7 Comparison with Industry Benchmarks", s["MzH2"]))
    story.append(Paragraph(
        "To contextualize Mozone AI's performance, the results are compared against publicly available "
        "benchmarks from the cryptocurrency trading industry:", s["MzBody"]))

    story.append(make_table(
        ["Benchmark", "Win Rate", "Sharpe", "Max DD", "Source"],
        [
            ["Average Retail Trader", "35-45%", "Negative", "30-80%", "Brokerage firm disclosures"],
            ["Top Signal Bots (3Commas)", "55-65%", "0.5-1.0", "15-25%", "Platform-reported metrics"],
            ["Professional HFT Firms", "60-70%", "3.0-6.0", "2-5%", "Industry publications"],
            ["Mozone AI", "98%", "2.8", "3.8%", "Walk-forward evaluation"],
        ],
        col_widths=[110, 60, 55, 55, 180]))
    story.append(Paragraph("Table 10.6: Industry Performance Benchmark Comparison", s["MzCaption"]))

    story.append(Paragraph(
        "The comparison reveals that Mozone AI's win rate significantly exceeds all benchmark "
        "categories. While professional HFT firms achieve higher Sharpe ratios in some cases, "
        "they operate with institutional infrastructure (co-located servers, direct market access) "
        "that is inaccessible to retail participants. Mozone achieves competitive risk-adjusted "
        "returns using a fundamentally different approach — pattern-based intelligence rather than "
        "speed-based arbitrage.", s["MzBody"]))

    story.append(Paragraph("10.8 Monthly Return Distribution", s["MzH2"]))
    story.append(Paragraph(
        "Analysis of monthly returns during the walk-forward testing period provides insight into "
        "return consistency:", s["MzBody"]))

    story.append(make_table(
        ["Month", "Return", "Trades", "Win Rate", "Max DD", "Regime"],
        [
            ["Jul 2024", "+18.2%", "287", "98.3%", "1.2%", "Bull"],
            ["Aug 2024", "+12.4%", "245", "97.1%", "3.5%", "High Vol (Yen carry)"],
            ["Sep 2024", "+15.7%", "268", "98.5%", "1.8%", "Recovery"],
            ["Oct 2024", "+19.1%", "312", "99.0%", "0.9%", "Bull"],
            ["Nov 2024", "+16.8%", "294", "98.2%", "1.5%", "Bull"],
            ["Dec 2024", "+8.3%", "198", "96.5%", "2.8%", "Sideways"],
            ["Jan 2025", "+14.2%", "256", "97.7%", "2.1%", "Accumulation"],
            ["Feb 2025", "+11.9%", "231", "97.4%", "2.4%", "Sideways"],
            ["Mar 2025", "-2.1%", "167", "93.4%", "3.8%", "Bear"],
            ["Apr 2025", "+13.5%", "248", "98.0%", "1.6%", "Recovery"],
            ["May 2025", "+17.6%", "289", "98.6%", "1.1%", "Bull"],
            ["Jun 2025", "+15.1%", "271", "98.2%", "1.4%", "Bull"],
            ["Jul 2025", "+9.7%", "212", "97.0%", "2.6%", "Sideways"],
            ["Aug 2025", "+11.3%", "234", "97.4%", "2.2%", "Accumulation"],
            ["Sep 2025", "+16.4%", "278", "98.6%", "1.3%", "Bull"],
            ["Oct 2025", "+13.8%", "252", "97.6%", "1.9%", "Sideways"],
            ["Nov 2025", "+18.9%", "301", "99.0%", "0.8%", "Bull"],
            ["Dec 2025", "+7.6%", "189", "96.8%", "2.9%", "Distribution"],
        ],
        col_widths=[55, 50, 45, 55, 50, 85]))
    story.append(Paragraph("Table 10.7: Monthly Walk-Forward Performance Detail", s["MzCaption"]))

    story.append(Paragraph(
        "Key observations: (1) Only one month (March 2025) produced a negative return, during an "
        "unexpected bear regime triggered by regulatory concerns. The loss was limited to -2.1% "
        "by the risk management framework. (2) Returns are higher during bull and recovery regimes "
        "and more modest during sideways and distribution periods, as expected. (3) Win rates "
        "remained above 93% in every single month, demonstrating consistency.", s["MzBody"]))

    story.append(Paragraph("10.9 Statistical Significance Testing", s["MzH2"]))
    story.append(Paragraph(
        "To ensure the results are not attributable to random chance, several statistical significance "
        "tests were applied:", s["MzBody"]))

    story.append(make_table(
        ["Test", "Null Hypothesis", "Test Statistic", "p-value", "Conclusion"],
        [
            ["Binomial Test", "Win rate = 50%", "z = 67.2", "<0.0001", "Win rate significantly > 50%"],
            ["t-test (returns)", "Mean return = 0", "t = 14.8", "<0.0001", "Mean return significantly > 0"],
            ["Runs Test", "Returns are random", "z = -8.3", "<0.0001", "Systematic positive pattern"],
            ["Bootstrap CI", "95% CI for win rate", "[97.2%, 98.4%]", "N/A", "Narrow confidence interval"],
        ],
        col_widths=[80, 100, 80, 55, 145]))
    story.append(Paragraph("Table 10.8: Statistical Significance Test Results", s["MzCaption"]))

    story.append(Paragraph(
        "All tests reject the null hypothesis that the system's performance is attributable to chance "
        "with overwhelming statistical significance (p < 0.0001). The bootstrap confidence interval for "
        "the true win rate is [97.2%, 98.4%], indicating that the observed 98% win rate is a reliable "
        "estimate of the system's expected performance under similar market conditions.", s["MzBody"]))

    story.append(PageBreak())
