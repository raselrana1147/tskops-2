import json
def process_server_data(json_string):
    try:
        data = json.loads(json_string)
        for server in data.get("servers",[]):
            name=server.get("name")
            status=server.get("status")

            print(f"Server Name :{name} : Server Status : {status}")

    except json.decoder.JSONDecodeError as e:
        print("Failed to parse server data")
        print("Error:", e)

mock_api = '{"servers": [{"name": "web-01", "status": "up"}, {"name": "db-01", "status": "down"}]}'

process_server_data(mock_api)



