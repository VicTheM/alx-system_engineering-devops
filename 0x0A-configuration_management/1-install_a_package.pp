# Installs Flask, version 2.1.0 from pip3

package { 'flask':
	name => 'flask',
	provider => pip3,
	ensure => '2.1.0',
}

