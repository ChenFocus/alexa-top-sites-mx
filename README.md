# *A Brief Research in Mail Service Used by Organisations*

**Author:** Zeji Chen, student @ [Lancaster University](https://lancaster.ac.uk).

---------------

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Introduction](#introduction)
- [Datasets Used](#datasets-used)
  - [Alexa Top 1M Sites](#alexa-top-1m-sites)
  - [World Global University Dataset](#world-university-dataset)
  - [Datasets Availability](#datasets-availability)
- [Method](#method)
- [Accuracies/Error Analysis](#accuracieserror-analysis)
- [Method](#method-1)
  - [Getting the usage of mail service in Top 1k, 10k, 100k, 1M Alexa Ranked Sites](#getting-the-usage-of-mail-service-in-top-1k-10k-100k-1m-alexa-ranked-sites)
  - [Getting the usage of mail service in Global University Dataset](#getting-the-usage-of-mail-service-in-university-dataset)
- [Results](#results)
  - [Alexa Dataset](#alexa-dataset)
  - [Global University Dataset](#university-dataset)
- [Simple Conclusions](#simple-conclusions)
  - [Result Tables](#result-tables)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
 
## Introduction

This project, or research, is conducted in supplyment of evidence for the author's essay assignment. This project uses [Python](https://python.rg) as a [crawler](https://en.wikipedia.org/wiki/Web_crawler) to verify [MX Records](https://en.wikipedia.org/wiki/MX_record) (mail server record) for individual domains.

The Python crawler used is written by **Ryan Zhao** [(email)](mailto:lin.zhao-3@student.manchester.ac.uk) - student at [Manchester University](https://en.wikipedia.org/wiki/University_of_Manchester), UK. Ryan has fully agreed and authorised the use of his script in this research.

The data, scripts and other files of this project is made public at [https://github.com/ChenFocus/alexa-top-sites-mx](https://github.com/ChenFocus/alexa-top-sites-mx). The code repository contains some files involved in the early stage of this project, that may not be relevant.

### Aim of Research

This research attempts to find out the greater market share occupier between [Gmail](https://www.google.com/intl/en-GB/gmail/about/#) and [Outlook](https://www.microsoft.com/en-gb/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook), by looking at a large sample of organisations' domains in both technology and education sector. Please refer to [Dataset Used](#datasets-used).

## Datasets Used

### Alexa Top 1M Sites

[Alexa](https://alexa.com) is a web analytic & intelligence company owned by [Amazon](https://www.aboutamazon.com). The [Alexa World Site Rank](https://www.alexa.com/topsites) is often regarded as the most representive world site rank.

### World Global University Dataset

### Datasets Availability

Alexa Top 1M Sites Dataset: [http://s3.amazonaws.com/alexa-static/top-1m.csv.zip](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip)

> *Please be aware that although this data is from Alexa officially, some [said](https://hackertarget.com/top-million-site-list-download/) it's no longer updated.*

Global University Dataset: [https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json](https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json)

> *Please be aware that as this data is from an open source project, which its content may change anytime in the future, if you would like to get the same dataset as this project, at the date of this research is conducted, please instead download the data from this repository, or at [https://raw.githubusercontent.com/ChenFocus/university-domains-list/master/world_universities_and_domains.json](https://raw.githubusercontent.com/ChenFocus/university-domains-list/master/world_universities_and_domains.json).*

## Method

Through the [dig](https://en.wikipedia.org/wiki/Dig_(command)) commandline software, one is able to find the MX Record (mail server record) for a domain. By running this command:

```bash
dig +short mx example.com
```

If we tried to find, for example, what mail service is used by Twitter. Inc, we can run:

```bash
dig +short mx example

# response
10 aspmx.l.google.com.
30 aspmx3.googlemail.com.
20 alt1.aspmx.l.google.com.
20 alt2.aspmx.l.google.com.
30 aspmx2.googlemail.com.
```

Therefore we know that [Twitter](https://about.twitter.com/en) use googlemail, which is [Gmail](https://gmail.com), for its domain twitter.com.

The Python crawler, can read a single-lined `.csv` (a data-sheet format), then run the `dig` command from a Python library (dependecy) [dnspython](https://pypi.org/project/dnspython/), print the current progress of querying MX records and current stats gathered, eventually output the result as such:

```text
Gmail:  305 
Outlook:  83 
Others:  524 
N/A:  88
```

Explanation:

| Service name/type| Description|
|-------------------|---------------------------------------------------------------------------------------------|
|`Gmail: `| The count of domains in the dataset provided that use Gmail on their domain                 |
|`Outlook: `| The count of domains in the dataset provided that use Outlook on their domain               |
|`Other: `| The count of domains in the dataset provided that use other email serviceson their domain   |
|`N/A: `| No relevant record detected; the domain could have not been configured to run email service |

## Accuracies/Error Analysis


As the Alexa dataset may contain asset domains (domains that are used to solely distribute static file/other recources), such as `software-download.microsoft.com`, which `dig +short mx software-download.microsoft.com` wouldn't return anything as there is no mail services running on the domain; or, no mail service is ran on the root domain. However, all calculations made from the result will exclude occassions like this.

It's known that The World Global University Dataset may not be complete and contains some inaccurate information (for example, the domain of Lancaster University in the dataset is `lancs.ac.uk`, instead of `lancaster.ac.uk`). This may affect the conclusion drawn from this dataset.

It's also known that different runs of the script may produce slightly different results, as one's DNS record may be failed to be fetched due to server/internet errors. Multiple runs of the script should eliminate this error partially.

Effort had been made to eliminate any error for any calculations made / conclusions drawn, at the best of personal knowledge, capabiltiy and computer/network limits.

## Method

### Getting the usage of mail service in Top 1k, 10k, 100k, 1M Alexa Ranked Sites

At a Linux computer:

```bash
git clone github.com/ChenFocus/alexa-top-sites-mx
cd alexa-top-sites-mx
cd python_method

# make sure Python 3 and Pip 3 is installed
pip install dnspython
python main.py 1000 | tee result_1000.txt # modify the `1000` to 10000 and more to get different results
# wait for completion of the script
```

A cloud computer (server) is used to calculate results for above targets.

As the Alexa rank list goes further, more irrevelant/personal domains may be recorded, therefore resulting in more inaccurate results.

### Getting the usage of mail service in Global University Dataset

At a Linux computer:
```bash
git clone github.com/ChenFocus/alexa-top-sites-mx
cd alexa-top-sites-mx
cd python_method

# make sure Python 3 and Pip 3 is installed
pip install dnspython
python main.py 9773 | tee result.txt # Check whole dataset - usage of mail services
python us_uni.py 2730 | tee result_us_uni.txt # Check for US universities only
python uk_uni.py 161 | tee result_uk_uni.txt # Check for UK universities only
# wait for completion of the script
```

> *The conversion of the original `.json` data to `.csv` format is through a series of replace/regrex match/plugin operation conducted in [Visual Studio Code](https://code.visualstudio.com).*

## Results

### Alexa Dataset

| Dataset   Name/Variation | Gmail Counts | Outlook Counts | Others Counts | N/A Counts | Total Counts | Total Valid Counts | Calculated Gmail Share | Calculated Outlook Share | Gmail Outcompete Outlook in   Technology Sector By |
|:------------------------:|:------------:|:--------------:|:-------------:|:---------:|:------------:|:------------------:|:----------------------:|:------------------------:|:--------------------------------------------------:|
|  Alexa Top 1M - 1k list  |      305     |       83       |      524      |     88    |     1000     |         912        | 33.4%                  | 9.1%                     | 73%                                                |
|  Alexa Top 1M - 10k list |     2779     |       873      |      4961     |    1387   |     10000    |        8613        | 32.3%                  | 10.1%                    | 69%                                                |
| Alexa Top 1M - 100k list |     22527    |      8461      |     51942     |   17070   |    100000    |        82930       | 27.2%                  | 10.2%                    | 62%                                                |

> *Note that the result for the whole 1 million site is currently being calculated by a cloud server. The result of this may be updated in the future.*

### Global University Dataset

|      Dataset   Name/Variation     | Gmail Counts | Outlook Counts | Others Counts | N/A Counts | Total Counts | Total Valid Counts | Calculated Gmail Share | Calculated Outlook Share | Outlook Outcompete Gmail in   Education Sector By |
|:---------------------------------:|:------------:|:--------------:|:-------------:|:---------:|:------------:|:------------------:|:----------------------:|:------------------------:|:-------------------------------------------------:|
|       World University list       |     1296     |      2158      |      4691     |    1628   |     9773     |        8145        | 15.9%                  | 26.5%                    | 40%                                               |
| World University list - US   only |      298     |       923      |      876      |    273    |     2370     |        2097        | 14.2%                  | 44.0%                    | 68%                                               |
| World University list - UK   only |       8      |       63       |       65      |     25    |      161     |         136        | 5.9%                   | 46.3%                    | 87%                                               |

## Simple Conclusions

From the results, **Gmail leads the competition in the technology sector** by occupying 33.4% market share in the Top 1000 websites ranked by Alexa. This data is extended into 32.3%, 27.2% when 10k, 100k top sites are used as samples. From results available, Gmail beats Outlook in the technology sector with at least 60% more market share.

**Outlook outcompetes Gmail in the education sector**, occupying 44.0% and 46.3% market share in education section in US & UK respectively, outcompeting Gmail with 68% and 87% more market share.

### Result Tables

#### Technology Sector - From Alexa Top 1M Dataset

| Dataset   Name/Variation | Calculated Gmail Share | Gmail Outcompete Outlook in Technology   Sector By |
|:------------------------:|------------------------|----------------------------------------------------|
|  Alexa Top 1M - 1k list  | 33.4%                  | 73%                                                |
|  Alexa Top 1M - 10k list | 32.3%                  | 69%                                                |
| Alexa Top 1M - 100k list | 27.2%                  | 62%                                                |

#### Education Sector - From Global University Dataset

|      Dataset   Name/Variation     | Calculated Outlook Share | Outlook Outcompete Gmail in   Education Sector By |
|:---------------------------------:|--------------------------|---------------------------------------------------|
|       World University list       | 26.5%                    | 40%                                               |
| World University list - US   only | 44.0%                    | 68%                                               |
| World University list - UK   only | 46.3%                    | 87%                                               |