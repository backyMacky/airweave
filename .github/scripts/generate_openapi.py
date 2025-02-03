"""Generate OpenAPI schema for Airweave API."""

from fastapi.openapi.utils import get_openapi
import json
import os
import sys
from pathlib import Path

# Get the absolute path to the project root (2 levels up from .github/scripts)
project_root = Path(__file__).parent.parent.parent.absolute()
backend_dir = project_root / "backend"

# Add backend to Python path
sys.path.append(str(backend_dir))
os.chdir(backend_dir)  # Change working directory to backend

from app.main import app


def generate_openapi():
    """Generate OpenAPI schema for Airweave API."""
    print("Generating OpenAPI schema...")

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    )

    # Path to fern/openapi directory from project root
    fern_dir = project_root / "fern" / "openapi"
    fern_dir.mkdir(parents=True, exist_ok=True)

    output_path = fern_dir / "openapi.json"
    print(f"📝 Writing OpenAPI spec to: {output_path}")

    with open(output_path, "w") as f:
        json.dump(openapi_schema, f, indent=2)

    print(f"✅ OpenAPI schema saved to {output_path}")


if __name__ == "__main__":
    generate_openapi()
