from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===


def test_get_spaces(page, test_web_address, db_connection):
    db_connection.seed('seeds/spaces.sql')
    page.goto(f'http://{test_web_address}/spaces')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Ben house\nfree',
        'Emily house\nfree',
        'Harry house\noccupied',
        'Josh house\nfree',
        'James house\noccupied'
    ])


"""
POST /space
  Parameters:
    name: Ben's house
    availability: Free
  Expected response (200 OK):
  "Ben's house
Availability: Free"
"""


def test_get_space(page, test_web_address, db_connection):
    db_connection.seed('seeds/spaces.sql')
    page.goto(f'http://{test_web_address}/spaces/1')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Ben house\nfree'
    ])


# === End Example Code ===
