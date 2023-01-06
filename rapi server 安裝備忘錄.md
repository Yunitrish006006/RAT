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
>
> - sudo apt-get install apache
>
## 在 /var/www/html 中建立CGI-BIN連結
>
> - nano /etc/apache2/conf-enabled/serve-cgi-bin.conf
>
    <IfModule mod_alias.c>
            <IfModule mod_cgi.c>
                    Define ENABLE_USR_LIB_CGI_BIN
                    Define ENABLE_WWW_CGI_BIN
            </IfModule>

            <IfModule mod_cgid.c>
                    Define ENABLE_USR_LIB_CGI_BIN
                    Define ENABLE_WWW_CGI_BIN
            </IfModule>

            <IfDefine ENABLE_USR_LIB_CGI_BIN>
                    ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
                    <Directory "/usr/lib/cgi-bin">
                            AllowOverride None
                            Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                            Require all granted
                    </Directory>
            </IfDefine>
            <IfDefine ENABLE_WWW_CGI_BIN>
                    ScriptAlias /cgi-www/ /var/www/html/cgi-bin/
                    <Directory "/var/www/html/cgi-bin">
                            AllowOverride None
                            Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                            Require all granted
                    </Directory>
            </IfDefine>
    </IfModule>
>
> - cd /etc/apache2/mods-enabled
>
> - sudo ln -s ../mods-available/cgi.load
>
> - sudo service apache2 reload
>