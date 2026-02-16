from fastmcp import FastMCP
import subprocess

# Initialize the MCP server
mcp = FastMCP("Command Executor")

def execute_command_logic(command: str) -> str:
    """
    Executes a shell command on the host machine and returns the output.
    This function contains the core logic, separated for easier testing.
    """
    try:
        # Run the command
        # shell=True allows using shell features like pipes, redirects, etc.
        # text=True ensures output is returned as string instead of bytes
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        
        output = f"Exit Code: {result.returncode}\n"
        if result.stdout:
            output += f"\nSTDOUT:\n{result.stdout}"
        if result.stderr:
            output += f"\nSTDERR:\n{result.stderr}"
            
        return output
        
    except Exception as e:
        return f"Failed to execute command '{command}': {str(e)}"

@mcp.tool()
def execute_command(command: str) -> str:
    """
    Executes a shell command on the host machine and returns the output.
    
    Args:
        command: The shell command to execute.
        
    Returns:
        The combined stdout and stderr of the command, or an error message.
    """
    return execute_command_logic(command)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Command Executor MCP Server")
    parser.add_argument(
        "--transport", 
        default="stdio", 
        choices=["stdio", "sse", "streamable-http"],
        help="Transport protocol to use"
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind to (for sse/streamable-http)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to listen on (for sse/streamable-http)"
    )
    
    args = parser.parse_args()
    
    kwargs = {}
    if args.transport != "stdio":
        kwargs["host"] = args.host
        kwargs["port"] = args.port
        
    mcp.run(transport=args.transport, **kwargs)
