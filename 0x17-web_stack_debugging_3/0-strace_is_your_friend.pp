# Fixes the Apache 500 error by using sed to replace all instances of 'phpp' with 'php'

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

