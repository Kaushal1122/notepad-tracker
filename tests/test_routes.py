def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Notepad Tracker" in response.data


def test_create_file(client, tmp_path):
    file_path = tmp_path / "notes.txt"

    response = client.post(
        "/api/files",
        json={"path": str(file_path)}
    )

    assert response.status_code == 201
    assert file_path.exists()


def test_create_file_without_path(client):
    response = client.post("/api/files", json={})

    assert response.status_code == 400


def test_create_existing_file(client, tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("Existing content", encoding="utf-8")

    response = client.post(
        "/api/files",
        json={"path": str(file_path)}
    )

    assert response.status_code == 409


def test_open_file(client, tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("Hello from Flask", encoding="utf-8")

    response = client.get(
        "/api/files",
        query_string={"path": str(file_path)}
    )

    assert response.status_code == 200
    assert response.json["content"] == "Hello from Flask"


def test_open_file_without_path(client):
    response = client.get("/api/files")

    assert response.status_code == 400


def test_save_file(client, tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("Old content", encoding="utf-8")

    response = client.put(
        "/api/files",
        json={
            "path": str(file_path),
            "content": "Updated content"
        }
    )

    assert response.status_code == 200
    assert file_path.read_text(encoding="utf-8") == "Updated content"
    assert response.json["committed"] is True


def test_save_file_without_path(client):
    response = client.put(
        "/api/files",
        json={"content": "Some content"}
    )

    assert response.status_code == 400


def test_save_file_without_content(client, tmp_path):
    file_path = tmp_path / "notes.txt"

    response = client.put(
        "/api/files",
        json={"path": str(file_path)}
    )

    assert response.status_code == 400


def test_save_file_with_non_string_content(client, tmp_path):
    file_path = tmp_path / "notes.txt"

    response = client.put(
        "/api/files",
        json={
            "path": str(file_path),
            "content": 123
        }
    )

    assert response.status_code == 400
