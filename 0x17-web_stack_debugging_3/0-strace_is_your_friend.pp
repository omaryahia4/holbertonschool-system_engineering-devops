# Puppet code to fix why Apache is returning 500 error .
exec { 'fix-phpp':
path     => 'usr/bin/:/bin/',
command  => "sed -i -e 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
