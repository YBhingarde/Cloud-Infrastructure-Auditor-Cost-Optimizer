from cleanup.cleanup_manager import CleanupManager, confirm_cleanup

def test_dry_run():
    manager = CleanupManager()

    result = manager.dry_run(["bucket1"])

    assert result["mode"] == "dry-run"


def test_execute():
    manager = CleanupManager()

    result = manager.execute(["bucket1"])

    assert result["mode"] == "execute"

def test_confirm_cleanup():
    assert confirm_cleanup("yes") == "execute"
    assert confirm_cleanup("no") == "dry-run"