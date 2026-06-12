from django.http import HttpResponse


def api_home(request):

    return HttpResponse("""
    <h1>Student Allocation System</h1>

    <h2>Core APIs</h2>

    <a href="/api/students/">Students</a><br><br>

    <a href="/api/courses/">Courses</a><br><br>

    <a href="/api/allocations/">Allocations</a><br><br>

    <a href="/api/allocate/">Run Allocation</a><br><br>

    <h2>Dashboard APIs</h2>

    <a href="/api/dashboard/allocated/">Allocated Students</a><br><br>

    <a href="/api/dashboard/seats/">Available Seats</a><br><br>

    <a href="/api/dashboard/course-stats/">Course Statistics</a><br><br>

    <a href="/api/dashboard/category-summary/">Category Summary</a><br><br>
    """)