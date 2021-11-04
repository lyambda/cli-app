# cmd-app

Тут находится приложение для консоли

## Инструкция

### Команды

Подробнее читать тут: https://github.com/lyambda/api#readme

#### me 

args:

```-```

return: 
```
{
    'ok': True, 
    'result': {
        '_id': 2, 
        'contacts': [], 
        'description': 'Developer', 
        'email': 'kreepmeister@yandex.ru', 
        'groups': [1], 
        'name': 'vsecoder',
        'surname': ''
    }
}
```

#### createGroup

args:

```
Name >>> ...
Link >>> ...
Description >>> ...
```

return:

```
{
    "ok": true,
    "result": {
        "_id": 1,
        "description": null,
        "link": null,
        "messages": [],
        "name": "Чат",
        "owner": 1,
        "participants": [
          1
        ]
    }
}
```

#### joinGroup

args:

```
Group ID >>> ...
```

return:

```
{
    "ok": true,
    "result": {
        "_id": 1,
        "description": null,
        "link": null,
        "messages": [],
        "name": "Чат",
        "owner": 1,
        "participants": [
          1, 2
        ]
    }
}
```

#### sendMessage

args:

```
Group ID >>> ...
Text >>> ...
```

return:

```
{
    "ok": true,
    "result": {
        "_id": 1,
        "date": "Wed, 03 Nov 2021 17:23:50 GMT",
        "from_id": 1,
        "text": "Привет"
    }
}
```

#### getMessages

args:

```
Group ID >>> ...
```

return:

```
{
    "ok": true,
    "result": [
        {
            "_id": 1,
            "date": "Wed, 03 Nov 2021 17:23:50 GMT",
            "from_id": 1,
            "text": "Привет"
        }
    ]
}
```

###

## P.S.
!!! В данный момент просто набросок для теста API !!!
