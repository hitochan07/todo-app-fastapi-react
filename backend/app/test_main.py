from __future__ import annotations

import json
import threading
import time
import unittest
from http.client import HTTPConnection

from backend.app.main import TodoRequestHandler, TodoStore, create_server


class TodoAPITestCase(unittest.TestCase):
    def setUp(self) -> None:
        store = TodoStore()
        TodoRequestHandler.store = store
        self.server = create_server("127.0.0.1", 0, store)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.host, self.port = self.server.server_address
        time.sleep(0.05)

    def tearDown(self) -> None:
        self.server.shutdown()
        self.thread.join(timeout=1)

    def _request(self, method: str, path: str, body: dict | None = None):
        conn = HTTPConnection(self.host, self.port, timeout=5)
        headers = {"Content-Type": "application/json"}
        payload = json.dumps(body).encode("utf-8") if body is not None else None
        conn.request(method, path, body=payload, headers=headers)
        response = conn.getresponse()
        raw = response.read()
        conn.close()
        return response.status, json.loads(raw.decode() or "null")

    def test_todo_lifecycle(self) -> None:
        status, body = self._request("GET", "/todos")
        self.assertEqual(status, 200)
        self.assertEqual(body, [])

        status, body = self._request(
            "POST",
            "/todos",
            {"title": "Sample", "description": "demo", "completed": False},
        )
        self.assertEqual(status, 201)
        todo_id = body["id"]

        status, body = self._request("GET", "/todos")
        self.assertEqual(status, 200)
        self.assertEqual(len(body), 1)

        status, body = self._request("DELETE", f"/todos/{todo_id}")
        self.assertEqual(status, 200)
        self.assertEqual(body["message"], "Deleted successfully")

        status, body = self._request("DELETE", f"/todos/{todo_id}")
        self.assertEqual(status, 404)
        self.assertEqual(body["detail"], "Todo not found")

    def test_invalid_payloads(self) -> None:
        status, body = self._request("POST", "/todos", {})
        self.assertEqual(status, 400)
        self.assertIn("title", body["detail"])

        status, body = self._request("POST", "/todos", {"title": "", "description": 1})
        self.assertEqual(status, 400)
        self.assertIn("description", body["detail"])

        status, body = self._request("POST", "/todos", {"title": "ok", "completed": "y"})
        self.assertEqual(status, 400)
        self.assertIn("completed", body["detail"])


if __name__ == "__main__":
    unittest.main()
