# `points and resources`

**`creating api key on data-gov-in`**
- register and login
- go to my account section(logged In) and
- just click on create API key; there you have it
- this key can be used for any datasset
- to see how to use it [look at](how-to-use-dataGov-APIs.ipynb)

---
**`important open data websites`**
- [India](https://data.gov.in/)
- [USA](https://www.data.gov/)
- [All Open Data Sites](https://www.data.gov/open-gov/) or [this](https://data.gov.in/opendatasites)
- Visit any site using above link.
---
**`avoid headers problem`**
- some websites like `amazon` use systems that can detect bot/automated(basically not through a web-browser, rather done programmatically) requests,
- to avoid them we can use headers parameter in out get request
- to get your user-agent [visit](https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes#parse-useragent)
- or to learn more about headers go to requests docs and also look into network-inspection tab to know more about them for a particular website
- we also can use slenium/helium automation but that is resource heavy even with headless running 
- Notes:
    - we also can use other user agents like for other web-browsers(safari,firefox etc) and try what sort of info we get
    - you also can trying to rotate through different user-agents when facing problem your usual user-agent; might help when there is some IP blocks etc
---