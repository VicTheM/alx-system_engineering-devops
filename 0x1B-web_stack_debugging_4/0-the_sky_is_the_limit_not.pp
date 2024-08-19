# This file chnages the number of fd the holberton user can have

exec {'replace_limit for nginx':
  provider => shell,
  command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 8192\"/" /etc/default/nginx',
}

exec {'restart_nginx':
  provider => shell,
  command  => 'service nginx restart',
}
