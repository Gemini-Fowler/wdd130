from database import add_milestone, get_milestones, init_db

def test_add_milestone():
    """Test if a milestone can be added successfully."""
    init_db()  # Ensure database is initialized
    add_milestone('Alice', 'First Steps', '2024-10-18', None)  # Add a milestone for Alice
    milestones = get_milestones('Alice')  # Retrieve milestones for Alice
    assert len(milestones) == 1  # Check if one milestone exists
    assert milestones[0][0] == 'First Steps'  # Verify the milestone text is correct
