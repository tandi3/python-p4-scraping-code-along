#!/usr/bin/env python3

import sys
sys.path.append('lib')

from Scraper import Scraper

if __name__ == "__main__":
    print("Web Scraping Demo - Flatiron School Courses")
    print("=" * 50)
    
    scraper = Scraper()
    scraper.print_courses()