# Giving holberton user acces to open a file without any error message.
exec{ 'OS-configuration':
    command => 'echo "" > /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/',
}
