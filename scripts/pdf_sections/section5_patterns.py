from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section5(story, s, make_table, hr):
    """Pattern Recognition Engine — pages 22-27."""
    story.append(Paragraph("5. Pattern Recognition Engine — 200M+ Dataset", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph("5.1 What Constitutes a 'Pattern'", s["MzH2"]))
    story.append(Paragraph(
        "The pattern library is the core intellectual property of Mozone AI and the primary source of "
        "predictive capability. A 'pattern' in the Mozone system is fundamentally different from simplistic "
        "technical analysis constructs like candlestick formations or moving average crossovers. Each "
        "pattern is a structured, multi-dimensional representation of market behavior that captures the "
        "full context of a trading situation:", s["MzBody"]))

    story.append(make_table(
        ["Dimension", "Components", "Example Features"],
        [
            ["Price Behavior", "Returns, trend, momentum, fractal structure",
             "5-bar return: +0.8%, momentum: up"],
            ["Volume Dynamics", "Volume profile, accum/dist, VWAP dev",
             "Vol: 2.3x avg, buy ratio: 65%"],
            ["Regime", "Volatility, trend, correlation regime",
             "High vol, bullish, BTC corr: 0.82"],
            ["Cross-Market", "BTC dominance, sector rotation, TVL",
             "BTC.D: declining, DeFi TVL: up"],
            ["Event Context", "News sentiment, social mentions, regulatory",
             "Positive, medium urgency, [BNB]"],
            ["Temporal", "Time-of-day, day-of-week, event proximity",
             "14 UTC, Tuesday, 2h post-FOMC"],
        ],
        col_widths=[85, 175, 200]))
    story.append(Paragraph("Table 5.1: Pattern Dimensionality", s["MzCaption"]))

    story.append(Paragraph(
        "This multi-dimensional representation ensures that pattern matching captures not just what happened "
        "to price, but the full market context in which it happened. Two identical price movements occurring "
        "in different regimes, with different volume profiles, and different news contexts are treated as "
        "fundamentally different patterns — because their forward return distributions are statistically "
        "different.", s["MzBody"]))

    story.append(Paragraph("5.2 Pattern Labeling Methodology", s["MzH2"]))
    story.append(Paragraph(
        "Each pattern in the library is paired with comprehensive labeled outcomes describing what "
        "happened after the pattern was observed historically:", s["MzBody"]))

    labels = [
        "<b>Forward return distributions</b> — Probability distributions of returns at 1-hour, "
        "4-hour, 24-hour, and 7-day horizons, capturing expected value and uncertainty.",
        "<b>Maximum drawdown profiles</b> — Worst-case intra-trade drawdown before eventual "
        "outcome, critical for stop-loss calibration.",
        "<b>Time-to-profit metrics</b> — Distribution of time to reach profit target, enabling "
        "time-based exit decisions.",
        "<b>Post-event volatility</b> — How volatility evolved after the pattern, informing "
        "position sizing decisions.",
        "<b>Regime transition probabilities</b> — Likelihood that the pattern preceded a regime "
        "change, enabling proactive risk adjustment.",
    ]
    for l in labels:
        story.append(Paragraph(l, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("5.3 Dataset Scale and Coverage", s["MzH2"]))

    story.append(make_table(
        ["Market Regime", "Count", "% of Dataset", "Date Range"],
        [
            ["Bull Market (sustained uptrend)", "52M", "26%", "2017-18, 2020-21, 2024-25"],
            ["Bear Market (sustained downtrend)", "38M", "19%", "2018-19, 2022, partial 2025"],
            ["Sideways / Range-bound", "44M", "22%", "Various consolidation periods"],
            ["High-Volatility Cascades", "30M", "15%", "Flash crashes, liquidation events"],
            ["Accumulation Phases", "24M", "12%", "Pre-breakout quiet periods"],
            ["Distribution Phases", "12M", "6%", "Pre-breakdown events"],
        ],
        col_widths=[140, 50, 70, 200]))
    story.append(Paragraph("Table 5.2: Pattern Dataset Composition by Market Regime", s["MzCaption"]))

    story.append(Paragraph(
        "The deliberate over-representation of bull and sideways markets reflects the statistical "
        "distribution of historical market time in each regime. The dataset is periodically rebalanced "
        "as new patterns are collected from live operation, particularly for rarer cascade events.", s["MzBody"]))

    story.append(Paragraph(
        "Geographic and exchange diversity is also maintained. Patterns are sourced from 20+ exchanges "
        "across all major time zones, ensuring the library represents global market behavior rather than "
        "being biased toward any single venue or region. This diversity is essential because market "
        "microstructure varies significantly between venues.", s["MzBody"]))

    story.append(Paragraph("5.4 Matching Algorithm", s["MzH2"]))
    story.append(Paragraph(
        "The pattern matching algorithm uses a weighted multi-dimensional distance metric comparing "
        "the current market state against all patterns. It operates in three stages:", s["MzBody"]))

    stages = [
        "<b>Stage 1: Regime Filtering</b> — Current regime is classified and the search space narrowed "
        "to same or adjacent regimes, reducing comparisons from 200M+ to ~30-50M patterns.",
        "<b>Stage 2: Approximate Nearest Neighbors</b> — Using locality-sensitive hashing (LSH), the "
        "top 1,000 candidates are identified in sub-linear time relative to dataset size.",
        "<b>Stage 3: Exact Ranking</b> — The 1,000 candidates are evaluated using the full weighted "
        "distance metric. Top 50 matches contribute weighted votes for consensus signal generation.",
    ]
    for st in stages:
        story.append(Paragraph(st, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph(
        "The consensus mechanism requires at least 30 of the top 50 matches (60%) to agree on direction "
        "for a valid signal. This supermajority requirement dramatically reduces false positives at the "
        "cost of occasionally missing marginal opportunities — a tradeoff that aligns with the risk-first "
        "design philosophy.", s["MzBody"]))

    story.append(Paragraph("5.5 Distance Metric Design", s["MzH2"]))
    story.append(Paragraph(
        "The weighted distance metric assigns different importance to each pattern dimension based on "
        "empirically determined predictive power:", s["MzBody"]))

    story.append(make_table(
        ["Dimension", "Weight", "Rationale"],
        [
            ["Price Behavior", "35%", "Most directly predictive of forward returns"],
            ["Volume Dynamics", "25%", "Volume confirmation is second most predictive"],
            ["Regime Context", "15%", "Same price pattern has different outcomes in different regimes"],
            ["Cross-Market", "10%", "Provides confirmation but less direct causation"],
            ["News/Event", "10%", "Catalytic context, not standalone predictor"],
            ["Temporal", "5%", "Useful for time-of-day effects but least predictive"],
        ],
        col_widths=[100, 55, 305]))
    story.append(Paragraph("Table 5.3: Distance Metric Weight Distribution", s["MzCaption"]))

    story.append(Paragraph("5.6 Continuous Learning Protocol", s["MzH2"]))
    story.append(Paragraph(
        "The pattern library grows continuously as the system processes live market data. Pattern addition "
        "follows strict quality criteria to prevent library contamination:", s["MzBody"]))

    story.append(Paragraph(
        "New patterns must achieve minimum 80% confidence in out-of-sample validation before library "
        "admission. Patterns enter a 30-day staging area for forward evaluation. Only patterns "
        "demonstrating predictive power exceeding random chance by a statistically significant margin "
        "(p < 0.01) are promoted to the active library. Degrading patterns are automatically deprecated "
        "through periodic maintenance cycles.", s["MzBody"]))

    story.append(Paragraph(
        "The expected growth rate of the pattern library is approximately 500,000-1,000,000 new validated "
        "patterns per month during normal market conditions, with accelerated growth during high-volatility "
        "periods that generate novel market behaviors. At this rate, the library will exceed 250M patterns "
        "within the first year of live operation.", s["MzBody"]))

    story.append(Paragraph("5.7 Pattern Obsolescence Management", s["MzH2"]))
    story.append(Paragraph(
        "Not all patterns remain predictive indefinitely. Market microstructure evolves, regulatory changes "
        "alter participant behavior, and technological advances change execution dynamics. The system "
        "implements a pattern aging mechanism that gradually reduces the weight of older patterns in the "
        "matching process. Patterns older than 3 years receive a 50% weight reduction, and patterns older "
        "than 5 years are archived unless they demonstrate continued predictive relevance in periodic "
        "validation cycles.", s["MzBody"]))

    story.append(Paragraph("5.8 Pattern Validation Framework", s["MzH2"]))
    story.append(Paragraph(
        "To ensure the pattern library maintains its predictive quality, a comprehensive validation "
        "framework is applied both during initial pattern admission and during ongoing maintenance. "
        "The framework evaluates patterns along four dimensions:", s["MzBody"]))

    story.append(make_table(
        ["Dimension", "Metric", "Minimum Threshold", "Evaluation Method"],
        [
            ["Predictive Power", "Information Coefficient", ">0.05", "Rank correlation of prediction vs outcome"],
            ["Statistical Significance", "p-value", "<0.01", "Permutation test against random predictions"],
            ["Robustness", "Stability Ratio", ">0.7", "Performance consistency across time sub-periods"],
            ["Generalizability", "Cross-Asset Transfer", ">60% retention", "Pattern tested on unseen assets"],
        ],
        col_widths=[95, 100, 95, 170]))
    story.append(Paragraph("Table 5.4: Pattern Validation Framework Dimensions", s["MzCaption"]))

    story.append(Paragraph(
        "The Information Coefficient measures the rank correlation between predicted and actual returns. "
        "An IC of 0.05 may appear low, but in financial prediction, even small positive ICs compound into "
        "significant edge when applied consistently across thousands of trades. The permutation test "
        "generates 10,000 random permutations of the prediction labels and compares the observed IC "
        "against this null distribution — only patterns where the observed IC exceeds 99% of random "
        "permutations are considered statistically significant.", s["MzBody"]))

    story.append(Paragraph(
        "The stability ratio measures whether a pattern's predictive power is consistent across "
        "different time periods or concentrated in a single lucky period. The evaluation data is "
        "split into three equal sub-periods, and the pattern is evaluated independently on each. "
        "The stability ratio is the minimum sub-period IC divided by the maximum — a ratio of 1.0 "
        "indicates perfectly consistent performance across all periods, while a ratio near 0 indicates "
        "that the pattern only works in one specific period (likely overfit).", s["MzBody"]))

    story.append(Paragraph("5.9 Computational Infrastructure", s["MzH2"]))
    story.append(Paragraph(
        "Processing a library of 200M+ patterns in real-time requires specialized computational "
        "infrastructure. The pattern matching pipeline is designed for maximum throughput with "
        "minimal latency:", s["MzBody"]))

    story.append(make_table(
        ["Component", "Specification", "Purpose"],
        [
            ["Pattern Storage", "Distributed key-value store with in-memory indexing", "Sub-millisecond pattern retrieval"],
            ["LSH Index", "128-bit hash signatures with 64 hash tables", "Approximate nearest neighbor in O(1) amortized"],
            ["Distance Computation", "Vectorized operations on SIMD-capable hardware", "Parallel distance calculation for 1000 candidates"],
            ["Consensus Engine", "Weighted voting with threshold filtering", "Aggregate 50 match votes into single signal"],
            ["Cache Layer", "LRU cache for recently matched patterns", "Avoid redundant computation for correlated queries"],
        ],
        col_widths=[100, 190, 170]))
    story.append(Paragraph("Table 5.5: Pattern Matching Computational Infrastructure", s["MzCaption"]))

    story.append(Paragraph(
        "The total end-to-end latency from feature vector construction to signal output averages "
        "under 3 seconds in production conditions. This includes regime filtering (200ms), LSH lookup "
        "(500ms), exact distance computation for top 1,000 candidates (1,500ms), and consensus "
        "aggregation (300ms). The remaining budget is consumed by data serialization and network "
        "transfer between pipeline stages.", s["MzBody"]))

    story.append(Paragraph("5.10 Comparison with Alternative Approaches", s["MzH2"]))
    story.append(Paragraph(
        "The pattern-based approach was selected after extensive comparison with alternative "
        "prediction methodologies:", s["MzBody"]))

    story.append(make_table(
        ["Approach", "Advantage", "Disadvantage", "Mozone Assessment"],
        [
            ["Deep Neural Networks", "Can learn complex nonlinear relationships", "Black box; overfit-prone; hard to interpret",
             "Used in sentiment model, not in core trading"],
            ["Reinforcement Learning", "Optimizes for cumulative reward directly", "Unstable training; poor sample efficiency",
             "Research stage; not production-ready for trading"],
            ["Statistical Arbitrage", "Well-understood mathematical framework", "Assumes stationarity; breaks in regime changes",
             "Incorporated as one ensemble component"],
            ["Pattern Matching (Mozone)", "Interpretable; regime-aware; naturally adaptive", "Requires large curated dataset",
             "Core approach — 200M+ pattern advantage"],
        ],
        col_widths=[90, 115, 120, 135]))
    story.append(Paragraph("Table 5.6: Comparison of Prediction Approaches", s["MzCaption"]))

    story.append(Paragraph(
        "The key advantage of pattern matching over opaque deep learning is interpretability. When "
        "Mozone generates a trade signal, it can point to the specific historical analogs that informed "
        "the decision. This transparency is valuable for three reasons: (1) it enables human review and "
        "validation, (2) it facilitates debugging when the system underperforms, and (3) it builds user "
        "trust by showing the evidence behind each decision.", s["MzBody"]))

    story.append(PageBreak())
