import subprocess
import json
import logging
from typing import List, Dict, Any, Optional, Union

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class GitHubClientError(Exception):
    pass

def run_gh_command(args: List[str], capture_output: bool = True) -> Union[str, Dict[str, Any], List[Any]]:
    """
    Run a gh CLI command and return the parsed JSON or raw output.
    """
    cmd = ["gh"] + args
    try:
        # Check if auth status is valid implicitly by just running the command
        result = subprocess.run(
            cmd,
            capture_output=capture_output,
            text=True,
            check=True
        )
        
        if not capture_output:
            return ""

        output = result.stdout.strip()
        
        # Try to parse as JSON if it looks like JSON
        if output.startswith("{") or output.startswith("["):
            try:
                return json.loads(output)
            except json.JSONDecodeError:
                return output
        return output

    except subprocess.CalledProcessError as e:
        error_msg = f"Command '{' '.join(cmd)}' failed with exit code {e.returncode}.\nStderr: {e.stderr}"
        logger.error(error_msg)
        raise GitHubClientError(error_msg) from e

def check_auth() -> bool:
    """Check if gh cli is authenticated."""
    try:
        res = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
        if res.returncode != 0:
            logger.error(f"gh auth status failed: {res.stderr}")
            return False
        return True
    except subprocess.CalledProcessError:
        return False
