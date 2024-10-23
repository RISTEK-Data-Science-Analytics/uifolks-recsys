achievement_type = {
    0: 'Data Science',
    1: 'Hackathon',
    2: 'Artificial Intelligence',
    3: 'Capture The Flag',
    4: 'Business Case',
    5: 'Business Proposal',
    6: 'Analytics',
    7: 'UI/UX',
    8: 'Competitive Programming',
    9: 'Olympiad',
    10: 'Game Development',
    11: 'Scientific Paper',
    12: 'Internet of Things',
    13: 'Animation',
    14: 'Smart City'
}

achievement_categories = {
    "Data & Analytics": ['Data Science', 'Analytics', 'Artificial Intelligence'],
    "Business & Strategy": ['Business Case', 'Business Proposal'],
    "Technology & Engineering": ['Internet of Things', 'Smart City', 'Game Development'],
    "Competitions": ['Hackathon', 'Capture The Flag', 'Competitive Programming', 'Olympiad'],
    "Creative & Design": ['UI/UX', 'Animation'],
    "Research & Development": ['Scientific Paper']
}

MAX_ACHIEVEMENT_TYPE_ID = max(achievement_type.keys())