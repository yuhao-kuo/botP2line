# botP2line

line bot push message **functions**.

## download

```
git clone https://github.com/yuhao-kuo/botP2line
```

## Set infomation

add all infomation

| name | description |
|---|---|
| channel_secret | LINE Channel secret |
| channel_access_token | LINE Channel access token |
| line_user_id | LINE Your user ID |
| imgur_user_id | Imgur application user id |

## build and install

```
sh install_tools.sh
```

ok! next run unit test code.

```
python testpush.py
```

## api

- LINE_TransmitText
	- transmit text message
	- args:
		- mess : your send string
- LINE_TransmitImage
	- transmit image
	- args:
		- img_path : your send image path(rootfs location).

