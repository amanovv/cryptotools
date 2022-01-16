# Crypto trading tools
These are group of tools for crypto trading that I usually use for my trading, mainly margin trading. 

### 1. Latest news summarizer based on keyword.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://ec2-54-172-234-158.compute-1.amazonaws.com:8501)

This tool is mainly to have short summarized look at news about cryptocurrency since sometimes news about crypto can be explosive. Or just use it anyway you want, because it works with any keyword not necessarily for crypto.

Even though you can use the tool with above link, it might be convenient to run it locally on your machine.

So, to run it locally:

- Create virtual env
- Install pytorch for your machine
- `pip install bs4 bert-extractive-summarizer streamlit requests`
- Then, `streamlit run streamlit_crypto.py`

### 2. Reinforcement Learning based simulator

This tool is about simulating the trading environment based on wallets and their share of certain cryptocurrency holding where traders try to maximize their profit for certain timestep.

`Will release shortly`

### 3. Reddit/Twitter sentiment hedger

This tool that I have been using is little different from just guessing negative or positive sentiment of random tweets. The overall sentiment focuses on particular people that has been able to affect the cryptocurrency price, for example, Nayib Bukele, Elon Musk, or some of reddit users. Once those people identified, the tool looks at social network of those people and hedges the potential impact from their social media activity. 

This tool took some engineering to build, so not sure to releaase it fully out, but happy to put out glimpse.





