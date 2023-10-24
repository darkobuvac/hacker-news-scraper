# Custom Hacker News Scraper

This is a Python script for customizing Hacker News scraping based on your preferences. It allows you to specify the number of Hacker News pages to scrape, set a minimal score number for the posts, and specify a folder path to store the scraped news data.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python installed on your local machine.

## Usage

To use the custom Hacker News scraper, run the `main.py` script with the following command-line options:

```
python main.py [-h] [-s SITES] [-v VOTES] [-f FOLDER]
```

### Options:

- `-h, --help`: Show help message and exit.
- `-s SITES, --sites SITES`: Number of Hacker News pages to scrape.
- `-v VOTES, --votes VOTES`: Minimal score number for the posts.
- `-f FOLDER, --folder FOLDER`: Folder path to store scraped news data.

### Example Usage:

- Scrape 3 pages of Hacker News with posts having a score of at least 100 and store the data in the `output` folder:
  ```
  python main.py -s 3 -v 100 -f output
  ```

### Output:

The script will generate a CSV file containing the scraped Hacker News posts based on your specified criteria.


---

Feel free to modify the content to match your project structure or add more details as needed.
