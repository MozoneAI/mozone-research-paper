from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section6(story, s, make_table, hr):
    """News-Aware Intelligence System — pages 28-32."""
    story.append(Paragraph("6. News-Aware Intelligence System", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph("6.1 Information Architecture", s["MzH2"]))
    story.append(Paragraph(
        "Mozone's news intelligence system represents a critical differentiator from purely technical "
        "trading systems. By integrating real-time information from over 200 global sources, the system "
        "detects and contextualizes market-moving events before they are fully reflected in price, "
        "providing a temporal edge in signal generation.", s["MzBody"]))

    story.append(make_table(
        ["Source Category", "Count", "Examples", "Priority", "Latency"],
        [
            ["Financial News", "25+", "Bloomberg, Reuters, CNBC, FT, WSJ", "High", "<30s"],
            ["Crypto Outlets", "40+", "CoinDesk, The Block, Decrypt", "High", "<15s"],
            ["Exchange Announcements", "30+", "Binance Blog, Coinbase, OKX", "Critical", "<10s"],
            ["Regulatory Bodies", "20+", "SEC, CFTC, MiCA (EU), FATF", "Critical", "<60s"],
            ["Social Sentiment", "50+", "Twitter/X, Reddit, Telegram", "Medium", "<30s"],
            ["On-Chain Analytics", "15+", "Whale Alert, Nansen, Arkham", "Medium", "<120s"],
            ["Macro Economic", "20+", "Fed releases, CPI, employment", "High", "<60s"],
        ],
        col_widths=[90, 35, 150, 55, 50]))
    story.append(Paragraph("Table 6.1: News Source Categories and Coverage", s["MzCaption"]))

    story.append(Paragraph("6.2 NLP Processing Pipeline", s["MzH2"]))
    story.append(Paragraph(
        "Each incoming news item is processed through a six-stage NLP pipeline designed for financial "
        "and cryptocurrency content. The pipeline handles crypto-specific challenges including token name "
        "disambiguation, sarcasm detection in social media, and differentiation between speculation and "
        "factual reporting:", s["MzBody"]))

    story.append(make_table(
        ["Stage", "Function", "Output", "Accuracy"],
        [
            ["1. Ingestion", "Monitoring, dedup, normalization", "Unique news items", "99.5% dedup"],
            ["2. Classification", "Category + relevance scoring", "Tags + score (0-1)", "94% accuracy"],
            ["3. Entity Extraction", "Tokens, exchanges, people, orgs", "Named entities", "91% F1-score"],
            ["4. Sentiment", "Polarity (-1 to +1) and intensity", "Sentiment vector", "92% accuracy"],
            ["5. Urgency", "Time-criticality assessment", "Urgency score (0-1)", "88% accuracy"],
            ["6. Event Mapping", "Map to pattern library context", "Context enrichment", "Validated by outcome"],
        ],
        col_widths=[75, 135, 115, 105]))
    story.append(Paragraph("Table 6.2: NLP Processing Pipeline Stages", s["MzCaption"]))

    story.append(Paragraph("6.3 The Context-Not-Trigger Principle", s["MzH2"]))
    story.append(Paragraph(
        "News alone is never sufficient to trigger a trade. Mozone uses news events as context for "
        "pattern matching, not as independent trade signals. Price and volume confirmation from the "
        "pattern recognition engine are always required before any capital is committed.", s["MzBody"]))

    story.append(Paragraph(
        "This design is empirically grounded. Analysis of 50,000 news events over two years revealed "
        "that only 23% of events classified as 'market-moving' resulted in sustained price movements "
        "exceeding 1% within 4 hours. The remaining 77% were already priced in, quickly reversed, or "
        "had no measurable impact. By requiring price/volume confirmation, Mozone reduces exposure to "
        "false signals while retaining news as a contextual catalyst.", s["MzBody"]))

    story.append(Paragraph(
        "The practical effect of this principle is significant: during major news events where many "
        "traders rush to enter positions based on headlines alone, Mozone waits for confirmatory price "
        "action. This typically means entering 5-15 minutes after the initial headline — after the "
        "initial knee-jerk reaction but before the sustained move — achieving better entry prices and "
        "higher confidence signals.", s["MzBody"]))

    story.append(Paragraph("6.4 Sentiment Model Training", s["MzH2"]))
    story.append(Paragraph(
        "The sentiment model was trained on a proprietary dataset of 250,000 manually labeled "
        "crypto-specific news articles and social media posts. Labeling was performed by 15 annotators "
        "with cryptocurrency market expertise, achieving inter-annotator agreement of 89% (Cohen's "
        "kappa: 0.83). The model was fine-tuned from a pre-trained transformer architecture with "
        "domain-specific vocabulary additions.", s["MzBody"]))

    story.append(Paragraph(
        "Validation against a held-out test set of 10,000 items achieved 92% accuracy on binary "
        "sentiment and 87% on fine-grained 5-class sentiment (very negative, negative, neutral, "
        "positive, very positive). The model is retrained quarterly with new labeled data to maintain "
        "accuracy as market language evolves.", s["MzBody"]))

    story.append(Paragraph("6.5 Information Decay Functions", s["MzH2"]))
    story.append(Paragraph(
        "Not all news ages equally. A regulatory announcement may have market implications lasting weeks "
        "or months, while a social media rumor may be fully priced in within minutes. The system "
        "applies category-specific exponential decay functions to all processed news items:", s["MzBody"]))

    story.append(make_table(
        ["News Category", "Half-Life", "Full Decay", "Rationale"],
        [
            ["Exchange Hacks/Exploits", "4 hours", "48 hours", "Immediate impact, extended uncertainty"],
            ["Regulatory Announcements", "72 hours", "30 days", "Slow institutional response cycle"],
            ["Token Listings/Delistings", "2 hours", "24 hours", "Fast price adjustment"],
            ["Protocol Upgrades", "24 hours", "7 days", "Gradual market assessment"],
            ["Social Media Sentiment", "30 minutes", "4 hours", "Extremely rapid turnover"],
            ["Macro Economic Data", "12 hours", "7 days", "Gradual correlation effects"],
        ],
        col_widths=[120, 65, 65, 210]))
    story.append(Paragraph("Table 6.3: Information Decay Parameters by Category", s["MzCaption"]))

    story.append(Paragraph("6.6 Deduplication and Source Credibility", s["MzH2"]))
    story.append(Paragraph(
        "In the age of content aggregation, the same news event is often reported by dozens of sources "
        "within minutes. Without deduplication, this creates artificial amplification where a single event "
        "is counted multiple times, inflating its perceived significance. The system uses content "
        "fingerprinting (locality-sensitive hashing on normalized text) to identify duplicate reports and "
        "consolidate them into a single event record.", s["MzBody"]))

    story.append(Paragraph(
        "Source credibility scores are maintained for each monitored source based on historical accuracy "
        "of their reporting. Sources that have historically correlated with actual market movements receive "
        "higher credibility weights. This creates a dynamic reputation system where consistently reliable "
        "sources have greater influence on the aggregate sentiment signal.", s["MzBody"]))

    story.append(Paragraph("6.7 Social Media Signal Processing", s["MzH2"]))
    story.append(Paragraph(
        "Social media platforms — particularly Twitter/X, Reddit, and Telegram — represent a uniquely "
        "challenging data source. They offer the fastest information propagation (often preceding "
        "mainstream news by minutes or hours) but also the highest noise-to-signal ratio. The system "
        "employs specialized processing for social media content:", s["MzBody"]))

    story.append(make_table(
        ["Challenge", "Solution", "Effectiveness"],
        [
            ["Bot-generated content", "Account age/activity scoring, network analysis", "Filters 85%+ of bot content"],
            ["Sarcasm and irony", "Context-aware transformer model with crypto-specific training", "78% sarcasm detection accuracy"],
            ["Coordinated campaigns", "Temporal clustering detection, similar content fingerprinting", "Identifies 90%+ of coordinated posts"],
            ["Influencer amplification", "Follower-weighted sentiment with engagement normalization", "Reduces influencer bias by 60%"],
            ["Language variation", "Crypto-specific tokenizer with slang/meme vocabulary", "Handles $CASHTAGS, emoji sentiment, abbreviations"],
            ["Temporal noise", "30-minute half-life decay for social signals", "Prevents stale social data from affecting decisions"],
        ],
        col_widths=[95, 185, 180]))
    story.append(Paragraph("Table 6.4: Social Media Processing Challenges and Solutions", s["MzCaption"]))

    story.append(Paragraph(
        "A particularly important innovation is the distinction between 'organic' social sentiment "
        "and 'manufactured' sentiment. Organic sentiment arises from genuine market participants "
        "reacting to real events, while manufactured sentiment comes from coordinated groups attempting "
        "to manipulate market perception (pump-and-dump schemes, FUD campaigns). The system's "
        "coordinated campaign detection uses temporal analysis — if 50+ similar posts appear within "
        "a 5-minute window from accounts with correlated activity patterns, the sentiment signal "
        "from those posts is suppressed.", s["MzBody"]))

    story.append(Paragraph("6.8 Regulatory and Macro Event Processing", s["MzH2"]))
    story.append(Paragraph(
        "Regulatory announcements and macroeconomic data releases require specialized processing "
        "because their impact on cryptocurrency markets is often non-linear and delayed:", s["MzBody"]))

    story.append(Paragraph(
        "For regulatory events, the system maintains a structured database of regulatory bodies, "
        "their jurisdictions, and historical market impact profiles. When a regulatory announcement "
        "is detected, it is classified by type (enforcement action, new rule proposal, approval, "
        "ban, guidance) and matched against historical analogs to estimate expected market response. "
        "This classification feeds directly into the pattern matching engine as a contextual feature.", s["MzBody"]))

    story.append(Paragraph(
        "For macroeconomic events (CPI releases, Federal Reserve decisions, employment data), the "
        "system compares actual values against consensus expectations. The deviation from consensus — "
        "not the absolute value — is the primary signal, as markets have already priced in expected "
        "values. A CPI reading 0.3% above consensus has a very different market impact than a reading "
        "exactly at consensus, even if the absolute numbers are similar.", s["MzBody"]))

    story.append(Paragraph("6.9 News System Performance Metrics", s["MzH2"]))

    story.append(make_table(
        ["Metric", "Value", "Measurement Period", "Notes"],
        [
            ["Average news ingestion latency", "8.2 seconds", "Q4 2025", "From publication to system processing"],
            ["Deduplication accuracy", "99.5%", "Q4 2025", "False positive rate: 0.3%"],
            ["Sentiment classification accuracy", "92.1%", "Q4 2025", "Binary (positive/negative)"],
            ["Entity extraction F1-score", "91.4%", "Q4 2025", "Tokens, exchanges, people"],
            ["Event-to-pattern mapping accuracy", "84.7%", "Q4 2025", "Correct context enrichment"],
            ["False signal suppression rate", "77%", "Q4 2025", "News events not confirmed by price"],
            ["Average daily news items processed", "12,400", "Q4 2025", "Across all 200+ sources"],
            ["Unique events per day (post-dedup)", "2,100", "Q4 2025", "83% dedup compression ratio"],
        ],
        col_widths=[130, 65, 85, 180]))
    story.append(Paragraph("Table 6.5: News Intelligence System Performance Metrics", s["MzCaption"]))

    story.append(PageBreak())
