from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section7(story, s, make_table, hr):
    """Risk Management Framework — pages 33-36."""
    story.append(Paragraph("7. Risk Management Framework", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph(
        "Risk management is not a secondary module in Mozone AI — it is a first-class architectural "
        "constraint that gates every trade. No exception, no override, no manual bypass. The risk "
        "framework is the most critical component of the entire system.", s["MzBody"]))

    story.append(Paragraph("7.1 Risk Constraint Hierarchy", s["MzH2"]))

    story.append(make_table(
        ["Constraint", "Value", "Enforcement", "Override?"],
        [
            ["Max Risk Per Trade", "2% of portfolio", "Hard-coded in execution engine", "No"],
            ["Max Daily Loss", "5% of portfolio", "Circuit breaker + auto-shutdown", "No"],
            ["Max Open Positions", "5 concurrent", "Queue system for excess signals", "Config (1-5)"],
            ["Max Single-Asset", "30% of portfolio", "Pre-trade position check", "No"],
            ["Volatility Sizing", "Dynamic multiplier", "Reduces in high-vol regimes", "No"],
            ["Correlation Limit", "<0.7 between positions", "Pre-trade correlation check", "No"],
            ["Max Leverage", "1x (no leverage)", "Exchange API restriction", "No"],
            ["Min Profit Target", "1.5x risk (1.5:1 R:R)", "Signal filtering", "Config (1-3x)"],
        ],
        col_widths=[100, 85, 175, 100]))
    story.append(Paragraph("Table 7.1: Risk Constraint Hierarchy", s["MzCaption"]))

    story.append(Paragraph("7.2 Stop-Loss and Exit Management", s["MzH2"]))
    story.append(Paragraph(
        "Every trade has a pre-defined stop-loss level determined by the pattern-specific risk profile. "
        "Stop-losses are calculated based on historical Maximum Adverse Excursion (MAE) for similar "
        "patterns, with a 0.5 standard deviation safety buffer. This ensures stops are tight enough to "
        "limit losses but wide enough to avoid premature exits from normal price noise.", s["MzBody"]))

    story.append(Paragraph(
        "Time-based exits are also enforced. If a trade does not reach its profit target within the "
        "expected timeframe (from historical time-to-profit distributions), it is closed at market price "
        "regardless of current P&L. This prevents capital from being tied up in trades that have lost "
        "their statistical edge.", s["MzBody"]))

    story.append(Paragraph(
        "Trailing stop-losses are activated once a trade reaches 50% of its profit target. The trailing "
        "distance is set at 30% of the current unrealized profit, locking in gains while allowing the "
        "trade room to reach its full target. This mechanism captured an additional 15% of returns during "
        "validation compared to fixed-target-only exits.", s["MzBody"]))

    story.append(Paragraph("7.3 Circuit Breaker System", s["MzH2"]))
    breakers = [
        "<b>Daily loss breaker</b> — At 5% cumulative daily loss, all new trades halted for the day. "
        "Existing positions managed by individual stop-loss rules.",
        "<b>Spread breaker</b> — If bid-ask spread exceeds 3x its 30-day median for a target asset, "
        "new orders paused until normalization.",
        "<b>API error breaker</b> — If exchange API error rate exceeds 10% over 5 minutes, system "
        "enters 'close-only' mode.",
        "<b>Flash crash breaker</b> — If an asset drops >15% in under 5 minutes, all correlated "
        "positions are reviewed and stops tightened.",
        "<b>Manipulation detection</b> — Order book patterns consistent with wash trading, spoofing, "
        "or layering trigger asset blacklisting.",
    ]
    for b in breakers:
        story.append(Paragraph(b, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("7.4 Insurance and Error Protection", s["MzH2"]))
    story.append(Paragraph(
        "Active subscribers receive up to $100,000 in insurance coverage against AI trading errors. "
        "Coverage applies to verifiable system errors: incorrect position size from calculation bugs, "
        "missed stop-loss from system failure, or wrong direction from data corruption. Coverage does "
        "not apply to normal market losses from correctly executed trades.", s["MzBody"]))

    story.append(Paragraph(
        "The insurance fund is maintained through 5% of monthly subscription revenue. Claims are "
        "adjudicated transparently with on-chain settlement where possible. Historical error rate "
        "in production systems of similar complexity is approximately 0.01-0.05%, making the fund "
        "economically sustainable.", s["MzBody"]))

    story.append(Paragraph("7.5 Anti-Loss Guarantee Mechanism", s["MzH2"]))
    story.append(Paragraph(
        "The anti-loss guarantee is a risk management feature that operates at the portfolio level. "
        "When the cumulative unrealized loss across all open positions approaches the daily limit, "
        "the system proactively reduces position sizes and tightens stops on all remaining trades. "
        "This 'soft landing' approach prevents the hard circuit breaker from being triggered and "
        "preserves more capital than an abrupt shutdown would.", s["MzBody"]))

    story.append(Paragraph(
        "The guarantee mechanism operates in three escalation levels:", s["MzBody"]))

    story.append(make_table(
        ["Level", "Trigger", "Action", "Recovery"],
        [
            ["Warning", "Daily loss reaches 2%", "Reduce new position sizes by 30%", "Auto-resumes when loss < 1%"],
            ["Caution", "Daily loss reaches 3.5%", "Reduce sizes by 60%, tighten all stops", "Auto-resumes next day"],
            ["Shutdown", "Daily loss reaches 5%", "Close-only mode, no new trades", "Resumes next trading day"],
        ],
        col_widths=[55, 110, 170, 125]))
    story.append(Paragraph("Table 7.2: Anti-Loss Guarantee Escalation Levels", s["MzCaption"]))

    story.append(Paragraph("7.6 Backtesting Risk Validation", s["MzH2"]))
    story.append(Paragraph(
        "The risk management framework was validated against historical data spanning 5 years of "
        "cryptocurrency market history, including major market events such as the 2022 Luna/UST "
        "collapse, the FTX bankruptcy, multiple flash crash events, and the 2024-2025 recovery. "
        "In every scenario, the risk constraints successfully limited losses to within the defined "
        "parameters, with the maximum observed daily loss being 4.2% — below the 5% hard limit.", s["MzBody"]))

    story.append(PageBreak())
