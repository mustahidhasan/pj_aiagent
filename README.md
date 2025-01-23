steps to run this project
# set up claude desktop server
- install claude desktop
- sign in with google

# set up environemnt
- install uv(from powersell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- set venv path if not set earlier: `$env:Path = "C:\Users\Sunny\.local\bin;$env:Path"`
- create venv: `uv venv`
- ativate venv: `.venv\Scripts\activate`
- sync the requiremnts and dependencies: `uv sysnc`

# claude config
- open claude
- from file select file > setting > developer > edit config
- edit the config file `claude_desktop_config.json` [path should locate your server file]
   ``` {
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "C:\\Users\\Sunny\\Desktop\\bc-projects\\playwright-plus-python-mcp\\src\\playwright_server",
                "run",
                "server.py"
            ]
        }
    }
    }```
- resetart the system 
- in claude home check the hammer sign click it and look for configured server.