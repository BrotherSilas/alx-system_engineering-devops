# This Puppet manifest increases the file descriptor limit for the user
# Changes os configuration for holberton userexec { 'change-os-configuration-for-holberton-user':

exec { 'change-os-configuration-for-holberton-user':
  command  => "sed -i '/holberton hard/d' /etc/security/limits.conf &&
              sed -i '/holberton soft/d' /etc/security/limits.conf &&
              echo 'holberton hard nofile 8192' >> /etc/security/limits.conf &&
              echo 'holberton soft nofile 4096' >> /etc/security/limits.conf",
  path     => '/usr/local/bin/:/bin/',
  provider => 'shell',
}

