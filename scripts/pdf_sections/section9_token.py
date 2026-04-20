from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm


def add_section9(story, s, make_table, hr):
    """$MZONE Token Economics — pages 41-45."""
    story.append(Paragraph("9. $MZONE Token Economics", s["MzH1"]))
    story.append(hr())

    story.append(Paragraph("9.1 Token Overview", s["MzH2"]))

    story.append(make_table(
        ["Property", "Value"],
        [
            ["Token Name", "$MZONE"],
            ["Token Standard", "BEP-20 (Binance Smart Chain)"],
            ["Contract Address", "0x49d6d5359cE2BB622a783AB31cc833e34d88f597"],
            ["Total Supply", "10,000,000,000 (10 billion)"],
            ["Initial Token Price", "~$0.006"],
            ["Liquidity Lock", "2 years (verifiable on-chain)"],
            ["Primary DEX", "PancakeSwap (Q2 2026)"],
            ["Contract Audit", "Planned pre-listing (third-party firm)"],
        ],
        col_widths=[140, 320]))
    story.append(Paragraph("Table 9.1: $MZONE Token Specifications", s["MzCaption"]))

    story.append(Paragraph(
        "The $MZONE token is designed as a utility token with concrete, clearly defined use cases "
        "within the Mozone ecosystem. It is explicitly not a security, investment contract, or "
        "financial instrument. The token enables access to platform features, provides economic "
        "incentives for community growth, and serves as the coordination mechanism for the "
        "decentralized aspects of the ecosystem.", s["MzBody"]))

    story.append(Paragraph("9.2 Token Distribution", s["MzH2"]))

    story.append(make_table(
        ["Allocation", "%", "Tokens", "Vesting", "Purpose"],
        [
            ["Airdrop & Community", "30%", "3,000,000,000", "Immediate via bot/app", "User acquisition, community growth"],
            ["Liquidity Pool", "25%", "2,500,000,000", "Locked 2 years on-chain", "DEX liquidity for trading"],
            ["Ecosystem & Rewards", "15%", "1,500,000,000", "24-month linear release", "Staking, competitions, bonuses"],
            ["Team", "15%", "1,500,000,000", "12-mo cliff, 24-mo vest", "Long-term team alignment"],
            ["Marketing", "10%", "1,000,000,000", "Quarterly as needed", "Growth campaigns, partnerships"],
            ["Reserve Fund", "5%", "500,000,000", "Multi-sig emergency", "Contingency and insurance backing"],
        ],
        col_widths=[90, 30, 75, 120, 145]))
    story.append(Paragraph("Table 9.2: Token Distribution Schedule", s["MzCaption"]))

    story.append(Paragraph(
        "The distribution design prioritizes community ownership (30% airdrop + 15% ecosystem = 45% "
        "to community) while ensuring adequate liquidity (25%) and long-term team alignment through "
        "meaningful vesting (15% with 12-month cliff). The team allocation vesting schedule ensures "
        "that the team's economic interests are aligned with long-term project success rather than "
        "short-term token price manipulation.", s["MzBody"]))

    story.append(Paragraph("9.3 Token Utility", s["MzH2"]))
    utility = [
        "<b>Subscription Discount</b> — Pay up to $15 of the $39/month subscription with $MZONE "
        "at market rate, creating consistent buy-side demand.",
        "<b>Boosted Returns</b> — Token holders unlock higher profit-sharing tiers and priority "
        "in trade execution queue during high-demand periods.",
        "<b>Referral Multiplier</b> — Holding 5,000+ $MZONE provides 2x referral rewards, "
        "incentivizing both holding and community growth.",
        "<b>Insurance Access</b> — $100,000 AI error insurance requires active $MZONE holding "
        "above the minimum threshold (1,000 $MZONE).",
        "<b>Governance (Future)</b> — Token holders will gain voting rights on key ecosystem "
        "parameters: fee structures, feature priorities, and fund allocations.",
    ]
    for u in utility:
        story.append(Paragraph(u, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("9.4 Deflationary Mechanism", s["MzH2"]))
    story.append(Paragraph(
        "A buyback-and-burn mechanism funded by 2% of all subscription revenue creates sustained "
        "deflationary pressure on the token supply. The mechanism operates as follows:", s["MzBody"]))

    story.append(Paragraph(
        "Each month, 2% of total subscription revenue is used to purchase $MZONE tokens from the "
        "open market via PancakeSwap. Purchased tokens are sent to a verified burn address "
        "(0x000...dEaD), permanently removing them from circulation. The burn is executed transparently "
        "on-chain and announced via the official Telegram channel.", s["MzBody"]))

    story.append(make_table(
        ["Users", "Monthly Revenue", "2% Burn Fund", "Tokens Burned (est.)", "Annual Deflation"],
        [
            ["1,000", "$39,000", "$780", "~130,000", "~0.16%"],
            ["5,000", "$195,000", "$3,900", "~650,000", "~0.78%"],
            ["10,000", "$390,000", "$7,800", "~1,300,000", "~1.56%"],
            ["50,000", "$1,950,000", "$39,000", "~6,500,000", "~7.8%"],
        ],
        col_widths=[50, 90, 80, 110, 90]))
    story.append(Paragraph("Table 9.3: Projected Deflationary Impact at Various User Counts", s["MzCaption"]))

    story.append(Paragraph("9.5 Airdrop Program Design", s["MzH2"]))
    story.append(Paragraph(
        "The airdrop program is designed as the primary user acquisition mechanism with carefully "
        "calibrated incentives:", s["MzBody"]))

    story.append(make_table(
        ["Reward Type", "Amount", "USD Value", "Condition"],
        [
            ["Joining Bonus", "2,000 $MZONE", "~$12", "Register via @mozoneaiairdropbot"],
            ["Per Referral", "3,000 $MZONE", "~$18", "Referred user completes registration"],
            ["Daily Bonus", "50 $MZONE", "~$0.30", "Daily claim in Mini App"],
            ["Task Completion", "100-500 $MZONE", "~$0.60-3.00", "Social tasks, quiz completions"],
        ],
        col_widths=[90, 90, 80, 200]))
    story.append(Paragraph("Table 9.4: Airdrop Reward Structure", s["MzCaption"]))

    story.append(Paragraph(
        "Withdrawal requires a minimum of 5 referrals and a minimum balance of approximately $100 "
        "equivalent in $MZONE. Withdrawal windows are scheduled periodically to manage liquidity "
        "impact and ensure orderly market behavior. This design prevents low-effort farming while "
        "rewarding genuine community building.", s["MzBody"]))

    story.append(Paragraph("9.6 Liquidity Strategy", s["MzH2"]))
    story.append(Paragraph(
        "The 25% liquidity allocation (2,500,000,000 tokens) will be paired with BNB in a PancakeSwap "
        "V3 liquidity pool. The liquidity is locked for 2 years via a reputable on-chain locking "
        "service, with the lock verifiable by any user. This lock prevents rug-pull scenarios and "
        "provides assurance to token holders.", s["MzBody"]))

    story.append(Paragraph(
        "Concentrated liquidity positions will be managed to optimize capital efficiency around the "
        "active trading range. As the token matures and price stabilizes, the liquidity range will "
        "be widened to support larger trading volumes with minimal slippage.", s["MzBody"]))

    story.append(Paragraph("9.7 Token Economic Sustainability", s["MzH2"]))
    story.append(Paragraph(
        "The long-term economic sustainability of the $MZONE token depends on the balance between "
        "demand drivers (subscription payments, utility access, holding incentives) and supply "
        "pressures (airdrop distribution, team vesting, ecosystem rewards). The deflationary burn "
        "mechanism provides a structural offset to new supply entering circulation.", s["MzBody"]))

    story.append(Paragraph(
        "At projected user growth rates, the system reaches economic equilibrium — where burn rate "
        "matches or exceeds new supply distribution — at approximately 15,000-20,000 active "
        "subscribers. Beyond this threshold, the token becomes net deflationary, creating favorable "
        "supply-demand dynamics for long-term holders.", s["MzBody"]))

    story.append(Paragraph("9.8 Smart Contract Security", s["MzH2"]))
    story.append(Paragraph(
        "The $MZONE smart contract follows established BEP-20 best practices with minimal custom "
        "logic to reduce attack surface. The contract implements:", s["MzBody"]))

    security = [
        "<b>Standard BEP-20 interface</b> — Full compliance with the ERC-20/BEP-20 standard "
        "including transfer, approve, transferFrom, and allowance functions.",
        "<b>Ownership controls</b> — OpenZeppelin Ownable pattern with renounce capability. "
        "Initial ownership used for liquidity setup, then ownership can be renounced.",
        "<b>No mint function</b> — Total supply is fixed at deployment. No additional tokens "
        "can ever be created, ensuring hard supply cap.",
        "<b>No pause/blacklist</b> — The contract does not include pause or blacklist functions, "
        "ensuring that token transfers cannot be arbitrarily restricted.",
        "<b>Verified source code</b> — Contract source will be verified on BscScan immediately "
        "after deployment, enabling public inspection by any user.",
        "<b>Third-party audit</b> — Pre-listing audit by a reputable blockchain security firm. "
        "Audit report will be published publicly on the website and GitHub.",
    ]
    for sec in security:
        story.append(Paragraph(sec, s["MzBullet"], bulletText="\u2022"))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("9.9 Token Velocity and Circulation Analysis", s["MzH2"]))
    story.append(Paragraph(
        "Token velocity — the rate at which tokens change hands — is a critical factor in token "
        "economic design. Excessive velocity (tokens are sold immediately after receipt) depresses "
        "price, while healthy velocity (tokens circulate through genuine utility) supports a "
        "sustainable market.", s["MzBody"]))

    story.append(Paragraph(
        "Mozone's token design incorporates multiple velocity reduction mechanisms:", s["MzBody"]))

    story.append(make_table(
        ["Mechanism", "Effect on Velocity", "Estimated Impact"],
        [
            ["Subscription payments", "Tokens sent to treasury, reducing circulating supply", "5-10% of supply locked in subscriptions"],
            ["Holding incentives (boosted returns)", "Users hold rather than sell to maintain tier benefits", "15-20% of supply held for utility"],
            ["Referral multiplier threshold", "5,000 $MZONE held unlocks 2x referral rewards", "Encourages accumulation"],
            ["Insurance access threshold", "1,000 $MZONE minimum for insurance coverage", "Base holding requirement"],
            ["Buyback-and-burn", "Permanently removes tokens from circulation", "1-8% annual deflation"],
            ["Liquidity lock", "25% of supply locked for 2 years", "Cannot enter circulation"],
            ["Team vesting", "15% of supply under time-lock", "Released gradually over 36 months"],
        ],
        col_widths=[115, 195, 150]))
    story.append(Paragraph("Table 9.5: Token Velocity Reduction Mechanisms", s["MzCaption"]))

    story.append(Paragraph("9.10 Comparison with Comparable Token Models", s["MzH2"]))
    story.append(Paragraph(
        "The $MZONE token economic model was designed after studying both successful and failed "
        "token launches in the DeFi and AI sectors:", s["MzBody"]))

    story.append(make_table(
        ["Project", "Token Model", "Outcome", "Lesson Applied to Mozone"],
        [
            ["Chainlink (LINK)", "Utility for oracle payments; staking", "Sustained value growth",
             "Genuine utility drives long-term demand"],
            ["FTT (FTX Token)", "Exchange discounts; buyback; collateral", "Collapsed (misuse of token as collateral)",
             "No collateral use; transparent burn; no leverage"],
            ["BNB", "Fee discounts; burn; ecosystem utility", "Massive success",
             "Multi-utility design; deflationary burn mechanism"],
            ["LUNA/UST", "Algorithmic stablecoin backing", "Catastrophic failure (death spiral)",
             "No algorithmic backing; fixed supply; no mint function"],
        ],
        col_widths=[70, 115, 105, 170]))
    story.append(Paragraph("Table 9.6: Comparable Token Model Analysis", s["MzCaption"]))

    story.append(Paragraph(
        "The key lessons incorporated into the $MZONE design are: (1) genuine, concrete utility "
        "is the only sustainable basis for token demand, (2) transparency in token operations "
        "(verifiable burns, public lock contracts) builds trust, (3) fixed supply with no mint "
        "function eliminates inflationary risk, and (4) avoiding complex algorithmic mechanisms "
        "reduces the risk of catastrophic failure modes.", s["MzBody"]))

    story.append(PageBreak())
