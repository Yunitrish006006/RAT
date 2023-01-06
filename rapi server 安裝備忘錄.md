# 樹梅派伺服器安裝備忘錄

## 網路國碼更改

## 鍵盤修改

## ssh啟用

## 連上網路

## frpc安裝

<https://blog.markkulab.net/2022/01/23/raspberry-pi-frpc/>

    [common]
    server_addr = frp.4hotel.tw
    server_port = 7000
    #auth_token = 97145312
    token = 97145312
    pool_count = 10000
    authentication_method = token

    [rsdpi_ssh_1]
    type = tcp
    local_ip = 127.0.0.1
    local_port = 22
    remote_port = 25522

    [raspi_web_1]
    type = tcp
    local_ip = 127.0.0.1
    local_port = 80
    remote_port = 25580

## 安裝apache

## 在 /var/www/html 中建立CGI-BIN連結
