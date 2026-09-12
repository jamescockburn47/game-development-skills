"""Public trust-boundary tests for the packaged design-review builder."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "evidence-led-game-development"
EXAMPLE = SKILL / "assets" / "design-review-example.json"
SYNTHETIC_DESCRIPTION = (
    "Synthetic test description; no real-user provenance; internal tests only.\n\n"
    "Unicode: 雪と海 — café. Script-looking text: "
    "<script>window.testOnly = true;</script> ${testOnly}."
)
SYNTHETIC_SOURCE = (
    "Synthetic test source; no real-user provenance; internal tests only."
)


def load_module(path, name):
    """Load a shipped script without requiring it to be an installed package."""
    scripts = str(path.parent)
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    spec = importlib.util.spec_from_file_location(name, path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


builder = load_module(SKILL / "scripts" / "build_design_review.py", "public_review_builder")
document = load_module(SKILL / "scripts" / "review_document.py", "public_review_document")


def completed_review():
    """Clone the shipped blank review and complete it with synthetic test data."""
    review = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    review.update(review_id="test", revision=1, example=False)
    review["game"] = {
        "description": SYNTHETIC_DESCRIPTION,
        "recorded_from": SYNTHETIC_SOURCE,
    }
    review["open_questions"] = []
    review["development"]["change_note"] = "Completed with synthetic internal test data."
    return review


def response_for(review, decision="approve"):
    return {
        "schema_version": 2,
        "review_id": review["review_id"],
        "revision": review["revision"],
        "fingerprint": builder.fingerprint(review),
        "decision": decision,
        "game_description": review["game"]["description"],
        "values": {item["id"]: item["value"] for item in review["decisions"]},
        "notes": "",
        "example": review["example"],
    }


class PublicReviewTests(unittest.TestCase):
    def setUp(self):
        self.review = completed_review()
        self.response = response_for(self.review)

    def test_description_is_exact_in_response_and_safe_in_rendered_html(self):
        result = builder.check_response(self.review, self.response)
        self.assertEqual(result["changed_decisions"], [])
        self.assertEqual(self.response["game_description"], SYNTHETIC_DESCRIPTION)
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "review.html"
            builder.build(self.review, output)
            html = output.read_text(encoding="utf-8")
        self.assertNotIn("<script>window.testOnly = true;</script>", html)
        self.assertIn("\\u96ea\\u3068\\u6d77", html)
        self.assertIn("\\u003cscript\\u003ewindow.testOnly = true;\\u003c/script\\u003e", html)

    def test_blank_or_missing_provenance_cannot_authorize(self):
        blank = copy.deepcopy(self.review)
        blank["game"] = {"description": "", "recorded_from": None}
        builder.validate_review(blank)
        with self.assertRaises(ValueError):
            builder.check_response(blank, response_for(blank))
        for game in (
            {"description": SYNTHETIC_DESCRIPTION},
            {"description": SYNTHETIC_DESCRIPTION, "recorded_from": "  "},
            {"description": "", "recorded_from": SYNTHETIC_SOURCE},
        ):
            invalid = copy.deepcopy(self.review)
            invalid["game"] = game
            with self.subTest(game=game), self.assertRaises(ValueError):
                builder.validate_review(invalid)

    def test_edited_content_invalidates_approval(self):
        variants = []
        description = copy.deepcopy(self.response)
        description["game_description"] += " Edited."
        variants.append(description)
        choice = copy.deepcopy(self.response)
        choice["values"]["platform"] = "browser"
        variants.append(choice)
        variants.append(dict(self.response, notes="Change the plan."))
        for response in variants:
            with self.subTest(response=response), self.assertRaises(ValueError):
                builder.check_response(self.review, response)

    def test_stale_or_substituted_response_is_rejected(self):
        for field, value in (
            ("review_id", "different-test"),
            ("revision", 2),
            ("fingerprint", "0" * 64),
        ):
            with self.subTest(field=field), self.assertRaises(ValueError):
                builder.check_response(self.review, dict(self.response, **{field: value}))

    def test_structural_approval_never_claims_verified_user_authorization(self):
        result = builder.check_response(self.review, self.response)
        self.assertTrue(result["valid"])
        self.assertEqual(result["decision"], "approve")
        self.assertIs(result["user_authorization_verified"], False)

    def test_archived_source_history_rejects_rewrite_and_tampering(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "review.html"
            builder.build(self.review, output)
            rewritten = copy.deepcopy(self.review)
            rewritten["summary"] += " Changed without a revision."
            with self.assertRaises(ValueError):
                document.check_archive(rewritten, output)
            archived_html = output.parent / "history" / "test-r1.html"
            archived_html.write_text(archived_html.read_text(encoding="utf-8") + "tamper", encoding="utf-8")
            with self.assertRaises(ValueError):
                document.check_archive(self.review, output)

    def test_progress_cannot_expand_the_approved_scope(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "review.html"
            builder.build(self.review, output)
            progress = copy.deepcopy(self.review)
            progress["revision"] = 2
            progress["development"].update(
                purpose="update",
                next="step:1",
                approved_plan={
                    "revision": 1,
                    "fingerprint": builder.fingerprint(self.review),
                    "recorded_from": SYNTHETIC_SOURCE,
                },
                milestones=[],
                change_note="Synthetic internal progress test.",
            )
            document.check_archive(progress, output)
            progress["scope"] += " Expanded work outside the approved scope."
            with self.assertRaises(ValueError):
                document.check_archive(progress, output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
