from pathlib import Path
from bs4 import BeautifulSoup

def get_coverage(path):
    if path.exists():
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        if not soup.is_empty_element:
            footer = soup.find('tfoot')
            if not footer.is_empty_element:
                coverage_percentage = footer.find('td',{'class':'ctr2'})
                if not coverage_percentage.is_empty_element :
                    return int(coverage_percentage.get_text().removesuffix("%"))
    else:
        print("Jacoco code coverage report is not found. Please run `./gradlew test` first.")
            
    return 0

def main():
    path = Path("target/site/jacoco/index.html")
    coverage = get_coverage(path)
    if coverage < 80:
        print(f'Minimum 80% code coverage is required. Current coverage is {coverage}%. Check {path.absolute()} for current coverage report.')
        return 1
    else:
        print(f'Passed minimum 80% code coverage. Current coverage is {coverage}%. Check {path.absolute()} for current coverage report.')
        return 0

if __name__ == '__main__':
    raise SystemExit(main())