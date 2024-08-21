# This Puppet manifest fixes the Nginx performance issue by increasing the number of worker processes
# and the maximum number of open files.

exec { 'nginx-worker-processes-increase':
  command => 'sed -i "s/worker_processes 4/worker_processes auto/g" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin:/usr/bin:/bin/',
  notify  => Service['nginx'],
}

exec { 'max-open-files-increase':
  command => 'sed -i "s/worker_rlimit_nofile 768/worker_rlimit_nofile 65536/g" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin:/usr/bin:/bin/',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}

