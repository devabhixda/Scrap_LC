# Scrap_LC

Scrap_LC is a tool designed to scrape LeetCode problem data for various companies and generate CSV files with the collected information.

## Features

- Scrapes LeetCode problems for multiple companies
- Generates CSV files with problem details
- Easy to use and customizable

## Company Data

The following table shows the companies for which problem data is scraped:

| Company | CSV File |
|---------|----------|
| Amazon | [amazon.csv](output/amazon_leetcode_3mo.csv) |
| Meta | [meta.csv](output/meta_leetcode_3mo.csv) |

## Installation

To use Scrap_LC, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/devabhixda/Scrap_LC.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Scrap_LC
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the scraper and generate CSV files:

1. Download html file from leetcode company page
    ```
    Right Click -> Save as
    https://leetcode.com/company/amazon/
    ```

2. Move the html to input folder

3. Add the company name in the script
    ```
    companies = ["amazon", "meta"]
    ```


4. Execute the main script:
   ```bash
   python scrap_lc.py
   ```

5. The script will start scraping LeetCode problems for each company and save the results in the `output` folder.

6. Once completed, you can find the generated CSV files in the `output` directory.

## Contributing

Contributions to Scrap_LC are welcome! Please feel free to submit a Pull Request.
