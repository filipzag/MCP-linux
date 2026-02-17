# Command Executor MCP Server

An MCP server that enables command execution on the host Linux machine.

## Installation

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### STDIO (Default)
Run the server:
```bash
python server.py
```

### HTTP (SSE)
Run the server over SSE:
```bash
python server.py --transport sse --port 8000
```

### HTTP (Streamable)
Run the server over Streamable HTTP:
```bash
python server.py --transport streamable-http --port 8000
```

### Authentication
Enable Bearer authentication with `--auth-token`:
```bash
python server.py --transport sse --auth-token "your-secret-token"
```

## Tools

- `execute_command(command: str) -> str`: Executes a shell command and returns the output (stdout + stderr).

> [!WARNING]
> This server exposes arbitrary command execution. Use with caution.
