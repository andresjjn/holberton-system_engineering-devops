#Manifest that make changes to a configuration file in a server.
file { 'ssh configuration file':
  line => ['  IdentityFile ~/.ssh/holberton'],
}
