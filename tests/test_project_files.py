from pathlib import Path
import importlib.util
import pytest
ROOT = Path(__file__).resolve().parents[1]
def test_required_pages_exist():
    for name in ["index", "approach", "architecture", "about", "faq", "contact"]:
        assert (ROOT / "static" / f"{name}.html").exists()
def test_required_docs_exist():
    assert (ROOT / "docs" / "research_note.md").exists()
    assert (ROOT / "docs" / "ai_usage_log.md").exists()
def test_human_review_language():
    html=(ROOT / "static" / "index.html").read_text()
    assert "authorised credit officer retains the final decision" in html

def test_flask_pages_and_health_start_without_cloud_login():
    if importlib.util.find_spec("flask") is None:
        pytest.skip("Install requirements.txt to run Flask integration tests")
    import sys
    sys.path.insert(0, str(ROOT))
    import app as loan_app
    client = loan_app.app.test_client()
    assert client.get('/').status_code == 200
    assert client.get('/approach').status_code == 200
    assert client.get('/api/health').status_code == 200


def test_decision_api_rejects_invalid_payload_without_cloud_call():
    if importlib.util.find_spec("flask") is None:
        pytest.skip("Install requirements.txt to run Flask integration tests")
    import sys
    sys.path.insert(0, str(ROOT))
    import app as loan_app
    response = loan_app.app.test_client().post('/api/decision', json={'id': '', 'choice': 'Maybe'})
    assert response.status_code == 400
    assert response.get_json()['ok'] is False
