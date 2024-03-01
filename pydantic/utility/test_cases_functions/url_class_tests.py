from pydantic_models.pydantic_classes import *
import pytest
from pydantic import ValidationError

def test_valid_data(data):
    assert URLClass(**data)
    print("Valid data")
    
@pytest.mark.parametrize("invalid_title", ["", None])
def test_invalid_title(invalid_title):
    data = {
        "title": invalid_title,
        "topic": "Quantitative Methods",
        "published_year": 2024,
        "level": "Level II",
        "introduction": "Investment firms are increasingly using technology at every step of the investment management value chain—from improving their understanding of clients to uncovering new sources of alpha and executing trades more efficiently. Machine learning techniques, a central part of that technology, are the subject of this reading. These techniques first appeared in finance in the 1990s and have since flourished with the explosion of data and cheap computing power.This reading provides a high-level view of machine learning (ML).",
        "learning_outcomes": "The member should be able to: describe supervised machine learning, unsupervised machine learning, and deep learning;",
        "summary": "Machine learning methods are gaining usage at many stages in the investment management value chain. Among the major points made are the following",
        "overview": "",
        "link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/machine-learning"
    }
    with pytest.raises(ValidationError) as excinfo:
        URLClass(**data)
    # Print the captured exception
#     print(excinfo)
    # Or print the exception message
    print(str(excinfo.value))

# Test function for invalid published_year
@pytest.mark.parametrize("invalid_published_year", [1999, 2051])
def test_invalid_published_year(invalid_published_year):
    data = {
        "title": "Machine Learning",
        "topic": "Quantitative Methods",
        "published_year": invalid_published_year,
        "level": "Level II",
        "introduction": "Investment firms are increasingly using technology at every step of the investment management value chain—from improving their understanding of clients to uncovering new sources of alpha and executing trades more efficiently. Machine learning techniques, a central part of that technology, are the subject of this reading. These techniques first appeared in finance in the 1990s and have since flourished with the explosion of data and cheap computing power.This reading provides a high-level view of machine learning (ML).",
        "learning_outcomes": "The member should be able to: describe supervised machine learning, unsupervised machine learning, and deep learning;",
        "summary": "Machine learning methods are gaining usage at many stages in the investment management value chain. Among the major points made are the following",
        "overview": "",
        "link": "https://www.cfainstitute.org/membership/professional-development/refresher-readings/machine-learning"
    }
    # Ensure validation error is raised for invalid published year
    with pytest.raises(ValidationError) as excinfo:
        URLClass(**data)
    print(str(excinfo.value))

@pytest.mark.parametrize("invalid_link", ["invalid_link", "ftp://example.com"])
def test_invalid_link(invalid_link):
    data = {
        "title": "Machine Learning",
        "topic": "Quantitative Methods",
        "published_year": 2024,
        "level": "Level II",
        "introduction": "Investment firms are increasingly using technology at every step of the investment management value chain—from improving their understanding of clients to uncovering new sources of alpha and executing trades more efficiently. Machine learning techniques, a central part of that technology, are the subject of this reading. These techniques first appeared in finance in the 1990s and have since flourished with the explosion of data and cheap computing power.This reading provides a high-level view of machine learning (ML).",
        "learning_outcomes": "The member should be able to: describe supervised machine learning, unsupervised machine learning, and deep learning;",
        "summary": "Machine learning methods are gaining usage at many stages in the investment management value chain. Among the major points made are the following",
        "overview": "",
        "link": invalid_link  # Invalid link
    }
    # Ensure validation error is raised for invalid link
    with pytest.raises(ValidationError) as excinfo:
        URLClass(**data)
    print(str(excinfo.value))



