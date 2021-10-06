# Puppet script to change the limit of how many files Nginx can open.
exec{ 'fix-nginx':
    command => 'echo "ULIMIT=\"-n 2000\"" > /etc/default/nginx && /etc/init.d/nginx restart',
    path    => '/usr/local/bin/:/bin/',
}
