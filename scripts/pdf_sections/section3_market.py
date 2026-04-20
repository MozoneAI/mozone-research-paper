from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section3(story, s, make_table, hr):
    """Cryptocurrency Market Analysis — pages 10-14."""
    story.append(Paragraph("3. Cryptocurrency Market Analysis", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph("3.1 Market Structure and Size", s["MzH2"]))
    story.append(Paragraph(
        "The global cryptocurrency market in 2026 represents a maturing but still highly dynamic financial "
        "ecosystem. Total market capitalization has stabilized in the $2-3 trillion range, with Bitcoin "
        "maintaining approximately 45-50% dominance and Ethereum capturing 15-18%. The remaining market share "
        "is distributed across thousands of altcoins, with Binance Smart Chain tokens representing a "
        "significant and growing portion of DeFi activity.", s["MzBody"]))

    story.append(Paragraph(
        "Daily trading volumes across all exchanges regularly exceed $100 billion, with peak days reaching "
        "$200-300 billion during major market events. This liquidity provides the execution environment for "
        "AI trading systems to operate at scale without significant market impact. The derivatives market, "
        "particularly perpetual futures, has grown to represent 60-70% of total trading volume, creating "
        "additional data sources for sentiment analysis and positioning signals.", s["MzBody"]))

    story.append(Paragraph(
        "The institutional landscape has evolved considerably with the approval and adoption of Bitcoin and "
        "Ethereum spot ETFs in major markets. Institutional participation brings larger capital flows, "
        "improved liquidity, and correlation shifts with traditional financial markets that create both "
        "opportunities and new risk dimensions for trading systems.", s["MzBody"]))

    story.append(Paragraph("3.2 Binance Smart Chain: Strategic Selection", s["MzH2"]))
    story.append(Paragraph(
        "Binance Smart Chain was selected as the primary execution and settlement layer after comprehensive "
        "evaluation across multiple dimensions:", s["MzBody"]))

    story.append(make_table(
        ["Factor", "BSC", "Ethereum", "Solana", "Assessment"],
        [
            ["Transaction Fees", "$0.05-0.30", "$2-50+", "$0.001-0.01",
             "BSC optimal for frequent trading"],
            ["Block Time", "3 seconds", "12 seconds", "0.4 seconds",
             "Fast confirmation, manageable complexity"],
            ["DeFi TVL", "$5B+", "$50B+", "$8B+",
             "Sufficient liquidity for operations"],
            ["DEX Ecosystem", "PancakeSwap", "Uniswap", "Jupiter/Raydium",
             "Deep liquidity for BEP-20 tokens"],
            ["Developer Tooling", "EVM-compatible", "Native EVM", "Rust/Anchor",
             "EVM enables rapid development"],
            ["Network Stability", "High", "Very High", "Variable",
             "Consistent uptime maintained"],
        ],
        col_widths=[80, 75, 75, 75, 155]))
    story.append(Paragraph("Table 3.1: Multi-Chain Comparison for Trading Agent Deployment", s["MzCaption"]))

    story.append(Paragraph(
        "The EVM compatibility of BSC is particularly valuable — it enables deployment of battle-tested "
        "Ethereum smart contract patterns and tooling while benefiting from significantly lower transaction "
        "costs. For a trading system that may execute dozens of transactions daily per user, the fee "
        "differential between BSC ($0.05-0.30) and Ethereum ($2-50+) represents a substantial operational "
        "advantage that directly impacts net returns.", s["MzBody"]))

    story.append(Paragraph("3.3 AI Trading Market Landscape", s["MzH2"]))
    story.append(Paragraph(
        "The global algorithmic trading market is projected to reach $31.5 billion by 2028, representing "
        "a compound annual growth rate of approximately 12.7%. Within this category, cryptocurrency-specific "
        "AI trading is one of the fastest-growing segments.", s["MzBody"]))

    story.append(make_table(
        ["Tier", "Type", "Examples", "Limitations"],
        [
            ["1", "Signal Bots", "3Commas, Cornix", "No autonomous execution; user must act"],
            ["2", "Copy Trading", "eToro, Bybit Copy", "Dependent on lead trader quality"],
            ["3", "HFT Systems", "Jump, Citadel", "Inaccessible to retail; co-location needed"],
            ["4", "AI Agents", "Mozone AI", "New category; requires sophisticated engineering"],
        ],
        col_widths=[35, 85, 130, 210]))
    story.append(Paragraph("Table 3.2: Competitive Landscape in Crypto Trading Automation", s["MzCaption"]))

    story.append(Paragraph(
        "Mozone AI occupies the fourth tier — autonomous AI agents with integrated risk management — "
        "a category currently underserved despite representing the highest-value solution. Unlike signal bots, "
        "Mozone executes trades autonomously. Unlike copy trading, decisions are made by AI algorithms rather "
        "than fallible human lead traders. Unlike institutional HFT, Mozone is accessible to individuals at "
        "$39/month.", s["MzBody"]))

    story.append(Paragraph("3.4 Target Market Segments", s["MzH2"]))
    segments = [
        "<b>Experienced Traders</b> — Active crypto traders who understand dynamics but lack 24/7 monitoring "
        "capability. Value proposition: time liberation without sacrificing edge.",
        "<b>DeFi Enthusiasts</b> — Users engaged in decentralized finance seeking AI-driven alpha as portfolio "
        "diversification. Value proposition: systematic, data-driven return source.",
        "<b>Market Newcomers</b> — Individuals interested in crypto but lacking expertise, time, or emotional "
        "discipline. Value proposition: professional-grade access without personal expertise.",
    ]
    for seg in segments:
        story.append(Paragraph(seg, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("3.5 Market Timing and Opportunity", s["MzH2"]))
    story.append(Paragraph(
        "The convergence of several trends creates a particularly favorable environment for Mozone AI's "
        "launch in 2026: increasing institutional adoption through ETFs, growing demand for passive income "
        "in high-inflation environments, rapid AI/ML advances making sophisticated pattern recognition "
        "accessible, and BSC's maturation as a low-cost execution environment. The airdrop program is "
        "designed to capture early adopters during this window of opportunity.", s["MzBody"]))

    story.append(Paragraph("3.6 Regulatory Landscape", s["MzH2"]))
    story.append(Paragraph(
        "The regulatory environment for cryptocurrency and AI-driven trading varies significantly by "
        "jurisdiction. The European Union's Markets in Crypto-Assets (MiCA) regulation provides the most "
        "comprehensive framework, while the United States maintains a fragmented approach across the SEC, "
        "CFTC, and state regulators. Mozone AI's token ($MZONE) is designed as a utility token with "
        "concrete, functional use cases to minimize regulatory ambiguity. The system does not provide "
        "investment advice, manage client funds in a custodial manner, or operate as a registered "
        "investment vehicle.", s["MzBody"]))

    story.append(Paragraph(
        "The trading agent operates on the user's own exchange account or wallet, executing trades "
        "within parameters the user configures. This non-custodial design — where users maintain full "
        "control of their funds at all times — aligns with the self-sovereign principles of decentralized "
        "finance and simplifies the regulatory classification of the service.", s["MzBody"]))

    story.append(Paragraph("3.7 DeFi Ecosystem on BSC", s["MzH2"]))
    story.append(Paragraph(
        "Binance Smart Chain hosts a mature and diverse DeFi ecosystem that provides the operational "
        "environment for Mozone AI. Understanding this ecosystem is essential because it defines the "
        "liquidity landscape, fee structures, and trading pair availability:", s["MzBody"]))

    story.append(make_table(
        ["Protocol", "Category", "TVL (est.)", "Relevance to Mozone"],
        [
            ["PancakeSwap", "DEX (AMM)", "$2.5B+", "Primary trading venue for BEP-20 tokens"],
            ["Venus Protocol", "Lending/Borrowing", "$1.2B+", "Liquidity indicator; interest rate signals"],
            ["Alpaca Finance", "Leveraged Yield", "$500M+", "Leverage demand as market sentiment indicator"],
            ["Biswap", "DEX (V3 concentrated)", "$200M+", "Secondary trading venue; arbitrage opportunities"],
            ["Thena", "DEX (ve(3,3) model)", "$150M+", "Emerging liquidity source"],
            ["ListaDAO", "Liquid Staking", "$400M+", "BNB staking flow as macro indicator"],
        ],
        col_widths=[85, 95, 65, 215]))
    story.append(Paragraph("Table 3.3: Key BSC DeFi Protocols", s["MzCaption"]))

    story.append(Paragraph(
        "The presence of deep liquidity on PancakeSwap — with multiple trading pairs routinely "
        "maintaining $1M+ in pool depth — ensures that Mozone AI can execute trades of $1,000-10,000 "
        "with minimal price impact (typically under 0.1% slippage). For larger position sizes, the "
        "system automatically splits orders across multiple pools and routes to minimize impact.", s["MzBody"]))

    story.append(Paragraph("3.8 Market Microstructure Considerations", s["MzH2"]))
    story.append(Paragraph(
        "The microstructure of cryptocurrency markets differs substantially from traditional equity "
        "markets in ways that directly affect trading system design:", s["MzBody"]))

    micro = [
        "<b>AMM pricing mechanics</b> — Unlike order book markets, DEX prices are determined by "
        "automated market maker formulas (constant product: x*y=k for V2, concentrated liquidity "
        "for V3). This creates predictable price impact curves that can be modeled precisely.",
        "<b>MEV (Miner Extractable Value)</b> — On-chain transactions are visible in the mempool "
        "before confirmation, enabling front-running and sandwich attacks. Mozone mitigates this "
        "through private transaction submission where available and slippage tolerance limits.",
        "<b>Gas price dynamics</b> — BSC gas prices are generally stable ($0.05-0.30) but can "
        "spike during network congestion. The system monitors gas prices and delays non-urgent "
        "transactions during spikes to minimize costs.",
        "<b>Cross-venue arbitrage</b> — Price discrepancies between CEX and DEX venues create "
        "arbitrage opportunities that the system can exploit while contributing to market efficiency.",
        "<b>Impermanent loss signals</b> — Large impermanent loss in liquidity pools indicates "
        "directional price movement, serving as an additional signal source.",
    ]
    for m in micro:
        story.append(Paragraph(m, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("3.9 Total Addressable Market", s["MzH2"]))
    story.append(Paragraph(
        "The total addressable market for AI-powered cryptocurrency trading services can be estimated "
        "from multiple perspectives:", s["MzBody"]))

    story.append(make_table(
        ["Market Segment", "Est. Size (2026)", "Mozone Target Share", "Revenue Potential"],
        [
            ["Active crypto traders globally", "50M+", "0.01% (5,000)", "$2.3M ARR"],
            ["DeFi-active wallets", "10M+", "0.05% (5,000)", "$2.3M ARR"],
            ["Algorithmic trading market (crypto)", "$3B+", "0.1% ($3M)", "$3M ARR"],
            ["Crypto subscription services", "$500M+", "0.5% ($2.5M)", "$2.5M ARR"],
        ],
        col_widths=[120, 80, 100, 100]))
    story.append(Paragraph("Table 3.4: Total Addressable Market Analysis", s["MzCaption"]))

    story.append(Paragraph(
        "Even conservative market share assumptions yield significant revenue potential. The key "
        "insight is that the market is large enough that even a small share can sustain a profitable "
        "and growing business. The airdrop program and community-first strategy are designed to "
        "capture this initial market share efficiently, with the quality of the AI agent's performance "
        "driving organic growth through word-of-mouth and demonstrable results.", s["MzBody"]))

    story.append(PageBreak())
