from mcp.server.fastmcp import FastMCP
from typing import List
import subprocess

mcp = FastMCP("Search")

@mcp.tool()
def get_processes(dump_image_path: str) -> List[str]:
    """
    Get the processes running in the memory image.
    """
    result = subprocess.run(
        ['python', '-m' 'vol', '-f', dump_image_path, 'windows.pslist.PsList'],
        capture_output=True,
        text=True
    )
    return result.stdout

@mcp.tool()
def get_connections(dump_image_path: str) -> List[str]:
    """
    Get the connections running in the memory image.
    """
    result = subprocess.run(
        ['python', '-m' 'vol', '-f', dump_image_path, 'windows.netscan.NetScan'],
        capture_output=True,
        text=True
    )
    return result.stdout

@mcp.tool()
def get_cmdline(dump_image_path: str) -> List[str]:
    """
    Get the command line arguments of the processes in the memory image.
    """

    result = subprocess.run(
        ['python', '-m' 'vol', '-f', dump_image_path, 'windows.cmdline.CmdLine'],
        capture_output=True,
        text=True
    )
    return result.stdout


if __name__ == "__main__":
    mcp.run(transport="stdio")