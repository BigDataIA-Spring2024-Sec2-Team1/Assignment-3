from utility.test_cases_functions.url_class_tests import *


data1 = {
        "title": "Time Value of Money in Finance",
        "topic": "Quantitative Methods",
        "published_year": 2024,
        "level": "Level I",
        "introduction": "Faced with an overwhelming amount of data, analysts must deal with the task of wrangling those data into something that provides a clearer picture of what is going on. We use the concepts and tools of hypothesis testing to address these issues. Hypothesis testing is part of statistical inference, the process of making judgments about a larger group (a population) based on a smaller group of observations (that is, a sample). The concepts and tools of hypothesis testing provide an objective means to gauge whether the available evidence supports the hypothesis. After applying a statistical test of a hypothesis, we should have a clearer idea of the probability that a hypothesis is true or not, although our conclusion always stops short of certainty.",
        "learning_outcomes": "The member should be able to: define a hypothesis, describe the steps of hypothesis testing, and describe and interpret the choice of the null and alternative hypotheses; compare and contrast one-tailed and two-tailed tests of hypotheses; explain a test statistic, Type I and Type II errors, a significance level, how significance levels are used in hypothesis testing, and the power of a test; explain a decision rule and the relation between confidence intervals and hypothesis tests, and determine whether a statistically significant result is also economically meaningful.",
        "summary": "In this reading, we have presented the concepts and methods of statistical inference and hypothesis testing. A hypothesis is a statement about one or more populations. The steps in testing a hypothesis are as follows: State the hypotheses. Identify the appropriate test statistic and its probability distribution. Specify the significance level. State the decision rule. Collect the data and calculate the test statistic. Make a decision.",
        "overview": "",
        "link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/hypothesis-testing"
    }
test_valid_data(data1)


data2 = {
        "title": "Hypothesis Testing",
        "topic": "Quantitative Methods",
        "published_year": 2024,
        "level": "Level I",
        "introduction": "Faced with an overwhelming amount of data, analysts must deal with the task of wrangling those data into something that provides a clearer picture of what is going on. We use the concepts and tools of hypothesis testing to address these issues. Hypothesis testing is part of statistical inference, the process of making judgments about a larger group (a population) based on a smaller group of observations (that is, a sample). The concepts and tools of hypothesis testing provide an objective means to gauge whether the available evidence supports the hypothesis. After applying a statistical test of a hypothesis, we should have a clearer idea of the probability that a hypothesis is true or not, although our conclusion always stops short of certainty.",
        "learning_outcomes": "The member should be able to: define a hypothesis, describe the steps of hypothesis testing, and describe and interpret the choice of the null and alternative hypotheses; compare and contrast one-tailed and two-tailed tests of hypotheses; explain a test statistic, Type I and Type II errors, a significance level, how significance levels are used in hypothesis testing, and the power of a test; explain a decision rule and the relation between confidence intervals and hypothesis tests, and determine whether a statistically significant result is also economically meaningful.",
        "summary": "In this reading, we have presented the concepts and methods of statistical inference and hypothesis testing. A hypothesis is a statement about one or more populations. The steps in testing a hypothesis are as follows: State the hypotheses. Identify the appropriate test statistic and its probability distribution. Specify the significance level. State the decision rule. Collect the data and calculate the test statistic. Make a decision.",
        "overview": "",
        "link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/hypothesis-testing"
    }
test_valid_data(data2)


data2 = {
        "title": "Machine Learning",
        "topic": "Quantitative Methods",
        "published_year": 2024,
        "level": "Level II",
        "introduction": "Investment firms are increasingly using technology at every step of the investment management value chain—from improving their understanding of clients to uncovering new sources of alpha and executing trades more efficiently. Machine learning techniques, a central part of that technology, are the subject of this reading. These techniques first appeared in finance in the 1990s and have since flourished with the explosion of data and cheap computing power.This reading provides a high-level view of machine learning (ML).",
        "learning_outcomes": "The member should be able to: describe supervised machine learning, unsupervised machine learning, and deep learning;",
        "summary": "Machine learning methods are gaining usage at many stages in the investment management value chain. Among the major points made are the following",
        "overview": "",
        "link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/machine-learning"
    }
test_valid_data(data2)



test_invalid_published_year(1992)



data3 = {
        "title": "Interest Rate Risk and Return",
        "topic": "Fixed Income",
        "published_year": 2024,
        "level": "Level I",
        "introduction": "",
        "learning_outcomes": "",
        "summary": "",
        "overview": "Prior lessons on yield measures established that a fixed-income investor’s rate of return will equal a bond’s yield-to-maturity (YTM) under certain assumptions. In these lessons, we explore the sources of return for fixed-income investments and demonstrate investment returns in different scenarios, including the one embedded in the YTM calculations. Prior lessons also established interest rate risk. We show how investment horizon, in relation to a bond’s features, is a key determinant of interest rate risk for investors and how different investors in the same fixed-income invest- ment can have different returns and views on risk.",
        "link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/Interest-Rate-Risk-and-Return"
    }
test_valid_data(data3)


test_invalid_title("")


test_invalid_link("ftp://example.com")


test_invalid_link("https://example.com")