from django.core.management.base import BaseCommand
from faker import Faker
from core.models import Department, Employee, Attendance, PerformanceReview
import random

class Command(BaseCommand):
    help = "Generate synthetic employee data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = ['Engineering', 'HR', 'Marketing', 'Sales']
        dept_objs = [Department.objects.get_or_create(name=name)[0] for name in departments]

        for _ in range(5):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                department=random.choice(dept_objs),
                date_joined=fake.date_between(start_date='-3y', end_date='today'),
                salary=random.randint(40000, 120000),
                is_active=random.choice([True, False])
            )
            for _ in range(5):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_between(start_date='-3mo', end_date='today'),
                    status=random.choice(['Present', 'Absent'])
                )
            for _ in range(2):
                PerformanceReview.objects.create(
                    employee=emp,
                    review_date=fake.date_between(start_date='-1y', end_date='today'),
                    score=random.randint(1, 10),
                    remarks=fake.sentence()
                )
