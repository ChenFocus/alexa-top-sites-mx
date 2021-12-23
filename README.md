# A Brief Research in Mail Service Used by Organisations 

Author: Zeji Chen, student at @LancasterUniversity

## Table of Content

<!-- START doctoc -->

<!-- END doctoc -->
 
## Introduction

This project, or research, is conducted in supplyment of evidence for my essay assignment. This project uses Python as a crawler to verify MX Records (mail server record) for individual domains. The Python crawler used is written by Ryan Zhao - student at Manchester University, UK. This code repository contains some files that may not be relevant to the final method used and result.

## Method

Through the dig commandline software, one is able to find the MX Record (mail server record) for a domain. By running this command:

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

Therefore we know that Twitter use googlemail, which is Gmail, for its domain twitter.com.

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

This method is somewhat precise. The two main datasets used is from either Alexa, an Amazon company that focus at website intelligence, or the Open Source project xxx.

However, as the Alexa dataset may contain asset domains (domains that are used to solely distribute static file/other recources), such as `dl.google.com`, which `dig +short mx dl.google.com` wouldn't return anything as there is no mail services running on the domain; or, no mail service is ran on the root domain. However, all calculations made from the result will exclude occassions like this.

It's known that The World University Dataset may not be complete and contains some inaccurate information (for example, the domain of Lancaster University in the dataset is `lancs.ac.uk`, instead of `lancaster.ac.uk`). This may affect the conclusion drawn from this dataset.

It's also known that different runs of the script may produce slightly different results, as one's DNS record may be failed to fetch due to server/internet errors. Multiple runs of the script should eliminate this error partially.

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

### Getting the usage of mail service in University Dataset

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

## Results

### Alexa Dataset

| Dataset   Name/Variation | Gmail Counts | Outlook Counts | Others Counts | N/A Count | Total Counts | Total Valid Counts | Calculated Gmail Share | Calculated Outlook Share | Gmail Outcompete Outlook in   Technology Sector By |
|:------------------------:|:------------:|:--------------:|:-------------:|:---------:|:------------:|:------------------:|:----------------------:|:------------------------:|:--------------------------------------------------:|
|  Alexa Top 1M - 1k list  |      305     |       83       |      524      |     88    |     1000     |         912        | 33.4%                  | 9.1%                     | 73%                                                |
|  Alexa Top 1M - 10k list |     2779     |       873      |      4961     |    1387   |     10000    |        8613        | 32.3%                  | 10.1%                    | 69%                                                |
| Alexa Top 1M - 100k list |     22527    |      8461      |     51942     |   17070   |    100000    |        82930       | 27.2%                  | 10.2%                    | 62%                                                |

> *Note that the result for the whole 1 million site is currently being calculated by a cloud server. The result of this may be updated in the future.

### University Dataset

|      Dataset   Name/Variation     | Gmail Counts | Outlook Counts | Others Counts | N/A Count | Total Counts | Total Valid Counts | Calculated Gmail Share | Calculated Outlook Share | Outlook Outcompete Gmail in   Education Sector By |
|:---------------------------------:|:------------:|:--------------:|:-------------:|:---------:|:------------:|:------------------:|:----------------------:|:------------------------:|:-------------------------------------------------:|
|       World University list       |     1296     |      2158      |      4691     |    1628   |     9773     |        8145        | 15.9%                  | 26.5%                    | 40%                                               |
| World University list - US   only |      298     |       923      |      876      |    273    |     2370     |        2097        | 14.2%                  | 44.0%                    | 68%                                               |
| World University list - UK   only |       8      |       63       |       65      |     25    |      161     |         136        | 5.9%                   | 46.3%                    | 87%                                               |

## Simple Conclusions

From the results, Gmail leads the competition in the technology sector by occupying 33.4% market share in the Top 1000 websites ranked by Alexa.

Outlook outcompetes Gmail in the education sector, occupying 44.0% and 46.3% market share in education section in US & UK respectively.

### Result Tables

| Dataset   Name/Variation | Calculated Gmail Share | Gmail Outcompete Outlook in Technology   Sector By |
|:------------------------:|------------------------|----------------------------------------------------|
|  Alexa Top 1M - 1k list  | 33.4%                  | 73%                                                |
|  Alexa Top 1M - 10k list | 32.3%                  | 69%                                                |
| Alexa Top 1M - 100k list | 27.2%                  | 62%                                                |

|      Dataset   Name/Variation     | Calculated Outlook Share | Outlook Outcompete Gmail in   Education Sector By |
|:---------------------------------:|--------------------------|---------------------------------------------------|
|       World University list       | 26.5%                    | 40%                                               |
| World University list - US   only | 44.0%                    | 68%                                               |
| World University list - UK   only | 46.3%                    | 87%                                               |