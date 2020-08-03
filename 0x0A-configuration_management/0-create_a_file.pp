#Create a file resourse:
file { '/tmp/holberton':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744',
}
