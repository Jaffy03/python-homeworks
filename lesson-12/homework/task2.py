import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
job_listings = soup.find_all("div", class_="card-content")
jobs = []

for job in job_listings:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    application_link = job.find("a", class_="card-footer-item")["href"]
    jobs.append({
        "title": title,
        "company": company,
        "location": location,
        "application_link": application_link
    })

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT NOT NULL,
    application_link TEXT NOT NULL,
    UNIQUE(title, company, location)
)
""")
conn.commit()

def insert_job(job):
    cursor.execute("""
    INSERT OR IGNORE INTO jobs (title, company, location, application_link)
    VALUES (?, ?, ?, ?)
    """, (job["title"], job["company"], job["location"], job["application_link"]))
    conn.commit()

def update_job(job):
    cursor.execute("""
    UPDATE jobs
    SET application_link = ?
    WHERE title = ? AND company = ? AND location = ?
    """, (job["application_link"], job["title"], job["company"], job["location"]))
    conn.commit()

for job in jobs:
    insert_job(job)

for job in jobs:
    cursor.execute("""
    SELECT application_link FROM jobs
    WHERE title = ? AND company = ? AND location = ?
    """, (job["title"], job["company"], job["location"]))
    result = cursor.fetchone()
    if result:
        if result[0] != job["application_link"]:
            update_job(job)

def filter_jobs(location=None, company=None):
    query = "SELECT * FROM jobs"
    conditions = []
    if location:
        conditions.append(f"location = '{location}'")
    if company:
        conditions.append(f"company = '{company}'")
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    cursor.execute(query)
    return cursor.fetchall()

filtered_jobs = filter_jobs(location="Bellberg, AP")

def export_to_csv(jobs, filename="filtered_jobs.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Company", "Location", "Application Link"])
        for job in jobs:
            writer.writerow(job)

export_to_csv(filtered_jobs)
conn.close()