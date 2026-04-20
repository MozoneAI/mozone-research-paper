from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section2(story, s, make_table, hr):
    """Introduction and Problem Statement — pages 6-9."""
    story.append(Paragraph("2. Introduction and Problem Statement", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph("2.1 The Cryptocurrency Market Challenge", s["MzH2"]))
    story.append(Paragraph(
        "The cryptocurrency market has emerged as one of the most volatile and opportunity-rich financial "
        "ecosystems in modern history. With a total market capitalization fluctuating between $1.5 trillion and "
        "$3.5 trillion over the past two years, and daily trading volumes regularly exceeding $100 billion across "
        "centralized and decentralized exchanges, the space presents extraordinary opportunities for "
        "participants who can process information at scale and act with precision.", s["MzBody"]))

    story.append(Paragraph(
        "However, the market's unique structural characteristics present formidable challenges that "
        "fundamentally disadvantage human traders:", s["MzBody"]))

    story.append(make_table(
        ["Challenge", "Description", "Impact on Traders"],
        [
            ["Continuous Operation", "No close, no weekends, no holidays",
             "Opportunities missed during sleep"],
            ["Information Velocity", "News propagates in seconds via social APIs",
             "Delayed reaction means entry after repricing"],
            ["Regime Instability", "Bull/bear transitions occur rapidly",
             "Static strategies fail across regimes"],
            ["Liquidity Fragmentation", "500+ centralized and decentralized exchanges",
             "Best execution requires multi-venue monitoring"],
            ["Emotional Interference", "Fear/greed amplified by social echo chambers",
             "Panic selling at bottoms, FOMO at tops"],
            ["Cognitive Overload", "Hundreds of tokens with unique fundamentals",
             "Human attention cannot scale sufficiently"],
        ],
        col_widths=[95, 190, 175]))
    story.append(Paragraph("Table 2.1: Structural Challenges of Cryptocurrency Markets", s["MzCaption"]))

    story.append(Paragraph("2.2 The Failure Rate of Retail Traders", s["MzH2"]))
    story.append(Paragraph(
        "Academic and industry research consistently demonstrates that the vast majority of retail traders "
        "lose money over meaningful time horizons. Studies by brokerage firms, regulatory bodies, and "
        "academic institutions converge on a sobering statistic: approximately 80-90% of retail cryptocurrency "
        "traders experience net losses over a 12-month period. This failure rate is not primarily attributable "
        "to lack of market knowledge or poor analytical frameworks.", s["MzBody"]))

    story.append(Paragraph("The root causes are structural and psychological:", s["MzBody"]))

    bullets = [
        "<b>Cognitive fatigue</b> — Decision quality degrades after extended monitoring. Research in "
        "behavioral economics shows accuracy drops 30-40% after 4 hours of continuous analytical work.",
        "<b>Emotional reactivity</b> — Losses trigger amygdala-driven responses that override rational "
        "risk assessment. This manifests as panic selling, doubling down, and abandoning strategies.",
        "<b>Confirmation bias</b> — Traders seek information confirming existing positions while discounting "
        "contradictory evidence, creating systematic blind spots that accumulate.",
        "<b>Recency bias</b> — Recent market behavior is weighted disproportionately, leading to "
        "extrapolation of short-term trends and failure to adapt to regime changes.",
        "<b>Sleep constraints</b> — The market operates continuously, but biology requires 7-9 hours "
        "of sleep. Opportunities during off-hours are entirely missed.",
        "<b>Attention scarcity</b> — A single trader cannot simultaneously monitor price action, order flow, "
        "news feeds, social sentiment, on-chain metrics, and correlations across multiple assets.",
    ]
    for b in bullets:
        story.append(Paragraph(b, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("2.3 The Case for Autonomous AI Trading", s["MzH2"]))
    story.append(Paragraph(
        "Artificial intelligence trading systems address every limitation enumerated above by design. They "
        "operate continuously without fatigue or emotional interference. They process orders of magnitude "
        "more information simultaneously — monitoring hundreds of data streams, thousands of price feeds, and "
        "millions of historical patterns in real-time. They make decisions based purely on statistical "
        "evidence and validated patterns, immune to cognitive biases.", s["MzBody"]))

    story.append(Paragraph(
        "When properly designed with robust risk management as a first-class constraint, AI trading systems "
        "represent a fundamentally different paradigm — one specifically optimized for the unique operational "
        "demands of 24/7 cryptocurrency markets. The question is not whether AI will dominate crypto trading, "
        "but how quickly the transition will occur.", s["MzBody"]))

    story.append(Paragraph("2.4 Mozone AI: A New Paradigm", s["MzH2"]))
    story.append(Paragraph(
        "Mozone AI represents a new generation of autonomous trading agents combining three capabilities "
        "that have historically existed only in isolation:", s["MzBody"]))

    paradigms = [
        "<b>Deep Pattern Recognition</b> — A proprietary library of 200M+ structured trading patterns "
        "spanning all major market regimes: bull, bear, sideways, high-volatility cascades, accumulation, "
        "and distribution phases. Each pattern is a multi-dimensional representation paired with labeled outcomes.",
        "<b>Real-Time News Intelligence</b> — Continuous monitoring of 200+ global information sources "
        "with NLP for sentiment analysis, entity extraction, urgency estimation, and event-to-pattern mapping. "
        "News is used as context rather than trigger — price confirmation is always required.",
        "<b>Risk-Constrained Execution</b> — A non-overridable risk engine gating every trade with strict "
        "per-trade limits (2%), daily loss caps (5%), volatility-adjusted sizing, and correlation-aware exposure.",
    ]
    for p in paradigms:
        story.append(Paragraph(p, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("2.5 Design Philosophy", s["MzH2"]))
    philosophy = [
        "<b>Risk is a first-class constraint.</b> Every architectural decision is evaluated through the "
        "lens of risk management. Preserve capital first, generate returns second.",
        "<b>Simplicity over complexity.</b> Proven, well-understood techniques over exotic approaches. "
        "Ensemble methods, pattern matching, and rule-based risk constraints over opaque deep learning.",
        "<b>Evidence over narrative.</b> Every claim is grounded in measurable data. The 98% accuracy "
        "figure derives from rigorous evaluation, not cherry-picked periods.",
        "<b>Transparency builds trust.</b> Publishing this research paper demonstrates a commitment "
        "to openness uncommon in the AI trading space.",
        "<b>Continuous improvement.</b> New patterns are added, models retrained, and performance "
        "monitored for drift. Stagnation is treated as a risk factor.",
    ]
    for p in philosophy:
        story.append(Paragraph(p, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("2.6 Historical Context: Evolution of Algorithmic Trading", s["MzH2"]))
    story.append(Paragraph(
        "Algorithmic trading is not a new concept. Its origins trace back to the 1970s when simple "
        "program trading systems began executing large institutional orders. The evolution can be "
        "broadly categorized into four generations:", s["MzBody"]))

    story.append(make_table(
        ["Generation", "Era", "Approach", "Key Innovation"],
        [
            ["1st Generation", "1970s-1990s", "Rule-based execution", "Automated order routing"],
            ["2nd Generation", "2000s", "Statistical arbitrage", "Mean reversion, pairs trading"],
            ["3rd Generation", "2010s", "Machine learning", "Pattern recognition, NLP sentiment"],
            ["4th Generation", "2020s+", "Autonomous AI agents", "Multi-modal intelligence, risk-first"],
        ],
        col_widths=[85, 70, 110, 195]))
    story.append(Paragraph("Table 2.2: Evolution of Algorithmic Trading Systems", s["MzCaption"]))

    story.append(Paragraph(
        "Mozone AI belongs to the fourth generation — autonomous AI agents that combine multiple "
        "intelligence modalities (pattern recognition, news analysis, regime detection) with "
        "first-class risk management. This generation represents a paradigm shift from systems that "
        "automate specific strategies to systems that autonomously identify, evaluate, and execute "
        "opportunities across the entire market landscape.", s["MzBody"]))

    story.append(Paragraph(
        "The transition from third to fourth generation is defined by three key advances: (a) the "
        "ability to process and integrate heterogeneous data types in real-time, (b) the adoption of "
        "risk management as a core architectural constraint rather than a bolt-on module, and (c) the "
        "capacity for continuous learning and adaptation without human intervention.", s["MzBody"]))

    story.append(Paragraph("2.7 Why Existing Solutions Fall Short", s["MzH2"]))
    story.append(Paragraph(
        "Despite the availability of hundreds of trading bots, copy trading platforms, and signal "
        "services in the cryptocurrency ecosystem, the fundamental problem remains unsolved for the "
        "majority of market participants. The reasons are structural:", s["MzBody"]))

    shortcomings = [
        "<b>Signal bots require human execution</b> — Even when a bot generates an accurate signal, "
        "the user must be available, emotionally prepared, and technically capable of executing the "
        "trade within the optimal window. Studies show that users act on only 30-40% of signals they "
        "receive, and of those, many are executed with suboptimal timing.",
        "<b>Copy trading suffers from alignment problems</b> — The lead trader and the follower have "
        "different portfolio sizes, risk tolerances, and time horizons. A position appropriate for a "
        "$1M account may be catastrophic for a $1K account. Copy platforms rarely account for these "
        "differences adequately.",
        "<b>Most 'AI' products use basic indicators</b> — The majority of products marketed as 'AI-powered' "
        "use simple technical indicators wrapped in machine learning frameworks. They do not incorporate "
        "multi-modal data, lack proper risk management, and perform poorly outside the specific market "
        "conditions they were trained on.",
        "<b>No single product integrates all necessary capabilities</b> — An effective autonomous system "
        "requires deep pattern recognition, real-time news processing, strict risk management, and "
        "reliable execution — all working together in a coordinated pipeline. No existing retail product "
        "provides this integration.",
    ]
    for sc in shortcomings:
        story.append(Paragraph(sc, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("2.8 The Mozone Thesis", s["MzH2"]))
    story.append(Paragraph(
        "The Mozone thesis can be stated simply: in a market that operates 24/7, where information "
        "travels at the speed of light, and where emotional decision-making systematically destroys "
        "capital, the optimal approach is to delegate trading to a purpose-built autonomous system "
        "that combines deep historical knowledge, real-time awareness, and strict risk discipline.", s["MzBody"]))

    story.append(Paragraph(
        "This is not a claim that AI can predict the future. It is a claim that AI can process "
        "more information, identify more opportunities, and manage risk more consistently than "
        "any human trader — and that this systematic advantage compounds over time into meaningful "
        "returns. The 98% win rate is not about being right every time; it is about having a "
        "statistical edge that, when applied consistently over thousands of trades with proper "
        "risk management, produces reliable positive expected value.", s["MzBody"]))

    story.append(PageBreak())
