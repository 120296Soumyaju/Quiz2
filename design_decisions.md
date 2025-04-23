📐Architectural Overview

The application is structured with the Django REST Framework using the MVP paradigm:

Models define employee, attendance, department, and performance data

Serializers handle object serialization and deserialization

ViewSets provide RESTful endpoints and one analytical /summary/ view

Swagger (drf-yasg) used for interactive API documentation

🔍 Key Design Decisions

Django REST Framework: Chosen for its speed and simplicity to deliver powerful APIs quickly.

Faker Library: Simplifies generating realistic dummy data.

PostgreSQL: Selected for its advanced relational data support and compatibility with Django.

Throttling & Authentication: Rate limiting and token auth included for minimal security and scalability.

Swagger UI: Essential for visual exploration of APIs during testing.


📌 Extensibility Notes

Add more analytical endpoints as needed (e.g., department-wise performance)

Integrate user roles and permissions for admin vs. employee

Add testing with pytest or Django’s TestCase

Optional frontend dashboard with Chart.js or Plotly

✅ Tradeoffs

Focused on core backend logic within 3 hours, left UI/basic testing as optional

Chose Faker data instead of uploading CSV for simplicity
