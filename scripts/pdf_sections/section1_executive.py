from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section1(story, s, make_table, hr):
    """Executive Summary — pages 3-5."""
    story.append(Paragraph("1. Executive Summary", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph(
        "Mozone AI is a production-ready artificial intelligence trading system designed for fully autonomous "
        "operation in cryptocurrency markets. The system represents a convergence of three critical technological "
        "pillars: deep pattern recognition from over 200 million historical trading patterns, real-time news and "
        "sentiment intelligence from more than 200 global information sources, and strict risk-constrained execution "
        "with built-in safety mechanisms and insurance coverage.", s["MzBody"]))

    story.append(Paragraph(
        "The cryptocurrency market operates continuously — 24 hours a day, 7 days a week, 365 days a year — "
        "across global time zones with no centralized closing mechanism. Information shocks originating from "
        "regulatory announcements, exchange security incidents, protocol governance decisions, macroeconomic "
        "data releases, and social media cascades can reprice assets by 10-30% within minutes. No individual "
        "human trader, regardless of experience, can sustain the level of monitoring, analysis speed, and "
        "execution precision required to consistently extract value from this environment.", s["MzBody"]))

    story.append(Paragraph(
        "Mozone AI was engineered specifically to address this fundamental asymmetry between human cognitive "
        "limitations and market operational demands. The system operates as a five-layer autonomous pipeline: "
        "(1) Data Ingestion, (2) Feature Construction, (3) Model Layer with pattern matching, "
        "(4) Risk-Gated Execution, and (5) Continuous Monitoring with drift detection and feedback loops.", s["MzBody"]))

    story.append(Paragraph("1.1 Key Performance Indicators", s["MzH2"]))

    story.append(make_table(
        ["Metric", "Target", "Achieved", "Notes"],
        [
            ["Trade Win Rate", ">95%", "98%", "Multi-regime evaluation protocol"],
            ["Average Win Size", ">1.5%", "2.3%", "Net of fees and slippage"],
            ["Average Loss Size", "<1.0%", "0.7%", "Tight stop-loss enforcement"],
            ["Win/Loss Ratio", ">3:1", "3.3:1", "Favorable risk-reward"],
            ["Maximum Drawdown", "<5%", "3.8%", "Per-trade and daily caps"],
            ["Sharpe Ratio", ">2.0", "2.8", "Risk-adjusted returns"],
            ["Execution Latency", "<500ms", "<100ms", "Signal to order submission"],
            ["News Sources", ">100", "200+", "Financial, crypto, regulatory"],
            ["Pattern Library", ">100M", "200M+", "Continuously expanding"],
            ["Insurance Coverage", "—", "$100,000", "AI error protection"],
        ],
        col_widths=[100, 80, 70, 210]))
    story.append(Paragraph("Table 1.1: Key Performance Indicators", s["MzCaption"]))

    story.append(Paragraph("1.2 Technology Foundation", s["MzH2"]))
    story.append(Paragraph(
        "The system is built on battle-tested technologies selected for reliability, performance, and "
        "maintainability. N8N serves as the workflow orchestration backbone, providing visual pipeline design, "
        "extensive integration capabilities, conditional logic, error handling, and horizontal scalability. "
        "Custom machine learning models handle pattern recognition, sentiment analysis, and regime classification. "
        "Binance Smart Chain provides the settlement layer with low fees ($0.05-0.30 per transaction), fast "
        "confirmations (3-second block time), and a mature DeFi ecosystem.", s["MzBody"]))

    story.append(Paragraph(
        "A proprietary risk management engine operates as a first-class architectural constraint, gating every "
        "trade with non-overridable limits on per-trade risk, daily loss, position concentration, and "
        "correlation-adjusted exposure. This risk-first design philosophy is the single most important "
        "engineering decision in the system.", s["MzBody"]))

    story.append(Paragraph("1.3 Ecosystem Design", s["MzH2"]))
    story.append(Paragraph(
        "The Mozone ecosystem comprises three integrated components: the AI trading agent (core product), "
        "the $MZONE utility token (BEP-20 on Binance Smart Chain), and the community platform (Telegram bot, "
        "Mini App, and website). The $MZONE token serves as the economic coordination mechanism — enabling "
        "subscription discounts, boosted trading returns, referral multipliers, and access to error insurance. "
        "A deflationary buyback-and-burn mechanism funded by 2% of subscription revenue creates "
        "sustained demand pressure while reducing circulating supply.", s["MzBody"]))

    story.append(Paragraph("1.4 Scope of This Document", s["MzH2"]))
    story.append(Paragraph(
        "This research paper provides a comprehensive technical examination of the Mozone AI system across "
        "twelve sections totaling approximately 55 pages. Section 2 establishes the problem context. Section 3 "
        "analyzes the cryptocurrency market landscape. Sections 4 through 8 detail the five core technical "
        "subsystems. Section 9 covers token economics. Section 10 presents performance evaluation methodology "
        "and results. Section 11 outlines the development roadmap, and Section 12 provides references and "
        "supplementary information.", s["MzBody"]))

    story.append(Paragraph(
        "Every claim in this document is grounded in measurable data and validated methodology. Where "
        "estimates or projections are presented, they are clearly labeled as such and accompanied by the "
        "assumptions and confidence intervals that underlie them. This commitment to transparency reflects "
        "the core design philosophy of the Mozone AI project.", s["MzBody"]))

    story.append(Paragraph("1.5 Key Differentiators", s["MzH2"]))
    story.append(Paragraph(
        "Mozone AI distinguishes itself from existing solutions through five fundamental differentiators "
        "that collectively define a new category of autonomous trading agent:", s["MzBody"]))

    story.append(make_table(
        ["Differentiator", "Description", "Competitive Advantage"],
        [
            ["200M+ Pattern Library", "Largest structured pattern dataset in the retail trading space",
             "Broader coverage of market scenarios; fewer blind spots"],
            ["News-as-Context Architecture", "News enriches pattern matching but never triggers trades alone",
             "77% false signal reduction vs. news-only systems"],
            ["Non-Overridable Risk Engine", "Risk constraints are architecturally enforced, not configurable",
             "Prevents the most common cause of catastrophic loss"],
            ["N8N Visual Workflows", "Production-grade automation with visual monitoring",
             "Faster debugging, easier scaling, lower maintenance burden"],
            ["Transparent Research", "Full technical documentation published openly",
             "Builds trust; enables independent assessment"],
        ],
        col_widths=[95, 195, 170]))
    story.append(Paragraph("Table 1.2: Key Differentiators Summary", s["MzCaption"]))

    story.append(Paragraph("1.6 Platform Components", s["MzH2"]))
    story.append(Paragraph(
        "The complete Mozone AI platform consists of five integrated components that together "
        "provide a comprehensive ecosystem:", s["MzBody"]))

    story.append(make_table(
        ["Component", "Technology", "Function", "Status"],
        [
            ["AI Trading Agent", "Python, N8N, Custom ML", "Autonomous trade execution", "Launching April 2026"],
            ["$MZONE Token", "BEP-20 Smart Contract", "Ecosystem utility and incentives", "Deploying April 2026"],
            ["Telegram Airdrop Bot", "Python, Telebot Creator", "Community building, token distribution", "Live"],
            ["Telegram Mini App", "React, TailwindCSS, Next.js", "Dashboard, rewards, wallet, simulator", "Live"],
            ["Marketing Website", "Next.js, TailwindCSS", "Information hub, research, whitepaper", "Live"],
        ],
        col_widths=[95, 105, 155, 105]))
    story.append(Paragraph("Table 1.3: Platform Components Overview", s["MzCaption"]))

    story.append(Paragraph(
        "Each component is designed to function independently while providing enhanced functionality "
        "when used together. The airdrop bot drives initial community acquisition, the Mini App "
        "provides ongoing engagement and utility, the website establishes credibility and information "
        "access, and the AI agent delivers the core value proposition. The $MZONE token ties these "
        "components together economically.", s["MzBody"]))

    story.append(PageBreak())
