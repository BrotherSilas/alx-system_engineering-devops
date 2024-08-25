# This Puppet manifest fixes the Nginx performance issue by increasing 
# the number of worker processes to auto
# and the maximum number of open files.

exec { 'fix-for-nginx':
  command => "sed -i '/worker_processes/s/[0-9]+/auto/' /etc/nginx/nginx.conf /etc/nginx/sites-available/default",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -f /etc/nginx/nginx.conf || test -f /etc/nginx/sites-available/default',
}

# Increase the ULIMIT
exec { 'increase-ulimit':
  command => 'sed -i "/^ULIMIT=/c\ULIMIT=\'-n 65536\'" /etc/default/nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -f /etc/default/nginx',
}

# Restart Nginx to apply changes
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart || service nginx restart || systemctl restart nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  require => [Exec['fix-for-nginx'], Exec['increase-ulimit']],
}

