from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section4(story, s, make_table, hr):
    """System Architecture — pages 15-21."""
    story.append(Paragraph("4. System Architecture", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph("4.1 Architectural Overview", s["MzH2"]))
    story.append(Paragraph(
        "Mozone AI operates as a five-layer autonomous pipeline, where each layer is designed for "
        "modularity, fault tolerance, and real-time performance. The architecture ensures no single "
        "point of failure can compromise the system, and each component can be independently scaled, "
        "tested, and updated without full system downtime.", s["MzBody"]))

    story.append(Paragraph(
        "The five-layer pipeline processes market data from raw inputs through pattern recognition, "
        "risk validation, execution, and post-trade monitoring in a continuous streaming architecture. "
        "Data flows forward through the pipeline, while feedback signals flow backward to enable "
        "adaptive behavior and continuous model improvement.", s["MzBody"]))

    story.append(make_table(
        ["Layer", "Name", "Function", "Latency"],
        [
            ["1", "Data Ingestion", "Collect, normalize, validate market data from multiple sources", "<1s"],
            ["2", "Feature Construction", "Transform raw data into multi-timeframe feature vectors", "<2s"],
            ["3", "Model Layer", "Pattern matching, regime detection, signal generation", "<5s"],
            ["4", "Risk & Execution", "Risk validation, position sizing, order management", "<1s"],
            ["5", "Monitoring", "Performance tracking, drift detection, alerting", "Cont."],
        ],
        col_widths=[35, 95, 250, 80]))
    story.append(Paragraph("Table 4.1: Five-Layer Pipeline Architecture", s["MzCaption"]))

    story.append(Paragraph("4.2 Layer 1: Data Ingestion", s["MzH2"]))
    story.append(Paragraph(
        "The data ingestion layer continuously collects and normalizes market data from multiple sources, "
        "handling authentication, rate limiting, data quality validation, and fault-tolerant reconnection:", s["MzBody"]))

    story.append(make_table(
        ["Data Type", "Sources", "Frequency", "Validation"],
        [
            ["OHLCV Price", "Binance, DEXs", "1s ticks", "Gap detection, outlier filtering"],
            ["Order Flow", "Exchange WebSockets", "Real-time", "Timestamp sync, dedup"],
            ["Volatility", "Derived from price", "1m rolling", "Range checks, regime tagging"],
            ["Funding Rates", "Perpetual exchanges", "8-hour", "Cross-exchange comparison"],
            ["Correlations", "Multi-exchange agg", "15m rolling", "Positive-definite validation"],
            ["News/Sentiment", "200+ sources", "Real-time", "Dedup, relevance scoring"],
            ["On-Chain", "BSC/ETH RPCs", "Per-block", "Reorg handling"],
        ],
        col_widths=[85, 90, 70, 215]))
    story.append(Paragraph("Table 4.2: Data Ingestion Sources and Processing", s["MzCaption"]))

    story.append(Paragraph(
        "Each data source is equipped with health monitoring that tracks availability, latency, and data "
        "quality metrics. If a primary source degrades below acceptable thresholds, the system automatically "
        "fails over to a pre-configured secondary source. All incoming data is timestamped using a unified "
        "clock reference to ensure temporal consistency across the pipeline.", s["MzBody"]))

    story.append(Paragraph("4.3 Layer 2: Feature Construction", s["MzH2"]))
    story.append(Paragraph(
        "Raw data is transformed into a rich feature space using multi-timeframe extraction at six "
        "standard intervals: 1-minute, 5-minute, 15-minute, 1-hour, 4-hour, and daily. At each timeframe, "
        "the system computes comprehensive features capturing different aspects of market behavior:", s["MzBody"]))

    features = [
        "<b>Momentum indicators</b> — RSI, MACD, Rate of Change, Bollinger Band width and position, "
        "stochastic oscillator, and momentum divergence detection across timeframes",
        "<b>Volume profile analysis</b> — VWAP deviation, volume delta (buy vs. sell), cumulative volume "
        "distribution, Point of Control identification, and volume-at-price heat maps",
        "<b>Volatility regime classification</b> — Historical and implied volatility, ATR, "
        "Garman-Klass estimator, regime labels (low/medium/high/extreme) with transition probabilities",
        "<b>Order flow imbalance</b> — Bid-ask spread dynamics, order book depth asymmetry, "
        "large trade detection, aggressive flow identification, and trade clustering analysis",
        "<b>Cross-asset correlations</b> — Rolling correlations with BTC, ETH, DeFi index; "
        "decorrelation events flagged as regime change signals",
        "<b>News sentiment features</b> — Aggregated scores, urgency ratings, entity-specific sentiment, "
        "temporal decay functions, and event-type categorical embeddings",
        "<b>Microstructure features</b> — Trade arrival rate, quote-to-trade ratio, effective spread, "
        "market impact estimation, and toxicity scores from trade classification",
    ]
    for f in features:
        story.append(Paragraph(f, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph(
        "The total feature vector dimensionality across all timeframes exceeds 400 features per asset "
        "per evaluation cycle. Dimensionality reduction techniques (PCA and feature importance ranking) "
        "create a compact representation suitable for efficient pattern matching. Feature engineering is "
        "one of the most critical determinants of system performance — more so than model architecture.", s["MzBody"]))

    story.append(Paragraph("4.4 Layer 3: Model Layer", s["MzH2"]))
    story.append(Paragraph(
        "The model layer performs the core intelligence function: matching current market states against "
        "the historical pattern library to generate directional signals with confidence scores. The "
        "matching process uses an ensemble of five specialized components:", s["MzBody"]))

    story.append(make_table(
        ["Component", "Function", "Weight", "Update Frequency"],
        [
            ["Pattern Matcher", "Historical analog identification", "40%", "Continuous"],
            ["Trend Classifier", "Regime detection (bull/bear/sideways)", "20%", "Hourly"],
            ["Sentiment Scorer", "News/social signal integration", "20%", "Real-time"],
            ["Volatility Predictor", "Forward volatility estimation", "10%", "15-minute"],
            ["Correlation Analyzer", "Cross-market confirmation", "10%", "Hourly"],
        ],
        col_widths=[100, 170, 50, 140]))
    story.append(Paragraph("Table 4.3: Model Ensemble Components", s["MzCaption"]))

    story.append(Paragraph(
        "A trade signal is generated when ensemble confidence exceeds a configurable threshold "
        "(default: 85%). The signal includes direction, entry price range, profit target, stop-loss, "
        "expected time-to-profit, confidence score, contributing pattern count, and regime context. "
        "Signals below threshold are logged for analysis but not executed.", s["MzBody"]))

    story.append(Paragraph(
        "The ensemble approach provides resilience against individual component failures. If a single "
        "model experiences degraded performance, the remaining four models can still generate valid signals "
        "provided the reduced-weight confidence still exceeds the threshold. This design was validated "
        "empirically — removing any single component reduces system accuracy by only 3-7%, while removing "
        "two components degrades performance below acceptable levels.", s["MzBody"]))

    story.append(Paragraph("4.5 Layer 4: Risk and Execution", s["MzH2"]))
    story.append(Paragraph(
        "Every signal must pass through the risk management gate before execution. This is a non-negotiable "
        "architectural constraint — the risk engine cannot be bypassed, overridden, or disabled by any other "
        "component, including administrative interfaces.", s["MzBody"]))

    risk_checks = [
        "<b>Per-trade risk limit</b> — Maximum 2% of portfolio value at risk. If calculated risk "
        "exceeds threshold, position size is reduced or trade rejected.",
        "<b>Daily loss limit</b> — Maximum 5% cumulative daily losses. Breach triggers automatic "
        "shutdown of all new trade initiation for the remainder of the day.",
        "<b>Position concentration</b> — Maximum 30% allocated to any single asset to prevent "
        "over-exposure to correlated movements.",
        "<b>Correlation check</b> — New positions must have correlation below 0.7 with existing "
        "open positions, ensuring genuine diversification.",
        "<b>Volatility-adjusted sizing</b> — Dynamic adjustment based on current and predicted "
        "volatility. Higher volatility results in smaller positions.",
        "<b>Slippage estimation</b> — Expected slippage estimated from order book depth. Trades "
        "where slippage exceeds profit margin are rejected.",
        "<b>Circuit breaker status</b> — Checks for active breakers (exchange errors, unusual "
        "spreads, detected manipulation patterns).",
    ]
    for r in risk_checks:
        story.append(Paragraph(r, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("4.6 Layer 5: Monitoring and Feedback", s["MzH2"]))
    story.append(Paragraph(
        "Post-trade, the monitoring layer continuously tracks performance against expected outcomes. "
        "This serves dual purposes: operational monitoring (system health) and model monitoring "
        "(detecting performance degradation indicating drift or regime change).", s["MzBody"]))

    story.append(make_table(
        ["Metric", "Threshold", "Action on Breach"],
        [
            ["Actual vs. Expected Profit", ">2 std dev over 20 trades", "Flag for review; reduce confidence"],
            ["Time-to-Exit Accuracy", ">50% exceeding expected", "Review time-based exit parameters"],
            ["Slippage Analysis", ">0.3% average increase", "Switch to conservative execution"],
            ["Regime Detection", "<80% correct identification", "Force model recalibration"],
            ["Win Rate Rolling 50", "<90% over last 50 trades", "Reduce positions 50%; alert team"],
            ["System Latency", ">500ms average pipeline", "Switch to backup infrastructure"],
        ],
        col_widths=[130, 150, 180]))
    story.append(Paragraph("Table 4.4: Monitoring Metrics and Escalation Actions", s["MzCaption"]))

    story.append(Paragraph("4.7 Fault Tolerance and Redundancy", s["MzH2"]))
    story.append(Paragraph(
        "The architecture incorporates multiple layers of fault tolerance. Each data source has at least "
        "one backup alternative. The execution pipeline runs in active-passive redundancy with automatic "
        "failover. All state is persisted to durable storage with transaction guarantees. The N8N workflow "
        "engine provides built-in retry logic with exponential backoff and dead-letter queues.", s["MzBody"]))

    story.append(Paragraph(
        "Disaster recovery is designed for a Recovery Time Objective (RTO) of under 5 minutes and "
        "Recovery Point Objective (RPO) of zero (no data loss). State replication occurs synchronously "
        "to a standby instance, and the monitoring system can detect and initiate failover within 30 seconds "
        "of a primary instance failure.", s["MzBody"]))

    story.append(Paragraph("4.8 Security Architecture", s["MzH2"]))
    story.append(Paragraph(
        "Security is implemented as a defense-in-depth strategy with multiple overlapping layers "
        "of protection. The system processes sensitive financial data and controls trade execution, "
        "making security a top-priority concern:", s["MzBody"]))

    story.append(make_table(
        ["Security Layer", "Implementation", "Threat Addressed"],
        [
            ["Network Security", "VPN-isolated infrastructure, firewall rules, DDoS protection",
             "Unauthorized access, network attacks"],
            ["API Authentication", "JWT tokens with HMAC-SHA256, Telegram init data validation",
             "Impersonation, unauthorized API access"],
            ["Data Encryption", "AES-256 for wallet keys, TLS 1.3 for all network traffic",
             "Data interception, key compromise"],
            ["Access Control", "Role-based access, principle of least privilege",
             "Insider threats, privilege escalation"],
            ["Audit Logging", "Immutable logs for all state-changing operations",
             "Forensic investigation, compliance"],
            ["Input Validation", "Strict type checking, rate limiting, request size limits",
             "Injection attacks, resource exhaustion"],
            ["Dependency Security", "Automated vulnerability scanning, pinned versions",
             "Supply chain attacks"],
            ["Key Management", "Hardware-backed key storage for hot wallet, multi-sig for treasury",
             "Key theft, single point of compromise"],
        ],
        col_widths=[95, 195, 170]))
    story.append(Paragraph("Table 4.5: Security Architecture Layers", s["MzCaption"]))

    story.append(Paragraph(
        "The wallet security model is particularly important. User wallets created by the Mini App "
        "use private keys encrypted with AES-256 before storage. The encryption key is derived from "
        "a combination of user-specific and system-wide secrets using PBKDF2 with 600,000 iterations. "
        "Private keys are only decrypted in memory during transaction signing and are never written "
        "to disk in plaintext. For the system's trading wallet, a hardware security module (HSM) "
        "is used to protect the signing key, with transaction limits enforced at the HSM level.", s["MzBody"]))

    story.append(Paragraph(
        "Penetration testing is conducted quarterly by an external security firm, with all findings "
        "addressed within 48 hours for critical issues and 7 days for non-critical issues. A responsible "
        "disclosure program rewards external security researchers who discover and report vulnerabilities.", s["MzBody"]))

    story.append(PageBreak())
