---
layout: page
title: Commands
description: >
  Description of every command in OpenCryptoBot
hide_description: true
menu: true
order: 4
---

[/about](#about) - About the bot  
[/ath](#ath) - All Time High  
[/best](#best) - Best movers  
[/bpmn](#bpmn) - Command diagrams  
[/ch](#ch) - Price Change  
[/comp](#comp) - Compare currencies  
[/cs](#cs) - Candlestick chart  
[/c](#c) - Price and Volume chart  
[/des](#des) - Currency description  
[/dev](#dev) - Development info  
[/donate](#donate) - Donate to bot development  
[/ex](#ex) - Exchange details & toplist  
[/feedback](#feedback) - Feedback  
[/g](#g) - Global stats  
[/help](#help) - List available commands  
[/ico](#ico) - Initial Coin Offering  
[/i](#i) - Technical coin info  
[/mc](#mc) - Market Capitalization  
[/m](#m) - List coin markets  
[/n](#n) - Crypto news  
[/pe](#pe) - People in crypto  
[/p](#p) - Current price  
[/restart](#restart) - Restart bot  
[/roi](#roi) - Return on Investment  
[/se](#se) - Coin search  
[/shutdown](#shutdown) - Shutdown bot  
[/soc](#soc) - Social links and stats  
[/s](#s) - Currency stats  
[/tr](#tr) - Google Trends  
[/t](#t) - Team details  
[/update](#update) - Update bot  
[/vol](#vol) - Volume for a coin  
[/v](#v) - Value of coin quantity  
[/worst](#worst) - Worst movers  
[/wp](#wp) - Whitepaper download  

## `/about`

![Screenshot](assets/cmds/about.png)

**Alternative commands**  
None

**Description**  
Show informations about the author / developer of this Telegram bot and about the bot itself.

**Syntax**  
`/about`

**Examples**  
`/about`

## `/ath`

![Screenshot](assets/cmds/ath.png)

**Alternative commands**  
None  

**Description**  
Show informations about the highest price ever reached. Including the date, the price (in a specifiable currency) and past days since ATH.

**Syntax**  
`/ath (<target symbol>,[...]-)<symbol>`  

**Examples**  
Get All Time High price for ETH  
`/ath eth`  
Get All Time High price for ETH in BTC  
`/ath btc-eth`  
Get All Time High price for ETH in BTC and XRP  
`/ath btc,xrp-eth`  

## `/best`

![Screenshot](assets/cmds/best.png)

**Alternative commands**  
None

**Description**  
Show best movers for hour or day by change of price in %.

**Syntax**  
`/best hour [or] day (<# of entries>) (<min. volume>)`

**Examples**  
Show best performing coins (default is 10 coins for last hour)
`/best`  
Show 10 best performing coins for last hour  
`/best hour`  
Show 20 best performing coins for last 24 hours  
`/best day 20`  
Show 30 best performing coins in the last hour that had a volume of at least 1 million  
`/best hour 30 1000000`  

## `/bpmn`

![Screenshot](assets/cmds/bpmn.png)

**Alternative commands**  
None

**Description**  
Show a BPMN diagram for the given command. This will give you an understanding which APIs the command is calling and how the command words internally.

**Syntax**  
`/bpmn <command>`

**Examples**  
Show BPMN diagram for `/p` command  
`/bpmn p`  

## `/ch`

![Screenshot](assets/cmds/ch.png)

**Alternative commands**  
`/change`  

**Description**  
Show the price change of a cryptocurrency over time (day, week, month and year) in target currency. Target currency can be:

- BTC
- ETH
- LTC
- BCH
- BNB
- EOS
- XRP
- XLM
- And most fiat currencies

**Syntax**  
`/ch (<target symbol>-)<symbol>`

**Examples**  
Show price change over time for XMR (default target symbol is USD)  
`/ch xmr`  
Show price change over time for XMR in BTC  
`/ch btc-xmr`  

## `/comp`

![Screenshot](assets/cmds/comp.png)

**Alternative commands**  
`/compare`  

**Description**  
Show link to [Coinlib](https://coinlib.io) to compare the given cryptocurrencies.

**Syntax**  
`/comp <symbol> <symbol> [...]`

**Examples**  
Show link to compare XMR, DASH and DERO  
`/comp xmr dash dero`  

## `/cs`

![Screenshot](assets/cmds/cs.png)

**Alternative commands**  
`/candle`  
`/candlestick`  

**Description**  
Show a candlestick diagram for a given cryptocurrency and a given timeframe.

**Syntax**  
`/cs (<target symbol>-)<symbol> (<timeframe>m[or]h[or]d)`

**Examples**  
Show candlestick chart for XMR (default timeframe is 3 days)  
`/cs xmr`  
Show candlestick chart for XMR in XRP  
`/cs xrp-xmr`  
Show candlestick chart for XMR in XRP for last 90 days  
`/cs xrp-xmr 90d`  
Show candlestick chart for XMR for last 60 minutes  
`/cs xmr 60m`  

## `/c`

![Screenshot](assets/cmds/c.png)

**Alternative commands**  
`/chart`  

**Description**  
Show a price and volume chart for the given timeframe.

**Syntax**  
`/c (<vs symbol>-)<symbol> (<# of days>)`

**Examples**  
Show chart for XMR  
`/c xmr`  
Show chart for XMR in XRP  
`/c xrp-xmr`  
Show chart for XMR in XRP for last 90 days  
`/c xrp-xmr 90`  

## `/des`

![Screenshot](assets/cmds/des.png)

**Alternative commands**  
`/description`  

**Description**  
Show description for a given cryptocurrency.

**Syntax**  
`/des <symbol>`

**Examples**  
Show description for LOKI 
`/des loki`  

## `/dev`

![Screenshot](assets/cmds/dev.png)

**Alternative commands**  
`/developer`  

**Description**  
Show development and source code related GitHub info for given cryptocurrency.  

**Syntax**  
`/dev <symbol>`

**Examples**  
Show development related info for LOKI  
`/dev loki`  

## `/donate`

![Screenshot](assets/cmds/donate.png)

**Alternative commands**  
None  

**Description**  
Shows other commands that allow the user to see QR-Codes for donation wallets (donations to the developer of this bot).

**Syntax**  
`/donate`

**Examples**  
Show all available donation options  
`/donate`  
Show QR-Code for Bitcoin donation address  
`/donateBTC`  
Show QR-Code for Bitcoin Cash donation address  
`/donateBCH`  
Show QR-Code for Ethereum donation address  
`/donateETH`  
Show QR-Code for Monero donation address  
`/donateXMR`  

## `/ex`

![Screenshot](assets/cmds/ex.png)

**Alternative commands**  
`/exchange`  

**Description**  
Show the description for a given exchange or show a toplist for exchanges based on trading volume per day.

**Syntax**  
`/ex <exchange> [or] top=<# of exchanges>`

**Examples**  
Show info about Binance  
`/ex binance`  
Show top 10 exchanges by 24h volume  
`ex top=10`  

## `/feedback`

**Alternative commands**  
None

**Description**  
Provide your feedback, bug reports, feature requests or anything else you want to tell me, for this bot.

**Syntax**  
`/feedback <some text>`

**Examples**  
Send me some positive feedback :-)  
`/feedback hey bro, really like your bot!`  

## `/g`

![Screenshot](assets/cmds/g-dom.png)

**Alternative commands**  
`/global`  

**Description**  
Get info about global dominance, volume and market capitalization.

**Syntax**  
`/g mcap [or] vol [or] dom`

**Examples**  
Show global crypto market capitalization  
`/g mcap`  
Show global crypto market volume  
`/g vol`  
Show global crypto market dominance
`/g dom`  

## `/help`

![Screenshot](assets/cmds/help.png)

**Alternative commands**  
`/h`  

**Description**  
Returns a list of all available commands sorted by category.

**Syntax**  
`/help`

**Examples**  
Show all available commands  
`/help`  

## `/ico`

![Screenshot](assets/cmds/ico.png)

**Alternative commands**  
None  

**Description**  
Show info about the ICO of a cryptocurrency.

**Syntax**  
`/ico`

**Examples**  
Show ICO info  
`/ico`  

## `/i`

![Screenshot](assets/cmds/i.png)

**Alternative commands**  
`/info`  

**Description**  
Show general cryptocurrency specs.

**Syntax**  
`/i <symbol>`

**Examples**  
Show info about XMR  
`/i xmr`  

## `/mc`

![Screenshot](assets/cmds/mc.png)

**Alternative commands**  
`/mcap`  

**Description**  
Show market capitalization of specific cryptocurrency or a toplist (max 100 currencies).

**Syntax**  
`/mc (<target symbol>-)<symbol> [or] top=<# of currencies>`

**Examples**  
Show market cap for XMR  
`/mc xmr`  
Show market cap for XMR in BTC  
`/mc btc-xmr`  
Show top 10 currencies by market cap  
`/mc top=10`  

## `/m`

![Screenshot](assets/cmds/m-vol.png)

**Alternative commands**  
`/market`  

**Description**  
Show exchanges that trade specified cryptocurrency or show top 10 trading pairs (with exchange) by volume for the cryptocurrency.

**Syntax**  
`/m <symbol> (vol)`

**Examples**  
Show where to trade XMR  
`/m xmr`  
Show top 10 trading pairs for XMR
`/m xmr vol`  

## `/n`

![Screenshot](assets/cmds/n.png)

**Alternative commands**  
`/news`  

**Description**  
Show latest crypto news or show news filtered by cryptocurrency and / or by one of these filters:

- rising
- hot
- bullish
- bearish
- important
- saved
- lol

**Syntax**  
`/n (<symbol>) (filter=<filter>)`

**Examples**  
Show current news (default is no filter and no currency)  
`/n`  
Show news for XMR  
`/n xmr`  
Show news for XMR and add filter 'hot'  
`/n xmr filter=hot`  
Show news for filter 'lol' (not currency specific)  
`/n filter=lol`  

## `/pe`

![Screenshot](assets/cmds/pe.png)

**Alternative commands**  
`/people`  

**Description**  
Show info about people in the crypto business. To get to know the names, use the `/t` command. There you will also have direct links to team members.

**Syntax**  
`/pe <forename>-<surname>`

**Examples**  
Show info about Vitalik Buterin  
`/pe vitalik-buterin`  
Show info about Wladimir J. van der Laan  
`/pe wladimir-j-van-der-laan`  

## `/p`

![Screenshot](assets/cmds/p.png)

**Alternative commands**  
`/price`  

**Description**  
Show current price for given cryptocurrency. Per default, the price will be shown in `BTC`, `ETH`, `USD` and `EUR` but it's also possible to show the price in one of the supported currencies:

- BTC
- ETH
- LTC
- BCH
- BNB
- EOS
- XRP
- XLM
- And most fiat currencies

This command can also be used in [inline mode](https://core.telegram.org/bots/inline).

**Syntax**  
Regular  
`/p (<target symbol>,[...]-)<symbol>`  
Inline mode  
`@opencryptobot /p (<target symbol>,[...]-)<symbol>.`  

**Examples**  
Show price for XMR  
`/p xmr`  
Show price for XMR in EOS  
`/p eos-xmr`  
Show price for XMR in XRP, XLM and LTC  
`/p xrp,xlm,ltc-xmr`  
Show price for XMR (inline mode)  
`@opencryptobot /p xmr.`  
Show price for XMR in EOS (inline mode)  
`@opencryptobot /p eos-xmr.`  
Show price for XMR in XRP, XLM and LTC (inline mode)  
`@opencryptobot /p xrp,xlm,ltc-xmr.`  

## `/restart`

![Screenshot](assets/cmds/restart.png)

**Alternative commands**  
None  

**Description**  
Restart the bot. This will only work if you are the owner of the bot.

**Syntax**  
`/restart`  

**Examples**  
Restart the bot  
`/restart`  

## `/roi`

![Screenshot](assets/cmds/roi.png)

**Alternative commands**  
None  

**Description**  
Show Return on Investment for a cryptocurrency. Will only work if the cryptocurrency had an ICO.  

**Syntax**  
`/roi <symbol>`  

**Examples**  
Show Return on Investment for LOKI  
`/roi loki`  

## `/se`

![Screenshot](assets/cmds/se.png)

**Alternative commands**  
`/search`  

**Description**  
Find all cryptocurrencies (with symbol) for the given search-string  

**Syntax**  
`/se <coin name>`  

**Examples**  
Search for the symbol of Monero  
`/se monero`  

## `/shutdown`

![Screenshot](assets/cmds/shutdown.png)

**Alternative commands**  
None  

**Description**  
Shutdown the bot. This will only work if you are the owner of the bot.

**Syntax**  
`/shutdown`  

**Examples**  
Shutdown the bot  
`/shutdown`  

## `/soc`

![Screenshot](assets/cmds/soc.png)

**Alternative commands**  
`/social`  

**Description**  
Show all available social media platforms with links and followers / likes if available.

**Syntax**  
`/soc <symbol>`  

**Examples**  
Show social media for XMR  
`/soc xmr`  

## `/s`

![Screenshot](assets/cmds/s.png)

**Alternative commands**  
`/stats`  

**Description**  
Show summary for a cryptocurrency to get a general idea about it.

**Syntax**  
`/s <symbol>`  

**Examples**  
Show summary LOKI  
`/s loki`  

## `/tr`

![Screenshot](assets/cmds/tr.png)

**Alternative commands**  
`/trend`  

**Description**  
Get *Interest Over Time* chart from Google Trends for a set of given keywords and a timeframe.

**Syntax**  
`/tr <keyword> (<keyword> [...] t=<# of days/months/years>d[or]m[or]y[or]all)`  

**Examples**  
Show interest over time for keyword 'blockchain'  
`/tr blockchain`  
Show comparison of interest over time for a list of keywords  
`/tr blockchain bitcoin litecoin`  
Show interest over time for keyword 'blockchain' for the last 30 days  
`/tr blockchain t=30d`  
Show comparison of interest over time for a list of keywords for last 5 years  
`/tr blockchain bitcoin litecoin t=5y`  
Show interest over time for keyword 'blockchain' and whole available timeframe  
`/tr blockchain t=all`  

## `/t`

![Screenshot](assets/cmds/t.png)

**Alternative commands**  
`/team`  

**Description**  
List people that are working on a project with their role and a link to the `/pe` command to get details about a team member.

**Syntax**  
`/t <symbol>`  

**Examples**  
Show people that are working on BTC  
`/t btc`  

## `/update`

![Screenshot](assets/cmds/update.png)

**Alternative commands**  
None  

**Description**  
Update the bot to the latest release version, to a specific release, to a specific branch name or just check if a new version (latest release) is available.

**Syntax**  
`/update (relase=<release tag> [or] branch=<branch name> [or] check)`  

**Examples**  
Update bot to latest release  
`/update`  
Update bot to release 0.1.0  
`/update release=0.1.0`  
Update bot to latest version of branch 'master'  
`/update branch=master`  
Check if an update is available  
`/update check`  
Check if a new release update is available  
`/update release check`  
Check if a new branch update is available  
`/update branch check`  

## `/v`

![Screenshot](assets/cmds/v.png)

**Alternative commands**  
`/value`  

**Description**  
Show the value of specific cryptocurrency quantity in `BTC`, `ETH`, `USD` and `EUR` or the specified currency.

**Syntax**  
`/v (<target symbol>,[...]-)<symbol> <quantity>`  

**Examples**  
Show value of 971 LOKI coins in default currencies  
`/v loki 971`  
Show value of 1500 XRP coins in XLM  
`/v xlm-xrp 1500`  
Show value of 1500 XRP coins in XLM and EUR  
`/v xlm,eur-xrp 1500`  

## `/vol`

![Screenshot](assets/cmds/vol.png)

**Alternative commands**  
`/volume`  

**Description**  
Show total volume for a cryptocurrency or volume toplist (max 100 currencies).

**Syntax**  
`/vol (<target symbol>-)<symbol> [or] top=<# of currencies>`  

**Examples**  
Show volume for LOKI  
`/vol loki`  
Show volume for LOKI in BTC  
`/vol btc-loki`  
Show top 10 currencies by total volume  
`/vol top=10`  

## `/worst`

![Screenshot](assets/cmds/worst.png)

**Alternative commands**  
None  

**Description**  
Show worst movers for hour or day by change of price.  

**Syntax**  
`/worst (hour[or]day <# of entries> <min. volume>)`  

**Examples**  
Show worst performing coins (default is 10 coins for last hour)  
`/worst`  
Show 10 worst performing coins for last hour  
`/worst hour`  
Show 20 worst performing coins for last 24 hours  
`/worst day 20`  
Show 30 worst performing coins in the last hour that had a volume of at least 1 million  
`/worst hour 30 1000000`  

## `/wp`

![Screenshot](assets/cmds/wp.png)

**Alternative commands**  
`/whitepaper`  

**Description**  
Download the whitepaper of a given cryptocurrency. If no whitepaper can be found then there is the possibility to add a keyword to search an additional source.  

**Syntax**  
`/wp <symbol> (all)`  

**Examples**  
Download whitepaper for XMR  
`/wp xmr`  
Download whitepaper for BCH and search in additional source  
`/wp bch all`  