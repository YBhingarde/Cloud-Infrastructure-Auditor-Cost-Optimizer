# cleanup/cleanup_manager.py

class CleanupManager:

    def dry_run(self, resources):
        return {
            "mode": "dry-run",
            "resources": resources
        }

    def execute(self, resources):
        return {
            "mode": "execute",
            "resources": resources
        }


def confirm_cleanup(choice):
    if choice.lower() == "yes":
        return "execute"
    return "dry-run"