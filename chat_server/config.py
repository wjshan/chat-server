import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="CHAT_SERVER",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml"],
    environments=True,
    env_switcher="CHAT_SERVER_ENV",
    load_dotenv=True,
    merge_enabled=True
)
"""
# How to use this application settings

```
from chat_server.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export chat_server_KEY=value
export chat_server_KEY="@int 42"
export chat_server_KEY="@jinja {{ this.db.uri }}"
export chat_server_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
chat_server_ENV=production chat_server run
```

Read more on https://dynaconf.com
"""
