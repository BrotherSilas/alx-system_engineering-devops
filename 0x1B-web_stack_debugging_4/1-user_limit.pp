# This Puppet manifest increases the file descriptor limit for the user
# Changes os configuration for holberton user

file_line { 'set-soft-nofile-limit-for-holberton':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 4096',
  match => '^holberton\s+soft\s+nofile',
}

file_line { 'set-hard-nofile-limit-for-holberton':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 8192',
  match => '^holberton\s+hard\s+nofile',
}

