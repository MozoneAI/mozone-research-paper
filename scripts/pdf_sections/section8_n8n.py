from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section8(story, s, make_table, hr):
    """N8N Workflow Automation Engine — pages 37-40."""
    story.append(Paragraph("8. N8N Workflow Automation Engine", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph("8.1 Platform Selection Rationale", s["MzH2"]))
    story.append(Paragraph(
        "N8N is an open-source, self-hostable workflow automation platform serving as the orchestration "
        "backbone for Mozone AI. Selection over alternatives was based on comprehensive evaluation:", s["MzBody"]))

    story.append(make_table(
        ["Criterion", "N8N", "Zapier", "Airflow", "Custom"],
        [
            ["Self-Hosted", "Yes", "No", "Yes", "Yes"],
            ["Visual Design", "Excellent", "Good", "Limited", "None"],
            ["Error Handling", "Retry + dead letters", "Basic retry", "Robust", "Must build"],
            ["Integrations", "400+", "5000+", "Depends", "Must build"],
            ["Cost at Scale", "Free (self-hosted)", "Expensive", "Free", "Eng. time"],
            ["Real-Time", "WebSocket + Webhook", "Webhook only", "Scheduled", "Must build"],
            ["Scaling", "Worker nodes", "Auto (cloud)", "Celery", "Must build"],
        ],
        col_widths=[80, 90, 80, 80, 80]))
    story.append(Paragraph("Table 8.1: Workflow Platform Comparison", s["MzCaption"]))

    story.append(Paragraph(
        "N8N's combination of self-hosting capability, visual workflow design, built-in error handling, "
        "and extensive integration library made it the optimal choice. Self-hosting is critical for a "
        "trading system — dependence on a third-party cloud service for trade execution introduces "
        "unacceptable counterparty risk and latency.", s["MzBody"]))

    story.append(Paragraph("8.2 Core Workflows", s["MzH2"]))

    story.append(make_table(
        ["Workflow", "Function", "Trigger", "Frequency", "SLA"],
        [
            ["Data Pipeline", "Collect, normalize, store data", "WebSocket", "Real-time", "<1s"],
            ["Signal Gen", "Pattern matching, signals", "Timer + events", "30s cycles", "<5s"],
            ["News Processing", "Monitor, classify, score", "Webhooks", "Real-time", "<30s"],
            ["Trade Execution", "Submit orders, confirm fills", "Signal events", "On-signal", "<100ms"],
            ["Position Mgmt", "Monitor trades, manage exits", "Continuous", "10s cycles", "<1s"],
            ["Risk Monitor", "Enforce limits, breakers", "Continuous", "Real-time", "<100ms"],
            ["Reporting", "Calculate metrics, reports", "Scheduled", "Hourly + daily", "Best effort"],
            ["Alerts", "Send notifications", "Event-driven", "On-event", "<5s"],
        ],
        col_widths=[80, 120, 70, 70, 60]))
    story.append(Paragraph("Table 8.2: N8N Workflow Specifications", s["MzCaption"]))

    story.append(Paragraph("8.3 Workflow Design Patterns", s["MzH2"]))
    story.append(Paragraph(
        "Several design patterns are applied consistently across all workflows to ensure reliability "
        "and maintainability:", s["MzBody"]))

    patterns = [
        "<b>Idempotent Operations</b> — Every workflow step is designed to be safely re-executed without "
        "side effects. This enables automatic retry on failure without risk of duplicate trades or "
        "double-counted data.",
        "<b>Checkpoint and Resume</b> — Long-running workflows periodically save state checkpoints. If a "
        "workflow is interrupted (server restart, crash), it resumes from the last checkpoint rather than "
        "restarting from scratch.",
        "<b>Dead Letter Queues</b> — Failed operations that exhaust retry limits are routed to dead letter "
        "queues for manual review. This ensures no operation is silently lost.",
        "<b>Circuit Breaker Pattern</b> — External service calls (exchange APIs, data providers) are wrapped "
        "in circuit breakers that open after consecutive failures, preventing cascading failures.",
        "<b>Correlation IDs</b> — Every operation is tagged with a unique correlation ID that traces the "
        "full lifecycle from data ingestion through signal generation to trade execution and monitoring.",
    ]
    for p in patterns:
        story.append(Paragraph(p, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("8.4 Fault Tolerance", s["MzH2"]))
    story.append(Paragraph(
        "Primary data sources have secondary alternatives activated automatically on failure. Failed "
        "steps are retried with exponential backoff (initial: 1s, max: 60s, max retries: 5). "
        "Critical workflows run in active-passive redundancy with heartbeat-based failover in under "
        "5 seconds.", s["MzBody"]))

    story.append(Paragraph("8.5 Scalability", s["MzH2"]))
    story.append(Paragraph(
        "The N8N deployment is designed for horizontal scalability. Current architecture supports up to "
        "10,000 concurrent users with a 3-worker deployment. Beyond 10,000, the system scales linearly "
        "by adding workers, each handling approximately 3,000-5,000 additional users.", s["MzBody"]))

    story.append(Paragraph(
        "The scalability design considers three growth dimensions: user count (which increases the "
        "number of portfolio management workflow instances), asset count (which increases data pipeline "
        "throughput), and trade frequency (which increases execution and monitoring load). Each dimension "
        "is independently scalable by adding resources to the appropriate worker pool.", s["MzBody"]))

    story.append(Paragraph("8.6 Monitoring and Observability", s["MzH2"]))
    story.append(Paragraph(
        "Every workflow execution is instrumented with detailed metrics including: execution duration, "
        "step-level latency, data volume processed, error count and types, retry count, and resource "
        "utilization. These metrics are aggregated into dashboards that provide real-time visibility "
        "into system health and performance trends.", s["MzBody"]))

    story.append(Paragraph(
        "Alerting is configured at multiple levels: individual workflow failure (immediate notification), "
        "elevated error rates (5-minute rolling threshold), latency degradation (15-minute trending), "
        "and capacity projections (daily capacity planning reports). This multi-level approach ensures "
        "that operational issues are detected and addressed before they impact trading performance.", s["MzBody"]))

    story.append(Paragraph("8.7 Integration Architecture", s["MzH2"]))
    story.append(Paragraph(
        "N8N's extensive integration library enables Mozone AI to connect with a wide range of "
        "external services. The following table summarizes the key integration points:", s["MzBody"]))

    story.append(make_table(
        ["Integration", "Type", "Purpose", "Data Flow"],
        [
            ["Binance/BSC RPC", "WebSocket + REST", "Real-time price data, on-chain events", "Inbound (continuous)"],
            ["PancakeSwap Router", "Smart contract calls", "Trade execution, liquidity queries", "Bidirectional"],
            ["News APIs (multiple)", "REST + WebSocket", "News article ingestion", "Inbound (continuous)"],
            ["Twitter/X API", "REST (polling)", "Social sentiment monitoring", "Inbound (every 30s)"],
            ["Reddit API", "REST (polling)", "Community sentiment analysis", "Inbound (every 60s)"],
            ["Telegram Bot API", "REST + Webhook", "User notifications, alerts", "Outbound (event-driven)"],
            ["PostgreSQL", "Direct connection", "State persistence, trade history", "Bidirectional"],
            ["Redis", "Direct connection", "Caching, real-time feature store", "Bidirectional"],
            ["Prometheus/Grafana", "Metrics push", "Monitoring and dashboards", "Outbound (continuous)"],
        ],
        col_widths=[85, 80, 140, 105]))
    story.append(Paragraph("Table 8.3: N8N Integration Points", s["MzCaption"]))

    story.append(Paragraph("8.8 Deployment Architecture", s["MzH2"]))
    story.append(Paragraph(
        "The production deployment uses a containerized architecture on dedicated infrastructure. "
        "The N8N instance runs alongside supporting services in a Docker Compose environment with "
        "automatic restart policies and health checks:", s["MzBody"]))

    story.append(make_table(
        ["Service", "Container", "Resources", "Replicas", "Health Check"],
        [
            ["N8N Main", "n8n:latest", "4 vCPU, 8GB RAM", "1 (primary)", "HTTP /healthz every 10s"],
            ["N8N Worker", "n8n:latest (worker mode)", "2 vCPU, 4GB RAM each", "2-5 (auto-scale)", "Queue depth monitoring"],
            ["PostgreSQL", "postgres:16", "2 vCPU, 4GB RAM", "1 + standby", "pg_isready every 5s"],
            ["Redis", "redis:7-alpine", "1 vCPU, 2GB RAM", "1 + sentinel", "redis-cli PING every 5s"],
            ["Nginx Proxy", "nginx:alpine", "0.5 vCPU, 512MB", "1", "HTTP status every 10s"],
            ["Prometheus", "prom/prometheus", "1 vCPU, 2GB RAM", "1", "HTTP /-/healthy every 30s"],
        ],
        col_widths=[70, 95, 85, 85, 105]))
    story.append(Paragraph("Table 8.4: Production Deployment Architecture", s["MzCaption"]))

    story.append(Paragraph(
        "The N8N worker auto-scaling mechanism monitors the workflow execution queue depth. When "
        "the queue exceeds 100 pending items for more than 60 seconds, an additional worker is "
        "provisioned. When the queue drops below 20 items for more than 5 minutes and more than "
        "the minimum 2 workers are running, excess workers are gracefully drained and terminated. "
        "This elastic approach minimizes infrastructure costs while ensuring adequate capacity "
        "during peak trading periods.", s["MzBody"]))

    story.append(Paragraph("8.9 Backup and Recovery Procedures", s["MzH2"]))
    story.append(Paragraph(
        "Data integrity is protected through multiple backup layers:", s["MzBody"]))

    backups = [
        "<b>Real-time replication</b> — PostgreSQL streaming replication to a hot standby "
        "with synchronous commit, ensuring zero data loss (RPO = 0).",
        "<b>Hourly snapshots</b> — Full database snapshots stored in encrypted off-site "
        "storage, retained for 30 days.",
        "<b>Workflow version control</b> — All N8N workflow definitions are exported to Git "
        "after every modification, providing full audit trail and rollback capability.",
        "<b>Configuration backup</b> — All service configurations, environment variables, and "
        "deployment manifests are stored in version-controlled infrastructure-as-code.",
        "<b>Disaster recovery drills</b> — Monthly exercises to validate that the system can "
        "be fully restored from backups within the 5-minute RTO target.",
    ]
    for b in backups:
        story.append(Paragraph(b, s["MzBullet"], bulletText="\u2022"))

    story.append(PageBreak())
