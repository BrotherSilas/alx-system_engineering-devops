# This Puppet manifest increases the file descriptor limit for the user
# Changes os configuration for holberton user

exec { 'change-configuration-for-user':
  command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf && echo "holberton hard nofile 8192" >> /etc/security/limits.conf',
  path    => '/usr/local/bin:/usr/bin:/bin/',
}

