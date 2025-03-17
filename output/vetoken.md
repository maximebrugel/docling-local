## Emergent Outcomes of the veToken Model

Thomas Lloyd ∗ 1 , Daire O'Broin † 1 , and Martin Harrigan ‡ 1

1 Dept. of Computing, Carlow Campus, South East Technological University, Rep. of Ireland

## Abstract

Decentralised organisations use blockchains as a basis for governance: they use on-chain transactions to allocate voting weight, publish proposals, cast votes, and enact the results.

However, blockchain-based governance structures have challenges, mostly notably, the need to align the short-term outlook of pseudononymous voters with the long-term growth and success of the decentralised organisation. The Vote-Escrowed Token (veToken) model attempts to resolve this tension by requiring voters to escrow or lock tokens of value for an extended period in exchange for voting weight.

In this paper, we describe the veToken model and analyse its emergent outcomes. We show that voting behaviour follows bribes set by higherlevel protocols, and that the cost per vote varies depending on how it is acquired. We describe the implementation of the veToken model by Curve Finance, a popular automated market maker for stablecoins, and the ecosystem of protocols that has arisen on top of this implementation. We show that voting markets such as Votium largely determine the outcome of fortnightly votes held by Convex Finance, and we show that Frax Finance, a stablecoin issuer, plays a central role in the ecosystem even though they directly lock relatively few tokens with Curve. Instead, they indirectly lock tokens through yield aggregators such as Convex Finance and purchase voting weight through voting markets such as Votium.

Although the veToken model in isolation is straight-forward and easily explained, it leads to many complex and emergent outcomes. Decentralised organisations should consider these outcomes before adopting the model.

## 1 Introduction

At their core, blockchains are a decentralising technology: they push operations away from centralised entities and intermediaries and toward individual actors

and stakeholders. Decentralised organisations, or, the somewhat aspirationally named, decentralised autonomous organisations (DAOs), involve stakeholders that manage shared resources via a blockchain. Frequently, they need to make decisions that require the combined input of the stakeholders. For example, a decentralised finance platform such as Aave might want to decide on supporting an additional asset, 1 or an NFT collection such as Nouns DAO might want to decide on funding an animated short movie. 2 In the simplest model, stakeholders are allocated voting weight using governance tokens, where one token equals one vote. They cast their votes using on-chain transactions or off-chain signed messages. This process mirrors stockholder voting in corporate governance.

However, two significant characteristics of decentralised organisations and the simple voting model are that stakeholders are identified pseudonymously and voting weight (tokens) can be traded, and even borrowed for short terms. This creates a tension between the desire of stakeholders for short-term gains and self-serving actions and the long-term prospects of the organisation. A particularly egregious example of this tension occurred in April 2022 when a malicious actor borrowed a controlling stake of tokens in the Beanstalk DAO and voted for a proposal to send USD $ 182 million from the DAO's treasury to himself [12]. Although these actions resemble a corporate raid, their speed and flagrancy were due to the pseudonymity of the attacker and the borrowability of voting weight.

The Vote-Escrowed Token (veToken) model attempts to resolve this tension by requiring stakeholders to lock their tokens for a fixed time period in exchange for voting weight. Locked tokens cannot be transferred. Therefore, the voting preferences of the stakeholders should better align with the long-term prospects of the decentralised organisation. In this paper we explain the veToken model and analyse its emergent outcomes. We describe the implementation of the model by Curve Finance, a popular automated market maker, and the ecosystem of protocols that has arisen on top of their implementation. These include yield aggregators such as Convex Finance, voting markets such as Votium, and significant stakeholders that are themselves decentralised organisations such as Frax Finance. We show that the veToken model has created a complex ecosystem with emergent outcomes.

Specifically, this paper examines the dual nature of the veToken model. The model avoids shortcomings of earlier versions of decentralised token governance by ensuring a robust alignment between stakeholder and organisational goals. However, this has led to the emergence of additional protocols keen on leveraging its distinctive features. In the context of Decentralised Finance (DeFi), such developments are regarded as beneficial and described as 'money legos'. However, for governance, it creates a complex dynamic where influence may be disproportionately higher at the upper-tiers of the governance ecosystem while not being subject to the same rules of engagement. We show this by highlighting the impact of Votium's incentivisation mechanisms on the outcomes

of Convex's fortnightly proposals. Additionally, we highlight players like Frax who directly lock relatively few tokens with Curve but indirectly lock a significant number of tokens through Convex and purchase voting weight using bribes through Votium.

The paper is organised as follows. We survey related work in Sec. 2, specifically, blockchain-based decentralised governance and token-based voting. Section 3 introduces the veToken model and its implementation within the Curve ecosystem. We explain the relevance of gauges (Sect. 3.1), gauge proposals, and higher-level protocols such as Convex, Votium, and Frax (Sect. 3.2). In Sect. 4 we describe our data collection process. Section 5 is the core of the paper. We analyse the veToken model at the Curve, Convex, and Votium levels. We show that votes follow bribes (Sect. 5.1) and that votes can be acquired at different prices at the different levels (Sect. 5.2). Finally we conclude in Sect. 6.

## 2 Related Work

We categorise related work into two areas: blockchain-based decentralised governance and token-based voting.

Blockchains provide a fertile testing ground for decentralised governance. Schneider [15] discusses the use of economic incentives, enforced through cryptography and blockchains, to guide user behaviour, and to impose limitations on the possibilities for blockchain-based governance. Reijers et al. [14] consider the differences between on-chain and off-chain governance in blockchain-based systems: they equate on-chain governance to a mechanical, content-independent understanding of the law. DuPont [8] provides a historical account of the rise and fall of The DAO, a decentralised organisation that was deployed to the Ethereum blockchain in April 2016. It is considered a notable failure of blockchain-based governance. Bhambhwani [3] examines the governance structure of the most popular blockchain-based finance applications and categorises them based on their level of insider control.

In terms of token-based voting, Abramowicz [1] describes formal games that incentivise players to provide quantitative assessments on matters of opinion that match the assessments of future players, thereby elicting group answers to normative questions. Merrill et al. [13] propose a governance model called ping-pong governance where participants lock and, optionally spend, tokens in order to champion proposals and cast votes. If a proposal achieves enough votes within a fixed period, it enters a review period where participants can try to veto the proposal. If a proposal is vetoed, it enters another review period, where participants can try to veto the veto. This process is repeated until the proposal is settled. The model is superficially similar to the veToken model discussed in this paper.

Buterin [4] warns against the dangers of token-based voting, in particular, inequalities and the misalignment of incentives. Fritsch et al. [11] analyse the token holders, delegates and proposals of Compound, Uniswap and ENS over a 27-month period. They calculate the distribution of voting rights among

delegates using the Gini and Nakamoto coefficients [17], the participation of tokens and delegates in past proposals, and the potential and exercised voting power of delegates. In all cases, the calculations show the existence of a small number of powerful actors. They classify delegates based on the number of tokens and token holders that delegate to them. They show that their voting behaviour in all cases is similar. Finally, they perform some rudimentary address clustering that suggests even more centralisation [2]. Sun et al. [19] analyse voting behaviour within MakerDAO to identify voting coalitions, to examine their group cohesion and internal structure, and to evaluate their influence on the Maker protocol. They draw many parallels between voting in corporate finance and voting within decentralised organisations.

## 3 The veToken Model

The veToken model was proposed and implemented by Michael Egorov as part of Curve Finance, an automated market maker that specialises in stablecoin trading [7, 9]. The model was implemented using smart contracts that extend Aragon [6], a DAO governance framework. The critical difference between it and previous systems was that it replaced the one-token one-vote model with a voting weight proportional to lock time.

Users need to lock or escrow tokens for a fixed period in exchange for voting weight. The longer the period, the more voting weight is granted. For Curve Finance, the token is known as CRV and the corresponding locked tokens or voting weight is known as veCRV. During the lockup period, the locked tokens are non-transferrable, i.e., CRV is transferrable but veCRV is not.

Voting weight, w , for a user can be calculated using:

<!-- formula-not-decoded -->

where a is the number of tokens (e.g., CRV), t is the desired lockup period, and t max is the maximum lockup period [9]. In Curve Finance, the minimum lockup period is one week and the maximum is four years. Consequently, a user who locks up their tokens for one week would need to lockup 208 times the number of tokens compared to a user who locks for the maximum lockup period of four years to get the same voting weight. The intention is to align the, potentially short-term, interest of the voters with the long-term goals of the decentralised organisation by having users commit to a lockup period to become voters with their voting weight being proportional to the duration of the lockup.

There is another aspect to the veToken model that warrants discussion. In general, decentralised organisations suffer from poor voter turnout [11] and voting weight alone might not be incentive enough for users to lock tokens for extended periods. Therefore, the veToken model includes an additional economic incentive: the allocation of new tokens (CRV tokens in the case of Curve Finance) is directed via voting using a mechanism known as gauges .

## 3.1 Gauges

Curve Finance is a platform for stablecoin trading. It uses gauges to measure the amount of liquidity provided by users to the various liquidity pools. Each gauge is assigned a weight and those weights determine the daily emission of new CRV tokens. The weights are set every week at Thursday midnight UTC after a gauge proposal vote. Therefore, users with voting weight decide on the allocation of new CRV tokens to liquidity providers. In fact, the voters may be liquidity providers and they can choose to direct the new tokens to themselves. This incentivises the lockup of tokens for extended periods.

## 3.2 Higher-Level Protocols

Curve has spawned several higher-level protocols and strategies. For example, yield aggregators such as Convex Finance [5], Yearn Finance [21], and Stake DAO [18] provide smart contracts that hold and lock CRV on behalf of users. This allows users to lock tokens for the maximum lockup period, to trade tokenised claims on those locked tokens, and to amortise gas costs. Voting markets such as Votium [20] allows anyone to incentivise particular Curve gauges by rewarding votes with bribes. Frax Finance [10] is a stablecoin issuer that interacts with many of these protocols. For example, they use Curve to lock CRV for veCRV, they hold tokenised veCRV via Convex, and they incentivise Curve gauges using Votium.

## 4 Method

We collected on-chain and off-chain data from three primary sources within the Curve ecosystem. Firstly, we gathered transaction data from the Ethereum blockchain relating to Curve: transactions involving the CRV token contract, the veCRV token contract, and the Gauge Controller contract. Curve executes its governance entirely on-chain. Our data for Curve covers the period from the deployment of the CRV token on 12th August 2020 until 17th March 2023. Secondly, we gathered transaction data from the Ethereum blockchain relating to Convex: transactions involving the CVX token contract, the vlCVX token contract, and the cvxCRV token contract. CVX is Convex's governance token; vlCVX is a locked version of CVX - it works in a manner similar to CRV and veCRV except that the maximum lockup period is much shorter (16 weeks) and the voting weight per vlCVX is determined by the amount of veCRV the Convex protocol owns. Users that lock CVX to get vlCVX receive voting weight on Convex, and in turn, voting weight from the veCRV held by Convex. Our data for Convex covers the period from the deployment of the CVX token on 17th May 2021 until 17th March 2023. Additionally, we collected the details of all Convex proposals via Snapshot [16] using their GraphQL API. Thirdly, we gathered transaction data from the Ethereum blockchain relating to Votium: transactions involving the bribing contracts for the gauges. Our data for Votium covers the period from the deployment of the Voting bribing contracts on 12th

September 2021 until 17th March 2023. We mapped the bribes in the Votium contracts to their associated gauge in the Curve Gauge Controller contract.

## 5 Results

We begin with results relating to Curve's implementation of the veToken model. These can be considered first-order results, in that, they relate directly to CRV and veCRV. In the subsequent subsections (Sect. 5.1 and 5.2) we consider two significant second-order results that relate to higher-level protocols, i.e., Convex, Votium and Frax, that build upon the Curve ecosystem.

Firstly, we analysed participation in the weekly gauge proposals and the non-gauge proposals. The former are economically incentivised through bribes and CRV emissions whereas the latter are not. We found 9551 unique addresses that lock their CRV tokens to get veCRV, with 2555 (27%) voting in the fortnightly gauge proposals. However, participation in the non-gauge proposals is significantly lower. For example, 'ownership proposals' that seek the community's decision on adding new gauges, receive votes from an average of 24 unique addresses. This mirrors the low participation found in other decentralised organisations [11] and shows that the economically incentivised gauge proposals have better turnout, but this turnout does not carry-over to the non-gauge proposals.

Secondly, we considered the quantity of CRV tokens that are locked for veCRV: there are 644 million CRV (46%) locked for veCRV, leaving 770 million CRV in circulation. The tokens are locked with an average remaining lockup period of 181 weeks, or 3 5 years. . This duration indicates a high level of commitment by the token holders to the ecosystem and a long-term outlook on the value of the protocol. Arguably, these numbers show the veToken model is working as expected: users are incentivised to lockup their CRV tokens for extended periods in order to gain voting weight. They use that voting weight to vote on the gauge proposals and direct the emissions of CRV to liquidity providers. However, the participation in non-gauge proposals remains low with just 24 addresses voting on an average non Gauge Proposal.

## 5.1 Votes Follow Bribes

We turn our attention to the higher-level protocols. Convex participates in the Curve ecosystem as one of nine whitelisted contract accounts that can lock CRV for veCRV. In fact, 290 million (45%) of all locked CRV belongs to Convex, making them the entity with the largest voting weight in Curve. However, Convex's voting weight is itself governed by its own token, CVX. There are 71 million CVX, of which 78% is locked for vlCVX to gain voting weight. This is higher than the equivalent number for Curve. Voting on Convex is conducted off-chain via Snapshot with the results relating to Curve proposals posted onchain.

Figure 1: Votium incentivises holders of veCRV and vlCVX to vote for particular Curve gauges through bribes. The chart shows the total USD value of those bribes for each fortnightly vote. The USD value is highly dependent on broader market conditions. We divide the data into a bootstrapping phase (red) and a mature phase (blue).

<!-- image -->

As with Curve, the fortnightly gauge proposals attract the most interest: 1124 unique addresses and 95% of all vlCVX vote in the gauge proposals. The number of unique addresses might be higher except for delegation where a single address can vote using voting weight delegated to it from many other addresses. There is less interest in non-gauge proposals which receive votes from an average of 77 unique addresses. All of this voting activity appears as a single address when analysing Curve in isolation.

Votium operates at a higher level than Convex. It gathers and distributes bribes to holders of veCRV and vlCVX in return for them voting a particular way in the gauge proposals. Fig 1 shows the total USD value of those bribes for each fortnightly vote. The USD value is highly dependent on broader market conditions: the peaks in late 2021 and early 2022 coincide with peaks across cryptocurrency markets. At the time of writing, the total value of Votium bribes to date is USD $ 248 million and the value for and the value for the most recent fortnight period is over $ 3 million.

We can divide the data in Fig. 1 into a bootstrapping phase and a mature phase. The bootstrapping phase includes the first eight gauge proposals; the mature phase includes all subsequent gauge proposals and continues to the present day. Figure 2 illustrates the change in voting behaviour between the two phases. Each dot represents a single instance of a fortnightly vote for a gauge proposal. The x-axis shows the percentage of the total USD value of Votium bribes directed to each gauge. The y-axis shows the percentage of the total vote received by each gauge. In the bootstrapping phase (red dots) the correlation coefficient between the percentage of bribes attracted and the percentage of votes received is 0 88. . In the mature phase (blue dots) the correlation

## Bribes and \_Votes\_for\_Curve\_Gauge\_Votes

Figure 2: Each dot represents a single instance of a fortnightly vote for a Curve gauge. The x-axis shows the percentage of the total USD value of Votium bribes directed to each gauge. The y-axis shows the percentage of the total vote received by each gauge. The red dots correspond to the bootstrapping phase (corr. coeff. = 0 88); the blue dots correspond to . the mature phase (corr. coeff. = 0.99).

<!-- image -->

<!-- image -->

8

Figure 4: Frax incentivises holders of veCRV and vlCVX to vote for Frax pools through Votium. They contribute almost half of the bribes to Votium.

<!-- image -->

## coefficient is 0 99. .

There were few outliers in the mature phase. Of the 691 dots in Fig. 2, only one represented a gauge that received a percentage of votes less than 0 8 . of its relative bribe in a given fortnight. In other words, votes follow bribes. Conversely, there were 91 instances where a gauge received a percentage of votes more than 1 2 times its relative bribe. . However, this can be explained due to two overlapping factors. Firstly, 71 received a vote that was less than 1% of the total number of votes for a given fortnight - the bribes and votes associated with the gauges were too small to be meaningful. Secondly, 79 involved Frax gauges: since Frax owns vlCVX and is a major briber to Votium (see Sect 5.2), it is to be expected that they would vote for their own lesser-bribed gauges.

This analysis shows that bribes have a significant impact on the outcome of gauge proposals, and, specifically, that votes follow bribes. Figure 3 illustrates this on a per gauge/gauge proposal basis. In the heat map, the non-white cells show the difference in percentage points between the bribes directed to and the votes received by a Curve gauge for a single instance of a fortnightly vote. The white cells indicate no bribes or votes. All of the percentage point differences are within the -6%-2% range. As Charlie Munger once said, 'Show me the incentive, and I will show you the outcome.'

Figure 5: Frax acquires votes for Frax pools through at least three distinct avenues: by locking CRV for veCRV, by locking CVX for vlCVX, and by paying Votium bribes. The cost per vote varies depending on the avenue, and the cost changes over time.

<!-- image -->

## 5.2 The Cost of Votes

Frax is a central player in the Curve ecosystem. They participate at the three levels already mention: they lock CRV for veCRV, they lock CVX for vlCVX, and they make bribes via Votium. The Frax/USDC pool has the second-highest total value locked (TVL) across all Curve pools, trailing only to the Eth/Staked ETH pool. We considered Frax's involvement in the Curve ecosystem at each level.

At the Curve level, Frax began locking CRV for veCRV in July 2022 after a successful governance proposal whitelisted the Frax staking contract. As of February 2023, Frax has locked 697 114 CRV for veCRV, or just 0 01% of all . locked veCRV. We determined the USD value of the locked CRV by the price at which it traded when it was locked. This resulted in a total locked value of USD 618830. $ Frax used this voting weight to exercise a total of 17 3 million . votes. This yielded a cost per vote of USD $ 0 051. . It is important to note that the cost per vote decreases over time as the upfront cost of the token is amortised (see the green line in Fig 5). Additionally, these tokens do have the potential to be traded once the lockup period has expired

At the Convex level, Frax plays a more influential role. Using the same metric as above, we found that, as of February 2023, Frax has locked USD $ 64 74 . million worth of CVX for vlCVX. To determine their voting weight at the Curve level, we examined the amount of veCRV tokens held by Convex during each fortnightly period and the percentage of voting weight held by Frax. This showed that Frax exercised a total of 2 88 billion votes which yields a cost per . vote of USD $ 0 022 (see the blue line in Fig. 5). .

Finally, we analysed Frax's bribes via Votium. Frax is the largest contributor to bribes, accounting for 41% of all bribes to vlCVX, or USD $ 103 69 million. .

Based on the correlations in Sect. 5.1, we estimate that these bribes resulted in following bribes, we estimated that this contribution resulted in 6 72 billion votes . at the Curve level. As of Febraury 2023, Votium bribes for Frax cost USD $ 0 015 . per vote (see the red line in Fig. 5), making it the most cost-efficient option for Frax. However, it is important to note that, unlike the previously described levels, the value of bribes is realised immediately, whereas locking tokens still provides Frax with a claim to the asset once the lock reaches maturity.

The veToken model creates a system where voting weight can be acquired through different mechanisms. In the most direct method, users can lock tokens, say CRV for veCRV, and receive the corresponding voting weight. At another level, users can have a claim to locked tokens and their corresponding voting weight through an intermediary, say CVX locked for vlCVX. At yet another level, users can bribe the holders of locked tokens, say veCRV or vlCVX, to vote a particular way. We can calculate as cost per vote for each of these levels.

## 6 Conclusion

We described the veToken model and its implementation within the Curve ecosystem. We analysed its usage by looking at locking rates, lockup durations, voting participation rates, and financial incentives. We showed that, while the mechanism is simple in isolation, the outcomes are complex. We showed that votes follow bribes. In other words, the voting behaviour of users can be directed through bribes from higher-level protocols. This has a significant impact on the outcome of the gauge proposals. In fact, the distribution of the bribes largely determines the outcome. We also showed that the cost per vote depends on how the vote is acquired. It can be acquired at the base level by locking, but also at intermediary levels using yield aggregators which lock indirectly, or by paying bribes to voting markets.

Our findings show a difference in participation between gauge proposals and non-gauge proposals. For non-gauge proposals, voter participation is low, which mirrors many other decentralised organisations [11]. However, for gauge proposals, voter participation is significantly higher. This affirms the design of the veToken model: users commit to locking tokens for extended durations in exchange for voting weight. In turn, this creates greater participation.

However, participation in gauge proposals is economically incentivised. Voters use their voting weight to direct emissions of CRV. Higher-level protocols including yield aggregators like Convex and voting markets like Votium have emerged to maximise the return for users. Convex's 45% share of all locked CRV and Votium's USD 248 million worth of bribes have a major influence $ on outcomes: Since January 2022, when Votium began to gain recognition, we observed a 0 99 correlation between voting percentages and the percentage of . bribes distributed to each gauge. This is in contrast to existing decentralised organisations where voting coalitions and influential leaders play a more significant role [19].

One entity that participates in Votium bribes and has influence at all levels of the Curve ecosystem is Frax, a stablecoin issuer. They hold less than 0 1% of . all veCRV, yet wield significant influence at other levels. They have spent more than USD 100 million in bribes using Votium. $ In this way, Frax can impact the outcome of gauge proposals without having to lock tokens for extended periods. The maximum lockup period for Convex is just sixteen weeks whereas the maximum lockup period for Curve is four years. Votium does not have any lockup requirement. One might expect such votes to cost more on a per-vote basis, i.e., there might be a premium to acquiring votes without the requirement to lock for an extended period. However, the cost per vote acquired through Convex is currently lower than the cost of votes acquired through Curve, and the cost per vote acquired through Votium is currently lower than the cost of votes acquired through Convex.

In conclusion, our study shows the dynamic interplay between the various levels of the Curve ecosystem, and, more generally, the veToken model. While the token locking mechanism is straight-forward to understand, it results in higher-level protocols that have complex outcomes. The model was developed to address the limitations of the one-token one-vote model. In doing so it has spawned additional protocols that try to capitalise on its behaviour. In the case of Decentralised Finance (DeFi), this is viewed as a positive (i.e., 'money legos'). However, for governance, it means that higher-level protocols can have surprising and, perhaps, undue influence on lower-level ones. In our future work, we will extend this analysis to other implementations and adaptations of the veToken model.

## Acknowledgements

The authors are grateful to the anonymous reviewers that provided feedback on earlier versions of this article.

## References

- [1] M. Abramowicz. The very brief history of decentralized blockchain governance. Vanderbilt Journal of Entertainment and Technology Law , 22(2):273-298, 2020.
- [2] J. Amico. Open sourcing our token delegate program. https://a16z.com/ 2021/08/26/open-sourcing-our-token-delegate-program and https: //archive.today/X47Kb , 2021.
- [3] S. Bhambhwani. Governing decentralized finance (DeFi). https://ssrn. com/abstract=4225775 , 2022.
- [4] V. Buterin. Moving beyond coin voting governance. https://vitalik. ca/general/2021/08/16/voting3.html and https://archive.today/ y5i5B , 2021.

- [5] Convex Finance Community. Convex Finance. https://www. convexfinance.com/ and https://docs.convexfinance.com/ .
- [6] L. Cuende and J. Izquierdo. Aragon network: A decentralized infrastructure for value exchange. https://github.com/aragon/whitepaper/raw/ v1/Aragon%20Whitepaper.pdf , 2017.
- [7] Curve Finance Community. Curve Finance. https://curve.fi/ and https://curve.readthedocs.io/ .
- [8] Q. DuPont. Experiments in algorithmic governance: A history and ethnography of 'The DAO', a failed decentralized autonomous organization. In M. Campbell-Verduyn, editor, Bitcoin and Beyond: Cryptocurrencies, Blockchains and Global Governance . Routledge, 2017.
- [9] M. Egorov. Curve DAO. https://classic.curve.fi/files/CurveDAO. pdf and https://archive.today/wZwV0 , 2020.
- [10] Frax Finance Community. Frax Finance. https://frax.finance/ and https://docs.frax.finance/ .
- [11] R. Fritsch, M. M¨ uller, and R. Wattenhofer. Analyzing voting power in decentralized governance: Who controls DAOs? https://arxiv.org/ abs/2204.01176 , 2022.
- [12] Immunefi. Hack analysis: Beanstalk governance attack, april 2022. https://medium.com/immunefi/ hack-analysis-beanstalk-governance-attack-april-2022-f42788fc821e and https://archive.today/ooHar , 2023.
- [13] P. Merrill, T. H. Austin, J. Rietz, and J. Pearce. Ping-pong governance: Token locking for enabling blockchain self-governance. In Mathematical Research for Blockchain Economy , pages 13-29. Springer, 2020.
- [14] W. Reijers, I. Wuisman, M. Mannan, P. D. Filippi, C. Wray, V. Rae-Looi, A. C. V´lez, and L. Orgad. Now the code runs itself: On-chain and off-chain e governance of blockchain technologies. Topoi: An International Review of Philosophy , 2018.
- [15] N. Schneider. Cryptoeconomics as a limitation on governance. https: //osf.io/wzf85?view\_only=a10581ae9a804aa197ac39ebbba05766 and https://archive.today/RbeYv , 2022.
- [16] Snapshot Labs. Snapshot. https://snapshot.org/ and https://docs. snapshot.org/ .
- [17] B. S. Srinivasan and L. Leland. Quantifying decentralization. https: //news.earn.com/quantifying-decentralization-e39db233c28e and https://archive.today/kRyia , 2017.

- [18] Stake DAO Community. Stake dao. https://stakedao.org/ and https: //stakedao.gitbook.io/ .
- [19] X. Sun, C. Stasinakis, and G. Sermpinis. Decentralization illusion in DeFi: Evidence from MakerDAO. https://arxiv.org/abs/2203.16612 , 2022.
- [20] Votium Community. Votium. https://votium.app/ and https://docs. votium.app/ .
- [21] Yearn Finance Community. Yearn Finance. https://yearn.finance/ and https://docs.yearn.finance/ .