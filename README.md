# Usage

First, this repository probably isn't of much interest to anyone but me...

## 1. build the container

### 1a. You may have to do this first.

```bash
podman machine init
podman machine start
```

### 1b. Now do the actual build

```bash
cd $HOME/repos/mcp/nd3_develop
podman build -t mcp-nd-developer .
```

## 2. Configure Claude Desktop to use the MCP server

a. In Claude Desktop: Claude -> Settings -> Developer -> Edit Config

b. Open the config and add the JSON from claude_desktop_config_docker.json

c. Save

d. Quit and relaunch Claude

