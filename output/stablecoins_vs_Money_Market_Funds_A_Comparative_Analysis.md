## Are Stablecoins the Money Market Mutual Funds of the Future?

Nico Oefele *† , Dirk G. Baur , Lee A. Smales * *

October 2024

## Abstract

This paper is the first to provide a comprehensive comparison of two financial instruments: stablecoins and money market mutual funds (MMFs). We observe similar reserve asset backing  for  fiat  reserve  backed  (FRB)  stablecoins  and  MMFs,  similar  importance  of sponsor support, and the same negative association between macroeconomic indicators and peg deviations. Both instruments serve as short-term facilities for investors to park funds and  their  primary  market  microstructure  is  similar.  However,  FRB  stablecoins  exhibit larger  dispersions  from  the  dollar  peg,  significantly  higher  volatility,  and  a  lack  of transparency in their market infrastructure. Larger FRB stablecoins show reduced volatility compared to their smaller counterparts, with peg deviation drivers more closely resembling those of MMFs. We conclude that FRB stablecoins demonstrate remarkable similarities to MMFs and have the potential to become the MMFs of the future.

Keywords: stablecoins, money market mutual funds, financial intermediation, peg deviations, sponsor support

JEL codes : E44, G15, G18, G23

Declarations of interest : none

E-mail address: nico.oefele@uwa.edu.au.

We thank Peter O'Neill, Chanelle Duley, and participants at the 37th PhD Conference in Business and Economics in Melbourne and the 36th Australasian Finance and Banking Conference in Sydney for their helpful suggestions. We also extend our gratitude to Daniel Cahill, David Yermack and Ganesh Viswanath-Natraj for their valuable comments and suggestions.

"I have no intention to ban them [stablecoins], but, stablecoins are like money market funds, they're like bank deposits, but they're, to some extent, outside the regulatory perimeter and it's appropriate that they be regulated […] same activity, same regulation.'

## J. Powell, Sep 2021, Testimony before the House Financial Services Committee

## 1 Introduction

From  January  2020  to  December  2022,  the  global  cryptocurrency  market,  dominated  by Bitcoin  and  Ethereum,  approximately  quadrupled  in  size. Over  the  same  period,  the  total market capitalization of the fourteen largest stablecoins increased from around $6 billion to $138 billion, a 23-fold increase. Stablecoins are a category of crypto assets that aim to maintain a stable value relative to a specified currency, asset, or basket of assets, and they are commonly denominated in US dollars. In December 2022, the three largest stablecoins - Tether (USDT), USD Coin (USDC) and Binance USD (BUSD) - account for more than 90% of the stablecoin market. All three claim to be fully fiat reserve backed (FRB), meaning each issued coin is backed 1:1 by reserve assets, generally cash or high-quality liquid assets that can be considered cash  equivalents.  These  asset  holdings  connect  the  global  cryptocurrency  market  with  the traditional finance system.

The Financial Stability Board (FSB) emphasizes the potential threat that crypto assets pose to the global financial system. Among other structural features of stablecoins, the FSB highlights the maturity- and liquidity mismatches revealed by the balance sheets of stablecoin issuers. For example, liquidity  transformation  measures  the  ratio  of  less  liquid  assets  held  by  financial intermediaries that are funded through short-term liabilities. 3 Together with credit intermediation, maturity transformation, and leverage, liquidity transformation is one aspect the FSB utilizes to categorize financial intermediaries into the Narrow Measure sub-group of financial assets. The sub-group is part of the Non-Bank Financial Intermediation (NBFI) sector and poses a risk to financial stability through their bank-like activity but absence of bank-like regulation.

Money market mutual funds (MMFs) are one of the largest categories of entities within the Narrow Measure. MMFs are open-end mutual funds, meaning that investors can invest  or redeem  from  the  fund  at  any  time.  MMFs  bridge  short-term  financing  and  lending  by connecting entities with excess cash and entities with short-term financing needs. Shareholders of MMFs consider their investment as short-term, deposit like, and highly liquid. Bouveret et al. (2022) see a similarity in MMFs and stablecoins regarding their liquidity transformation activities.

Global  regulators  have  pursued  legislation  to  regulate  stablecoins  and  crypto  assets  more broadly.  For  example,  in  June  2022,  the  European  Parliament  provisionally  agreed  on  the markets in crypto assets (MiCA) bill, requiring stablecoin issuers to provide adequate minimum liquidity.  Martino (2022) analyzes the regulation, while also comparing it to MMF regulation. 4 He finds that MiCA does well in terms of investor protection and regulatory competition but does not sufficiently emphasize financial stability. Moreover, Martino suggests that stablecoins should be regulated similarly to MMFs, using MMF regulation after the Global Financial Crisis (GFC) as a blueprint.

Other legislation is lagging. For example, the US and Australia drafted, but have not passed any bills as of December 2022. In February 2023, the US Securities and Exchange Commission (SEC) announced that emerging technologies and crypto assets are one of their examination priorities for 2023.

The rapid growth of stablecoins in recent years and their similarity to MMFs suggest the need for a detailed comparison between the two. Our paper is the first to offer such a comparison, potentially  helping  investors  and  regulators  to  better  understand  the  benefits  and  risks  of stablecoins. We focus on the US market, as the large majority of stablecoins are pegged to the US  dollar.  Additionally,  more  than  half  of  the  roughly  $9  trillion  global  assets  under management by MMFs in 2022 are held in the US. 5

Our results reveal comparable reserve asset backing for FRB stablecoins and MMFs, similar importance of sponsor support, and the same negative association between macroeconomic indicators and peg deviations. Both instruments serve as cash management tools for investors, and their primary market microstructures are alike. However, differences emerge concerning the extent of dispersions from the peg, volatility, and transparency in market infrastructure. Larger FRB stablecoins show increased similarity to MMFs due to reduced volatility compared to  their  smaller  counterparts,  with  peg  deviation  drivers  more  closely  resembling  those  of MMFs.

The remainder of the paper is structured as follows. Section 2 provides an overview on the existing  literature.  Section  3  describes  the  data  collection  process  and  summarizes  the institutional  background  of  both  financial  instruments.  Section  4  includes  the  empirical analysis with subsections on descriptive statistics, peg deviations, volatility, and correlation. Lastly, Section 5 summarizes our main findings and draws conclusions.

## 2 Literature Review

Until  2020,  the  stablecoin  literature  mostly  addressed  the  connection  to  crypto  assets  primarily  Bitcoin  and  Ethereum.  The  primary  focus  was  on  cryptocurrencies'  response  to movements in the stablecoin market and vice versa, addressing price discovery and market efficiency (Ante et al., 2021; Griffin &amp; Shams, 2020). Additionally, Baur and Hoang (2021) and Lyons and Viswanath-Natraj (2023) find that stablecoins act as a safe haven in the crypto sphere  despite  the  link  between  the  volatility  of  the  largest  cryptocurrency,  Bitcoin,  and stablecoins (Grobys et al., 2021; Hoang &amp; Baur, 2021; Lyons &amp; Viswanath-Natraj, 2023).

The  growing  variety  of  stablecoins  has  also  triggered  research  into  differences  in  design. Catalini et al. (2022) describe the categorization of stablecoins as a spectrum ranging from centralization to decentralization in the following order: backed by fiat currency, backed by cryptocurrency, and backed by investment tokens corresponding to an algorithmic approach. They find that, during stressed market conditions, price stability decreases in the same order. Gadzinski  et  al.  (2023)  account  for  the  protocol  architecture  of  stablecoins  and  show  that stablecoins' price dynamics do not depend on the respective protocol design.

Bullmann et al. (2019) differentiate stablecoins based on three dimensions: the accountability of issuers, the decentralization of responsibilities and the asset by which its value is supported. Moreover, they describe how stablecoin issuers either create new coins when there is excess market demand or withdraw coins from circulation when there is demand contraction putting upward or downward pressure on the secondary market price (see also Catalini and de Gortari (2021)). In addition to the intervention by the stablecoin issuer, Lyons and Viswanath-Natraj (2023) identify arbitrageurs as a complementary decentralized mechanism to stabilize the peg.

Arbitrageurs take advantage of peg deviations in the secondary market. The primary market price is fixed to one unit of account under the assumption that the stablecoin issuer honors redemption requests of investors. Whenever a stablecoin trades at a discount in the secondary market, arbitrageurs buy stablecoins on the respective exchange and sell them in the primary market  at  par  to  the  issuer.  If  the  secondary  market  price  differs  between  exchanges, arbitrageurs can also employ cross-exchange arbitrage. Conversely, if the stablecoin trades at a premium in the secondary market, arbitrageurs may buy stablecoins at par in the primary market and sell them in the secondary market. Ma et al. (2023) find that while more efficient arbitrage increases price stability of stablecoins, it also increases run risk, as sellers gain a greater first-mover advantage.

Both the stablecoin issuer and the arbitrageur in the secondary market can exert upward or downward pressure on the price. Kwon et al. (2021) introduce a trilemma for stablecoin issuers, identifying two sources of downward and one source of upward price instability, showing that each stablecoin by design carries at least one source of price instability. The two sources for downward  price  instability  are  moral  hazard  of  the  operating  entity  and  poor  financial performance  of  the  entity,  along  with  its  exposure  to  external  market  risk.  Upward  price instability, on the other hand, is caused by limited coin supply.

Furthermore, Kwon et al. conduct a global survey in 34 countries to assess the general public's perception of the trilemma. Surprisingly, they find that FRB stablecoins are perceived as less stable  than  their  crypto  collateralized  counterparts,  with  moral  hazard  of  the  issuing  entity being the driver behind the results. In the absence of both mandatory audits and the obligation to distribute gains from reserve assets to holders, the issuer of FRB stablecoins might invest in riskier or less liquid assets to increase profitability.

Bruce et al. (2022) focus on legal aspects of stablecoins and question whether the relationship between a coin holder and reserve assets in the form of currency held in a bank account is a deposit. Wilmarth (2022) suggests that stablecoins should be regulated as securities to protect investors and markets and designated as deposits to bring issuers and distributors within the perimeter  of  regulators.  Liao  and  Caramichael  (2022)  argue  that  tokenization  of  financial markets may further drive growth in stablecoin usage.

Awrey (2020) was the first to mention MMFs in the context of stablecoins, differentiating good and bad money. Good money refers to the monetary liabilities of banks and MMFs, while bad money is privately issued debt, such as stablecoins. The comparative advantage of good money stems from the regulatory framework it's built upon.

Subsequent  research  focuses  on  private  money  creation,  specifically  privately  issued  debt (Gorton, Ross, et al., 2022; Gorton &amp; Zhang, 2021; Li &amp; Mayer, 2020, revised 2022; Liao &amp; Caramichael,  2022).  While  these  studies  draw  brief  comparison  between  stablecoins  and MMFs, they acknowledge differences. Gorton &amp; Zhang refer to the contractual relationship between stablecoin issuer and holder, arguing that most stablecoins could be deposits based on past logic applied by the US Department of Justice (DoJ). They further argue that coin holders do  not  have  '[…]  the  prospect  of  obtaining  gains  directly  from  holding  those  coins  […]' (Gorton &amp; Zhang, 2021, p. 12). Liao and Caramichael (2022) state that '[…] the behaviors of [these] public stablecoins are unique and differentiated from prime MMFs […].' It is worth mentioning that they solely refer to times of market distress.

Research  comparing  investor  behavior  and  fund  flow  patterns  during  crisis  periods  yields interesting results. Anadu et al. (2023) find similar flight-to-safety patterns among MMF and stablecoin holders during different run periods. Oefele et al. (2024) focus on the March 2023 banking crisis in the US and show that most FRB stablecoins and prime MMFs experience outflows in times of distress and that the largest FRB stablecoin and MMFs advised by the largest market players show capital inflows.

In  the  absence  of  regulation  requiring  regular  audits  of  FRB  stablecoins'  reserve  assets, stablecoins are subject to research questioning their existence (Barthelemy et al., 2021; Kim, 2022). Kim (2022) uses instrumental variables estimation to find a causal link between the crypto market and the traditional finance system, specifically the markets for commercial paper and Treasury bills. He shows that the fast-growing stablecoin sector created excess demand for

commercial paper and Treasury bills, with the yield of both instruments decreasing following a one standard deviation increase in the issuance of USDT and USDC.

In addition to the academic literature, organizations like the Bank for International Settlements, the International Monetary Fund, the FSB, and several central banks emphasize the increasing interconnectedness between crypto markets and the traditional finance system.

## 3 Data and Institutional Background

This  section  describes  the  data  collection  process,  categorization,  market  infrastructure, microstructure, legal environment, and monetary and financial characteristics of stablecoins and MMFs.

## 3.1 Data

Our stablecoin sample comprises a total of six FRB stablecoins. We retrieve daily prices (openhigh-low-close)  as  well  as  trading  volume  from  a  total  of  nine  centralized  cryptocurrency exchanges from CoinAPI. 6  Our analysis uses the aggregated volume-weighted price over all exchanges that offer a trading pair with the USD for the respective stablecoin. The exception to  this  is  the  price  analysis  provided  in  Section  3.3.  In  addition,  we  retrieve  the  market capitalization for the stablecoins in our sample from Coinmarketcap.  The sample period starts 7 1 January 2020 and ends 31 December 2022. Table 1 provides a summary of our stablecoin sample, including an indication of reserve assets held by each coin.

Table 1: Stablecoin sample descending by market capitalization as of 31 December 2022 . Reserve assets as of 30 December 2022. See Appendix A for sources.

| Name &amp;              | Market          | Reserve Assets                                                                                                                                                                                                                                                                                |
|---------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ticker              | Capitalization  |                                                                                                                                                                                                                                                                                               |
| Tether (USDT)       | $66,242,103,758 | 58.5% US Treasury Bills, 11% Money Market Funds, 7.9% Cash &amp; Bank  Deposits, 4% Other Investments, 8.7% Secured Loans, 4.5% Reserve  Repo Agreements, 5.1% Corporate Bonds, Funds &amp; Precious Metals,  0.1% Non-US Treasury Bills                                                              |
| USD Coin  (USDC)    | $44,540,806,740 | 53% Circle Reserve Fund Assets (BlackRock sponsored MMF with  Ticker USDXX), 23.5% US Treasury Securities, 23.5% USD Cash                                                                                                                                                                     |
| Binance USD  (BUSD) | $16,695,767,094 | 23% US Treasury Bills, 74% US Treasury Debt Pursuant to Overnight  Reverse Repo Agreements, 3% USD Cash                                                                                                                                                                                       |
| Pax Dollar  (USDP)  | $876,418,940    | 22% US Treasury Bills, 49% US Treasury Debt Pursuant to Overnight  Reverse Repo Agreements, 29% USD Cash                                                                                                                                                                                      |
| TrueUSD  (TUSD)     | $755,145,448    | US dollar balance held by US depository institutions, Hong Kong  depository institution, and Bahamian depository institution includes USD  cash, cash equivalents and short-term, highly liquid investments of  enough credit quality that are readily convertible to known amounts of  cash. |
| Gemini USD  (GUSD)  | $597,865,583    | 47% Cash Deposits, 20% Money Market Funds, 33% US Treasury Bills                                                                                                                                                                                                                              |

Table  2  presents  a  summary  of  the  MMF  sample.  The  sample  combines  two  datasets: DataStream  and  the  open  MMF  dataset  provided  by  the  SEC.   We  match  both  datasets 8 manually by comparing the name field of DataStream to the combination of series- and class name for the SEC database. We retrieve daily prices, monthly total net assets (TNA) as well as adjusted and unadjusted dividends from DataStream. The total net assets of each unique series identifier equal the sum of the total net assets for the share classes within, while the daily price per series identifier is the mean over all share classes. The breakdown of total net assets by type in Table 2 shows government MMFs are by far the largest category with $3.8 trillion.

Table 2: Summary of MMF sample by type. Total net assets in billion USD and aggregated as of 30 December 2022.

| Type       |   Number of MMFs |   Number of Investment Advisors | Total Net Assets   |
|------------|------------------|---------------------------------|--------------------|
| Government |              130 |                              57 | 3,766              |
| Prime      |               47 |                              22 | 524                |
| Tax-Exempt |               46 |                              18 | 98                 |
| Total      |              223 |                              59 | 4,388              |

The  open  MMF  dataset  aggregates  the  information  from  monthly  disclosures  via  N-MFP filings, including descriptive details such as registrant, class name, series name &amp; identifier, investment advisor and sub-advisors. The sample period aligns with our stablecoin sample.

To put the size of our MMF sample into context, we compare it to the weekly MMF asset data provided by the Investment Company Institute (ICI) for US MMFs. As of the end of December 2022, our MMF sample covers 92% - equivalent to $4.39 trillion - of all US MMFs.

## 3.2 Categorization

Issuers of stablecoins and MMFs can be categorized into different types primarily based on the assets backing the coins and shares.

The SEC defines three types of MMFs based on the fund's investments. Government MMFs invest in government securities, including cash, US Treasury bills, and other financial securities issued or guaranteed by the US government, with at least 99.5% invested in these assets. Taxexempt  municipal  security  MMFs  may  invest  in  securities  from  a  single  state  or  multiple municipalities.  Prime  MMFs  invest  in  riskier  assets  such  as  Repurchase  Agreements, Commercial Paper, Certificates of Deposit and Time Deposits of banks.

For stablecoins, we adopt a widely used categorization (Catalini et al. (2022); Grobys et al. (2021);  Harvey  et  al.  (2021))  of  three  types  based  on  the  underlying  assets  and  stability mechanisms used.

First, stablecoins backed by assets denominated in fiat currency, primarily in US dollar. The reserve assets  for  this  type  of  stablecoin  cover  a  range  like  that  of  MMFs,  including  cash, corporate debt, and Treasury bills (see Table 1). We categorize this type as fiat reserve backed

(FRB) stablecoins. As of December 2022, three FRB stablecoins have a direct link to MMFs, with USDT and GUSD partially backed by MMF shares as reserve assets. USDC collaborated with BlackRock in May 2022 to establish a government MMF, holding approximately half of its reserve assets.

Second, stablecoins backed by crypto reserves, known as crypto collateralized stablecoins. These stablecoins differ not only in their underlying assets but also in terms of scalability and decentralization. Issuers of crypto collateralized stablecoins can manage operations in a more decentralized manner, using smart contracts to automate reserve operations, and do not rely on centralized custodians to hold the underlying asset (Catalini et al., 2022).

Third, stablecoins that are neither backed by fiat reserves nor any collateral, generally referred to as algorithmic stablecoins.  Algorithmic stablecoins rely on smart contracts to adjust the 9 quantity of stablecoins through issuance and buybacks, using a rebase- or seigniorage algorithm to  maintain  the  peg.  These  stablecoins  typically  involve  a  pegged  cryptocurrency  with  a floating price to absorb short-term volatility. 10 The absence of an underlying reserve asset may explain the significant number of algorithmic stablecoin projects that have failed, including Basis Cash, Empty Set Dollar, and the notable example of TerraClassicUSD (USTC) in 2022.

Our  categorization  for  stablecoins  and  MMFs  is  summarized  in  Figure  1.  Design  options unique to crypto collateralized and algorithmic stablecoins preclude direct comparison with MMFs. The key difference is the absence of a direct connection to money markets, stemming from  the  lack  of  fiat  reserve  backing  through  money  market  instruments.  Therefore,  by definition, crypto collateralized and algorithmic stablecoins cannot evolve into future MMFs. Consequently, the subsequent comparison exclusively focuses FRB stablecoins and all MMFs.

## Categorization

Figure 1: Overview on MMF and stablecoin categorization

|             |               | Crypto              | Crypto              | Crypto              | Crypto         | Crypto      | Crypto   |
|-------------|---------------|---------------------|---------------------|---------------------|----------------|-------------|----------|
| Stablecoins | Stablecoins   | Fiat reserve backed | Fiat reserve backed | Fiat reserve backed | collateralized | Algorithmic |          |
| MMFs        | Retail        | Government          | Tax-exempt          | Prime               |                | Algorithmic |          |
|             | Institutional | Government          | Tax-exempt          | Prime               |                | Algorithmic |          |

Figure 1 underlines an important difference between both instruments: while stablecoins lack differentiation between retail and institutional investors, such differentiation exists for MMFs. Notably, some MMFs are only accessible to institutional investors.

Given  the  similarity  of  reserve  assets  between  both  instruments,  we  apply  the  SEC categorization for MMFs to FRB stablecoins. Our analysis reveals that USDC, BUSD, USDP and TUSD align closely to government MMFs. Conversely, USDT - the incumbent in the stablecoin market - and GUSD are closer to prime MMFs. Within the sample of stablecoins USDT is backed by the riskiest assets.

## 3.3 Market Infrastructure

MMFs are issued by a registrant that is backed by an investment advisor, typically referred to as  the  MMF's  sponsor.  Additionally,  they  often  have  one  or  more  subadvisors,  which  are typically  subsidiaries  of  the  sponsor.  Investment advisors may act as sponsors for multiple registrants and may group several MMFs under one registrant. Each MMF is designated with a series name and a unique series identifier. These series can be divided into share classes, identified by a distinct ticker symbol.

In  the  US,  Section  17  (f)  of  the  Investment  Company  Act  (ICA)  addresses  the  custody  of securities held by MMFs. We summarize the market infrastructure for MMFs in Figure 2.

Figure 2: Market infrastructure around MMFs. Dashed objects are optional.

<!-- image -->

The separation of funds held by the registrant and management by the sponsor is a defining characteristic  of  mutual  funds.  Morley  (2014)  identifies  three  common  features  of  this separation  of  funds  and  managers.  First,  economies  of  scope  and  scale  enable  sponsors  to manage  multiple  funds  simultaneously,  thereby  reducing  administrative  costs.  Second, precision in risk tailoring ensures that fund investors are exposed only to the risks associated with their investment. This separation shields investors from risk stemming from other lines of business of the sponsor. Third, exit rights are crucial, allowing investors to redeem their shares at the respective NAV daily under consideration of trading deadlines. This mechanism allows investors to express their preferences through withdrawals rather than control rights.

Fisch (2015) builds on the separation of funds and managers to argue for the beneficial effects of sponsor support. Mechanisms of sponsor support include leveraging the sponsor's reputation or purchasing reserve asset at a premium over their market value (Parlatore, 2016). Throughout history,  sponsor  support  proved  to  be  a  commonly  used  stability  mechanism.  Brady  et  al. (2012)  show  that  non-contractual  sponsor  support  for  prime  MMFs  was  frequent  and

significant during the period from 2007 and 2011. However, it's important to note that sponsor support is voluntary under SEC regulation. 11

The market infrastructure for FRB stablecoins, as summarized in Table 3, exhibits considerable heterogeneity. Issuers enjoy significant flexibility due to the current absence of comprehensive regulation. From the sample of stablecoins, Paxos Trust Company and Gemini Trust Company are headquartered in New York, making them subject to the Virtual Currency Guidance issued by the New York Department of Financial Services (NYDFS) in June 2022, becoming effective in September 2022. 12

The issuing entities of USDC and TUSD are incorporated in Massachusetts and the British Virgin  Islands,  respectively.  As  of  January  2023,  neither  jurisdiction  has  implemented comparable guidance. USDT is issued by Tether Holdings Limited, a company based in Hong Kong.

Table 3: Market infrastructure of fiat reserve backed stablecoins. See Appendix A for sources.

| Ticker   | Issuer                                                 | Jurisdiction                            | Parent                                             | Custodian                                                                                                                                        | Exchange   |
|----------|--------------------------------------------------------|-----------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| USDT     | Tether Limited                                         | Hong Kong,  HK                          | iFinex Inc.                                        | Undisclosed. Among others,  Deltec Bank &amp; Trust, Capital  Union                                                                                  | Bitfinex   |
| USDC     | Centre  Consortium   (backed by  Circle and  Coinbase) | Massachusetts,  US  and California,  US | Circle  Internet  Financial  Limited and  Coinbase | BNY Mellon, Citizens Trust Bank,  Customers Bank, NY Community  Bank, Signature Bank, Silicon  Valley Bank 13 , Silvergate Bank 14 ,  US Bancorp |            |
| BUSD     | Paxos Trust  Company  (in partnership  with Binance)   | New York, US                            |                                                    | BMO Harris Bank, Customers  Bank, Signature Bank, Silvergate  Bank, State Street Bank and Trust  Company                                         | (Binance)  |
| USDP     | Paxos Trust  Company                                   | New York, US                            |                                                    | BMO Harris Bank, Customers  Bank, Signature Bank, Silvergate  Bank, State Street Bank and Trust  Company                                         | itBIT      |
| TUSD     | Techteryx  Limited                                     | British Virgin  Islands (BVI)           |                                                    | Silvergate Bank, Signet, Fist Digital  Trust, Prime Trust, BitGo                                                                                 |            |
| GUSD     | Gemini Trust  Company                                  | New York, US                            |                                                    | State Street Bank and Trust  Company, Signature Bank,  Silvergate Bank, Oppenheimer &amp;  Co. Inc., Goldman Sachs Asset  Management                 | Gemini     |

Several FRB stablecoins are associated with a cryptocurrency exchange either directly operated by the issuer or its parent company. These exchanges facilitate stablecoin trading pairs, such as BUSD/USDT, effectively bridging transactions between stablecoins.

USDT is the largest stablecoin by market capitalization, yet it exhibits the least transparency in market infrastructure within our sample. The issuer of USDT operates outside of the US regulatory perimeter and does not disclose information about the custodians of its underlying reserve assets. Additionally, the issuer's parent company, iFinex Inc., registered in the British Virgin Islands, also owns the cryptocurrency exchange Bitfinex.

This affiliation of the stablecoin issuer or its parent company with a cryptocurrency exchange bears additional risks. Figure 3 shows that USDT demonstrates greater stability on Bitfinex, the parent exchange, compared to other exchanges. Moreover, the trading volume on Bitfinex

relative  to  six  other  exchanges  notably  increases  from  May  to  August  in  2022.  The  price discrepancies among exchanges violates the law-of-one-price principle, which arbitrageurs in traditional  financial  markets  typically  eliminate  almost  instantaneously.  Our  findings  echo those of Makarov and Schoar (2019), who identify enduring and recurring deviations in Bitcoin prices across different exchanges.

Figure 3: Daily closing prices for the trading pair USDT/USD on seven different exchanges and relative trading volume on Bitfinex in percent. Horizontal line equals 1 USDT/USD. Vertical dotted lines equal TerraUSD and FTX collapse, respectively. Exchanges in dashed lines indicate minor trading volume on average below two percent per day over the sample period. Data source: coinapi.io. Sample period: 1 April 2022 to 31 December 2022.

<!-- image -->

## 3.4 Market Microstructure

Investors holding MMF shares trade their shares in the primary market, directly with the issuing entity or through authorized intermediaries, primarily banks. Purchase and redemption requests submitted before to the cut-off time are processed on the same business day, reflecting MMFs' open-ended investment structure. Holders of MMF shares are charged operating expenses, and sometimes also transaction expenses depending on the backing investment advisor. Minimum investment thresholds vary based on fund categories or share classes, and redemptions can be temporarily suspended as defined in Rule 2a-7(c)(2)(i) of the ICA of 1940.

Stablecoins can be traded in both primary and secondary market. The process for redemptions and purchases directly with the issuer is consistent across all stablecoins, with no notice periods mentioned  in  their  terms  and  conditions. All  stablecoins  in  our  sample  allow  redemptions directly with the issuer. 15 However, Tether Limited, within our stablecoin sample, imposes charges  for  fiat  deposits  and  redemptions.  Fiat  deposits  carry  a  fee  of  0.1%,  while  fiat redemptions incur expenses equivalent to the greater of $1,000 US dollar or 0.1% of the trade value. 16 This asymmetric fee structure for fiat redemptions is interpreted as a mechanism to discourage direct redemptions and incentivize trading in the secondary market. Additionally, Tether  Limited  charges  a  one-time  account  verification  fee  of  $150  US  dollar  for  primary market participation, contrasting with other FRB stablecoin issuers who provide free account verification.

The issuers of USDT and TUSD reserve the right to delay or suspend wire submissions or redemption requests, while the issuer of USDC also reserves the right to change, suspend or delay transactions. Paxos and Gemini do not address the suspension of redemptions in their terms and conditions.

Secondary market trading for stablecoins is facilitated by cryptocurrency exchanges. We focus on trading pairs from stablecoins to USD, as only those allow a redemption to fiat currency. 17

Figure 4 displays the number of exchanges offering trading in stablecoins each day  in our sample. As the largest FRB stablecoin by market capitalization, USDT also has the largest secondary  market,  with  seven  exchanges.  As  of  December  2022,  USDT  accounts  for approximately  57%  of  trading  volume  by  pair  denomination  in  the  global  cryptocurrency market, reflecting its significant role in cryptocurrency trading. USDC, another widely adopted stablecoin, can be exchanged to USD on a maximum of six exchanges since the end of 2021. In contrast, all other stablecoins in our sample average trading on less than three exchanges per day.

Figure 4: Number of cryptocurrency exchanges offering a trading pair between the respective stablecoin and the US dollar. We use the 7-day rolling average to soften the impact of single days when trading pair data is not available for an exchange. Data source: coinapi.io. Sample period: 1 January 2020 to 31 December 2022.

<!-- image -->

We show the trading volume of the stablecoin/USD trading pairs in Table 4 Error! Not a valid bookmark self-reference. .  USDT, USDC and BUSD, the top three FRB stablecoins (Top3 FRB),  exhibit  significantly  larger  mean  daily  volumes  across  all  exchanges  analyzed. Additionally, BUSD is predominantly traded on a single exchange, Binance. The two smallest FRB stablecoins by market capitalization, TUSD and GUSD, demonstrate a mean daily trading volume to USD of less than $0.1 million. Moreover, their USD trading pairs were available on only one exchange until mid-2021.

Table 4: Descriptive table for daily volume traded for the trading pair stablecoin/USD. The three columns to the right indicate the percentage of days in the sample period when one exchange handles 75%, 90%, respectively 95% of the trading volume. Source: coinapi.io. Note: Figures are in million USD. Sample period: 1 January 2020 to 31 December 2022.

|      |       | Daily Volume (USD Trading Pair)   | Daily Volume (USD Trading Pair)   | Daily Volume (USD Trading Pair)   | Daily Volume (USD Trading Pair)   | Daily Volume on one exchange &gt;   | Daily Volume on one exchange &gt;   | Daily Volume on one exchange &gt;   |
|------|-------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|----------------------------------|----------------------------------|----------------------------------|
|      | Obs   | Mean                              | SD                                | Min                               | Max                               | 75%                              | 90%                              | 95%                              |
| USDT | 1,091 | 196                               | 193                               | 0.9                               | 2,100                             | 2%                               | 0%                               | 0%                               |
| USDC | 1,091 | 18                                | 21                                | 0                                 | 312                               | 65%                              | 22%                              | 12%                              |
| BUSD | 1,090 | 2.2                               | 4.1                               | 0                                 | 61                                | 98%                              | 94%                              | 91%                              |
| USDP | 1,088 | 0.3                               | 0.6                               | 0                                 | 8.7                               | 70%                              | 48%                              | 38%                              |
| TUSD | 1,074 | 0.1                               | 2                                 | 0                                 | 2.2                               | 97%                              | 92%                              | 86%                              |
| GUSD | 896   | 0.02                              | 0.04                              | 0                                 | 0.6                               | 88%                              | 78%                              | 70%                              |

## 3.5 Legal Environment

In the United States, MMFs are regulated by the SEC under Rule 2a-7 of the ICA of 1940, which governs the organization of companies offering their own securities to public investors. The latest amendment to the MMF regulatory framework in 2021 marks the third within eleven years, prompted by research following the COVID-19 market turmoil. However, there remains controversy over whether these regulations effectively address underlying issues (Anadu et al., 2022; Li et al., 2021).

Investors primarily use MMF shares for cash management rather than investment purposes (Ondersma, 2013). They receive compensation for the risk of a potential runs on MMFs in the form of a monthly dividend reflecting short-term interest rates (see Table 5). The monthly dividend payment is based on the performance of the underlying reserve assets. Within our sample of MMFs, the average monthly dividend paid is 0.04%.

MMFs emerged in the late 1970s, their popularity in the US driven by interest rate caps on bank deposits due to Regulation Q. Thus, the comparison to bank deposits was inherent to their emergence, prompting regulators to classify the relationship between holder and issuer of this new financial  instrument.  The  classification  aimed  to  determine  whether  MMFs  should  be considered  deposits  under  Section  21(a)  of  the  Glass-Steagall  Act  of  1933.  US  authorities decided that there is no debtor-creditor relationship between MMFs and their shareholders, who are considered owners of the fund. 18

In  2008, the Lehman Brothers bankruptcy triggered the liquidation of the Reserve Primary Fund, a prime MMF with over $60 billion in total net assets. The proceeds from liquidating the remaining reserve assets were distributed pro rata to shareholders. The protracted liquidation commenced  with  an  initial  distribution  of  $26  billion  in  October  2008.  Finally,  each shareholder recovered 98% of their individual investment after the final distribution in January 2010. 19 While the Reserve Primary Fund became a creditor of Lehman Brothers bankruptcy estate,  investors  in  the  fund  did  not  compete  with  external  creditors  for  the  funds'  reserve assets.

Stablecoins emerged in 2014 with the primary use case of facilitating cryptocurrency trading. Hoang and Baur (2021) found a high correlation between trading volumes of stablecoins and the largest cryptocurrency, Bitcoin, underlining the importance of stablecoins in crypto trading. Stablecoins also enable market participants to transfer funds between exchanges (Bullmann et al., 2019; Lyons &amp; Viswanath-Natraj, 2023) and to hold funds in the crypto space rather than in  fiat  currency.  Furthermore,  stablecoins  are  the  backbone  of  decentralized  trading  and lending, accounting for almost half of the liquidity available on decentralized exchanges. 20

Stablecoin issuers do not distribute capital gains obtained from holding reserve assets to coin holders. Therefore, holders of FRB stablecoins do not have the prospect of directly benefiting from holding them. Gorton and Zhang (2021) suggest that potential gains realized from holding

a stablecoin and selling it for a profit in the secondary market are not linked to the stablecoin issuers investments but rather depend on movements in the broader cryptocurrency market.

Despite the absence of direct compensation, stablecoin holders have the opportunity to actively manage their holding in order to achieve a return. Gorton, Klee, et al. (2022) interpret the option for stablecoin holders to lend out their coins to leveraged traders in crypto markets as an indirect compensation for the run risk they face. This process, known as staking, involves looking up stablecoins for periods ranging from 30 days to several months, which diminishes the staking incentive despite high lending rates. 21

Recent literature on stablecoins explores the fundamental nature of the relationship between stablecoin issuers and holders, and whether these instruments should be considered deposits, securities, or both. Gorton and Zhang (2021) address these questions by referencing the GlassSteagall Act and the history of MMFs. They conclude that, with the potential exception of USDT, the relationship between FRB stablecoin issuers and holders constitutes a debt contract. As a result, if the FRB stablecoin issuer faces bankruptcy, holders would become creditors.

The terms and conditions outlined by the FRB stablecoin issuers vary significantly. Bruce et al.  (2022)  identify  a  spectrum  ranging  from  reserve  assets  likely  being  the  property  of  the investors to reserve assets being property of the stablecoin issuer. If the issuer faces bankruptcy, the  latter  scenario  would  mean  investors'  redemption  rights  become  claims  against  the bankruptcy estate. However, there is substantial uncertainty regarding whether reserve assets would be included in the bankruptcy estate. If included, investors would likely be classified as unsecured creditors with low chances of recovering their investments.

## 3.6 Monetary and Financial Characteristics

This section analyzes whether MMFs and stablecoins qualify as money or as financial assets.

We place this discussion within the broader monetary economics literature, adopting the view of Lagos et al. (2017), who describe non-commodity money as a medium of exchange lacking consumption or production properties. This function as a medium of exchange is viewed as the

defining characteristic of money, alongside its role as a store of value and unit of account (Kiyotaki &amp; Wright, 1989).

MMF  shares  are  classified  as  broad  money  under  the  definition  of  the  Organization  for Economic  Co-operation  and  Development  (OECD).  Broad  money,  unlike  narrow  money, measures money supply beyond fiat currency in circulation and overnight deposits, including longer-dated  deposits,  repurchase  agreements,  debt  securities  up  to  two  years,  and  MMF shares. 22 The contractual obligation of MMFs to allow redemptions for cash on a daily basis and their regulatory treatment as marketable securities under the ICA qualify them as financial assets. Thus, MMF shares can be categorized as (broad) money and financial asset.

Independent of being debt or equity contract (see section 3.5), FRB stablecoins are financial assets  under  IAS  32  definition. 23 They  are  either  classified  as  equity  instrument  of  the stablecoin  issuer  or  as  contractual  right  to  receive  cash  upon  redemption.  Since  FRB stablecoins also act as a unit of account 24 for cryptocurrencies and as a medium of exchange between cryptocurrencies and fiat currency, we conclude that FRB stablecoins are also moneylike.

By  analyzing  the  USDT  trading  volume  to  fiat  currency,  to  cryptocurrency  and  to  other stablecoins, we further assess if FRB stablecoins' primary trading purpose is related to fiat currency or cryptocurrency. 25 Figure 5 shows the 30-day moving average of the USDT trading volume.

Figure 5: Tether (USDT) non-directional trading volume to and from fiat currency, cryptocurrency and other stablecoin. We show the 30-day moving average to smoothen the highly volatile daily observations. Sample period: 1 January 2020 to 31 December 2022.

<!-- image -->

Over the sample period, most USDT trading volume involves fiat currencies. This indicates that FRB stablecoins primarily serve as vehicle currency bridging the cryptocurrency market and the traditional financial market. The higher trading volume of USDT with fiat currency compared  to  cryptocurrency  suggests  FRB  stablecoins  have  money-like  status  beyond  the cryptocurrency market.

FRB stablecoins and MMFs are both financial assets and show money-like qualities. In the absence of centrally issued fiat money, FRB stablecoins are the most money-like instrument in cryptocurrency  markets.  However,  from  a  broader  global  perspective,  they  possess  fewer money-like qualities than MMFs which are defined as broad money.

## 4 Empirical Analysis

In this section, we investigate time series data for peg deviations and apply a regression model to identify drivers of peg deviations for both MMFs and FRB stablecoins.

## 4.1 Descriptive Statistics

Table 5 summarizes the descriptive statistics for samples of stablecoins in Panel A and MMFs in Panel B.

Table 5: Descriptive statistics for fiat reserve backed stablecoins in Panel A and MMFs by category in Panel B. Stablecoin prices and volume are from coinapi.io, market capitalization from coinmarketcap.com. MMF data from DataStream. Note: Volume, market capitalization, total net assets in billion USD; prices and dividends in USD. Sample period: 1 January 2020 to 31 December 2022.

|                                             | Obs     | Mean    | Std. Dev.   | Min     | Max      |
|---------------------------------------------|---------|---------|-------------|---------|----------|
| Panel A: Fiat Reserve Backed Stablecoins 26 |         |         |             |         |          |
| Open                                        | 6,330   | 0.9999  | 0.0062      | 0.9000  | 1.1999   |
| High                                        | 6,330   | 1.0028  | 0.0313      | 0.9555  | 1.9841   |
| Low                                         | 6,330   | 0.9980  | 0.0072      | 0.7807  | 1.0500   |
| Close                                       | 6,330   | 0.9997  | 0.0068      | 0.8141  | 1.1988   |
| Volume Traded                               | 6,576   | 11.8046 | 27.5200     | 0.0002  | 315.5510 |
| Market Capitalization                       | 6,576   | 13.6114 | 22.4695     | 0.0037  | 83.2359  |
| Panel B: MMFs 27                            |         |         |             |         |          |
| Total Net Assets                            | 173,529 | 17.3061 | 38.1243     | 0.00004 | 281.1826 |
| Price                                       | 25,056  | 1.0003  | 0.0004      | 0.9929  | 1.0015   |
| Dividend Rate 28                            | 29,283  | 0.0003  | 0.0006      | 0       | 0.0131   |
| Government                                  |         |         |             |         |          |
| Total Net Assets                            | 100,719 | 26.0241 | 46.9949     | 0.0001  | 281.1826 |
| Dividend Rate                               | 18,493  | 0.0003  | 0.0006      | 0       | 0.0131   |
| Prime                                       |         |         |             |         |          |
| Total Net Assets                            | 36,792  | 8.5101  | 16.8064     | 0.0001  | 161.2298 |
| Price                                       | 20,358  | 1.0003  | 0.0004      | 0.9980  | 1.0015   |
| Dividend Rate                               | 6,210   | 0.0004  | 0.0006      | 0       | 0.0035   |
| Tax-Exempt                                  |         |         |             |         |          |
| Total Net Assets                            | 36,018  | 1.9123  | 3.1192      | 0.00004 | 18.4045  |
| Price                                       | 4,698   | 1.0003  | 0.0004      | 0.9929  | 1.0011   |
| Dividend Rate                               | 4,580   | 0.0003  | 0.0005      | 0       | 0.0028   |

Not all MMFs have a floating NAV. In their 2014 amendment to Rule 2a-7 of the ICA of 1940, the  SEC  imposed  several  restrictions,  including  liquidity  fees,  redemption  gates  and  the requirement of a floating NAV on institutional prime and tax-exempt municipal MMFs. These funds must use mark-to-market pricing for all underlying reserve assets and to update their

share price daily after market close. 29 The amendment addresses the issue that investors in those funds have historically made the heaviest redemptions during times of market stress.

For MMFs with a floating NAV only one price per day is published, thus, Panel B shows one price per day with a mean of $1.0003. 30 Both the price range and standard deviation for MMFs are much smaller than those of FRB stablecoins. The mean for total net assets of prime MMF is $8.5 billion with a maximum of $161.2 billion and a standard deviation of $16.8 billion. This is  compared to an average market capitalization of $13.6 billion and a maximum of $83.2 billion and a standard deviation of $22.5 billion for FRB stablecoins. Hence, prime and taxexempt municipal MMFs and FRB stablecoins are similar in size. While the overall market size of the latter is only a fraction of the market for MMFs, it indicates that the size of individual stablecoins surpassed a critical value. The minimum price for all MMFs in Panel B is $0.9929, with a large gap between the minimum value and the second lowest value, $0.9980.

Table  6:  Price  range  for  MMFs  and  fiat  reserve  backed  stablecoins. The  table  reports  the  frequency distribution of peg deviations allocated to six categories. MMF data is based on DataStream, stablecoin data on coinapi.io. Note: Percentages are rounded to integers. Sample period: 1 January 2020 to 31 December 2022.

|          |                      | MMF    | MMF        | FRB SC   | FRB SC     |
|----------|----------------------|--------|------------|----------|------------|
| Interval | Price Range          | Obs.   | % of total | Obs.     | % of total |
| 1        | P &lt;= 0.9900          | 0      | 0%         | 130      | 2%         |
| 2        | 0.9900 &lt;= P &lt; 0.9975 | 1      | 0%         | 507      | 8%         |
| 3        | 0.9975 &lt;= P &lt; 1.0000 | 5,066  | 20%        | 2,349    | 37%        |
| 4        | 1.0000 &lt;= P &lt; 1.0025 | 19,989 | 80%        | 3,015    | 48%        |
| 5        | 1.0025 &lt;= P &lt; 1.0100 | 0      | 0%         | 249      | 4%         |
| 6        | P &gt;= 1.0100          | 0      | 0%         | 80       | 1%         |
|          | Total                | 25,056 | 100%       | 6,330    | 100%       |

Table 6 compares the frequency distribution for prices of MMFs and FRB stablecoins. The column for all MMFs shows only one observation outside the center intervals 3 and 4. In contrast, FRB stablecoins show a larger dispersion around the peg, with 10% of observations in intervals 1 and 2 and 5% in intervals 5 and 6.

Figure 6 shows the frequency distribution of prices within $0.0025 of par. The comparison of both  histograms  reveals  further  differences  between  the  instruments.  MMF  prices  tend  to deviate upward from the peg, resulting in a positively skewed distribution. FRB stablecoins, in contrast, are more dispersed within the observed price interval and do not show the positive skewness of MMF prices.

Figure 6: Frequency distribution histograms for intervals 3 and 4 of Table 6. Sample period: 1 January 2020 to 31 December 2022.

<!-- image -->

Figure 7 shows that the density plots for the individual FRB stablecoins differ substantially. Two of the Top3 FRB stablecoins by market capitalization, BUSD and USDC, are much more likely to have a secondary market price close to their peg value. The density plot for the largest FRB stablecoin  by  market  capitalization,  USDT,  reveals  similarities  to  MMFs  in  terms  of positive skewness and a mean price above the peg value.

Figure 7: Kernel density estimation (KDE) plot for fiat reserve backed stablecoins. Scott's Rule is used to calculate the estimator bandwidth. Source: coinapi.io. Sample period: 1 January 2020 to 31 December 2022.

<!-- image -->

Finally, Table 7 demonstrates that the mean prices of FRB stablecoins differ substantially from the those of MMFs.

Table 7: Difference in means for MMFs, fiat reserve backed (FRB) stablecoins and the three largest fiat reserve backed stablecoins (Top3 FRB). The price variable compares the average daily price over all share classes of a MMF with the daily closing pricing of stablecoins. The significance of the difference in means is computed with t-tests. Prior to the t-test we perform a variance-comparison test for each of the pairs. Due to the results of the variance-comparison test we drop the assumption of equal variances for the t-tests. *** indicates statistical significance at the 1%-level.

|       | MMF    | TOP3 FRB SC   | Difference   | Difference   |
|-------|--------|---------------|--------------|--------------|
|       | (1)    | (3)           | (1 - 2)      | (1 - 3)      |
| Price | 1.0003 | 1.0001        | 0.0005***    | 0.0001***    |

## 4.2 Peg Deviations

Figure 8 shows the mean monthly peg deviations for MMFs (Panel A), FRB stablecoins (Panel B) and the subsample of the Top3 FRB stablecoins (Panel C). We use daily closing prices for both MMFs and FRB stablecoins. The monthly time series of peg deviations includes two bars per month: upward deviations and downward deviations, split into those larger or smaller than $.005 deviations, equalling half a percent. This split indicates the threshold for when MMFs are 'breaking-the-buck', meaning investors cannot redeem the shares for one unit of currency, and there is no market mechanism to push the price back (Birdthistle, 2010).

Panels A and B show that the peg deviation patterns differ greatly. FRB stablecoins consistently exhibit downward peg deviations throughout the entire sample period. On average, each FRB stablecoin closes below the peg value on more than ten days each month. In contrast, MMFs usually close at a premium for most trading days each month. For the first half of the sample period, each MMF trades below its peg value on fewer than three days per month on average.

Figure 8: Mean monthly peg deviations for MMFs (Panel A), fiat reserve backed stablecoins (Panel B) and the three largest fiat reserve backed stablecoins - USDT, USDC and BUSD - (Panel C). MMF: Based on average price of all share classes per series identifier. Source: DataStream. Stablecoins: Based on average volume-weighted close price over all exchanges covered. Source: coinapi.io. Sample period: 1 January 2020 to 31 December 2022.

<!-- image -->

Beyond this rather general observation, there are two additional observations. First, the large dispersion  for  small  FRB  stablecoins  is  mirrored  in  the  average  number  of  downward  peg deviations larger than 0.5%. Comparing Panel B and Panel C shows that the latter more often close at  a  premium than their smaller counterparts. Furthermore, large FRB stablecoins on average  do  not  break-the-buck.  Second,  in  March  2020,  when  COVID-19  was  declared  a pandemic, only the MMF sample shows a temporary increase in downward peg deviations, while stablecoins do not. MMF peg deviations also show a similar reaction in response to the Russian invasion of Ukraine in February 2022. Once again, FRB stablecoins do not show such a clear reaction to the geopolitical events. In contrast, the collapse of TerraUSD in May 2022 and FTX in November 2022 are only reflected in the peg deviations of FRB stablecoins. MMF peg  deviations  remain  unaffected  by  the  exogenous  shock  within  the  crypto  market.  The differing  peg  deviation  patterns  around  the  events  suggest  that  these  financial  instruments respond differently to exogenous shocks.

To test this interpretation more formally, we use a linear regression to identify drivers of peg deviations and a logistic regression to identify drivers of upward and downward peg deviations separately. 31 We account for the magnitude of the deviations by running staggered models for the logistic regression with deviations ranging from peg deviations greater than 0.1% to greater than 0.5%. Table 8 shows all variables and their sources.

Table 8: Overview of dependent and independent variables of the regression analysis.

| Category                        | Variable                | Description                                                                                                                    | Source                                                                                                                                                                                                                |
|---------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dependent   variable            | peg\_dev                 | Peg deviation (scaled by factor 10,000)                                                                                        | As stated in section 3                                                                                                                                                                                                |
| Control variable                | log\_size                | Log total net assets for MMFs. Log  market capitalization for stablecoins.                                                     | As stated in section 3                                                                                                                                                                                                |
| Independent                     |                         |                                                                                                                                |                                                                                                                                                                                                                       |
| Variables                       |                         |                                                                                                                                |                                                                                                                                                                                                                       |
| Crypto market                   | crypto\_s                | Dummy variable indicating days in the  sample period when e.g.,  cryptocurrency exchanges got hacked,  stablecoins failed etc. | Several sources. See table in  Appendix C                                                                                                                                                                             |
|                                 | btc\_ret  btc\_lvol       | Bitcoin daily percentage return  Bitcoin daily log volume                                                                      | coinmarketcap.com  coinmarketcap.com                                                                                                                                                                                  |
|                                 | eth\_ret                 |                                                                                                                                |                                                                                                                                                                                                                       |
|                                 | eth\_lvol                | Ethereum daily percentage return  Ethereum daily log volume                                                                    | coinmarketcap.com  coinmarketcap.com                                                                                                                                                                                  |
| Global risk     and uncertainty | log\_gpr                 | Log Geopolitical Risk Index 32                                                                                                 | https://www.matteoiacoviello.com/ gpr.htm on March 07, 2023                                                                                                                                                           |
| Macroeconomic                   | log\_epu  t5yifr  t10yie | Log Economic Policy Uncertainty  Index  US 5-year forward inflation  expectation rate   US 10-year breakeven inflation rate    | https://www.policyuncertainty.com /us\_monthly.html  Federal Reserve Bank of St. Louis,  [T5YIFR], retrieved from FRED,  Federal Reserve Bank of St. Louis;  accessed 24 May 2023.  Federal Reserve Bank of St. Louis, |
|                                 | us2yt  us10yt           | US 10-year treasury bill interest rate                                                                                         | Federal Reserve Bank of St. Louis;  accessed 24 May 2023.  DataStream  DataStream                                                                                                                                     |
|                                 |                         | US 2-year treasury bill interest rate                                                                                          |                                                                                                                                                                                                                       |
|                                 | msci\_ret                | MSCI World daily percentage change                                                                                             | DataStream                                                                                                                                                                                                            |
|                                 | s&amp;p\_ret                 | S&amp;P500 daily percentage change                                                                                                 |                                                                                                                                                                                                                       |
|                                 |                         |                                                                                                                                | DataStream                                                                                                                                                                                                            |

In line with our interpretation of peg deviations, we divide the independent variables in three categories: crypto market, global risk and uncertainty, and macroeconomic. Table 9 shows the results for pairwise correlations. Due to high pairwise correlations, we drop the independent variables  for  daily  S&amp;P500  returns,  inflation  expectations  based  on  the  10-year  breakeven inflation rate,  and  the  interest  rate  for  10-year  US  Treasury  bills.  Furthermore, we  exclude Ethereum returns and volume due to pairwise correlations beyond 0.8 with Bitcoin returns and volume. Hence, we use a total of nine independent variables including size as a control variable. We show the estimation results of the regressions in Table 10.

The inclusion of all variables in the analysis for MMFs reveals that both geopolitical risk and economic policy uncertainty are highly significant drivers of MMF share prices. Particularly positive changes of geopolitical risk negatively affect MMF share prices.

Our results also validate the significant impact of scandals in crypto markets on prices of FRB stablecoins. In addition, Bitcoin trading volume is highly significant.

The results further identify size as a statistically significant driver of FRB stablecoin prices and MMF share prices. Inflation expectations serve as a statistically strong and equally influential factor in determining the prices of both instruments, resulting in price declines as inflation expectations increase. Short-term interest rates also display a negative relation with the prices of the Top3 FRB stablecoins and MMFs.

Monetary theory suggests that an increase in inflation leads to monetary tightening with higher interest rates, causing a decline in the market price of fixed-income instruments held in MMF portfolios. Consequently, the price of MMF shares decreases due to the daily mark-to-market pricing. This explains the negative effect of increasing inflation expectations and interest rates on MMFs prices.

In  contrast,  FRB  stablecoin  prices  are  determined  by  supply  and  demand  in  the  secondary market, not by mark-to-market pricing. Their association to riskier cryptocurrencies and the rising opportunity cost of holding a non-yielding financial asset in a regime of rising inflation expectations  and  rising  interest  rates  imply  decreasing  investor  demand.  This  explains  the decreasing price.

When  focusing  on  fund  flows  instead  of  prices,  research  indicates  that  monetary  policy tightening leads to deposit outflows (Drechsler et al., 2017) and MMF inflows (Xiao, 2020) due to the relatively slower adjustment of deposit interest rates compared to the yield of fixedincome  instruments  underlying  MMF  shares.  This  suggests  rebalancing  from  deposits  to MMFs.

Evaluating  the  flow  of  funds  for  FRB  stablecoins  during  monetary  tightening  is  less straightforward. While there may be a rebalancing from volatile cryptocurrencies to stablecoins or  to  fiat  currencies,  academic  research  does  not  provide  evidence  on  such  rebalancing. Moreover, because trading volume is non-directional, we cannot identify the direction of flows and are thus unable to close this gap in the literature.

Interestingly,  peg  deviations  of  FRB  stablecoins  are  sensitive  to  inflation  expectations regardless of their size, while interest rates exert a greater influence on peg deviations of the Top3 FRB stablecoins compared to their smaller counterparts. Notably, the models including all variables for the Top3 FRB stablecoins and MMFs show identical goodness-of-fit.

Table 9: Pairwise correlation of independent variables. This table presents pairwise correlation coefficients for all independent variables of the regression analysis. Bold numbers represent statistical significance at the 5%-level.

|          | t5yifr   | t10yie   | us2yt   | us10yt   | msci\_ret   | s&amp;p\_ret   | log\_gpr   | log\_epu   | crypto\_s   | btc\_ret   | eth\_ret   | btc\_lvol   | eth\_lvol   |
|----------|----------|----------|---------|----------|------------|-----------|-----------|-----------|------------|-----------|-----------|------------|------------|
| t5yifr   |          |          |         |          |            |           |           |           |            |           |           |            |            |
| t10yie   | 0.96     |          |         |          |            |           |           |           |            |           |           |            |            |
| us2yt    | 0.48     | 0.43     |         |          |            |           |           |           |            |           |           |            |            |
| us10yt   | 0.68     | 0.63     | 0.95    |          |            |           |           |           |            |           |           |            |            |
| msci\_ret | 0.02     | -0.01    | -0.04   | -0.04    |            |           |           |           |            |           |           |            |            |
| s&amp;p\_ret  | 0.01     | -0.01    | -0.04   | -0.03    | 0.97       |           |           |           |            |           |           |            |            |
| log\_gpr  | 0.40     | 0.47     | 0.49    | 0.51     | 0.01       | 0.02      |           |           |            |           |           |            |            |
| log\_epu  | -0.63    | -0.64    | - 0.33  | -0.47    | 0.10       | 0.10      | -0.25     |           |            |           |           |            |            |
| crypto\_s | 0.05     | 0.02     | 0.06    | 0.07     | -0.01      | 0.01      | -0.02     | 0.00      |            |           |           |            |            |
| btc\_ret  | -0.10    | -0.11    | -0.07   | -0.09    | 0.43       | 0.41      | -0.06     | 0.09      | -0.08      |           |           |            |            |
| eth\_ret  | -0.07    | -0.07    | -0.05   | -0.06    | 0.42       | 0.41      | -0.04     | 0.05      | -0.07      | 0.85      |           |            |            |
| btc\_lvol | 0.11     | 0.07     | -0.19   | -0.05    | 0.00       | 0.00      | -0.11     | -0.03     | 0.04       | 0.01      | -0.02     |            |            |
| eth\_lvol | 0.31     | 0.31     | -0.26   | -0.07    | -0.03      | -0.02     | -0.05     | -0.19     | 0.01       | -0.06     | -0.02     | 0.81       |            |

Table 10: Effect of macroeconomic, global risk and uncertainty and crypto market related variables on prices of fiat reserve backed stablecoins, the Top3 fiat reserve backed stablecoins and MMF shares. This  table  shows  multiple  linear  regression  estimates  for  which  the  dependent  variable  is  the  daily  peg  deviation (calculated as closing price t1 - closing price t0). Column (1) shows results for macroeconomic variables only. Column (2) and (3) for global risk and uncertainty variables only, respectively crypto-market related variables only. Column (4) uses all independent variables. We control for size (measured by total net assets for MMFs and market capitalization for fiat reserve backed stablecoins) in all columns. t-Statistics are reported in parentheses. *p &lt; 0.05, **p &lt; 0.01, ***p &lt; 0.001.

|                                     | Fiat Reserve Backed Stablecoins   | Fiat Reserve Backed Stablecoins                  | Fiat Reserve Backed Stablecoins     | Fiat Reserve Backed Stablecoins                                             | Top3 FRB Stablecoins   | Top3 FRB Stablecoins                      | Top3 FRB Stablecoins            | Top3 FRB Stablecoins                                     | MMFs                         | MMFs                         | MMFs                       | MMFs                                        |
|-------------------------------------|-----------------------------------|--------------------------------------------------|-------------------------------------|-----------------------------------------------------------------------------|------------------------|-------------------------------------------|---------------------------------|----------------------------------------------------------|------------------------------|------------------------------|----------------------------|---------------------------------------------|
|                                     | (1)                               | (2)                                              | (3)                                 | (4)                                                                         | (1)                    | (2)                                       | (3)                             | (4)                                                      | (1)                          | (2)                          | (3)                        | (4)                                         |
| t5yifr                              | -21.578 ***                       |                                                  |                                     | -24.764 ***                                                                 | -8.887***              |                                           |                                 | -9.657***                                                | -1.051 ***                   |                              |                            | -1.045 ***                                  |
|                                     | (-4.97)                           |                                                  |                                     | (-4.57)                                                                     | (-12.83)               |                                           |                                 | (-11.75)                                                 | (-10.88)                     |                              |                            | (-8.50)                                     |
| us2yt                               | -3.563 ***                        |                                                  |                                     | -2.034 *                                                                    | -0.641***              |                                           |                                 | -0.655***                                                | -0.758 ***                   |                              |                            | -0.667 ***                                  |
| msci\_ret                            | (-4.14)                           |                                                  |                                     | (-2.13)                                                                     | (-5.70)                |                                           |                                 | (-5.26)                                                  | (-36.06)                     |                              |                            | (-28.68)                                    |
|                                     | 0.409                             |                                                  |                                     | 0.870                                                                       | -0.160                 |                                           |                                 | -0.168                                                   | -0.016                       |                              |                            | 0.044 *                                     |
|                                     | (0.52)                            |                                                  |                                     | (0.99)                                                                      | (-1.58)                |                                           |                                 | (-1.49)                                                  | (-0.85)                      |                              |                            | (2.10)                                      |
| log\_gpr  log\_epu  crypto\_s  btc\_ret | 1.487 **   (2.94)                 | -10.388 ***   (-4.89)  7.956 ***   (3.88)  0.756 | 11.797  (1.82)  0.047  -0.218       | -3.739  (-1.56)  0.490  (0.20)  13.755 *   (2.12)  -0.253  (4.27)  1.655 ** | 1.006***               | -0.664*  (-2.25)  1.994***  (6.94)  0.102 | (1.74)  -0.202**                | 0.785*  (2.54)  -0.158  (-0.49)  0.011  (2.74)  1.007*** | 0.267 ***                    | -1.799 ***   0.255 ***       | 0.001  (1.31)  0.238 ***   | -0.915 ***   (-15.84)  -0.386 ***   (-6.42) |
| Constant                            | 14.895  (1.37)                    | (1.57)  -9.670  (-0.51)                          | (-0.48)  -289.654 ***               | (3.28)  -265.763 ***                                                        | (9.60)  -2.850         | (1.18)                                    | (-2.67)  -9.551                 | (9.56)  -28.635**                                        | (22.40)  3.682 ***   (18.05) | (21.01)  7.458 ***   (18.81) | (19.07)  -1.314  (-0.78)   | (22.43)  20.248 ***   (11.82)               |
| btc\_lvol  N                         | 4,329                             | 4,329                                            | (0.19)  12.021 ***   (-4.31)  4,329 | (-0.90)  12.187 ***   (-3.71)                                               | (-1.61)                | -7.861**  (-2.62)                         | (0.45)  0.647  (-1.04)          | (0.29)  1.011**  (-3.07)                                 |                              | (-34.84)  0.322 ***   (6.61) | (0.18)  0.090              | (-4.11)  -0.431 ***   (-6.26)  0.266 ***    |
|                                     |                                   |                                                  |                                     |                                                                             |                        | 2,231                                     | 2,231                           | 2,231                                                    | 23,808                       |                              |                            | 23,808                                      |
| log\_size  Adj.  R 2                 | 0.016                             | 0.010                                            | (4.41)  0.005                       | 4,329  0.021                                                                | 2,231  0.110           | 0.027                                     | -2.843**  (-3.20)  0.016  0.008 | -2.005*  (-2.38)  0.116                                  | 0.103                        | 0.072                        | -0.441 **   (-2.67)  0.015 | -0.061  (-0.38)  -0.028 ***   0.116         |
|                                     |                                   |                                                  |                                     |                                                                             |                        |                                           |                                 |                                                          |                              | 23,808                       | 23,808                     |                                             |

Table 11: Effect of macroeconomic, global risk and uncertainty and crypto market related variables on downward peg deviations of fiat reserve backed stablecoins and MMFs. This table shows logistic regression estimates for which the binary dependent variable is 1 if the daily closing price is below the peg value. Column 1 for downward peg deviations independent of the deviation size. The following columns are for peg deviations &gt;0.1% (column 2), &gt;0.2% (column 3), &gt;0.3% (column 4) and &gt;0.5% (column 5). We control for size (measured by total net assets for MMFs and market capitalization for fiat reserve backed stablecoins) in all columns. t-Statistics are reported in parentheses. *p &lt; 0.05, **p &lt; 0.01, ***p &lt; 0.001. Note that in column (2) of the MMF sample, the dummy variable indicating crypto scandals (crypto\_s) predicts failure perfectly, hence it is omitted, and 672 observations are not used.

|             | Fiat Reserve Backed Stablecoins   | Fiat Reserve Backed Stablecoins   | Fiat Reserve Backed Stablecoins   | Fiat Reserve Backed Stablecoins   | Fiat Reserve Backed Stablecoins   | MMFs       | MMFs        |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|------------|-------------|
|             | (1)                               | (2)                               | (3)                               | (4)                               | (5)                               | (1)        | (2)         |
| t5yifr      | 1.133 ***                         | 3.178 ***                         | 5.118 ***                         | 6.009 ***                         | 5.483 ***                         | 0.875 ***  | -5.956 ***  |
| t5yifr      | (6.97)                            | (11.78)                           | (14.56)                           | (14.85)                           | (12.28)                           | (9.87)     | (-7.63)     |
| us2yt       | 0.262 ***                         | 0.129 **                          | -0.092                            | -0.180 **                         | -0.045                            | 0.322 ***  | 1.860 ***   |
| us2yt       | (9.05)                            | (3.11)                            | (-1.84)                           | (-3.23)                           | (-0.73)                           | (23.08)    | (7.20)      |
| msci\_ret    | -0.022                            | -0.050                            | -0.062                            | -0.097                            | -0.050                            | -0.015     | 0.038       |
| msci\_ret    | (-0.81)                           | (-1.11)                           | (-1.09)                           | (-1.55)                           | (-0.73)                           | (-1.05)    | (0.83)      |
| log\_gpr     | 0.089                             | 0.386 ***                         | 0.588 ***                         | 0.840 ***                         | 0.952 ***                         | 0.782 ***  | 0.749 *     |
| log\_gpr     | (1.26)                            | (3.49)                            | (4.59)                            | (6.00)                            | (6.02)                            | (20.19)    | (2.07)      |
| log\_epu     | 0.075                             | -0.016                            | -0.176                            | -0.037                            | 0.069                             | 0.501 ***  | 4.177 ***   |
| log\_epu     | (1.01)                            | (-0.14)                           | (-1.30)                           | (-0.25)                           | (0.41)                            | (11.84)    | (7.28)      |
| crypto\_s    | 0.419 *                           | 0.304                             | -0.182                            | 0.008                             | -0.151                            | 0.026      | 0.000       |
| crypto\_s    | (2.14)                            | (1.10)                            | (-0.50)                           | (0.02)                            | (-0.34)                           | (0.26)     | (.)         |
| btc\_ret     | 0.000                             | 0.014                             | 0.012                             | 0.006                             | -0.007                            | 0.008      | -0.053 *    |
| btc\_ret     | (0.01)                            | (1.00)                            | (0.72)                            | (0.32)                            | (-0.32)                           | (1.72)     | (-2.07)     |
| btc\_lvol    | -0.100                            | -0.571 ***                        | -1.104 ***                        | -1.452 ***                        | -1.165 ***                        | -0.057     | 0.816       |
| btc\_lvol    | (-1.17)                           | (-4.11)                           | (-6.39)                           | (-7.41)                           | (-5.36)                           | (-1.21)    | (1.49)      |
| log\_size    | -0.176 ***                        | -0.750 ***                        | -1.015 ***                        | -1.114 ***                        | -1.014 ***                        | -0.050 *** | 0.424 ***   |
| log\_size    | (-11.53)                          | (-23.28)                          | (-22.19)                          | (-20.85)                          | (-17.55)                          | (-6.28)    | (4.65)      |
| Constant    | 2.616                             | 18.964 ***                        | 32.756 ***                        | 39.171 ***                        | 29.597 ***                        | -8.115 *** | -48.385 *** |
| Constant    | (1.22)                            | (5.41)                            | (7.48)                            | (7.89)                            | (5.39)                            | (-6.84)    | (-3.53)     |
| N           | 4,329                             | 4,329                             | 4,329                             | 4,329                             | 4,329                             | 23,808     | 23,136      |
| Pseudo  R 2 | 0.061                             | 0.262                             | 0.350                             | 0.380                             | 0.338                             | 0.110      | 0.447       |

Table 12: Effect of macroeconomic, global risk and uncertainty and crypto market related variables on upward peg deviations of fiat reserve backed stablecoins and MMFs. This table shows logistic regression estimates for which the binary dependent variable is 1 if the daily closing price is above the peg value. Column 1 for upward peg deviations independent of the deviation size. The following columns are for peg deviations &gt;0.1% (column 2), &gt;0.2% (column 3), &gt;0.3% (column 4) and &gt;0.5% (column 5). We control for size (measured by total net assets for MMFs and market capitalization for fiat reserve backed stablecoins) in all columns. t-Statistics are reported in parentheses. *p &lt; 0.05, **p &lt; 0.01, ***p &lt; 0.001.

|          | Fiat Reserve Backed Stablecoins   | Fiat Reserve Backed Stablecoins   | Fiat Reserve Backed Stablecoins   | Fiat Reserve Backed Stablecoins   | Fiat Reserve Backed Stablecoins   | MMFs            | MMFs                |
|----------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------|---------------------|
|          | (1)                               | (2)                               | (3)                               | (4)                               | (5)                               | (1)             | (2)                 |
| t5yifr   | -0.710 ***                        | -1.059 ***                        | -0.674 *                          | -0.036                            | 0.561                             | -0.822 ***      | -0.972 ***          |
| t5yifr   | (-4.42)                           | (-4.38)                           | (-2.15)                           | (-0.10)                           | (1.23)                            | (-10.88)        | (-6.64)             |
| us2yt    | -0.298 ***                        | -0.517 ***                        | -0.548 ***                        | -0.640 ***                        | -0.604 ***                        | -0.310 ***      | 0.020               |
| us2yt    | (-10.13)                          | (-6.35)                           | (-4.70)                           | (-4.46)                           | (-3.37)                           | (-24.16)        | (0.61)              |
| msci\_ret | -0.007                            | 0.001                             | -0.000                            | 0.004                             | 0.032                             | 0.016           | 0.029               |
| msci\_ret | (-0.27)                           | (0.04)                            | (-0.00)                           | (0.08)                            | (0.45)                            | (1.29)          | (1.32)              |
| log\_gpr  | -0.097                            | 0.146                             | 0.255                             | 0.248                             | -0.199                            | -0.635 ***      | -0.215 **           |
| log\_gpr  | (-1.38)                           | (1.21)                            | (1.56)                            | (1.33)                            | (-0.88)                           | (-18.54)        | (-3.08)             |
| log\_epu  | 0.031                             | -0.025                            | -0.380 *                          | -0.247                            | -0.311                            | -0.359 ***      | 0.403 ***           |
| log\_epu  | (0.41)                            | (-0.21)                           | (-2.47)                           | (-1.39)                           | (-1.45)                           |                 |                     |
| crypto\_s | -0.412 *                          | 0.143                             | 0.076                             | 0.079                             | -0.010                            | (-9.89)  -0.057 | (5.33)              |
| crypto\_s | (-2.06)                           | (0.44)                            | (0.17)                            | (0.16)                            | (-0.02)                           | (-0.64)         | -0.193  (-0.89)     |
| btc\_ret  | 0.006                             | -0.003                            | -0.013                            | -0.024                            | -0.036                            | -0.008          | -0.016              |
| btc\_ret  | (0.68)                            | (-0.23)                           | (-0.86)                           | (-1.39)                           | (-1.78)                           | (-1.92)         |                     |
| btc\_lvol | 0.014                             | 0.504 ***                         | 0.804 ***                         | 0.864 ***                         | 1.072 ***                         | 0.032           | (-1.85)  -0.706 *** |
| btc\_lvol | (0.16)                            | (3.98)                            | (4.80)                            | (4.59)                            | (4.74)                            | (0.78)          | (-8.42)             |
| log\_size | 0.213 ***                         | -0.263 ***                        | -0.608 ***                        | -0.741 ***                        | -0.772 ***                        | 0.150 ***       | 0.121 ***           |
| log\_size | (13.84)                           | (-10.10)                          | (-15.34)                          | (-15.87)                          | (-13.65)                          | (22.86)         | (7.08)              |
| Constant | -2.810                            | -7.038 *                          | -7.647                            | -8.707                            | -12.593 *                         | 5.864 ***       | 13.937 ***          |
| Constant | (-1.32)                           | (-2.20)                           | (-1.81)                           | (-1.84)                           | (-2.23)                           | (5.69)          | (6.65)              |
| N        | 4,329                             | 4,329                             | 4,329                             | 4,329                             | 4,329                             | 23,808          | 23,808              |
| N        | 0.065                             | 0.139                             | 0.244                             | 0.291                             | 0.294                             | 0.106           | 0.055               |

The results for the logistic regression, split in downward peg deviations (Table 11) and upward peg  deviations  (Table  12)  and  different  magnitudes  of  peg  deviations,  yield  four  main findings. 33

First, size matters for FRB stablecoins and MMFs. The probability of downward peg deviations for FRB stablecoins decreases with increasing size. While size is statistically significant for all variations of the outcome variable, with coefficients increasing from columns (1) to (3) and remain  constant  thereafter.  This  indicates  the  higher  the  market  capitalization  of  a  FRB stablecoin, the less likely it is to experience large downward peg deviations. The same holds for upward peg deviations.

Second,  the  probability  of  downward  peg  deviations  for  MMFs  increases  (decreases) significantly with an increase (decrease) in geopolitical risk. Additionally, economic policy uncertainty is a highly significant driver of downward peg deviations for MMFs. The results for the impact of geopolitical risk and economic policy uncertainty on upward peg deviations of FRB stablecoins confirm the results of the linear regression. Interestingly, the probability of downward peg deviations increases with rising geopolitical risk. The relationship is highly significant, with coefficients increasing from columns (1) to (5). Column (5) can be interpreted as showing the drivers that make FRB stablecoins 'break-the-buck'.

Third, an increase in inflation expectations significantly decreases the probability of downward peg deviations larger than 0.1% for MMFs. The result aligns with the common perception of MMFs as conservative short-term investments that are typically in high demand during periods of economic uncertainty. In the case of FRB stablecoins, higher inflation expectations correlate with  an  increased  probability  of  downward  peg  deviations,  irrespective  of  the  deviation's magnitude. Notably, this effect is most pronounced for deviations surpassing 0.2%. Increasing inflation expectations result in downward pressure on stablecoin prices due to a decrease in investor demand. In a low-interest rate environment, the gap between the dividends earned from MMF shares and the absence of compensation for FRB stablecoins is narrower compared to a higher-interest rate environment, which typically coincides with an increase in inflation

expectations.  This  contrasting  effect  on  both  instruments  highlights  that  investors  perceive FRB stablecoins as less attractive when inflation expectations increase.

Lastly, comparing columns (1) to (5) of Table 11 shows that improvement of the logistic model over the null model increases with increasing magnitudes of downward peg deviations for both samples.  The  logistic  model  seems  less  suited  to  explain  upward  than  downward  peg deviations.

## 4.3 Volatility and Correlation

We examine the time series of peg deviations to identify any trends or clusters of volatility throughout the sample period. Figure 9 presents the rolling 30-day volatility in percent in Panel A and the correlation of log peg deviations in Panel B. 34

Panel  A  shows  that  the  volatility  of  MMFs  and  FRB  stablecoins  differs  significantly.  The rolling 30-day volatility for MMFs is close to zero, with only a temporary marginal increase around the outbreak of the COVID-19 pandemic in early 2020, underlining the stability of the MMFs. In contrast, FRB stablecoins show significantly higher volatility. The volatility of the Top3 FRB stablecoins continuously decreased over the first half of the sample period and remains largely stable thereafter,  except  for  a  peak  in  November  2022.  We  argue  that  this increase in stability is due to the larger number of exchanges participating in the secondary market for the trading pair stablecoin/USD of the Top3 FRB stablecoins (see Figure 4).

Panel B shows that log peg deviations for FRB stablecoins exhibit no significant positive or negative correlation with MMF log peg deviations during the observed period. This finding is supported by the non-significant unconditional Pearson correlation coefficient. There is a small but statistically significant negative correlation between the log peg deviations of the Top3 FRB stablecoins and MMFs. However, the effect size of -0.1 does not support the idea that daily log peg deviations of the Top3 FRB stablecoins and MMFs move in opposite directions.

We  interpret  the  uncorrelated  peg  deviations  of  both  instruments  as  stemming  from  the significantly different price discovery mechanisms they utilize. MMF share prices are subject

to  daily  updates  by  the  issuer,  whereas  FRB  stablecoin  prices  remain  fixed  to  one  unit  of account in the primary market and experience fluctuations in the secondary market in response to supply and demand dynamics.

## Panel A Rolling 30-Day Volatility

Figure 9: Rolling 30-day volatility (Panel A) and rolling 30-day correlation of daily log peg deviations (Panel B). Source: coinapi.io and DataStream. Sample period: 1 January 2020 to 31 December 2022.

<!-- image -->

## 5 Summary and Concluding Remarks

Our paper is the first to conduct a holistic comparison of stablecoins and money market mutual funds  (MMFs),  including  the  institutional  background  of  both  financial  instruments.  The analysis reveals that only fiat reserve backed (FRB) stablecoins are truly comparable to MMFs. This  is  because  stablecoins  outside  this  category  are  either  unbacked  or  backed  by  crypto collateral, fundamentally altering the risk profile of these instruments.

The commonalities between FRB stablecoins and MMFs extend beyond their reserve assets. Both instruments are pegged to one unit of account and serve as short-term facilities to park funds.  The  market  infrastructure  is  similar,  with  indirect  support  through  an  exchange associated with the stablecoin issuer acting as a stability mechanism for FRB stablecoins. This indirect support resembles the sponsor support for MMFs and can distort the secondary market price  of  stablecoins  if  the  price  on  the  affiliated  exchange  is  higher  than  the  prevailing secondary market price on all other exchanges.

The microstructure of the primary market in which both financial instruments are traded is largely  identical,  encompassing  account  verifications,  redemption  rights,  and  redemption suspensions.

Regression models using macroeconomic variables explain peg deviations of both instruments better  than  models  relying  on  global  risk  and  uncertainty  or  crypto  indicators.  Inflation expectations  equally  impact  the  prices  of  both  instruments  regardless  of  their  size.  The noticeably larger effect size for FRB stablecoin reflects their generally heightened volatility and  substantially  larger  peg  deviations.  The  effect  size  for  the  Top3  FRB  stablecoins approaches that of MMFs, consistent with their decreasing volatility.

Despite these commonalities, our comparison also highlights several differences. First, FRB stablecoins fall short of the separation of funds and managers, which hinders the possibility of direct sponsor support. Unlike MMFs, where the investment advisor and the fund itself are distinct entities, allowing for sponsor support through outside assets or reserve asset purchases at  a  premium,  FRB  stablecoins  do  not  have  this  advantage.  The  absence  of  separation  is particularly  critical  if  an  issuer  or  its  parent  company  faces  bankruptcy,  as  claims  from stablecoin holders are unlikely to be successful, leading to substantial losses or even the total loss of their investment.

Second, investors in MMFs expect compensation for the bank-like run risk they face through dividends. In contrast, stablecoins do not pay dividends and investors must actively manage and stake their holdings to achieve a return.

Third, FRB stablecoins exhibit less stability due to their price discovery mechanism relying on the  secondary  market,  as  opposed  to  MMFs'  daily  mark-to-market  pricing  in  the  primary market.  Secondary  market  trading  is  distinctive  to  stablecoins.  Our  observation  that  larger secondary markets for FRB stablecoins, characterized by increased participation of exchanges, correspond to heightened stability underscores their favorable impact on stability.

It  is  noteworthy that the three largest FRB stablecoins exhibit greater similarities to MMFs compared to their smaller counterparts. The volatility of their peg deviations is much closer to those of MMFs, although still higher. Moreover, their peg deviations show a highly significant correlation with macroeconomic factors across all regression models. Short-term interest rates impact both MMFs and the three largest FRB stablecoins with nearly identical effect size.

FRB stablecoins possess many characteristics resembling MMFs. The decreasing disparities observed for the three largest FRB stablecoins suggest that they become more like MMFs with increasing market capitalization. The potential separation of stablecoin issuers and stablecoins through regulation could help protect investors from losses in the event of bankruptcies. The occurrence  of  mutual  fund  bankruptcies  following  the  GFC  validated  the  effectiveness  of separating  funds  and  managers  as  a  successful  mechanism  for  investor  protection.  The introduction  of  analogous  regulations  for  FRB  stablecoins  would  further  increase  the similarities between both instruments.

While significant differences continue to persist, FRB stablecoins have the potential to become the MMFs of the future if crypto markets continue to grow as an asset class 35 .

## References

- Anadu, K., Azar, P. D., Cipriani, M., Eisenbach, T. M., Huang, C., Landoni, M., La Spada, G., Macchiavelli, M., Malfroy-Camine, A., &amp;amp; Wang, C. J. (2023). Runs and Flights to Safety: Are Stablecoins the New Money Market Funds? Federal Reserve Bank of New York Staff Reports, no. 1073, September . https://doi.org/10.59576/sr.1073
- Anadu, K., Cipriani, M., Craver, R. M., &amp;amp; La Spada, G. (2022). The Money Market Mutual Fund Liquidity Facility. Economic Policy Review, Federal Reserve Bank of New York  28 , (1). https://doi.org/10.2139/ssrn.3951479
- Ante, L., Fiedler, I., &amp;amp; Strehle, E. (2021). The Influence of Stablecoin Issuances on Cryptocurrency Markets. Finance Research Letters  41 , (101867).

Awrey, D. (2020). Bad Money. Cornell Law Review 106 (1).

- Barthelemy, J., Gardin, P., &amp;amp; Nguyen, B. (2021). Stablecoins and the real economy [Working Paper]. Available at SSRN . https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3973538
- Baur, D. G., &amp;amp; Hoang, L. T. (2021). A crypto safe haven against Bitcoin. Finance Research Letters , 38 (101431).
- Birdthistle, W. A. (2010). Breaking Bucks in Money Market Funds. WISCONSIN LAW REVIEW  2010 , (5). Available at: https://scholarship.kentlaw.iit.edu/fac\_schol/77
- Bouveret, A., Martin, A., &amp;amp; Mc Cabe, P. E. (2022). Money Market Fund Vulnerabilities: A Global Perspective. Finance and Economics Discussion Series 2022-012  Washington: Board of Governors of the Federal , Reserve System . https://doi.org/10.17016/FEDS.2022.012
- Brady, S., Anadu, K., &amp;amp; Cooper, N. (2012). The Stability of Prime Money Market Mutual Funds: Sponsor Support from 2007 to 2011. Supervisory Research and Analysis Working Papers RPA 12-3, Federal Reserve Bank of Boston.
- Bruce, K., Odinet, C. K., &amp;amp; Tosato, A. (2022). The Private Law of Stablecoins. Arizona State Law Journal , 54 (4), 1073-1160.
- Bullmann, D., Klemm, J., &amp;amp; Pinna, A. (2019). In Search for Stability in Crypto-Assets: Are Stablecoins the Solution? Occasional Paper Series 230, European Central Bank . https://doi.org/10.2139/ssrn.3444847
- Caldara, D., &amp;amp; Iacoviello, M. (2022). Measuring Geopolitical Risk. American Economic Review  112 , (4), 11941225. https://doi.org/10.1257/aer.20191823
- Catalini, C., &amp;amp; de Gortari, A. (2021). On the Economic Design of Stablecoins [Working Paper]. Available at SSRN . https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=3899499
- Catalini, C., de Gortari, A., &amp;amp; Shah, N. (2022). Some Simple Economics of Stablecoins. Annual Review of Financial Economics  14 , (1), 117-135. https://doi.org/10.1146/annurev-financial-111621-101151
- Drechsler, I., Savov, A., &amp;amp; Schnabl, P. (2017). The Deposits Channel of Monetary Policy. The Quarterly Journal of Economics  132 , (4), 1819-1876.

Fisch, J. E. (2015). The Broken Buck Stops Here: Embracing Sponsor Support in Money Market Fund Reform. North Carolina Law Review  Vol. 93, No. 935 , .

| Gadzinski, G., Castello, A., &amp; Mazzorana, F. (2023). Stablecoins: Does design affect stability?  Finance  Research Letters  53 , , 103611.                                                                                  |                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| NBER Working Paper  No. w30796 , .                                                                                                                                                                                          | Gorton, G. B., Klee, E. C., Ross, C. P., Ross, S. Y., &amp; Vardoulakis, A. (2022). Leverage and Stablecoin Pegs.                                        |
| Gorton, G. B., Ross, C. P., &amp; Ross, S. Y. (2022). Making Money.  https://doi.org/10.3386/w29710                                                                                                                             | NBER Working Paper Series  No. 29710 , .  Gorton, G. B., &amp; Zhang, J. (2021). Taming Wildcat Stablecoins.  University of Chicago Law Review  90.3 , . |
|                                                                                                                                                                                                                             | Griffin, J. M., &amp; Shams, A. (2020). Is Bitcoin Really Untethered?  The Journal of Finance  75 , (4), 1913-1964.                                      |
| Grobys, K., Junttila, J., Kolari, J. W., &amp; Sapkota, N. (2021). On the stability of stablecoins.  Finance  64 , , 207-223.                                                                                                   | Journal of Empirical  DeFi and the Future of Finance . John Wiley &amp; Sons,                                                                            |
| Harvey, C. R., Ramachandran, A., &amp; Santoro, J. (2021).  Inc.                                                                                                                                                                | Hoang, L. T., &amp; Baur, D. G. (2021). How stable are stablecoins?  The European Journal of Finance , 1-17.                                             |
| Kim, S. R. (2022). How the Cryptocurrency Market is Connected to the Financial Market [Working Paper].  Available at SSRN . https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=4106815                                     |                                                                                                                                                      |
| Economy  97 , (4), 927-954.                                                                                                                                                                                                 | Kiyotaki, N., &amp; Wright, R. C. F. p. d. A. (1989). On Money as a Medium of Exchange.  Journal of Political                                            |
| Kwon, Y., Kim, J., Kim, Y., &amp; Song, D. (2021). The Trilemma of Stablecoin [Working Paper].                                                                                                                                  | Available at                                                                                                                                         |
| Literature  55 , (2), 371-440. https://doi.org/10.1257/jel.20141195   Li, L., Li, Y., Macchiavelli, M., &amp; Zhou, X. (2021). Liquidity Restrictions, Runs, and Central Bank  Interventions: Evidence from Money Market Funds. | The Review of Financial Studies  34 , (11), 5402-5437.                                                                                               |
| Li, Y., &amp; Mayer, S. (2020, revised 2022). Money Creation in Decentralized Finance: A Dynamic Model of  Stablecoin and Crypto Shadow Banking.  Available at SSRN . https://ssrn.com/abstract=3757083                         | Fisher College of Business Working Paper No. 2020-03-030.                                                                                            |
| Liao, G. Y., &amp; Caramichael, J. (2022). Stablecoins: Growth Potential and Impact on Banking. (International  Finance Discussion Paper No. 1334). https://doi.org/10.17016/IFDP.2022.1334                                     |                                                                                                                                                      |
| Lyons, R. K., &amp; Viswanath-Natraj, G. (2023). What keeps stablecoins stable?  and Finance  131 , . https://doi.org/10.1016/j.jimonfin.2022.102777.                                                                           | Journal of International Money  Working Paper.                                                                                                       |
| Ma, Y., Zeng, Y., &amp; Zhang, A. L. (2023). Stablecoin Runs and the Centralization of Arbitrage.  Available at SSRN                                                                                                            | . https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=4398546                                                                                        |
| Martino, E. D. (2022). Regulating Stablecoins as Private Money. A Critical Take on the EU Proposal between  Liquidity and Safety.                                                                                           | Amsterdam Law School Research Paper No. 2022-27, Amsterdam Center for Law &amp;                                                                          |

Morley, J. (2014). The Separation of Funds and Managers: A Theory of Investment Fund Structure and Regulation. The Yale Law Journal  123 , (5), 1228-1287.

- Oefele, N., Baur, D. G., &amp;amp; Smales, L. A. (2024). Flight-to-quality-Money market mutual funds and stablecoins during the March 2023 banking crisis. Economics Letters  234 , , 111464. https://doi.org/10.1016/j.econlet.2023.111464

Ondersma, C. (2013). Shadow Banking and Financial Distress: The Treatment of Money-Claims in Bankruptcy. Columbia Business Law Review  2013 , (1), 79-147.

Parlatore, C. (2016). Fragility in money market funds: Sponsor support and regulation. Journal of Financial Economics  121 , (3), 595-623.

Wilmarth, A. E. (2022). It's Time to Regulate Stablecoins as Deposits and Require Their Issuers to Be FDICInsured Banks. 41 Banking &amp; Financial Services Policy Report No. 2 (Feb. 2022). Available at SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=4000795

Xiao, K. (2020). Monetary Transmission through Shadow Banks. The Review of Financial Studies  33 , (6), 23792420. https://doi.org/10.1093/rfs/hhz112

## Appendix A

Sources for Table 1.

| Name   | Source                                                                                                                                                                                                                                                                                                                                                                                               |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| USDT   | Tether Transparency, accessed 3 February 2023,  https://tether.to/en/transparency/#reports.   Press Release, Tether Banking Relationship Announced (1 November 2018),  https://tether.to/en/tether-banking-relationship-announced/.   Tether has held some reserves at Bahamas bank Capital Union, FINANCIAL TIMES  (30 May 2022), https://www.ft.com/content/e4cb9a6e-cb29-4719-b6ee- 33a5bf01945e. |
| USDC   | Centre Monthly Attestations, accessed 3 February 2023, https://www.centre.io/usdc- transparency.   Circle Blog USDC Providing Greater Transparency, accessed 1 March 2023,  https://www.circle.com/blog/providing-greater-transparency.                                                                                                                                                              |
| BUSD   | BUSD Transparency Reports, accessed 3 February 2023, https://paxos.com/busd- transparency/.                                                                                                                                                                                                                                                                                                          |
| TUSD   | TrueUSD Real Time Attestation, accessed 3 February 2023, https://real-time- attest.trustexplorer.io/truecurrencies.                                                                                                                                                                                                                                                                                  |
| USDP   | Pax Dollar (USDP) Transparency Reports, accessed 3 February 2023,  https://paxos.com/busd-transparency/.                                                                                                                                                                                                                                                                                             |
| GUSD   | Gemini Dollar, accessed 3 February 2023, https://www.gemini.com/dollar.                                                                                                                                                                                                                                                                                                                              |

## Appendix B

Effect of macroeconomic, global risk and uncertainty as well as crypto market related variables on absolute peg deviation of fiat reserve backed stablecoins and MMFs. This table shows logistic regression estimates for which the binary dependent variable is 1 whenever the closing price is unequal 1. We control for size (measured by total net assets for MMFs and market capitalization for fiat reserve backed stablecoins) in all columns. tStatistics are reported in parentheses. *p &lt; 0.05, **p &lt; 0.01, ***p &lt; 0.001.

|             | Fiat Reserve Backed Stablecoins   | MMFs       |
|-------------|-----------------------------------|------------|
| t5yifr      | 1.991 ***                         | -0.355 **  |
|             | (5.70)                            | (-3.23)    |
| us2yt\_ry    | -0.135                            | -0.097 *** |
|             | (-1.66)                           | (-5.16)    |
| msci\_ret    | -0.145 **                         | 0.003      |
|             | (-2.73)                           | (0.16)     |
| log\_gpr     | -0.005                            | -0.110 *   |
|             | (-0.03)                           | (-2.20)    |
| log\_epu     | 0.539 **                          | 0.095      |
|             | (3.27)                            | (1.83)     |
| crypto\_s    | 0.126                             | -0.107     |
|             | (0.24)                            | (-0.83)    |
| btc\_ret     | 0.032                             | -0.002     |
|             | (1.66)                            | (-0.34)    |
| btc\_lvol    | -0.410 *                          | -0.009     |
|             | (-2.00)                           | (-0.15)    |
| log\_size    | 0.259 ***                         | 0.196 ***  |
|             | (6.39)                            | (25.11)    |
| Constant    | 1.411                             | 1.956      |
|             | (0.27)                            | (1.31)     |
| N           | 4329                              | 23808      |
| Pseudo  R 2 | 0.089                             | 0.043      |

## Appendix C

List with dates of scandals in the cryptocurrency market. Events range from stablecoin failures and the hacking of cryptocurrency exchanges to bankruptcies within the industry. Sources as listed in the last column. Sample period: 1 January 2020 to 31 December 2022.

| Date              | Event                              | Source          |
|-------------------|------------------------------------|-----------------|
| 5 February 2020   | Altsbit Exchange Hack              | Hedgewithcrypto |
| 19 April 2020     | Lendf.me and Uniswap Exchange Hack | Hedgewithcrypto |
| 29 June 2020      | Balancer Exchange Hack             | Hedgewithcrypto |
| 11 July 2020      | Cashaa Exchange Hack               | Hedgewithcrypto |
| 25 September 2020 | KuCoin Exchange Hack               | Hedgewithcrypto |
| 1 December 2020   | BTC Markets Exchange Hack          | Hedgewithcrypto |
| 8 December 2020   | Basis Cash (BAC) Failure           | FastCompany     |
| 21 December 2020  | EXMO Exchange Hack                 | Hedgewithcrypto |
| 23 December 2020  | Livecoin Exchange Hack             | Hedgewithcrypto |
| 27 December 2020  | Empty Set Dollar (ESD) Failure     | Fast Company    |
| 6 April 2021      | FEI Crash                          | Worldcoinstats  |
| 29 April 2021     | Hotbit Exchange Hack               | Hedgewithcrypto |
| 16 June 2021      | IRON Failure                       | FastCompany     |
| 10 August 2021    | Poly Network Hack                  | Fintechmagazine |
| 19 August 2021    | Liquid Exchange Hack               | Hedgewithcrypto |
| 5 December 2021   | BitMart Exchange Hack              | Hedgewithcrypto |
| 11 December 2021  | AscendEX Exchange Hack             | Hedgewithcrypto |
| 17 January 2022   | Crypto.com Exchange Hack           | Hedgewithcrypto |
| 9 May 2022        | Terra                              | WSJ             |
| 12 June 2022      | Celsius                            | WSJ             |
| 17 June 2022      | Babel Finance                      | WSJ             |
| 27 June 2022      | Three Arrows                       | WSJ             |
| 29 June 2022      | Three Arrows                       | WSJ             |
| 5 July 2022       | Voyager                            | WSJ             |
| 2 November 2022   | FTX                                | WSJ             |
| 9 November 2022   | FTX                                | WSJ             |
| 10 November 2022  | FTX                                | WSJ             |
| 11 November 2022  | FTX                                | WSJ             |
| 12 November 2022  | FTX Unauthorized transaction       | Hedgewithcrypto |
| 13 November 2022  | Binance halts USDC withdrawals     | CNBC            |
| 28 November 2022  | Blockfi                            | WSJ             |

## Sources for Appendix C:

Crypto crisis a timeline of key events , WALL STREET JOURNAL (10 April 2023), https://www.wsj.com/articles/crypto-crisis-a-timeline-of-key-events-11675519887.

Crypto exchange Binance halts USDC withdrawals, CNBC (13 December 2022), https://www.cnbc.com/2022/12/13/crypto-exchange-binance-temporarily-halts-usdc-stablecoinwithdrawals.html

Cryptocurrency exchange hacks, accessed 15 March 2023, https://www.hedgewithcrypto.com/cryptocurrencyexchange-hacks/.

Panics and death spirals a history of failed stablecoins, accessed 15 March 2023, https://www.fastcompany.com/90751716/panics-and-death-spirals-a-history-of-failed-stablecoins.

Timeline poly network and curious case Mr Whitehat, accessed 15 March 2023, https://fintechmagazine.com/crypto/timeline-poly-network-and-curious-case-mr-whitehat.

What  happened  to  algorithmic  stablecoins,  accessed  15  March  2023,  https://worldcoinstats.com/news/whathappened-to-algorithmic- stablecoins/#:~:text=To%20summarize%2C%20Empty%20Set%20Dollar,worthless%20and%20has%20not%2 0recovered.