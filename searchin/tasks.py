from crewai import Task
from agents import JobSearchAgent, AnalysisAgent, MessageWriterAgent

JobSearch = Task(
    description="Search and return 15 most recent {title} job postings ({years} yrs experience) in the Fortune 500 Tech companies in India on Linkedin (look for specific jobs, not job groups. Also ensure that the time the job was posted is within past 7 days max) and then look for HRs in those companies as structured JSON.[{\"name\":\"TCS\",\"industry\":\"IT Services & Consulting\",\"annual_hiring\":\"40000+\",\"fresher_salary\":\"3.6–6.5 LPA\",\"overview\":\"One of the largest IT firms in India, conducts extensive campus recruitment drives.\"},{\"name\":\"Infosys\",\"industry\":\"IT Services & Consulting\",\"annual_hiring\":\"50000+\",\"fresher_salary\":\"3.5–5 LPA\",\"overview\":\"Global IT leader, known for robust fresher training programs.\"},{\"name\":\"Wipro\",\"industry\":\"IT Services, Consulting & BPO\",\"annual_hiring\":\"40000+\",\"fresher_salary\":\"3.5–6 LPA\",\"overview\":\"Offers IT consulting and business process services with focus on fresh talent.\"},{\"name\":\"Capgemini\",\"industry\":\"Tech Services & Digital Transformation\",\"annual_hiring\":\"60000+\",\"fresher_salary\":\"3.5–5 LPA\",\"overview\":\"Global consulting and technology services company actively recruiting freshers.\"},{\"name\":\"Accenture\",\"industry\":\"Professional Services, IT & Consulting\",\"annual_hiring\":\"70000+\",\"fresher_salary\":\"3.5–6.5 LPA\",\"overview\":\"Provides a broad range of services in strategy, consulting, technology, and operations.\"},{\"name\":\"Cognizant\",\"industry\":\"IT Services, Consulting & BPO\",\"annual_hiring\":\"25000+\",\"fresher_salary\":\"4–6 LPA\",\"overview\":\"Leading IT and consulting service provider.\"},{\"name\":\"HCL Technologies\",\"industry\":\"IT Services, Consulting & Engineering\",\"annual_hiring\":\"40000+\",\"fresher_salary\":\"3.5–5 LPA\",\"overview\":\"Offers software-led IT solutions and R&D services.\"},{\"name\":\"IBM\",\"industry\":\"IT Services & Consulting\",\"annual_hiring\":\"25000+\",\"fresher_salary\":\"4–6 LPA\",\"overview\":\"Multinational tech company providing IT and consulting services.\"},{\"name\":\"Gini Talent\",\"industry\":\"Staffing & Recruitment\",\"overview\":\"Specializes in sourcing skilled talent across industries using innovative tech.\"},{\"name\":\"TeamLease Services\",\"industry\":\"Staffing & Recruitment\",\"overview\":\"Leading staffing company for temporary and permanent workforce across sectors.\"},{\"name\":\"Adecco India\",\"industry\":\"Staffing & Recruitment\",\"overview\":\"Offers bulk hiring solutions for logistics, e-commerce, and telecom industries.\"},{\"name\":\"Randstad India\",\"industry\":\"Staffing & Recruitment\",\"overview\":\"Global HR services leader, focusing on mass recruitment in IT, BFSI, and healthcare.\"},{\"name\":\"Seven Consultancy\",\"industry\":\"Staffing & Recruitment\",\"overview\":\"Provides mass hiring services across India, for temporary and permanent staffing.\"}], Give these priority.",
    expected_output="A JSON list with job title, company, {location}, description, {contact} information and application link.",
    agent=JobSearchAgent,
    output_file="./job-posts/job-results-2.json"
)

Analysis = Task(
    description="Analyze the job data to find best matches for a {title} candidate, common skills, and standout roles.",
    expected_output="3-paragraph summary with top roles, required skills, and any red flags.",
    agent=AnalysisAgent,
    output_file="./job-posts/new-job-analysis-2.md"
)

MessageWriting = Task(
    description="Write LinkedIn messages and cold emails for 3-5 top job entries. Include job title, company, location, tools/stack, and application link in a formatted daily digest.",
    expected_output="A job digest with 2–3 job entries, each containing a recruiter message and cold email.",
    agent=MessageWriterAgent,
    output_file="./job-posts/new-job-post-2.md"
)