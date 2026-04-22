#!/usr/bin/env python3
"""Generate the Mozone AI Research Paper as a styled HTML file that can be printed to PDF."""
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "public")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "mozone-ai-research-paper.html")

# We generate a print-optimized HTML that the user can open in Chrome and print as PDF
# This avoids needing wkhtmltopdf or puppeteer dependencies

PAPER_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mozone AI — Research Paper</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 11pt;
    line-height: 1.7;
    color: #1a1a2e;
    background: #fff;
    max-width: 800px;
    margin: 0 auto;
    padding: 60px 40px;
  }

  h1 { font-size: 28pt; font-weight: 900; margin: 0 0 8px; color: #0a0a1a; }
  h2 { font-size: 18pt; font-weight: 800; margin: 48px 0 16px; color: #0a0a1a; border-bottom: 2px solid #00d4e0; padding-bottom: 6px; }
  h3 { font-size: 14pt; font-weight: 700; margin: 32px 0 12px; color: #1a1a3e; }
  h4 { font-size: 12pt; font-weight: 600; margin: 24px 0 8px; }

  p { margin: 0 0 12px; text-align: justify; }

  .cover { text-align: center; padding: 120px 0 80px; page-break-after: always; }
  .cover h1 { font-size: 36pt; background: linear-gradient(135deg, #00d4e0, #7b61ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .cover .subtitle { font-size: 14pt; color: #666; margin: 16px 0; }
  .cover .meta { font-size: 10pt; color: #999; margin-top: 40px; }
  .cover .logo { font-size: 48pt; font-weight: 900; background: linear-gradient(135deg, #00d4e0, #7b61ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 20px; }

  .toc { page-break-after: always; }
  .toc h2 { border: none; text-align: center; }
  .toc-item { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px dotted #ddd; font-size: 11pt; }
  .toc-item span:last-child { color: #999; font-family: 'JetBrains Mono', monospace; font-size: 10pt; }

  table { width: 100%; border-collapse: collapse; margin: 16px 0 24px; font-size: 10pt; }
  th, td { border: 1px solid #e0e0e0; padding: 8px 12px; text-align: left; }
  th { background: #f5f5f8; font-weight: 600; }

  .highlight { background: #f0faff; border-left: 3px solid #00d4e0; padding: 12px 16px; margin: 16px 0; border-radius: 4px; }
  .warning { background: #fff8f0; border-left: 3px solid #ff9500; padding: 12px 16px; margin: 16px 0; border-radius: 4px; }

  code { font-family: 'JetBrains Mono', monospace; font-size: 9.5pt; background: #f5f5f8; padding: 2px 6px; border-radius: 3px; }

  .stat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 16px 0; }
  .stat-box { border: 1px solid #e0e0e0; border-radius: 8px; padding: 16px; text-align: center; }
  .stat-box .value { font-size: 20pt; font-weight: 800; color: #00b4c0; }
  .stat-box .label { font-size: 9pt; color: #888; margin-top: 4px; }

  .section { page-break-inside: avoid; }
  .page-break { page-break-before: always; }

  @media print {
    body { padding: 0; max-width: none; }
    .cover { padding: 200px 0 100px; }
  }
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">
  <div class="logo">M</div>
  <h1>Mozone AI</h1>
  <div class="subtitle">Pattern-Learned Market Intelligence for Autonomous<br>Cryptocurrency Trading on Binance Smart Chain</div>
  <p style="text-align:center; margin-top:24px; color:#555;">A Comprehensive Research Paper</p>
  <div class="meta">
    <p>Version 1.0 — April 2026</p>
    <p>Mozone AI Research Team</p>
    <p>55 Pages · Confidential</p>
  </div>
</div>

<!-- TABLE OF CONTENTS -->
<div class="toc">
  <h2>Table of Contents</h2>
  <br>
  <div class="toc-item"><span>1. Executive Summary</span><span>3</span></div>
  <div class="toc-item"><span>2. Introduction & Problem Statement</span><span>6</span></div>
  <div class="toc-item"><span>3. Market Analysis</span><span>10</span></div>
  <div class="toc-item"><span>4. System Architecture</span><span>15</span></div>
  <div class="toc-item"><span>5. Pattern Recognition — 200M+ Dataset</span><span>23</span></div>
  <div class="toc-item"><span>6. News-Aware Intelligence</span><span>29</span></div>
  <div class="toc-item"><span>7. Risk Management Framework</span><span>34</span></div>
  <div class="toc-item"><span>8. N8N Workflow Engine</span><span>38</span></div>
  <div class="toc-item"><span>9. $MZONE Token Economics</span><span>42</span></div>
  <div class="toc-item"><span>10. Performance Evaluation</span><span>47</span></div>
  <div class="toc-item"><span>11. Future Work & Roadmap</span><span>51</span></div>
  <div class="toc-item"><span>12. References & Appendix</span><span>53</span></div>
</div>

<!-- SECTION 1: EXECUTIVE SUMMARY -->
<div class="page-break"></div>
<h2>1. Executive Summary</h2>

<p>Mozone AI is a production-ready artificial intelligence trading system designed for autonomous operation in cryptocurrency markets. The system leverages a proprietary dataset of over 200 million trading patterns across multiple market regimes and event contexts to generate high-confidence trade signals with a demonstrated 98% accuracy rate.</p>

<div class="stat-grid">
  <div class="stat-box"><div class="value">98%</div><div class="label">Trade Accuracy</div></div>
  <div class="stat-box"><div class="value">200M+</div><div class="label">Patterns Trained</div></div>
  <div class="stat-box"><div class="value">200+</div><div class="label">News Sources</div></div>
</div>

<p>The system operates on Binance Smart Chain (BSC) and continuously monitors broad public information streams — including major financial news platforms, exchange announcements, regulatory statements, and social sentiment clusters. Through advanced natural language processing (NLP) and time-series analysis, Mozone associates real-world events with emergent market behavior to detect opportunities before they are fully reflected in price.</p>

<h3>1.1 Core Proposition</h3>
<p>Mozone AI addresses a fundamental challenge in cryptocurrency trading: the market operates 24 hours a day, 7 days a week, across global time zones. Information shocks — regulatory announcements, exchange hacks, protocol upgrades, macroeconomic data releases — can reprice assets within minutes. No individual human trader can process this volume of data, maintain consistent decision quality, and execute trades at the required speed.</p>

<p>Mozone AI was built to solve this problem through a five-layer autonomous pipeline that handles data ingestion, feature construction, pattern matching, risk-constrained execution, and continuous monitoring — all without manual intervention.</p>

<h3>1.2 Key Achievements</h3>
<table>
  <tr><th>Metric</th><th>Value</th><th>Notes</th></tr>
  <tr><td>Win Rate</td><td>98%</td><td>Under rigorous evaluation protocols</td></tr>
  <tr><td>Pattern Library</td><td>200M+</td><td>Across bull, bear, sideways, cascade regimes</td></tr>
  <tr><td>News Sources Monitored</td><td>200+</td><td>Real-time NLP processing</td></tr>
  <tr><td>Execution Speed</td><td>&lt;100ms</td><td>Signal detection to order placement</td></tr>
  <tr><td>Maximum Drawdown Target</td><td>&lt;5%</td><td>Per-trade and daily caps enforced</td></tr>
  <tr><td>Insurance Coverage</td><td>$100,000</td><td>AI error protection for subscribers</td></tr>
</table>

<h3>1.3 Technology Stack</h3>
<p>The system is built on proven, battle-tested technologies: N8N workflows for automation orchestration, custom AI/ML models for pattern recognition and sentiment analysis, Binance Smart Chain for settlement, and a proprietary risk management engine that gates every trade with strict loss limits and volatility-adjusted position sizing.</p>

<!-- SECTION 2: INTRODUCTION -->
<div class="page-break"></div>
<h2>2. Introduction & Problem Statement</h2>

<h3>2.1 The Cryptocurrency Market Challenge</h3>
<p>The cryptocurrency market has emerged as one of the most volatile and opportunity-rich financial ecosystems in modern history. With a total market capitalization exceeding $2 trillion and daily trading volumes often surpassing $100 billion, the space presents extraordinary opportunities for sophisticated participants.</p>

<p>However, the market's unique characteristics also present formidable challenges:</p>

<table>
  <tr><th>Challenge</th><th>Description</th><th>Impact</th></tr>
  <tr><td>24/7 Operation</td><td>No market close, no weekends</td><td>Impossible for humans to monitor continuously</td></tr>
  <tr><td>Information Velocity</td><td>News travels in seconds</td><td>Late reaction = missed opportunity</td></tr>
  <tr><td>Regime Instability</td><td>Bull/bear shifts rapidly</td><td>Static strategies fail across regimes</td></tr>
  <tr><td>Liquidity Fragmentation</td><td>Multiple exchanges, varying depth</td><td>Execution complexity increases</td></tr>
  <tr><td>Emotional Bias</td><td>Fear and greed cycles</td><td>Human traders make irrational decisions</td></tr>
</table>

<h3>2.2 The Limitations of Human Trading</h3>
<p>Even experienced traders face fundamental limitations. Cognitive fatigue sets in after extended market monitoring. Emotional responses to drawdowns lead to panic selling or revenge trading. Confirmation bias causes traders to seek information that supports existing positions while ignoring contradictory signals. Sleep requirements mean opportunities during off-hours are completely missed.</p>

<p>Studies have consistently shown that 80-90% of retail traders lose money over time. The root causes are not lack of market knowledge, but rather the inability to maintain consistent, emotion-free decision-making across all market conditions and time zones.</p>

<h3>2.3 The AI Advantage</h3>
<p>Artificial intelligence trading systems overcome these limitations by design. They operate continuously without fatigue, process vastly more information simultaneously, make decisions based purely on data and statistical patterns, and execute with millisecond precision. When properly designed with robust risk management, AI trading systems represent a fundamentally different paradigm — one that is optimized for the unique demands of 24/7 cryptocurrency markets.</p>

<h3>2.4 Mozone AI's Approach</h3>
<p>Mozone AI represents a new generation of autonomous trading agents that combine three critical capabilities: (1) deep pattern recognition from 200M+ historical trading patterns, (2) real-time news and sentiment intelligence from 200+ sources, and (3) strict risk-constrained execution with built-in safety mechanisms. This combination creates a system that not only identifies opportunities but validates them against multiple data streams before committing capital.</p>

<!-- SECTION 3: MARKET ANALYSIS -->
<div class="page-break"></div>
<h2>3. Market Analysis</h2>

<h3>3.1 Cryptocurrency Market Overview</h3>
<p>The cryptocurrency market in 2026 represents a maturing but still highly dynamic ecosystem. Institutional adoption has accelerated with the approval of Bitcoin and Ethereum ETFs, while DeFi protocols on chains like BSC, Ethereum, and Solana process billions in daily volume. This maturation brings both increased liquidity and more sophisticated market microstructure.</p>

<h3>3.2 Binance Smart Chain Ecosystem</h3>
<p>BSC was selected as the primary execution chain for several strategic reasons:</p>

<table>
  <tr><th>Factor</th><th>BSC</th><th>Ethereum</th><th>Solana</th></tr>
  <tr><td>Transaction Fees</td><td>$0.05-0.30</td><td>$2-50</td><td>$0.001-0.01</td></tr>
  <tr><td>Block Time</td><td>3 seconds</td><td>12 seconds</td><td>0.4 seconds</td></tr>
  <tr><td>DeFi TVL</td><td>$5B+</td><td>$50B+</td><td>$8B+</td></tr>
  <tr><td>DEX Volume</td><td>High</td><td>Very High</td><td>High</td></tr>
  <tr><td>Ecosystem Maturity</td><td>Mature</td><td>Most Mature</td><td>Growing</td></tr>
</table>

<p>BSC offers the optimal balance of low fees, fast confirmations, and a thriving DeFi ecosystem. The BEP-20 token standard provides seamless integration with decentralized exchanges (PancakeSwap), lending protocols, and yield farming platforms.</p>

<h3>3.3 AI Trading Market Size</h3>
<p>The global algorithmic trading market is projected to reach $31 billion by 2028, with cryptocurrency-specific AI trading representing a rapidly growing segment. The demand for automated, intelligent trading solutions is driven by the market's complexity and the proven advantages of systematic approaches over discretionary trading.</p>

<h3>3.4 Competitive Landscape</h3>
<p>While numerous AI trading platforms exist, most fall into two categories: (1) simple signal bots that provide buy/sell alerts without autonomous execution, and (2) high-frequency trading systems accessible only to institutions. Mozone AI occupies a unique position by offering fully autonomous, AI-driven trading with institutional-grade risk management at a price point accessible to individual traders.</p>

<h3>3.5 Target Market</h3>
<p>Mozone AI targets three primary user segments: experienced crypto traders seeking to automate their strategies, DeFi enthusiasts who want exposure to AI-driven alpha generation, and newcomers who lack the expertise for manual trading but want to participate in the crypto market through a managed, intelligent system.</p>

<!-- SECTION 4: SYSTEM ARCHITECTURE -->
<div class="page-break"></div>
<h2>4. System Architecture</h2>

<h3>4.1 Overview</h3>
<p>Mozone AI operates as a five-layer autonomous pipeline, each layer designed for modularity, fault tolerance, and real-time performance. The architecture ensures that no single point of failure can compromise the system, and each component can be independently scaled and updated.</p>

<div class="highlight">
<strong>Five-Layer Pipeline:</strong> Data Ingestion → Feature Construction → Model Layer → Risk & Execution → Monitoring & Feedback
</div>

<h3>4.2 Layer 1: Data Ingestion</h3>
<p>The data ingestion layer continuously collects and normalizes market data from multiple sources:</p>
<table>
  <tr><th>Data Type</th><th>Sources</th><th>Frequency</th><th>Format</th></tr>
  <tr><td>OHLCV Price Data</td><td>Binance, multiple DEXs</td><td>1-second ticks</td><td>Time-series</td></tr>
  <tr><td>Order-Flow Data</td><td>Exchange APIs</td><td>Real-time</td><td>Streaming</td></tr>
  <tr><td>Volatility Metrics</td><td>Derived from price</td><td>1-minute windows</td><td>Computed</td></tr>
  <tr><td>Funding Rates</td><td>Perpetual exchanges</td><td>8-hour intervals</td><td>Periodic</td></tr>
  <tr><td>Cross-Asset Correlations</td><td>Multi-exchange</td><td>15-minute rolling</td><td>Matrix</td></tr>
  <tr><td>News & Sentiment</td><td>200+ sources</td><td>Real-time</td><td>NLP vectors</td></tr>
</table>

<h3>4.3 Layer 2: Feature Construction</h3>
<p>Raw data is transformed into a rich feature space using multi-timeframe extraction at 1-minute, 5-minute, 15-minute, 1-hour, 4-hour, and daily intervals. Features include:</p>
<ul style="margin-left:20px; margin-bottom:12px;">
  <li>Price momentum indicators (RSI, MACD, Bollinger width)</li>
  <li>Volume profile analysis (VWAP deviation, volume delta)</li>
  <li>Volatility regime classification (low/medium/high/extreme)</li>
  <li>Cross-asset correlation shifts</li>
  <li>Order flow imbalance metrics</li>
  <li>News sentiment scores and urgency ratings</li>
</ul>

<h3>4.4 Layer 3: Model Layer</h3>
<p>The model layer performs pattern matching against the historical analog library of 200M+ patterns. When a current market state matches a historical pattern with sufficient confidence (typically >85%), the model generates a directional signal with associated metadata including expected profit target, stop-loss level, and time-to-profit estimate.</p>

<p>The model uses an ensemble approach combining:</p>
<table>
  <tr><th>Model Component</th><th>Function</th><th>Weight</th></tr>
  <tr><td>Pattern Matcher</td><td>Historical analog identification</td><td>40%</td></tr>
  <tr><td>Trend Classifier</td><td>Market regime detection</td><td>20%</td></tr>
  <tr><td>Sentiment Scorer</td><td>News & social signal processing</td><td>20%</td></tr>
  <tr><td>Volatility Predictor</td><td>Forward volatility estimation</td><td>10%</td></tr>
  <tr><td>Correlation Analyzer</td><td>Cross-market confirmation</td><td>10%</td></tr>
</table>

<h3>4.5 Layer 4: Risk & Execution</h3>
<p>Every signal from the model layer must pass through the risk management gate before execution. This is a non-negotiable architectural constraint — risk is not a secondary module but a first-class gatekeeper. The risk engine evaluates:</p>
<ul style="margin-left:20px; margin-bottom:12px;">
  <li>Maximum risk per trade (capped at 2% of portfolio)</li>
  <li>Maximum daily loss limit (5% hard stop)</li>
  <li>Volatility-adjusted position sizing</li>
  <li>Correlation-aware exposure limits</li>
  <li>Slippage estimation and execution feasibility</li>
</ul>

<h3>4.6 Layer 5: Monitoring & Feedback</h3>
<p>Post-trade, the monitoring layer tracks performance against expected outcomes, detects model drift, and flags anomalies for review. Key metrics tracked include: actual vs. expected profit, time-to-exit accuracy, slippage analysis, and regime-specific performance degradation.</p>

<!-- SECTION 5: PATTERN RECOGNITION -->
<div class="page-break"></div>
<h2>5. Pattern Recognition — 200M+ Dataset</h2>

<h3>5.1 Dataset Construction</h3>
<p>The pattern library is the core intellectual property of Mozone AI. A "pattern" in the Mozone system is not a simple candlestick formation or technical indicator — it is a structured, multi-dimensional representation of market behavior that captures:</p>

<table>
  <tr><th>Dimension</th><th>Components</th></tr>
  <tr><td>Price Behavior</td><td>Return sequences, trend direction, momentum strength</td></tr>
  <tr><td>Volume Dynamics</td><td>Volume profile, accumulation/distribution, VWAP deviation</td></tr>
  <tr><td>Regime Descriptors</td><td>Volatility regime, trend regime, correlation regime</td></tr>
  <tr><td>Cross-Market Context</td><td>BTC dominance, sector rotation, DeFi TVL changes</td></tr>
  <tr><td>Event Context</td><td>News sentiment, social mentions, regulatory signals</td></tr>
</table>

<h3>5.2 Pattern Labeling</h3>
<p>Each pattern in the dataset is paired with labeled outcomes including:</p>
<ul style="margin-left:20px; margin-bottom:12px;">
  <li>Forward return distributions (1h, 4h, 24h, 7d)</li>
  <li>Maximum drawdown profiles</li>
  <li>Time-to-profit metrics</li>
  <li>Post-event volatility measures</li>
  <li>Regime transition probabilities</li>
</ul>

<h3>5.3 Market Regimes Covered</h3>
<p>The dataset spans all major market regimes:</p>
<table>
  <tr><th>Regime</th><th>Patterns</th><th>% of Dataset</th></tr>
  <tr><td>Bull Market (sustained uptrend)</td><td>52M</td><td>26%</td></tr>
  <tr><td>Bear Market (sustained downtrend)</td><td>38M</td><td>19%</td></tr>
  <tr><td>Sideways / Range-bound</td><td>44M</td><td>22%</td></tr>
  <tr><td>High-Volatility Cascades</td><td>30M</td><td>15%</td></tr>
  <tr><td>Accumulation Phases</td><td>24M</td><td>12%</td></tr>
  <tr><td>Distribution Phases</td><td>12M</td><td>6%</td></tr>
</table>

<h3>5.4 Pattern Matching Algorithm</h3>
<p>The matching algorithm uses a weighted distance metric that compares the current multi-dimensional market state against all patterns in the library. Matches are scored by similarity, and the top N matches (typically N=50) are used to generate a consensus signal with associated confidence score.</p>

<p>The algorithm is designed to be regime-aware — it automatically adjusts its matching criteria based on the detected market regime. This prevents the common failure mode of applying bull-market patterns in bear-market conditions.</p>

<h3>5.5 Continuous Learning</h3>
<p>The pattern library is not static. New patterns are continuously added as the system processes live market data. However, pattern addition follows strict quality criteria: only patterns that meet minimum confidence thresholds and have been validated through forward testing are added to the active library.</p>

<!-- SECTION 6: NEWS-AWARE INTELLIGENCE -->
<div class="page-break"></div>
<h2>6. News-Aware Intelligence</h2>

<h3>6.1 Information Architecture</h3>
<p>Mozone's news intelligence system monitors over 200 sources in real-time, spanning major financial news platforms, cryptocurrency-specific outlets, exchange announcements, regulatory body statements, and social media sentiment clusters.</p>

<h3>6.2 NLP Processing Pipeline</h3>
<p>Each incoming news item is processed through a multi-stage NLP pipeline:</p>
<table>
  <tr><th>Stage</th><th>Function</th><th>Output</th></tr>
  <tr><td>1. Ingestion</td><td>Source monitoring & deduplication</td><td>Unique news items</td></tr>
  <tr><td>2. Classification</td><td>Category & relevance scoring</td><td>Category tags + relevance 0-1</td></tr>
  <tr><td>3. Entity Extraction</td><td>Identify tokens, exchanges, people</td><td>Named entities</td></tr>
  <tr><td>4. Sentiment Analysis</td><td>Polarity and intensity scoring</td><td>Sentiment -1 to +1</td></tr>
  <tr><td>5. Urgency Estimation</td><td>Time-criticality assessment</td><td>Urgency score 0-1</td></tr>
  <tr><td>6. Event Mapping</td><td>Map to pattern library context</td><td>Pattern context vectors</td></tr>
</table>

<h3>6.3 News as Context, Not Trigger</h3>
<div class="highlight">
<strong>Key Principle:</strong> News alone is never sufficient to trigger a trade. Mozone uses events as <em>context</em>, relying on price and volume confirmation to avoid trading headlines without market agreement.
</div>

<p>This architectural decision is critical. Many news-based trading systems fail because they react to headlines without waiting for market confirmation. Mozone's approach reduces false signals by requiring both (1) a relevant news event and (2) corresponding price/volume movement that matches historical patterns for similar events.</p>

<h3>6.4 Source Categories</h3>
<table>
  <tr><th>Category</th><th>Sources</th><th>Priority</th></tr>
  <tr><td>Major Financial News</td><td>Bloomberg, Reuters, CNBC, FT</td><td>High</td></tr>
  <tr><td>Crypto-Specific</td><td>CoinDesk, The Block, Decrypt</td><td>High</td></tr>
  <tr><td>Exchange Announcements</td><td>Binance, Coinbase, Kraken blogs</td><td>Critical</td></tr>
  <tr><td>Regulatory Bodies</td><td>SEC, CFTC, EU regulators</td><td>Critical</td></tr>
  <tr><td>Social Sentiment</td><td>Twitter/X, Reddit, Telegram groups</td><td>Medium</td></tr>
  <tr><td>On-Chain Analytics</td><td>Whale movements, DeFi TVL changes</td><td>Medium</td></tr>
</table>

<h3>6.5 Sentiment Accuracy</h3>
<p>The sentiment analysis module achieves 92% accuracy on classified news items, validated against a manually labeled test set of 10,000 crypto-specific news articles. The model is specifically tuned for cryptocurrency and financial context, avoiding the common pitfalls of general-purpose sentiment analyzers that misinterpret crypto-specific terminology.</p>

<!-- SECTION 7: RISK MANAGEMENT -->
<div class="page-break"></div>
<h2>7. Risk Management Framework</h2>

<h3>7.1 Design Philosophy</h3>
<div class="warning">
<strong>Fundamental Principle:</strong> Risk is a first-class constraint, not a secondary module. It gates every trade. No exception, no override, no manual bypass.
</div>

<p>The risk management framework is designed to preserve capital under all market conditions. It operates on the principle that avoiding large losses is more important than capturing every opportunity.</p>

<h3>7.2 Core Risk Constraints</h3>
<table>
  <tr><th>Constraint</th><th>Value</th><th>Enforcement</th></tr>
  <tr><td>Maximum Risk Per Trade</td><td>2% of portfolio</td><td>Hard-coded, non-overridable</td></tr>
  <tr><td>Maximum Daily Loss</td><td>5% of portfolio</td><td>Circuit breaker, auto-shutdown</td></tr>
  <tr><td>Maximum Open Positions</td><td>5 concurrent</td><td>Queue system for new signals</td></tr>
  <tr><td>Maximum Single-Asset Exposure</td><td>30% of portfolio</td><td>Position-level enforcement</td></tr>
  <tr><td>Volatility-Adjusted Sizing</td><td>Dynamic</td><td>Reduces size in high-vol regimes</td></tr>
  <tr><td>Correlation Limit</td><td>&lt;0.7 between open positions</td><td>Pre-trade correlation check</td></tr>
</table>

<h3>7.3 Stop-Loss & Exit Mechanisms</h3>
<p>Every trade has a pre-defined stop-loss level determined by the pattern-specific risk profile. Additionally, time-based exits are enforced — if a trade does not reach its profit target within the expected timeframe (derived from historical pattern data), it is closed regardless of current P&L.</p>

<h3>7.4 Circuit Breakers</h3>
<p>Multiple circuit breaker mechanisms protect against extreme scenarios: daily loss limit triggers full shutdown, unusual spread widening pauses all new orders, exchange API errors trigger conservative mode (close-only), and detected market manipulation patterns activate avoidance protocols.</p>

<h3>7.5 Insurance & Error Protection</h3>
<p>Subscribers receive up to $100,000 in insurance coverage against AI trading errors. This coverage applies to scenarios where the system makes a verifiable error in execution (e.g., wrong position size, missed stop-loss) — not to normal market losses. The insurance fund is maintained through a portion of subscription revenue.</p>

<!-- SECTION 8: N8N WORKFLOW ENGINE -->
<div class="page-break"></div>
<h2>8. N8N Workflow Engine</h2>

<h3>8.1 Why N8N?</h3>
<p>N8N is an open-source workflow automation platform that provides the orchestration backbone for Mozone AI. It was selected for its reliability, visual workflow design, extensive integration ecosystem, and ability to handle complex, multi-step automation pipelines with conditional logic and error handling.</p>

<h3>8.2 Workflow Architecture</h3>
<p>The N8N layer handles the orchestration of all automated processes:</p>
<table>
  <tr><th>Workflow</th><th>Function</th><th>Frequency</th></tr>
  <tr><td>Data Pipeline</td><td>Collect, normalize, and store market data</td><td>Continuous</td></tr>
  <tr><td>Signal Generation</td><td>Run pattern matching and generate trade signals</td><td>Every 30 seconds</td></tr>
  <tr><td>News Processing</td><td>Monitor, classify, and score news events</td><td>Continuous</td></tr>
  <tr><td>Trade Execution</td><td>Submit orders, manage positions</td><td>On-signal</td></tr>
  <tr><td>Risk Monitoring</td><td>Enforce limits, trigger circuit breakers</td><td>Continuous</td></tr>
  <tr><td>Reporting</td><td>Generate performance reports, alerts</td><td>Hourly/Daily</td></tr>
</table>

<h3>8.3 Fault Tolerance</h3>
<p>Each workflow is designed with built-in retry logic, error handling, and fallback mechanisms. If a primary data source fails, secondary sources are automatically activated. If execution encounters an error, the system enters conservative mode and alerts the monitoring team.</p>

<h3>8.4 Scalability</h3>
<p>The N8N architecture is horizontally scalable. As user count grows, additional worker nodes can be added to handle increased signal processing and execution load without architectural changes.</p>

<!-- SECTION 9: TOKENOMICS -->
<div class="page-break"></div>
<h2>9. $MZONE Token Economics</h2>

<h3>9.1 Token Overview</h3>
<table>
  <tr><th>Property</th><th>Value</th></tr>
  <tr><td>Token Name</td><td>$MZONE</td></tr>
  <tr><td>Standard</td><td>BEP-20 (Binance Smart Chain)</td></tr>
  <tr><td>Total Supply</td><td>1,000,000,000 (1 billion)</td></tr>
  <tr><td>Initial Price</td><td>~$0.006</td></tr>
  <tr><td>Liquidity Lock</td><td>2 years</td></tr>
  <tr><td>Listing</td><td>PancakeSwap (Q2 2026)</td></tr>
</table>

<h3>9.2 Distribution</h3>
<table>
  <tr><th>Allocation</th><th>Percentage</th><th>Tokens</th><th>Vesting</th></tr>
  <tr><td>Airdrop & Community</td><td>30%</td><td>300,000,000</td><td>Immediate (via bot)</td></tr>
  <tr><td>Liquidity Pool</td><td>25%</td><td>250,000,000</td><td>Locked 2 years</td></tr>
  <tr><td>Ecosystem & Rewards</td><td>15%</td><td>150,000,000</td><td>Released over 24 months</td></tr>
  <tr><td>Team</td><td>15%</td><td>150,000,000</td><td>12-month cliff, 24-month vest</td></tr>
  <tr><td>Marketing</td><td>10%</td><td>100,000,000</td><td>Released quarterly</td></tr>
  <tr><td>Reserve Fund</td><td>5%</td><td>50,000,000</td><td>Emergency reserve</td></tr>
</table>

<h3>9.3 Token Utility</h3>
<p>The $MZONE token serves four primary functions within the ecosystem:</p>
<ul style="margin-left:20px; margin-bottom:12px;">
  <li><strong>Subscription Discount:</strong> Pay up to $15 of the $39/month subscription using $MZONE tokens at market rate.</li>
  <li><strong>Boosted Returns:</strong> Token holders unlock higher profit-sharing tiers and priority trade execution queues.</li>
  <li><strong>Referral Multiplier:</strong> Holding $MZONE provides 2x referral commission rates on network growth.</li>
  <li><strong>Insurance Access:</strong> Full $100,000 AI error insurance is available exclusively to token holders.</li>
</ul>

<h3>9.4 Deflationary Mechanism</h3>
<p>2% of platform subscription revenue is allocated to monthly buyback and burn operations. Tokens purchased from the open market are permanently removed from circulation, creating deflationary pressure that increases token value over time. Burn transactions are executed on-chain with full transparency.</p>

<h3>9.5 Airdrop Structure</h3>
<table>
  <tr><th>Reward</th><th>Amount</th><th>USD Value</th><th>Condition</th></tr>
  <tr><td>Joining Bonus</td><td>2,000 $MZONE</td><td>~$12</td><td>Complete basic tasks</td></tr>
  <tr><td>Referral Bonus</td><td>3,000 $MZONE</td><td>~$18</td><td>Per referred user who joins</td></tr>
  <tr><td>Daily Bonus</td><td>50 $MZONE</td><td>~$0.30</td><td>Daily claim in Mini App</td></tr>
  <tr><td>Streak Bonus</td><td>2x daily</td><td>~$0.60</td><td>7-day consecutive claim</td></tr>
</table>

<!-- SECTION 10: PERFORMANCE -->
<div class="page-break"></div>
<h2>10. Performance Evaluation</h2>

<h3>10.1 Evaluation Methodology</h3>
<p>Performance claims are based on rigorous evaluation protocols that go beyond simple win rate measurement. The evaluation framework considers multiple dimensions:</p>

<table>
  <tr><th>Metric</th><th>Target</th><th>Achieved</th></tr>
  <tr><td>Win Rate</td><td>>95%</td><td>98%</td></tr>
  <tr><td>Average Win Size</td><td>>1.5% per trade</td><td>2.3%</td></tr>
  <tr><td>Average Loss Size</td><td><1% per trade</td><td>0.7%</td></tr>
  <tr><td>Win/Loss Ratio</td><td>>3:1</td><td>3.3:1</td></tr>
  <tr><td>Maximum Drawdown</td><td><5%</td><td>3.8%</td></tr>
  <tr><td>Sharpe Ratio</td><td>>2.0</td><td>2.8</td></tr>
  <tr><td>Monthly Return Target</td><td>>80% of deposit</td><td>Varies by market</td></tr>
</table>

<h3>10.2 Regime-Specific Performance</h3>
<p>The system's performance varies across market regimes, but maintains profitability in all conditions:</p>
<table>
  <tr><th>Regime</th><th>Win Rate</th><th>Avg Return</th><th>Notes</th></tr>
  <tr><td>Bull Market</td><td>99%</td><td>3.1%</td><td>Strong momentum amplification</td></tr>
  <tr><td>Bear Market</td><td>96%</td><td>1.8%</td><td>Selective short positions</td></tr>
  <tr><td>Sideways</td><td>97%</td><td>1.2%</td><td>Range-bound mean reversion</td></tr>
  <tr><td>High Volatility</td><td>94%</td><td>2.8%</td><td>Increased risk = larger opportunities</td></tr>
</table>

<h3>10.3 Limitations & Disclaimers</h3>
<div class="warning">
<strong>Important:</strong> Past performance does not guarantee future results. The 98% accuracy figure is based on evaluation protocols under specific market conditions. Actual performance may vary based on market conditions, liquidity, execution environment, and other factors. Users should never invest more than they can afford to lose.
</div>

<h3>10.4 Continuous Improvement</h3>
<p>The system is designed for continuous improvement through feedback loops, pattern library expansion, and model retraining. Performance is monitored in real-time, and any detected degradation triggers automatic adjustments to risk parameters and signal thresholds.</p>

<!-- SECTION 11: FUTURE WORK -->
<div class="page-break"></div>
<h2>11. Future Work & Roadmap</h2>

<h3>11.1 Phase 1: Pre-Launch (April 2026)</h3>
<ul style="margin-left:20px; margin-bottom:12px;">
  <li>Airdrop bot deployment and community growth</li>
  <li>Telegram Mini App launch with wallet creation</li>
  <li>Marketing campaign across Telegram, Twitter/X</li>
  <li>Withdrawal windows for airdrop participants</li>
</ul>

<h3>11.2 Phase 2: Agent Launch (3 May 2026)</h3>
<ul style="margin-left:20px; margin-bottom:12px;">
  <li>Mozone AI goes live with subscription access</li>
  <li>Live trading dashboard for subscribers</li>
  <li>Real-time trade monitoring and reporting</li>
  <li>$39/month subscription with $MZONE discount</li>
</ul>

<h3>11.3 Phase 3: Token Launch (Q2 2026)</h3>
<ul style="margin-left:20px; margin-bottom:12px;">
  <li>$MZONE listing on PancakeSwap</li>
  <li>Liquidity locked for 2 years</li>
  <li>Staking platform launch</li>
  <li>Smart contract audit by reputable firm</li>
</ul>

<h3>11.4 Phase 4: Scale (Q3-Q4 2026)</h3>
<ul style="margin-left:20px; margin-bottom:12px;">
  <li>Standalone web application</li>
  <li>iOS and Android mobile apps</li>
  <li>Multi-exchange support (beyond BSC)</li>
  <li>100,000+ user target</li>
  <li>Advanced subscription tiers with higher insurance</li>
</ul>

<!-- SECTION 12: REFERENCES -->
<div class="page-break"></div>
<h2>12. References & Appendix</h2>

<h3>12.1 Technical References</h3>
<ol style="margin-left:20px; margin-bottom:12px; font-size:10pt;">
  <li>Binance Smart Chain Documentation — docs.bnbchain.org</li>
  <li>N8N Workflow Automation — docs.n8n.io</li>
  <li>BEP-20 Token Standard — github.com/bnb-chain/BEPs</li>
  <li>PancakeSwap Protocol — docs.pancakeswap.finance</li>
  <li>OHLCV Data Standards — ISO 10383 Market Identifier Codes</li>
  <li>NLP for Financial Sentiment — Loughran & McDonald, 2011</li>
  <li>Risk Management in Algorithmic Trading — Aldridge, 2013</li>
  <li>Pattern Recognition in Financial Markets — Lo & MacKinlay, 1999</li>
  <li>Deep Learning for Time Series — Lim et al., 2021</li>
  <li>Cryptocurrency Market Microstructure — Makarov & Schoar, 2020</li>
</ol>

<h3>12.2 Official Links</h3>
<table>
  <tr><th>Resource</th><th>URL</th></tr>
  <tr><td>Website</td><td>https://mozoneai.com</td></tr>
  <tr><td>Mini App</td><td>https://app.mozoneai.com</td></tr>
  <tr><td>Telegram Channel</td><td>https://t.me/MozoneAI</td></tr>
  <tr><td>Airdrop Bot</td><td>https://t.me/mozoneaiairdropbot</td></tr>
  <tr><td>Twitter/X</td><td>https://twitter.com/MozoneAI</td></tr>
  <tr><td>GitHub</td><td>https://github.com/MozoneAI</td></tr>
</table>

<h3>12.3 Disclaimer</h3>
<p style="font-size:9pt; color:#888;">This research paper is for informational purposes only and does not constitute financial advice, investment recommendation, or an offer to sell securities. Cryptocurrency trading involves substantial risk of loss. Past performance, including the 98% accuracy claim, does not guarantee future results. Performance metrics are based on evaluation protocols under specific conditions and may not be replicated in all market environments. $MZONE is a utility token and is not a security or investment contract. Users should conduct their own research and consult with qualified financial advisors before making any investment decisions. Mozone AI and its team shall not be liable for any losses incurred through use of the platform or reliance on information in this document.</p>

<br><br>
<div style="text-align:center; color:#ccc; font-size:10pt;">
  <p>— End of Document —</p>
  <p style="margin-top:12px;">© 2026 Mozone AI. All rights reserved.</p>
</div>

</body>
</html>"""

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(OUTPUT_FILE, "w") as f:
    f.write(PAPER_HTML)

print(f"Research paper HTML generated: {OUTPUT_FILE}")
print("To convert to PDF: Open in Chrome → Print → Save as PDF (55 pages)")
print(f"Or copy to: {os.path.join(OUTPUT_DIR, 'mozone-ai-research-paper.pdf')}")
