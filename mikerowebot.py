import requests
from bs4 import BeautifulSoup

#url for job listing
base_url = "https://www.seek.com.au/"
#headers for request
headers = {"User-Agent": "Mozilla/5.0"}
#maximum amount of scraped pages
max_pages = 5

#user inputs a keyword
keyword = input("Enter a keyword for the job listings: ")
#keyword is appended to the base_url
base_url += keyword + "-jobs"

for page in range(1, max_pages + 1):    
    #add the page parameter to the url
    url = f"{base_url}?page={page}"
    #send the request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        #parse the url with beautifulsoup
        soup = BeautifulSoup(response.text, 'html.parser')
        #soup finds all elements structured as 'article' by seek
        jobs = soup.find_all('article')

        #extracts relevant job information and prints in a specific format
        for job in jobs:
            job_title = job.find(attrs={"data-automation": "jobTitle"})
            job_title_text = job_title.text.strip() if job_title else "No job title found"

            job_company = job.find(attrs={"data-automation": "jobCompany"})
            job_company_text = job_company.text.strip() if job_company else "No job title found"

            job_salary = job.find(attrs={"data-automation": "jobSalary"})
            job_salary_text = job_salary.text.strip() if job_salary else "No job salary found"

            print(f"Job Title: {job_title_text}")
            print(f"Company Name: {job_company_text}")
            print(f"Salary: {job_salary_text}")
            print("-" * 50)
    else:
        #error handling, stops the loop if an error is encountered
        print(f"Failed to fetch page {page}. Status code: {response.status_code}")
        break
