# Volatility MCP 사용법

## 1. 의존성 설치

```python
pip install -r requirements.txt
```

## 2. Cursor IDE 또는 Claude Desktop config 설정 파일 내 아래 MCP 서버 json 코드 설정

```json
{
    "mcpServers": {
      "vol": {
         "command": "python",
         "args": [
          "/경로/volatility-mcp/vol_mcp_server.py"
         ]
       }
    }
}
```

