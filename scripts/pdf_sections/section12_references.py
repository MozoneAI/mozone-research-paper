from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section12(story, s, make_table, hr):
    """References and Appendix — pages 53-55."""
    story.append(Paragraph("12. References and Appendix", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph("12.1 Academic References", s["MzH2"]))

    refs = [
        "[1] Bao, W., Yue, J., & Rao, Y. (2017). A deep learning framework for financial time series using "
        "stacked autoencoders and long-short term memory. <i>PLOS ONE</i>, 12(7), e0180944.",
        "[2] Fischer, T., & Krauss, C. (2018). Deep learning with long short-term memory networks for "
        "financial market predictions. <i>European Journal of Operational Research</i>, 270(2), 654-669.",
        "[3] Jiang, Z., Xu, D., & Liang, J. (2017). A deep reinforcement learning framework for the "
        "financial portfolio management problem. <i>arXiv preprint arXiv:1706.10059</i>.",
        "[4] Sezer, O. B., Gudelek, M. U., & Ozbayoglu, A. M. (2020). Financial time series forecasting "
        "with deep learning: A systematic literature review. <i>Applied Soft Computing</i>, 90, 106181.",
        "[5] Tsantekidis, A., Passalis, N., Tefas, A., et al. (2017). Using deep learning to detect price "
        "change indications in financial markets. <i>EUSIPCO 2017</i>.",
        "[6] Zhang, Z., Zohren, S., & Roberts, S. (2019). DeepLOB: Deep convolutional neural networks for "
        "limit order books. <i>IEEE Transactions on Signal Processing</i>, 67(11), 3001-3012.",
        "[7] Xu, Y., & Cohen, S. B. (2018). Stock movement prediction from tweets and historical prices. "
        "<i>Proceedings of ACL 2018</i>, 1970-1979.",
        "[8] Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, "
        "dictionaries, and 10-Ks. <i>The Journal of Finance</i>, 66(1), 35-65.",
        "[9] Lopez de Prado, M. (2018). <i>Advances in Financial Machine Learning</i>. John Wiley & Sons.",
        "[10] Aldridge, I. (2013). <i>High-Frequency Trading: A Practical Guide to Algorithmic Strategies "
        "and Trading Systems</i>. John Wiley & Sons.",
    ]
    for r in refs:
        story.append(Paragraph(r, s["MzRef"]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("12.2 Industry References", s["MzH2"]))
    industry_refs = [
        "[11] Allied Market Research. (2024). Algorithmic Trading Market — Global Opportunity Analysis and "
        "Industry Forecast, 2024-2028.",
        "[12] CoinGecko. (2025). Annual Crypto Industry Report 2025. Retrieved from coingecko.com/research.",
        "[13] Chainalysis. (2025). The 2025 Crypto Crime Report. Retrieved from chainalysis.com.",
        "[14] DefiLlama. (2026). BSC Total Value Locked Historical Data. Retrieved from defillama.com.",
        "[15] N8N GmbH. (2025). N8N Documentation — Self-Hosting Guide. Retrieved from docs.n8n.io.",
        "[16] Binance. (2025). BNB Smart Chain Technical Whitepaper. Retrieved from github.com/bnb-chain.",
        "[17] PancakeSwap. (2025). PancakeSwap V3 Documentation. Retrieved from docs.pancakeswap.finance.",
        "[18] CertiK. (2025). State of DeFi Security 2025. Retrieved from certik.com.",
    ]
    for r in industry_refs:
        story.append(Paragraph(r, s["MzRef"]))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("12.3 Technical Standards", s["MzH2"]))
    tech_refs = [
        "[19] ERC-20 Token Standard. Ethereum Improvement Proposal 20. ethereum.org.",
        "[20] BEP-20 Token Standard. BNB Chain Documentation. docs.bnbchain.org.",
        "[21] JSON Web Token (JWT) RFC 7519. Internet Engineering Task Force.",
        "[22] WebSocket Protocol RFC 6455. Internet Engineering Task Force.",
        "[23] HMAC-SHA256. FIPS PUB 198-1, NIST.",
    ]
    for r in tech_refs:
        story.append(Paragraph(r, s["MzRef"]))
    story.append(Spacer(1, 8*mm))

    # --- APPENDIX ---
    story.append(Paragraph("Appendix A: Glossary of Terms", s["MzH2"]))

    story.append(make_table(
        ["Term", "Definition"],
        [
            ["BSC", "Binance Smart Chain — EVM-compatible blockchain with low fees and fast finality"],
            ["BEP-20", "Token standard on BSC, equivalent to ERC-20 on Ethereum"],
            ["DeFi", "Decentralized Finance — financial services built on blockchain protocols"],
            ["DEX", "Decentralized Exchange — automated market maker for token trading"],
            ["AMM", "Automated Market Maker — algorithmic pricing for decentralized exchanges"],
            ["MAE", "Maximum Adverse Excursion — worst-case drawdown during an open position"],
            ["NLP", "Natural Language Processing — AI techniques for understanding text"],
            ["OHLCV", "Open-High-Low-Close-Volume — standard price data format"],
            ["PCA", "Principal Component Analysis — dimensionality reduction technique"],
            ["RSI", "Relative Strength Index — momentum oscillator (0-100)"],
            ["MACD", "Moving Average Convergence Divergence — trend-following indicator"],
            ["VWAP", "Volume Weighted Average Price — fair price benchmark"],
            ["ATR", "Average True Range — volatility measurement"],
            ["LSH", "Locality-Sensitive Hashing — approximate nearest neighbor technique"],
            ["N8N", "Open-source workflow automation platform (self-hostable)"],
            ["TVL", "Total Value Locked — aggregate deposits in DeFi protocols"],
            ["Sharpe Ratio", "Risk-adjusted return metric: (return - risk-free) / std deviation"],
            ["Walk-Forward", "Evaluation method simulating live trading with rolling windows"],
            ["MEV", "Miner/Maximal Extractable Value — profit from transaction ordering"],
            ["Slippage", "Difference between expected and actual execution price"],
            ["Regime", "Prevailing market condition (bull, bear, sideways, high-vol, etc.)"],
            ["Circuit Breaker", "Automated halt mechanism triggered by extreme conditions"],
            ["Ensemble", "Combination of multiple models for improved prediction accuracy"],
            ["IC", "Information Coefficient — rank correlation between predictions and outcomes"],
            ["RTO", "Recovery Time Objective — max acceptable downtime after failure"],
            ["RPO", "Recovery Point Objective — max acceptable data loss after failure"],
        ],
        col_widths=[75, 385]))
    story.append(Paragraph("Table A.1: Glossary of Technical Terms", s["MzCaption"]))
    story.append(Spacer(1, 8*mm))

    story.append(Paragraph("Appendix B: Frequently Asked Questions", s["MzH2"]))

    faqs = [
        ("<b>Q: Is Mozone AI a guaranteed way to make money?</b>", "A: No. While the system demonstrates "
         "a 98% win rate in rigorous evaluation, cryptocurrency trading always involves risk. Past "
         "performance does not guarantee future results. The system is designed to maximize the "
         "probability of positive outcomes while strictly limiting downside risk."),
        ("<b>Q: How is the 98% win rate calculated?</b>", "A: The 98% figure comes from walk-forward "
         "testing over 18 months (July 2024 - December 2025) across 4,847 trades. Walk-forward testing "
         "simulates live operation — the system only uses data available at the time of each decision."),
        ("<b>Q: Is $MZONE a security?</b>", "A: No. $MZONE is a utility token with specific functional "
         "use cases within the Mozone ecosystem: subscription discounts, boosted returns, referral "
         "multipliers, and insurance access. It does not confer ownership, equity, or dividend rights."),
        ("<b>Q: What happens if the AI makes an error?</b>", "A: Active subscribers with minimum $MZONE "
         "holdings receive up to $100,000 insurance coverage against verifiable AI trading errors. This "
         "covers execution bugs, missed stop-losses due to system failure, and data corruption events."),
        ("<b>Q: Can I lose more than I deposit?</b>", "A: No. Mozone AI operates at 1x (no leverage). "
         "The maximum loss is limited to the capital allocated for trading. The daily 5% loss limit "
         "further constrains potential losses."),
        ("<b>Q: Who controls my funds?</b>", "A: You do. Mozone AI operates on a non-custodial basis. "
         "The agent executes trades within your wallet or exchange account. You maintain full control "
         "at all times."),
        ("<b>Q: How do I withdraw my airdrop tokens?</b>", "A: Airdrop tokens can be withdrawn during "
         "scheduled withdrawal windows. Requirements: minimum 5 referrals and minimum $100 equivalent "
         "balance. Tokens can be withdrawn to the Mini App wallet or an external BSC wallet."),
        ("<b>Q: What subscription plans are available?</b>", "A: Basic subscription starts at $39/month. "
         "Paying with $MZONE tokens provides up to $15 discount. Premium tier at $99/month offers "
         "higher limits and priority execution."),
    ]
    for q, a in faqs:
        story.append(Paragraph(q, s["MzBody"]))
        story.append(Paragraph(a, s["MzBody"]))
        story.append(Spacer(1, 2*mm))
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("Appendix C: Technical Specifications Summary", s["MzH2"]))

    story.append(make_table(
        ["Specification", "Value"],
        [
            ["Blockchain", "Binance Smart Chain (BNB Chain)"],
            ["Token Standard", "BEP-20"],
            ["Total Token Supply", "10,000,000,000 $MZONE"],
            ["Pattern Library Size", "200,000,000+ patterns"],
            ["News Sources Monitored", "200+ sources, 7 categories"],
            ["NLP Pipeline Stages", "6 (ingestion, classification, entity, sentiment, urgency, mapping)"],
            ["Feature Vector Dimensions", "400+ per asset per cycle"],
            ["Model Ensemble Components", "5 (pattern, trend, sentiment, volatility, correlation)"],
            ["Signal Confidence Threshold", "85% minimum for trade execution"],
            ["Maximum Per-Trade Risk", "2% of portfolio"],
            ["Maximum Daily Loss", "5% of portfolio (hard circuit breaker)"],
            ["Maximum Open Positions", "5 concurrent"],
            ["Maximum Leverage", "1x (no leverage)"],
            ["Signal-to-Order Latency", "< 100ms average"],
            ["End-to-End Pipeline Latency", "< 5 seconds"],
            ["Insurance Coverage", "Up to $100,000 per subscriber"],
            ["Subscription Price", "$39/month (Basic), $99/month (Premium)"],
            ["Airdrop Joining Bonus", "2,000 $MZONE (~$12)"],
            ["Airdrop Referral Bonus", "3,000 $MZONE (~$18) per referral"],
            ["Minimum Referrals for Withdrawal", "5"],
            ["Liquidity Lock Duration", "2 years"],
            ["Deflationary Mechanism", "2% subscription revenue buyback-and-burn"],
        ],
        col_widths=[160, 300]))
    story.append(Paragraph("Table C.1: Complete Technical Specifications", s["MzCaption"]))
    story.append(Spacer(1, 8*mm))

    story.append(Paragraph("Appendix D: Contact and Official Links", s["MzH2"]))

    story.append(make_table(
        ["Channel", "Link"],
        [
            ["Website", "mozoneai.com"],
            ["Mini App", "app.mozoneai.com"],
            ["API (Backend)", "api.mozoneai.com"],
            ["Telegram Channel", "t.me/MozoneAI"],
            ["Telegram Bot", "t.me/mozoneaiairdropbot"],
            ["Twitter / X", "twitter.com/MozoneAI"],
            ["GitHub", "github.com/MozoneAI"],
            ["Email", "team@mozoneai.com"],
        ],
        col_widths=[120, 340]))
    story.append(Paragraph("Table D.1: Official Contact Information", s["MzCaption"]))
    story.append(Spacer(1, 12*mm))

    # --- LEGAL DISCLAIMER ---
    story.append(Paragraph("Legal Disclaimer", s["MzH2"]))
    story.append(Paragraph(
        "This research paper is published for informational and educational purposes only. It does not "
        "constitute financial advice, investment advice, trading advice, or any other form of professional "
        "advice. Cryptocurrency trading involves substantial risk of loss and is not suitable for every "
        "investor. The value of $MZONE tokens and any cryptocurrencies can fluctuate significantly, and "
        "you may lose some or all of your investment.", s["MzBody"]))

    story.append(Paragraph(
        "The 98% accuracy figure and all performance metrics presented in this document are based on "
        "historical evaluation protocols and do not guarantee future results. Past performance is not "
        "indicative of future performance. Market conditions, regulatory environments, and technological "
        "landscapes can change in ways that affect system performance.", s["MzBody"]))

    story.append(Paragraph(
        "The $MZONE token is a utility token designed for use within the Mozone AI ecosystem. It is not "
        "a security, investment contract, share, bond, derivative, or financial instrument of any kind. "
        "Purchasing or holding $MZONE tokens does not confer ownership, equity, dividend rights, or "
        "voting rights (except as specifically described for future governance features).", s["MzBody"]))

    story.append(Paragraph(
        "Always conduct your own research and consult with qualified financial advisors before making "
        "any investment decisions. Never invest more than you can afford to lose.", s["MzBody"]))

    story.append(Spacer(1, 20*mm))
    story.append(Paragraph(
        "Copyright 2026 Mozone AI. All rights reserved.", s["MzCaption"]))
    story.append(Paragraph(
        "Version 1.0 — April 2026", s["MzCaption"]))
