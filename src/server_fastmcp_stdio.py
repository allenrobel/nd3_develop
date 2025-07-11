# pylint: disable=line-too-long
"""
A simple FastMCP server to provide developer resources for writing Ansible modules for ND 4.1
"""
import json
from pathlib import Path

from fastmcp import FastMCP
from fastmcp.resources import FileResource

def get_file_path(file_path: str) -> Path:
    """Get the absolute path of a file."""
    script_dir = Path(__file__).parent
    path = script_dir / file_path
    if path.exists():
        return path.resolve()
    raise ValueError(f"Path {path} does not exist")

def load_file(file_path: str) -> str:
    """Load a file and return its content"""
    path = get_file_path(file_path)
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return f.read()
    raise ValueError(f"Path {path.resolve()} does not exist")

def load_json_file(file_path: str) -> dict:
    """Load a JSON file and return its content as a dictionary."""
    return json.loads(load_file(file_path))


mcp: FastMCP = FastMCP(
    name="NexusDashboardDeveloperTools",
    instructions="""
    This server provides information that will be useful for developers
    working with the Nexus Dashboard REST API.  It includes tools for
    example payloads, links to Pydantic documentation, links to
    example Ansible playbooks, and more.
    """,
)

# VRF Payload Markdown Resource
vrf_payload_md_path = get_file_path("payloads/v3/md/vrf.md")
if vrf_payload_md_path.exists():
    vrf_payload_md_resource = FileResource(
        uri=f"file://{vrf_payload_md_path.as_posix()}",
        path=vrf_payload_md_path,
        name="VRF Payload Markdown",
        description="Markdown file that describes the VRF payload.",
        mime_type="text/markdown",
        tags={"documentation"},
    )
    mcp.add_resource(vrf_payload_md_resource)


# VRF Attachment Payload Markdown Resource
vrf_attachment_payload_md_path = get_file_path("payloads/v3/md/vrf_attachment.md")
if vrf_attachment_payload_md_path.exists():
    vrf_attachment_payload_md_resource = FileResource(
        uri=f"file://{vrf_attachment_payload_md_path.as_posix()}",
        path=vrf_attachment_payload_md_path,
        name="VRF Attachment Payload Markdown",
        description="Markdown file that describes the VRF attachment payload.",
        mime_type="text/markdown",
        tags={"documentation"},
    )
    mcp.add_resource(vrf_attachment_payload_md_resource)


@mcp.prompt(
    name="Ansible Developer Role",
    description="Loads and returns the Ansible developer role prompt."
)
async def prompt_developer_role() -> str:
    """
    Prompt that describes a Python developer writing an Ansible module.

    Returns:

    str: The contents of the prompt file
    """
    return load_file("prompts/developer_role.md")

@mcp.prompt(
    name="Project Shared Enums",
    description="Loads and returns the project shared enums prompt."
)
async def prompt_project_shared_enums() -> str:
    """
    Prompt that describes the shared enums used in this project.

    Returns:

    str: The contents of the prompt file
    """
    return load_file("prompts/project_shared_enums.md")

@mcp.prompt(
    name="Project Shared Models",
    description="Loads and returns the project shared Pydantic models prompt."
)
async def prompt_project_shared_models() -> str:
    """
    The shared Pydantic models used in this project.

    Returns:

    str: The contents of the prompt file
    """
    return load_file("prompts/project_shared_models.md")

@mcp.prompt(
    name="Project Shared Validators",
    description="Loads and returns the project shared validators prompt."
)
async def prompt_project_shared_validators() -> str:
    """
    Prompt that describes the shared validators used in this project.

    Returns:

    str: The contents of the prompt file
    """
    return load_file("prompts/project_shared_validators.md")


@mcp.prompt(
    name="Task VRF Module Create",
    description="Loads and returns the VRF module create prompt."
)
async def prompt_task_vrf_module_create() -> str:
    """
    Prompt that describes the requirements for creating a VRF module.

    Returns:

    str: The contents of the prompt file
    """
    return load_file("prompts/task_vrf_module_create.md")


@mcp.resource(
    uri="file:///resources/payloads/vrf.json",
    name="resource_nexus_dashboard_version_3_payload_vrf",
    description="Nexus Dashboard Version 3 VRF Payload Resource"
)
def resource_nexus_dashboard_version_3_payload_vrf() -> dict:
    """Nexus Dashboard Version 3 VRF Payload"""
    return load_json_file("./payloads/v3/vrf.json")

@mcp.tool(
    name="nexus_dashboard_version_3_payload_vrf",
    description="Nexus Dashboard Version 3 VRF Payload",
)
def nexus_dashboard_version_3_payload_vrf() -> dict:
    """Nexus Dashboard Version 3 VRF Payload"""
    return load_json_file("./payloads/v3/vrf.json")


@mcp.tool(name="nexus_dashboard_version_3_response_vrf_attachments")
def nexus_dashboard_version_3_response_vrf_attachments() -> dict:
    """
    Nexus Dashboard Version 3 VRF Attachments Response for the following endpoint:

    Path: /appcenter/cisco/ndfc/api/v1/lan-fabric/rest/top-down/fabrics/[fabric_name]/vrfs/attachments?vrf-names=[comma_separated_vrf_names]
    Verb: GET
    """
    return load_json_file("./responses/v3/vrf_attachments.json")


async def main():
    """Main function to run the FastMCP server."""
    print("In main()")
    await mcp.run_async(transport="stdio")


if __name__ == "__main__":
    print("Starting FastMCP server...")
    import asyncio

    asyncio.run(main())
